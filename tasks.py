# -*- coding: utf-8 -*-

import os
import shlex
import shutil
import sys
import datetime

from invoke import task
from invoke.main import program
from invoke.util import cd
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    'host': 'localhost',
    'port': 8000,
}

# @task
# def clean(c):
#     """Remove generated files"""
#     if os.path.isdir(CONFIG['deploy_path']):
#         shutil.rmtree(CONFIG['deploy_path'])
#         os.makedirs(CONFIG['deploy_path'])

@task
def build(c):
    """Build local version of site"""
    pelican_run('-s {settings_base}'.format(**CONFIG))

# @task
# def rebuild(c):
#     """`build` with the delete switch"""
#     pelican_run('-d -s {settings_base}'.format(**CONFIG))

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run('-r -s {settings_base}'.format(**CONFIG))

@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        (CONFIG['host'], CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving at {host}:{port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)

@task
def preview(c):
    """Build production version of site"""
    pelican_run('-s {settings_publish}'.format(**CONFIG))

@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured host and port
    server.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])

@task
def publish_output(c):
    pelican_run('-s {settings_publish}'.format(**CONFIG))

    # Commit the written content to GitHub from this repo
    os.chdir(CONFIG['deploy_path'])
    print(f'In Directory: {os.getcwd()}')
    c.run('git add .')
    c.run('git commit -m "auto-commit OUTPUT from Invoke"')
    c.run('git push origin master')

@task(publish_output)
def publish(c):
    # Commit the static html pages to thebouv.github.io repo
    os.chdir('..') # my output folder
    print(f'In Directory: {os.getcwd()}')
    c.run('git add .')
    c.run('git commit -m "auto-commit CONTENT from Invoke"')
    c.run('git push origin main')


def pelican_run(cmd):
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))