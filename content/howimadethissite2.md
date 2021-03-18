Title: How I made this site (part two)
Date: 2021-03-16
Category: meta
Summary: Now to finish off the tutorial on how I made this site including previewing the content and automating some tasks with invoke.
Tags: pelican, python, invoke

Last I left off in [part one](howimadethissite.md) I generated the content with `invoke build`. I want to go over the remaining steps on how to preview the content, how I'm publishing it to GitHub pages with the submodule created previously, and also how I plan to use **invoke** to automate some of this.

## Markdown Tweaks

First before we get to previewing the content, I had to make some adjustments to how the Markdown is processed, especially for code blocks. By default pygments, which pelican uses for code highlighting, didn't mesh well with my theme. So I made sure to make my pre/code blocks have a dark background for one. I also wanted it to stop guessing the language (it was giving weird results trying to guess at the command line code blocks since they're not really a 'language' per se), and for it to recognize GitHub style fenced blocks (using backticks to surrond code blocks instead of relying on indentation).

I added this to my *pelicanconf.py* file:

```python
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang': False},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}
```

## Preview

The `invoke build` command looks at my *pelicanconf.py* file for settings. Some of these settings are theme specific, but they also cover things like what is the site url, how many pages to show before paginating, and so forth. Below I will also be using *publishconf.py* for prod settings like my Google Analytics tag and FQDN for the site url.

Now that the *output* directory has my generated content, I want to preview it.

```
invoke serve
```

This will create a simple local webserver to show you my content on http://localhost:8000 so I open Firefox and make sure everything seems to be working as expected. I click around, look for formatting weirdness, agonize internally over whether I chose the right theme or not, and then ultimately decide all is well.

That's pretty cool, buuuuuuttttt:

### Invoke

Let's dive a bit more into the **invoke** command and the default *tasks.py* file that is created.

There are lot of built in invoke tasks in this file already like **build**, **serve**, and **publish**. Below are my tweaks.

First I remove the **clean**, and **rebuild** commands by commenting them out (maybe I'll redo them in the future). This is becaues they're destructive and will remove the *output* folder entirely, but remember that I'm using it as a submodule so it is its own git repo. Deleting the whole folder would be too destructive.  I also comment out the **preview** task as I only need to do a prod build when I'm publishing.

Next I need to change how the **publish** task works because I'm not using rsync to publish this, I'm pushing the content of output to my **thebouv.github.io** repo so that it serves automatically with GitHub Pages.

```python
@task
def publish(c):
    pelican_run('-s {settings_publish}'.format(**CONFIG))

    # Commit the static html pages to thebouv.github.io repo
    os.chdir(CONFIG['deploy_path']) # my output folder
    c.run('git add .')
    c.run('git commit -m "auto-commit from Invoke"')
    c.run('git push origin master')

    # Commit the written content to GitHub from this repo
    c.run('git add .')
    c.run('git commit -m "auto-commit from Invoke"')
    c.run('git push origin master')
```