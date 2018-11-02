#!/usr/bin/python

# Required chrome-driver, splinter, lorem
# $ pip install splinter lorem
# ChromeDriver under FreeBSD https://stackoverflow.com/questions/9861830/chromedriver-under-freebsd
# Please note that if you prefer to use Firefox you will need to install Gekodriver https://github.com/mozilla/geckodriver/releases
# How to setup: http://splinter.readthedocs.io/en/latest/drivers/chrome.html

# To run:
# pipenv install
# pipenv run python submit.py

import time
import random
from transliterate import translit, get_available_language_codes
from transliterate.contrib.apps.translipsum import TranslipsumGenerator
from splinter import Browser
import os

# Randomly select a language. EN will cause errors at this time.
languages = ['el', 'hy', 'ka', 'ru']
lorem = TranslipsumGenerator(language_code=random.choice(languages))

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

username = 'userB'
password = 'userB'
str1 = ''
########### END SET config section ###########

########### Lists to use for random selections ###########
person_role=['Artist','Creator','Designer','Engraver','Illustrator','Photographer','Printmaker']

type_of_resource=['text','cartographic','notated music','sound recording','sound recording-musical','sound recording-nonmusical','moving image','three dimensional object','software, multimedia','mixed material','still image']

genre=['Actuality','Adaptation','Adventure','Adventure (Nonfiction)','Ancient world','Animal','Art','Aviation','Biographical','Biographical (Nonfiction)','Buddy','Caper','Chase','Children\'s','College','Comedy','Crime','Dance','Dark comedy','Disability','Disaster','Documentary','Domestic comedy','Educational','Erotic','Espionage','Ethnic','Ethnic (Nonfiction)','Ethnographic','Experimental (for subdivisions below, see Appendix A)','Absolute','Abstract live action','Activist','Autobiographical','City symphony','Cubist','Dada','Diary','Feminist','Gay/lesbian','Intermittent animation','Landscape','Loop','Lyrical','Participatory','Portrait','Reflexive','Street','Structural','Surrealist','Text','Trance','Exploitation','Fallen woman','Family','Fantasy','Film noir','Game','Gangster','Historical','Home shopping','Horror','Industrial','Instructional','Interview','Journalism','Jungle','Juvenile delinquency','Lecture','Legal','Magazine','Martial arts','Maternal melodrama','Medical','Medical (Nonfiction)','Melodrama','Military','Music','Music video','Musical','Mystery','Nature','News','Newsreel','Opera','Operetta','Parody','Police','Political','Pornography','Prehistoric','Prison','Propaganda','Public access','Public affairs','Reality-based','Religion','Religious','Road','Romance','Science fiction','Screwball comedy','Show business','Singing cowboy','Situation comedy','Slapstick comedy','Slasher','Soap opera','Social guidance','Social problem','Sophisticated comedy','Speculation','Sponsored','Sports','Sports (Nonfiction)','Survival','Talk','Thriller','Training','Travelogue','Trick','Trigger','Variety','War','War (Nonfiction)','Western','Women','Youth','Yukon']

countries=['Africa','Antarctica','Asia','Australia','Europe','North America','South America']

places=['post office','cheese factory','convention center','club house']

