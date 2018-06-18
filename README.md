# TRACE Workflow Test
This is a front end workflow testing script. This relies on [chrome webdriver](https://splinter.readthedocs.io/en/latest/drivers/chrome.html) & [Splinter](https://splinter.readthedocs.io/en/latest/)

## What does this do?
It runs several ingestion tests that create a variety of submissions while inputting a random assortment of fields from a random array of options. In other words it's testing as many combinations as it can to test if something will break the stack. The extended_test folder has an assortment of PDFs in a variety of PDF Color Space and Resolutions.

## Before you start
Add 2 users to islandora
* Username: userA
  * Password: userA
* Username: userB
  * Password: userB

## Install software and modules
Required: __chrome-driver__, [splinter](https://pypi.python.org/pypi/splinter), [lorem](https://pypi.python.org/pypi/loremipsum) <br/>

[WINDOWS 10 install Video Tutorial __Chrome-Driver__](https://youtu.be/dz59GsdvUF8)
* Create a folder `c:\webdrivers`
* System Properties > Advanced System Settings > Environment Variables > System Variables > Path > Edit > New
  * c:\webdrivers
  * Click OK/OK/OK
* Go to and download "Latest Release" > chromedriver_win32.zip
* Zip will extract to a single executable file 'chromedriver'
* Extract file to "c:\webdrivers/chromedriver"
* To test install open a command terminal and type `chromedriver` and it should start and press `ctrl c` to quit test.

### Install
Chrome WebDriver is provided by Selenium2. To use it, you need to install Selenium2 via pip
```shell
$ [sudo] pip install selenium
```

It’s important to note that you also need to have Google Chrome installed in your machine.
```terminal
$ brew install chromedriver
```

## Manually Install Chrome drivers (OPTIONAL)
[ChromeDriver install for macOS](https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/)<br/>
[ChromeDriver install for FreeBSD](https://stackoverflow.com/questions/9861830/chromedriver-under-freebsd)<br/>
[ChromeDriver install for Windows 10](https://sites.google.com/a/chromium.org/chromedriver/getting-started)<br/>
[ChromeDriver install for Ubuntu](https://developers.supportbee.com/blog/setting-up-cucumber-to-run-with-Chrome-on-Linux/)<br/>
Please note that if you prefer to use Firefox you will need to install [Gekodriver](https://github.com/mozilla/geckodriver/releases)


# How to setup [Splinter](http://splinter.readthedocs.io/en/latest/drivers/chrome.html)

```terminal
$ pip install splinter
$ pip install lorem
```

#### Fail safe way (leveraging pipenv)
```terminal
$ pip install pipenv

# this installs the modules
$ pipenv sync

# this starts the python environment (optional and not suggested)
$ pipenv shell

# To start the script
$ pipenv run python submit.py
```

To exit pipenv just type (for using with pipenv shell)
```terminal
$ exit
```

## To modify submit.py
Use the 'SET config section'

```bash
########### SET config section ###########

# Set IMAGE: File path(s) need to be absolute
supplimental_file = dir_path + '/Example_ETD.jpg'

# Set PDF: Folder to look for pdfs (this current folder for PDFs)
path_to_PDFs = (dir_path)

# Set URL: (this works for islandora_vagrant)
url = "http://localhost:8000/user/"

# Set number of submissions to test: (anything under 3 will default to 3)
how_many_submissions_to_submit = 0

username = 'userB'
password = 'userB'

str1 = ''

########### END SET config section ########
```

### SET config section

__supplimental_file__<br/>Set to current directory image file

__path_to_PDFs__<br/>This will randomly select any one of the PDFs in this directory and use it to submit.

__url__<br/>This is the URL for a page to trigger logging in. Using the 'user' page is ideal.

__how_many_submissions_to_submit__<br/>This is how many times you want the script to submit an ETD.

### Sometime the script with fail because of a timeout.
Just restart the script and it will work.
