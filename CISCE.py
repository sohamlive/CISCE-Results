#####################################
##   GETTING CISCE 2013 RESULTS    ##
#####################################
# Copyright (c) Soham Banerjee, 2013
# Email - < sohamlive@ymail.com >
# Date  - 23rd May,2013
# -----------------------------------
# << CISCE.py >>

import os
import requests
import sqlite3
from bs4 import *

os.system('cls')
print "-"*80
print " "*25+"CISCE 2013 RESULTS (ICSE ONLY)"
print "-"*80

print 
print "."*37+" NOTE "+"."*37
print "1. This program will ONLY download the marks of students in CISCE(X).db"
print "2. It will work only for ENG, HIN, HCG, MATH, SCI, CST, CTA and EAS."
print "3. Please enter your school code ONLY not roll no:."
print "4. School Code (XXXX)- T/XXXX/YYY."
print "5. Run the HTML.py to get the html file."
print "."*80
print 

# VARIABLES
url = "http://cisce.examresults.net/JDK-ICSE-10th-Results-2013.aspx"
roll = 1
b = 0

# CREATING DATABASE
conn = sqlite3.connect('CISCE(X).db')
c = conn.cursor()

# CREATING TABLE
c.execute(""" CREATE TABLE IF NOT EXISTS Student_Result(
  		INDEXNO text, NAME text, SCHOOL text, DOB text, ENG int, HIN int,
			HCG int,  MATH int, SCI int, CST int, COMP int, ECO int);
	""")

print "Enter the School Code - ",
code = raw_input()
print "Please Wait..."
print "This thing is going to take some time. So have a break and enjoy it!"
print "*"*25


# SEARCHING
while True:
	resp = requests.post(url, {'center1': code, 'sno1': '{0:03}'.format(roll)})

	if "does not exist" in resp.content:
		b = b + 1

		# CHECK IF PRESENT
		if b<3:
			roll = roll + 1
		else:
			print "==> So thats it! The downloading of data is done. Cheers!"
			conn.close()
			exit()		
		
	else:
		soup = BeautifulSoup(resp.text)
		info = []
		marks = []
		student = soup.find_all("table" ,class_="sp6")

		for row in student[0].find_all("tr"):
			col = row.find_all("td")
			data = col[1].string
			info.append(str(data))

		name = info[1]
		info[1] = name.title()

		for row in student[1].find_all("tr")[1:7]:
			col = row.find_all("td")
			num = col[1].string
			if num=="XXX":
				marks.append(0)
			else:
				marks.append(int(num))

		if "SCI" in resp.content:
			marks.insert(5,0)
		if "CST" in resp.content:
			marks.insert(4,0)
		if "CTA" in resp.content:
			marks.insert(7,0)
		if "EAS" in resp.content:
			marks.insert(6,0)

		info.extend(marks)

		sql_tup = tuple(info)
		c.execute(" INSERT INTO Student_Result VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", sql_tup)
		conn.commit()
		print "Roll {0:03}".format(roll)
		roll = roll + 1

conn.close()