languages=['Afar','Abkhazian','Achinese','Acoli','Adangme','Adyghe; Adygei','Afro-Asiatic languages','Afrihili','Afrikaans','Ainu','Akan','Akkadian','Albanian','Aleut','Algonquian languages','Southern Altai','Amharic','English, Old (ca.450-1100)','Angika','Apache languages','Arabic','Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)','Aragonese','Armenian','Mapudungun; Mapuche','Arapaho','Artificial languages','Arawak','Assamese','Asturian; Bable; Leonese; Asturleonese','Athapascan languages','Australian languages','Avaric','Avestan','Awadhi','Aymara','Azerbaijani','Banda languages','Bamileke languages','Bashkir','Baluchi','Bambara','Balinese','Basque','Basa','Baltic languages','Beja; Bedawiyet','Belarusian','Bemba','Bengali','Berber languages','Bhojpuri','Bihari languages','Bikol','Bini; Edo','Bislama','Siksika','Bantu languages','Tibetan','Bosnian','Braj','Breton','Batak languages','Buriat','Buginese','Bulgarian','Burmese','Blin; Bilin','Caddo','Central American Indian languages','Galibi Carib','Catalan; Valencian','Caucasian languages','Cebuano','Celtic languages','Czech','Chamorro','Chibcha','Chechen','Chagatai','Chinese','Chuukese','Mari','Chinook jargon','Choctaw','Chipewyan; Dene Suline','Cherokee','Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic','Chuvash','Cheyenne','Chamic languages','Montenegrin','Coptic','Cornish','Corsican','Creoles and pidgins, English based','Creoles and pidgins, French-based','Creoles and pidgins, Portuguese-based','Cree','Crimean Tatar; Crimean Turkish','Creoles and pidgins','Kashubian','Cushitic languages','Welsh','Czech','Dakota','Danish','Dargwa','Land Dayak languages','Delaware','Slave (Athapascan)','German','Dogrib','Dinka','Divehi; Dhivehi; Maldivian','Dogri','Dravidian languages','Lower Sorbian','Duala','Dutch, Middle (ca.1050-1350)','Dutch; Flemish','Dyula','Dzongkha','Efik','Egyptian (Ancient)','Ekajuk','Greek, Modern (1453-)','Elamite','English','English, Middle (1100-1500)','Esperanto','Estonian','Basque','Ewe','Ewondo','Fang','Faroese','Persian','Fanti','Fijian','Filipino; Pilipino','Finnish','Finno-Ugrian languages','Fon','French','French','French, Middle (ca.1400-1600)','French, Old (842-ca.1400)','Northern Frisian','Eastern Frisian','Western Frisian','Fulah','Friulian','Ga','Gayo','Gbaya','Germanic languages','Georgian','German','Geez','Gilbertese','Gaelic; Scottish Gaelic','Irish','Galician','Manx','German, Middle High (ca.1050-1500)','German, Old High (ca.750-1050)','Gondi','Gorontalo','Gothic','Grebo','Greek, Ancient (to 1453)','Greek, Modern (1453-)','Guarani','Swiss German; Alemannic; Alsatian','Gujarati','Gwich\'in','Haida','Haitian; Haitian Creole','Hausa','Hawaiian','Hebrew','Herero','Hiligaynon','Himachali languages; Western Pahari languages','Hindi','Hittite','Hmong; Mong','Hiri Motu','Croatian','Upper Sorbian','Hungarian','Hupa','Armenian','Iban','Igbo','Icelandic','Ido','Sichuan Yi; Nuosu','Ijo languages','Inuktitut','Interlingue; Occidental','Iloko','Interlingua (International Auxiliary Language Association)','Indic languages','Indonesian','Indo-European languages','Ingush','Inupiaq','Iranian languages','Iroquoian languages','Icelandic','Italian','Javanese','Lojban','Japanese','Judeo-Persian','Judeo-Arabic','Kara-Kalpak','Kabyle','Kachin; Jingpho','Kalaallisut; Greenlandic','Kamba','Kannada','Karen languages','Kashmiri','Georgian','Kanuri','Kawi','Kazakh','Kabardian','Khasi','Khoisan languages','Central Khmer','Khotanese; Sakan','Kikuyu; Gikuyu','Kinyarwanda','Kirghiz; Kyrgyz','Kimbundu','Konkani','Komi','Kongo','Korean','Kosraean','Kpelle','Karachay-Balkar','Karelian','Kru languages','Kurukh','Kuanyama; Kwanyama','Kumyk','Kurdish','Kutenai','Ladino','Lahnda','Lamba','Lao','Latin','Latvian','Lezghian','Limburgan; Limburger; Limburgish','Lingala','Lithuanian','Mongo','Lozi','Luxembourgish; Letzeburgesch','Luba-Lulua','Luba-Katanga','Ganda','Luiseno','Lunda','Luo (Kenya and Tanzania)','Lushai','Macedonian','Madurese','Magahi','Marshallese','Maithili','Makasar','Malayalam','Mandingo','Maori','Austronesian languages','Marathi','Masai','Malay','Moksha','Mandar','Mende','Irish, Middle (900-1200)','Mi\'kmaq; Micmac','Minangkabau','Uncoded languages','Macedonian','Mon-Khmer languages','Malagasy','Maltese','Manchu','Manipuri','Manobo languages','Mohawk','Mongolian','Mossi','Maori','Malay','Multiple languages','Munda languages','Creek','Mirandese','Marwari','Burmese','Mayan languages','Erzya','Nahuatl languages','North American Indian languages','Neapolitan','Nauru','Navajo; Navaho','Ndebele, South; South Ndebele','Ndebele, North; North Ndebele','Ndonga','Low German; Low Saxon; German, Low; Saxon, Low','Nepali','Nepal Bhasa; Newari','Nias','Niger-Kordofanian languages','Niuean','Dutch; Flemish','Norwegian Nynorsk; Nynorsk, Norwegian','Bokmål, Norwegian; Norwegian Bokmål','Nogai','Norse, Old','Norwegian','N\'Ko','Pedi; Sepedi; Northern Sotho','Nubian languages','Classical Newari; Old Newari; Classical Nepal Bhasa','Chichewa; Chewa; Nyanja','Nyamwezi','Nyankole','Nyoro','Nzima','Occitan (post 1500)','Ojibwa','Oriya','Oromo','Osage','Ossetian; Ossetic','Turkish, Ottoman (1500-1928)','Otomian languages','Papuan languages','Pangasinan','Pahlavi','Pampanga; Kapampangan','Panjabi; Punjabi','Papiamento','Palauan','Persian, Old (ca.600-400 B.C.)','Persian','Philippine languages','Phoenician','Pali','Polish','Pohnpeian','Portuguese','Prakrit languages','Provençal, Old (to 1500);Occitan, Old (to 1500)','Pushto; Pashto','Reserved for local use','Quechua','Rajasthani','Rapanui','Rarotongan; Cook Islands Maori','Romance languages','Romansh','Romany','Romanian; Moldavian; Moldovan','Romanian; Moldavian; Moldovan','Rundi','Aromanian; Arumanian; Macedo-Romanian','Russian','Sandawe','Sango','Yakut','South American Indian languages','Salishan languages','Samaritan Aramaic','Sanskrit','Sasak','Santali','Sicilian','Scots','Selkup','Semitic languages','Irish, Old (to 900)','Sign Languages','Shan','Sidamo','Sinhala; Sinhalese','Siouan languages','Sino-Tibetan languages','Slavic languages','Slovak','Slovak','Slovenian','Southern Sami','Northern Sami','Sami languages','Lule Sami','Inari Sami','Samoan','Skolt Sami','Shona','Sindhi','Soninke','Sogdian','Somali','Songhai languages','Sotho, Southern','Spanish; Castilian','Albanian','Sardinian','Sranan Tongo','Serbian','Serer','Nilo-Saharan languages','Swati','Sukuma','Sundanese','Susu','Sumerian','Swahili','Swedish','Classical Syriac','Syriac','Tahitian','Tai languages','Tamil','Tatar','Telugu','Timne','Tereno','Tetum','Tajik','Tagalog','Thai','Tibetan','Tigre','Tigrinya','Tiv','Tokelau','Klingon; tlhIngan-Hol','Tlingit','Tamashek','Tonga (Nyasa)','Tonga (Tonga Islands)','Tok Pisin','Tsimshian','Tswana','Tsonga','Turkmen','Tumbuka','Tupi languages','Turkish','Altaic languages','Tuvalu','Twi','Tuvinian','Udmurt','Ugaritic','Uighur; Uyghur','Ukrainian','Umbundu','Undetermined','Urdu','Uzbek','Vai','Venda','Vietnamese','Volapük','Votic','Wakashan languages','Wolaitta; Wolaytta','Waray','Washo','Welsh','Sorbian languages','Walloon','Wolof','Kalmyk; Oirat','Xhosa','Yao','Yapese','Yiddish','Yoruba','Yupik languages','Zapotec','Blissymbols; Blissymbolics; Bliss','Zenaga','Standard Moroccan Tamazight','Zhuang; Chuang','Chinese','Zande languages','Zulu','Zuni','No linguistic content; Not applicable','Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki']

