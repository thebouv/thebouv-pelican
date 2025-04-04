Title: Setting up my new Mac  
Date: 2021-08-23  
Category: career  
Summary: When I set up a new Mac for dev work, I wanted to document some of the steps I do.
Tags: career, development, hardware

I was setting up a new Macbook laptop recently and as I was installing a few things I decided I should document what I normally do. This isn't a deeply technical article, and is really just a bunch of my opinions, but I think it'll be interesting to some.

## Let's delete a lot of stuff

### Dock

I'm a fan of deleting stuff. I feel like too many people keep too many things on their machines. The very first thing I do when I set up a machine is to delete software. For this machine, I immediately clear the 20+ icons in the Dock. My personal machine only has Finder, Firefox, iTerm2, and VSCode as the permanent apps -- then the Downloads folder and Trash after the divider. I don't understand having more than that as these are the apps I use the most often. Anything else is **&#x2318; + Spacebar** away with Spotlight Search.

<img src="/images/dock.png" alt="an image of my sparse dock, with only a few permanent icons">

### Apps

I also don't have any reason to keep any of the Apple Suite -- literally no one I know uses Pages, Keynote, or any other pieces. Either we have a license to Office365, or GSuite is used. And quite frankly -- I hope I never have to make another PowerPoint/Keynote or Word Doc the rest of my career.

This is also true for GarageBand and iMovie. Just 100% useless on my dev machine for work. But they're also gone from my home machine.

If I could delete more apps I would, but for some reason Chess, Mail, Messages, and others I am not allowed to remove. Reminds me of IE in the Windows world. Do any of the apps take up a lot of space? No, but dammit, I want to delete them. I've read a few articles on how to do it by disabling SIP and more, but at the end of the day I don't wanna mess with that. More a curiosity than anything.

### zsh

I know how awesome zsh is. And Apple thinks so too because now it is the default shell for OS X. However, I've used bash for 20 years and don't really feel like changing. That's pretty much it -- none of the features of zsh impress me enough to change, so I make sure to `chshell` and also add in an env to stop Apple's insistence that I use zsh when I open a terminal (added to my dotfiles of course which you will see below).

### Some trackpad stuff

I hate Apple's "natural scrolling" bullshit. Not even going to hide it. And most of the gestures I end up accidentally triggering all the damn time so I turn off a lot of those too.

For Point and Click settings I turn off "Look up & data detectors" and "Tap to click". I set the secondary click to be bottom right corner. 

For the Gestures setting, I only leave on "Swipe between pages" and "Swipe between full-screen apps". I detest the rest of them.

## Now to add things!

### Brew

Brew gets installed immediately. It is just too handy of a package manager not to do so and is a predecessor to a lot of the other software I want to install.

### iTerm2

The default Termina.app in Mac OS X is okay, but iTerm2 just overall feels better. Snappier, tabbed, and [a ton of other features](https://iterm2.com/features.html) makes it is my go to. 

```sh
brew install --cask iterm2
```

### pyenv

Well, as python is my favorite language, pyenv is an immediate add. Helps manage python versions on my machine including the global one. 

```sh
brew install pyenv
```

### git

Gotta get the real git and easily keep it up to date. The default one with XCode tools (which are necessary to install when installing Brew) lags behind official releases and that has bit me once or twice in the past.

```sh
brew install git
```

### dotfiles

Now that I have my iTerm all set up, I want my colors, aliases, and other things from my dotfiles. Thankfully I maintain them as a repo so I can use them anywhere I want. I simply clone [my dotfiles repo](https://github.com/thebouv/dotfiles) and run `./bootstrap.sh` to install them.  My dotfiles actually need some love to add in a few random things, or to even simplify pieces that I don't utilize. If you compare my [dotfiles](https://github.com/thebouv/dotfiles) to that of the [parent repo](https://github.com/mathiasbynens/dotfiles) you can see I've already done a few passes of simplification.

```sh
git clone https://github.com/thebouv/dotfiles
cd dotfiles
./bootstrap.sh
```

### Firefox

I open Safari once on the machine to download Firefox. I just can't get used to Safari and I prefer a lot of the built in privacy features of Firefox like encrypted DNS. Not to mention the extensions system where I immediately install uBlock Origin, Facebook Container, and my password manager. I also remove Pocket from the toolbar cause I've never used it and have no intention to do so now. I try to stay as extension-lite as I can in Firefox to keep bloat down.

I should have looked to see if I could install via brew but didn't so did it the traditional way via the Firefox/Mozilla website.

### VS Code

And of course, I have to get VS Code as soon as possible. Thankfully even VS Code is installable via Brew and that's exactly what I do.

```sh
brew install --cask visual-studio-code
```

### Rectangle

Previously I used to always install Spectacle as a window management tool for OS X but it is no longer actively developed. Rectangle is the replacement and of course it is on Brew too.

I really can't function without this app. My muscle memory for moving windows around is strongly keyboard based and when setting up Rectangle it forgivingly allowed me to use Spectacle shortcut combos without needing to learn new ones for Rectangle.

I actually need to switch this personal laptop over to it as well.

```sh
brew install --cask rectangle
```

## Physical stuff

Because I am known to be a fan of stickers for my laptops I immediately have to buy some things.

First up is a hard plastic shell for the laptop itself. It is a shame to hide the slick looking dark metal casing, but I can't have any stickers potentially gumming it up. Plus, adding a case gives it more protection and a way to swap out cases if I want new stickers or a new look in the future.

My last work laptop had a light purple look to it with a matte finish, but I found the matte didn't take as well as gloss to removing stickers over time if they start to peel.

So my new case is bright orange, gloss, and comes with a silicone keyboard cover. It's nice that this is a bundle cause I always buy keyboard covers for MacBook Pros as well. Their keyboards have been known on some models to be very sensitive to dust (looking at you butterfly keyboard on my personal laptop).

<img src="/images/maccase.png" alt="product image for the orange case I bought for my mac">

And of course I need to buy stickers next. Usually I can pull from my stacks and stacks of left overs. But most of those are programming related and my career has shifted over time to more [Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code) and other [DevOps tooling](https://en.wikipedia.org/wiki/DevOps) related.

So now I'm on the hunt for stickers for TerraForm, Jenkins, AWS and Azure, and more. Eventually I'll edit this post and add in pics of the laptop once it is all covered up in sticker goodness.

## That's all?!

Not really. I'm also going to install things specifically for work like Terraform, Azure and AWS CLI clients, Docker, and tools specifically for work. I didn't go into detail for each because pretty much everything I've said above is what I'd do on any new dev machine, even a personal one.

I'll post soon about my new role and likely more about my specific tooling for that as well.