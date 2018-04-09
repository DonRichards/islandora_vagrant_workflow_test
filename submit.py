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
how_many_submissions_to_submit = 10

########### END SET config section ###########

########### Lists to use for random selections ###########
users = ['userA','userB']
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


########### user submissions ###########
counter = 0
print (' ^^^^^^^^^^^ starting with user submissions ^^^^^^^^^^^ ')
while (counter < how_many_submissions_to_submit):
    with Browser('chrome') as browser:
        # Visit URL
        browser.visit(url)
        random_int = random.randint(0, 19)
        user = random.choice(users)
        print ('\n \t<-------------- ' + str(how_many_submissions_to_submit-counter) + ' -------------->')
        print ('\t' + str(user) + ' is logging in at ' + str(url))
        browser.fill('name', user)
        browser.fill('pass', user)

        # find the search button on the page and click it.
        button = browser.find_by_id('edit-submit')
        button.click()

        # From Profile Page click the collection to submit to.
        print ('\tclicking Submit to Grad Thes')
        browser.click_link_by_text('Submit Graduate Theses and Dissertations')

        # Filling out the form.
        print ('\tfilling out form')
        browser.fill('titleInfo[title]', str(time.strftime("%m/%d/%Y %H:%M:%S"))+' '+lorem.sentence())
        browser.fill('name[namePartGiven]', random.choice(first_names))
        browser.fill('name[namePartFamily]', random.choice(last_names))
        browser.fill('name[namePartTermsofAddress]', random.choice(name_suffix))
        browser.fill('name[valueURI]', '1234-1234-1234-1234')
        browser.find_option_by_text(random.choice(date_of_Award)).first.click()
        browser.find_option_by_text(random.choice(degree_Type)).first.click()
        browser.find_option_by_text(random.choice(department_name)).first.click()
        browser.find_option_by_text(random.choice(discipline)).first.click()

        # Thesis advisor
        browser.fill('advisor[0][namePartGiven]', random.choice(name_of_person))
        browser.fill('advisor[0][namePartFamily]', random.choice(name_of_person))

        # Committee Member
        browser.fill('committee[0][namePartGiven]', random.choice(name_of_person))
        browser.fill('committee[0][namePartFamily]', random.choice(name_of_person))
        browser.fill('abstract', lorem.paragraph())
        browser.fill('note', lorem.paragraph())

        # Keyword(s) generator
        keywords_count = random.randint(0, 5)
        keywords_string = ''
        while (keywords_count>0):
            keywords_string += random.choice(discipline)
            if (keywords_count > 1):
                keywords_string += ','
            keywords_count -= 1
        browser.fill('keywords', keywords_string)
        button = browser.click_link_by_id('edit-next')
        print ('\tclicked next')

        # Incase there's an issue loading the page
        time.sleep(1)
        print ('\tuploading file(s)')
        browser.check('certifying[certify]')
        browser.attach_file('files[file]', str(my_PDF))
        browser.find_by_name('file_upload_button').first.click()
        browser.check('supply_supplemental')
        supplimental_files_added = 0
        while (random_int>0):
            browser.attach_file('files[file'+str(random_int)+']', supplimental_file)
            random_int = random_int-1
            supplimental_files_added += 1
        print ('\t' + str(supplimental_files_added) + ' of supplimental files added')
        # input("Press Enter to continue...")
        # Submit
        browser.find_by_id('edit-next').click()
        #input("Press Enter to continue...")
        print ('\tsubmitting')
        time.sleep(15)
        print(browser.url)
        counter = counter + 1
        # input("Press Enter to continue...")

########### END user submissions ###########


########### thesis manager edit tests ###########
with Browser('chrome') as browser:
    print ('\n\n^^^^^^^^^^^ Now Thesis Manager ^^^^^^^^^^^ \n logging in')
    browser.visit(url)
    browser.fill('name', 'thesis_manager')
    browser.fill('pass', 'thesis_manager')
    # find the search button on the page and click it.
    print ('\tclicking the submit Grad Thes text')
    button = browser.find_by_id('edit-submit')
    button.click()
    for i in range(3):
        print ('\n\t<-------------- clicks item ' + str(i) + ' in list -------------->')
        browser.click_link_by_text('Items to Accept')
        print ('\tselects item ' + str(i) + ' in the list')
        xpath_for_a_submission = '//*[@id="trace-ext-workflow-form"]/div/table[2]/tbody/tr[' + str(i+1) + ']/td[2]/a'
        button = browser.find_by_xpath(xpath_for_a_submission)
        button.click()
        print ('\tmanage files for the submission and clicks edit metadata')
        browser.click_link_by_text('Manage Files')
        browser.click_link_by_text('edit')
        # Old title with new one
        print ('\tchanges the title')
        title_was = browser.find_by_tag("textarea").first.value
        browser.fill('titleInfo[title]', title_was + ' Modified Successfully by thesis_manager')
        print ('\tsaved changes')
        browser.find_by_id('edit-update').click()
        print ('\tsends email')
        browser.find_option_by_text(random.choice(thesis_manager_email_templates)).first.click()
        button = browser.find_by_xpath('//*[@id="tm_mail"]/form/input')
        button.click()
        browser.click_link_by_text('View the Previous Messages')
        print ('\tviewed messages')
        print ('\tnavigates to Items to accept list')
        browser.visit(url)
    # Time to Accept a few
    browser.visit(url)
    print ('\nnavigates to Items to accept list and clicks check boxes for the first 2 items')
    browser.click_link_by_text('Items to Accept')
    browser.find_by_xpath('//*[@id="trace-ext-workflow-form"]/div/table[2]/tbody/tr[1]/td[1]/div')[0].click()
    browser.find_by_xpath('//*[@id="trace-ext-workflow-form"]/div/table[2]/tbody/tr[2]/td[1]/div')[0].click()
    browser.find_by_id('edit-submit-accepted').click()
    browser.find_by_id('edit-confirm-accept').click()
    print ('\tsubmissions accepted')
    # Time to Publish 1
    for j in range(3):
        print ('\nnavigates to Items to Publish list')
        browser.click_link_by_text('Items to Publish')
        browser.find_by_xpath('//*[@id="islandora-simple-workflow-manage-form"]/div/div/table[2]/tbody/tr[1]/td[1]/div').click()
        print ('\tselects the 1st item and submits')
        button = browser.click_link_by_id('edit-submit-selected')
        button = browser.click_link_by_id('edit-confirm-submit')
        time.sleep(5)
print ('\n\n all done!')
########### END thesis manager edit tests ###########