physical_description=['videorecording','unspecified','text','tactile material','sound recording','remote-sensing image','projected graphic','notated music','nonprojected graphic','motion picture','microform','map','kit','globe','electronic resource']

date_of_Award=['December 2016','May 2017','August 2017','December 2017','May 2018','August 2018','December 2018','May 2019','August 2019','December 2020','May 2020','August 2020']

publishers=['Academic Search','Aerospace & High Technology Database','African Journals OnLine (AJOL)','AgeLine','AGRICOLA: Agricultural Online Access','AGRIS: Agricultural database','Airiti Inc','Analytical Abstracts','Analytical sciences digital library','Anthropological Index Online','Anthropological Literature','Arachne','Arnetminer','Arts & Humanities Citation Index','arXiv','ASCE Library','Association for Computing Machinery Digital Library','Astrophysics Data System','ATLA Religion Database','AULIMP: Air University Library\'s Index to Military Periodicals','BASE: Bielefeld Academic Search Engine','Beilstein database','Biological Abstracts','BioOne','Bioinformatic Harvester','Book Review Index Online','Books In Print','CAB Abstracts','Chemical Abstracts Service','Chemisches Zentralblatt Structural Database','ChemXSeer','Chinese Social Science Citation Index','CINAHL: Cumulative Index to Nursing and Allied Health','CiNii','CHBD: Circumpolar Health Bibliographic Database','Citebase Search','CiteULike','CiteSeer','CiteSeerX','Civil engineering database','Cochrane Library','CogPrints: Cognitive Sciences Eprint Archives','The Collection of Computer Science Bibliographies','Compendex','Current Index to Statistics','Current Contents','Directory of Open Access Journals','dblp computer science bibliography','EconBiz','EconLit','EMBASE','ERIC: Educational Resource Information Center','Europe PMC','FSTA – Food Science and Technology Abstracts','GENESIS','GeoRef','Global Health','Golm Metabolome Database','Google Scholar','HCI Bibliography','HubMed','IEEE Xplore','Index Copernicus','Information Bridge: Department of Energy Scientific and Technical Information','Informit','IngentaConnect','Indian Citation Index','IARP','Inspec','INSPIRE-HEP','International Directory of Philosophy','JournalSeek','JSTOR: Journal Storage','','Jurn','Lesson Planet','LexisNexis','Lingbuzz','Linguamatics','MathSciNet','MEDLINE','MedlinePlus','Mendeley','Merck Index','Meteorological and Geoastrophysical Abstracts','NBER: National Bureau of Economic Research','Microsoft Academic','MyScienceWork','National Criminal Justice Reference Service[98]','National Diet Library Collection','OAIster','OpenEdition.org','OpenSIGLE','Paperity','Philosophy Documentation Center eCollection','Philosophy Research Index','PhilPapers','POIESIS: Philosophy Online Serials','POPLINE','Project MUSE','PsycINFO','Psychology\'s Feminist Voices','PubChem','PubMed','PubPsych','Questia: Online Research Library','Readers\' Guide to Periodical Literature','Reader\'s Guide Retrospective: 1890–1982','RePEc: Research Papers in Economics','Reader\'s Guide Retrospective: 1890–1982','RePEc: Research Papers in Economics','Rock\'s Backpages','Russian Science Citation Index','SafetyLit','SciELO','Science.gov','Science Accelerator','Science Citation Index','ScienceOpen','Scientific Information Database (SID)','SCIndeks - Serbian Citation Index','Science Direct','Scopus','SearchTeam','Semantic Scholar','Social Science Citation Index','Socol@r: Socolar','SPRESI Database','SSRN: Social Science Research Network','Sparrho','INSPIRE-HEP','SpringerLink','Ulrich\'s Periodicals Directory','VET-Bib','Web of Science','WestLaw','WorldCat','WorldWideScience','Zasshi Kiji Sakuin: Japanese Periodicals Index','Zentralblatt MATH','The Zoological Record']

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

