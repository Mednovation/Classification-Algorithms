# Compute Engine Setup Instruction #

<!---
layout: page
mathjax: true
permalink: github.com/Mednovation/ClassificationALG/ComputeEngineSetu
-->

This document summerizes all the steps taken to setup the Google Cloud Platform Compute Engine and the other necessary comuptational resources including GPU, and storage and the like. The gola of this page is to have a refernce of steps taken to setup the run-time enviroenmtn, so it can be reolicated.

## Part One - Compute Engine Image Build
Instructions on how to create a VM in Google Cloud Platform (GCP) can be found in [here](http://cs231n.github.io/gce-tutorial/)


## Part Two - Instal Pyton and necessary enviroenmtns in VM
All steps listed below are taken from askubuntu forum in [here](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get)

### Install pyenv ###
Install headers needed to build CPythons (exotic Pythons like PyPy or Jython may have other dependencies):

```bash
sudo apt-get install -y build-essential libbz2-dev libssl-dev libreadline-dev \
                        libsqlite3-dev tk-dev

# optional scientific package headers (for Numpy, Matplotlib, SciPy, etc.)
sudo apt-get install -y libpng-dev libfreetype6-dev    
```

Run the installer script (installs pyenv and some very useful pyenv plugins by the original author; see here for more)
```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```
Add init lines to your ```bash ~/.profile or ~/.bashrc ``` (it mentions it at the end of the install script):
```bash
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Restart your shell (close & open or exec ```bash $SHELL ```) or reload the profile script. (with e.g. ```bash source ~/.bashrc ```)

### Setting up an environment ###
To not touch the system Python (generally a bad idea; OS-level services might be relying on some specific library versions, etc.) make your own environment, it's easy! Even better, no sudo, for it or pip installs!

Install your preferred Python version (this will download the source and build it for your user, no input required)
```bash
pyenv install 3.6.0
```
Make it a virtualenv so you can make others later if you want
```bash
pyenv virtualenv 3.6.0 general
```
Make it globally active (for your user)
```bash
pyenv global general
```
If you want to clean out your libraries later, you could delete the virtualenv (```bash pyenv uninstall general ```) or make a new one (```bash pyenv virtualenv 3.6.0 other_proj ```). You can also have environments active per-directory: pyenv local other_proj will drop a ```bash .python-version ``` file into your current folder and any time you invoke Python or ```bash pip-installed Python utilities ``` from it or under it, they will be shimmed by pyenv.
