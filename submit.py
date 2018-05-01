#!/usr/bin/python

# Required chrome-driver, splinter, lorem
# $ pip install splinter lorem
# ChromeDriver under FreeBSD https://stackoverflow.com/questions/9861830/chromedriver-under-freebsd
# Please note that if you prefer to use Firefox you will need to install Gekodriver https://github.com/mozilla/geckodriver/releases
# How to setup: http://splinter.readthedocs.io/en/latest/drivers/chrome.html

import time
import random
import lorem
from splinter import Browser
import os

# Current working dirrectory
dir_path = os.getcwd()

########### SET config section ###########

# Set IMAGE: File path(s) need to be absolute
supplimental_file = dir_path + '/Example_ETD.jpg'

# Set PDF: Folder to look for pdfs
path_to_PDFs = (dir_path)

# Set URL:
url = "http://localhost:8000/user/"

# Set number of submissions to test:
how_many_submissions_to_submit = 0

username = 'admin'
password = 'islandora'

########### END SET config section ###########

########### Lists to use for random selections ###########
date_of_Award=['December 2016','May 2017','August 2017','December 2017','May 2018','August 2018','December 2018','May 2019','August 2019','December 2020','May 2020','August 2020']
degree_Type=['Masters Thesis','Doctoral Dissertation']
department_name=['Doctor of Philosophy','Master of Architecture','Master of Arts','Master of Landscape Architecture','Master of Music','Master of Science']
discipline=['Aerospace Engineering','Agricultural and Resource Economics','Agricultural Leadership, Education and Communications','Animal Science','Anthropology','Architecture','Biochemistry and Cellular and Molecular Biology','Biomedical Engineering','Biosystems Engineering','Biosystems Engineering Technology','Business Administration','Business Analytics','Chemical Engineering','Chemistry','Child and Family Studies','Civil Engineering','College Student Personnel','Communication and Information','Comparative and Experimental Medicine','Computer Engineering','Computer Science','Counseling','Counselor Education','Ecology and Evolutionary Biology','Economics','Education ','Educational Administration','Educational Psychology','Educational Psychology and Research','Electrical Engineering','Energy Science and Engineering','Engineering Science','English','Enomology, Plant Pathology and Nematology','Entomology and Plant Pathology','Environmental and Soil Science','Environmental Engineering','Food Science and Technology','Forestry','French','Geography','Geology','German','Higher Education Administration','History','Human Resource Management','Industrial Engineering','Information Sciences','Kinesiology','Kinesiology and Sport Studies','Landscape Architecture','Law','Life Sciences','Management Science','Material Science and Engineering','Mathematics','Mechanical Engineering','Microbiology','Modern Foreign Languages','Music','Natural Resources','Nuclear Engineering','Nursing','Nutrition','Nutritional Sciences','Philosophy','Physics','Plant Sciences','Plant, Soil and Environmental Sciences','Political Science','Psychology','Public Health','Recreation and Sport Management','Reliability and Maintainability Engineering','Retail, Hospitality, and Tourism Management','School Psychology','Social Work','Sociology','Spanish','Statistics','Teacher Education','Veterinary Medicine','Wildlife and Fisheries Science']
name_of_person=['Ada Lovelace','Niklaus Wirth','Bill Gates','James Gosling','Guido van Rossum','Ken Thompson','Donald Knuth','Brian Kernighan','Tim Berners-Lee','Bjarne Stroustrup','Linus Torvalds','Dennis Ritchie']
first_names=['Jack','James','Daniel','Conor','Sean','Adam','Noah','Lucy','Michael','Charlie','Chloe','Luke','Mia']
last_names=["Murphy","Kelly","O'Sullivan","Walsh","Smith","O'Brien","Byrne","Ryan","O'Connor","O'Neill","O'Reilly","Doyle","McCarthy","Gallagher","O'Doherty","Kennedy","Lynch","Murray","Quinn","Moore"]
name_suffix=['M.A.','M.S.','M.F.A.','LL.M','M.L.A.','M.B.A.','M.Sc.','M.Eng','A.B','B.A.','B.S.','B.E.','B.F.A.','B.Tech.','L.L.B','B.Sc.','J.D.','M.D.','D.O.','Pharm.D.','Ph.D.','Ed.D.','D.Phil.','D.B.A.','LL.D','Eng.D.','Senior','Sr','Sr.','Junior','Jr.','Jr','']
thesis_manager_email_templates=['Simple Date-only Email Template','Additional Edits Needed','Notification of Acceptance']
########### END Lists to use for random selections ###########

# Randomly pick a PDF from the directory
my_PDF = dir_path + '/' + random.choice([f for f in os.listdir(path_to_PDFs) if os.path.isfile(f) and f.endswith('.pdf')])

# Checks to see if the number if submissions meets the minimum
if how_many_submissions_to_submit < 3:
    how_many_submissions_to_submit = 3


########### user submissions basic image ###########
counter = 0
print (' ^^^^^^^^^^^ starting with user submissions ^^^^^^^^^^^ ')
while (counter < how_many_submissions_to_submit):
    with Browser('chrome') as browser:
        print ('\n \t<-------------- #' + str(how_many_submissions_to_submit-counter) + ' of user submissions -------------->')
        # Visit URL
        browser.visit(url)
        print ('\t' + str(username) + ' is logging in at ' + str(url))
        browser.fill('name', username)
        browser.fill('pass', password)

        # find the search button on the page and click it.
        button = browser.find_by_id('edit-submit')
        button.click()

        # From Profile Page click the collection to submit to.
        print ('\tGoing to http://localhost:8000/islandora/object/islandora%3Asp_basic_image_collection/manage/overview/ingest')
        browser.visit('http://localhost:8000/islandora/object/islandora%3Asp_basic_image_collection/manage/overview/ingest')

        print ('\tclicking Next to start submission')
        button = browser.find_by_id('edit-next')
        button.click()

        # Filling out the form.
        print ('\tfilling out form')
        browser.fill('titleInfo[title]', str(time.strftime("%m/%d/%Y %H:%M:%S"))+' '+lorem.sentence())
        browser.fill('titleInfo[subTitle]', str(time.strftime("%m/%d/%Y %H:%M:%S"))+' '+lorem.sentence())
        browser.fill('originInfo[dateIssued]', '2018')

        print ('\tclicking Next to the upload page')
        button = browser.find_by_id('edit-next')
        button.click()

        time.sleep(1)
        print ('\tuploading file(s)')
        browser.attach_file('files[file]', str(supplimental_file))
        browser.find_by_name('file_upload_button').first.click()

        print ('\tClicking Injest')
        button = browser.find_by_id('edit-next')
        button.click()

        print ('\tPausing for ingest to complete')
        time.sleep(15)
        print ('\t' + str(browser.url) + '\n\n')
        counter = counter + 1
########### END user submissions basic image ###########