# Check to see if role exist
with Browser('chrome') as browser:
    browser.visit(url)
    browser.fill('name', 'admin')
    browser.fill('pass', 'islandora')
    button = browser.find_by_id('edit-submit')
    button.click()
    print ('\n\nInitial Checks for user roles\n\tGoing to http://localhost:8000/admin/people')
    browser.visit('http://localhost:8000/admin/people/permissions/roles')
    # time.sleep(3)
    if browser.is_text_not_present('submitter'):
        print ('\tno submitter role')
        browser.fill('name', 'submitter')
        button = browser.find_by_id('edit-add')
        button.click()
        # time.sleep(3)
        print('\tFinding the role to edit.')
        edit_role_for_user = browser.find_by_xpath("//td[. = 'edit role']/following-sibling::td/a")
        edit_role_for_user.last.click()
        # time.sleep(3)
        print ('\tgrabbing the role id')
        current_url = browser.url
        slashparts = current_url.split('/')
        str1 = ''.join(slashparts[-1:])
        browser.find_by_css("input#edit-" + str1 + "-ingest-fedora-objects.rid-" + str1 + ".form-checkbox.real-checkbox").click()
        browser.find_by_css("input#edit-" + str1 + "-manage-object-properties.rid-" + str1 + ".form-checkbox.real-checkbox").click()
        browser.find_by_css("input#edit-" + str1 + "-view-old-datastream-versions.rid-" + str1 + ".form-checkbox.real-checkbox").click()
        button = browser.find_by_id('edit-submit')
        button.click()
    print('\tUser roles ready...\n')
    # time.sleep(5)

