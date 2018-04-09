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

## Install modules
```terminal
pip install splinter
pip install lorem
```

#### Fail safe way (leveraging pipenv)
```terminal
pip install pipenv

# this installs the modules
pipenv sync

# this starts the python environment
pipenv shell

# To start the script
pipenv run python submit.py
```

To exit pipenv just type
```terminal
exit
```

## To modify submit.py
Use the 'SET config section'

```terminal
########### SET config section ###########

...

########### END SET config section ########
```

### SET config section

__supplimental_file__<br/>Set to current directory image file

__path_to_PDFs__<br/>This will randomly select any one of the PDFs in this directory and use it to submit.

__url__<br/>This is the URL for a page to trigger logging in. Using the 'user' page is ideal.

__how_many_submissions_to_submit__<br/>This is how many times you want the script to submit an ETD.

### Sometime the script with fail because of a timeout.
Just restart the script and it will work.