print('Initial Checks for non-admin user account\nCheck to see if ' + str(username) + ' exist')
with Browser('chrome') as browser:
    browser.visit(url)
    browser.fill('name', 'admin')
    browser.fill('pass', 'islandora')
    button = browser.find_by_id('edit-submit')
    button.click()

    print ('\tLooking at list of users for ' + str(username))
    browser.visit('http://localhost:8000/admin/people')
    if browser.is_text_not_present(username):
        print ('\tno' + str(username))
        browser.visit('http://localhost:8000/admin/people/create')
        browser.fill('name', str(username))
        browser.fill('mail', 'userb@example.com')
        browser.fill('pass[pass1]', str(password))
        browser.fill('pass[pass2]', str(password))
        browser.check('roles[' + str1 + ']')
        button = browser.find_by_id('edit-submit')
        button.click()
        print('\t' + str(username) + ' created.\n')
    print('\tNon-admin user account is ready...\n\n')
    # time.sleep(5)

print (' ^^^^^^^^^^^ starting with user submissions ^^^^^^^^^^^ ')
counter = 0

########### user submissions Audio Collection ###########
########### END user submissions Audio Collection #######

########### user submissions basic image ###########
while (counter < how_many_submissions_to_submit):
    with Browser('chrome') as browser:
        print ('\n \t<-------------- #' + str(how_many_submissions_to_submit-counter) + ' of user submissions basic image -------------->')
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
        browser.fill('titleInfo[title]', str(time.strftime("%m/%d/%Y %H:%M:%S"))+' '+lorem.generate_sentence())
        browser.fill('titleInfo[subTitle]', str(time.strftime("%m/%d/%Y %H:%M:%S"))+' '+lorem.generate_sentence())
        browser.fill('name[0][namePart]', random.choice(name_of_person))
        browser.fill('name[0][role]', random.choice(person_role))
        browser.find_option_by_text(random.choice(type_of_resource)).click()
        browser.fill('genre', random.choice(genre))
        browser.fill('originInfo[dateIssued]', '2018')
        browser.fill('originInfo[publisher]', random.choice(publishers))
        browser.fill('originInfo[country]', random.choice(countries))
        browser.fill('originInfo[place]', random.choice(places))
        browser.fill('language', random.choice(languages))

        browser.fill('abstract', lorem.generate_paragraph())
        browser.fill('identifier', str(time.strftime("%Y%m%d%H%M%S")))

        browser.find_option_by_text(random.choice(physical_description)).click()
        browser.fill('physicalDescription[extent]', '1 online resource (78 pages)')

        browser.fill('note',lorem.generate_sentence())

        browser.fill('subject[topic][0]',lorem.generate_sentence())
        browser.fill('subject[geographic][0]',lorem.generate_sentence())
        browser.fill('subject[temporal][0]',lorem.generate_sentence())

        browser.find_option_by_text(random.choice(countries)).click()

        browser.fill('subject[hierarchicalGeographic][country]',lorem.generate_sentence())
        browser.fill('subject[hierarchicalGeographic][province]',lorem.generate_sentence())
        browser.fill('subject[hierarchicalGeographic][region]',lorem.generate_sentence())
        browser.fill('subject[hierarchicalGeographic][county]',lorem.generate_sentence())
        browser.fill('subject[hierarchicalGeographic][city]',lorem.generate_sentence())
        browser.fill('subject[hierarchicalGeographic][citySection]',lorem.generate_sentence())
        browser.fill('subject[cartographics][coordinates]','37° 27.432′ N, 115° 28.962′ W')

        print ('\tclicking Next to the upload page')
        button = browser.find_by_id('edit-next')
        button.click()

        # time.sleep(1)
        print ('\tuploading file(s)')
        browser.attach_file('files[file]', str(supplimental_file))
        browser.find_by_name('file_upload_button').first.click()

        print ('\tClicking Injest')
        button = browser.find_by_id('edit-next')
        button.click()

        print ('\tPausing for ingest to complete')
        # time.sleep(3)
        print ('\t' + str(browser.url) + '\n\n')
        counter = counter + 1
########### END user submissions basic image ###########


########### user submissions Book Collection ###########
########### END user submissions Book Collection #######

########### user submissions Citations ###########
########### END user submissions Citations #######

########### user submissions Compound Collection ###########
########### END user submissions Compound Collection #######

########### user submissions Disk Image Collection ###########
########### END user submissions Disk Image Collection #######

########### user submissions Entity Collection ###########
########### END user submissions Entity Collection #######

########### user submissions Large Image Collection ###########
########### END user submissions Large Image Collection #######

########### user submissions Newspaper Collection ###########
########### END user submissions Newspaper Collection #######

########### user submissions PDF Collection ###########
########### END user submissions PDF Collection #######

########### user submissions Video Collection ###########
########### END user submissions Video Collection #######

########### user submissions Web ARChive Collection ###########
########### END user submissions Web ARChive Collection #######
