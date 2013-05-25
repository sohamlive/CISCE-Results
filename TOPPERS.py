#####################################
##     SUBJECT TOPPERS FINDER      ##
#####################################
# Copyright (c) Soham Banerjee, 2013
# Email - < sohamlive@ymail.com >
# Date  - 24th May,2013
# -----------------------------------
# << TOPPERS.py >>

import datetime
import sqlite3
import os
from bs4 import *

os.system('cls')
print "-"*80
print " "*25+"SUBJECT TOPPERS FINDER"
print "-"*80

# CONNECTING TO DATABASE
conn = sqlite3.connect('CISCE(X).db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# CREATING THE HTML FILE
html_doc = open('SUBJECT_TOPPERS.html' ,'a+')
html_data = "<!-- Coded by Soham Banerjee !-->"
html_style = ""

# PRINTING SOME RUBBISH TO KILL TIME
print 
print "Please Wait while the SUBJECT_TOPPERS.html file is generated."
print "This file will contain the name and marks of the toppers in each subject."

# WRITING THE HEADERS
html_data = html_data + "<html><head><title> SUBJECT TOPPERS OF ICSE 2013 </title>\n"

# THE SUBJECTS
subjects = ["ENG", "HIN", "HCG", "MATH", "SCI", "CST", "COMP", "ECO"]

# FULL NAME OF SUBJECTS
sub_full = {"ENG":"English (Language and Literature)","HIN":"Hindi","HCG":"History, Civics and Geography","MATH":"Mathematics", 
"SCI":"Science (Physics, Chemistry and Biology)", "CST":"Commercial Studies", "COMP":"Computer Applications", 
"ECO":"Economic Applications"}

# BEAUTIFYING THE HTML :-)
html_style = html_style + """<style>
    .sno{
        width:40px;
        font-family: Arial;
        background: #ffe9e9;
        text-align: center;
        font-weight: bold;        
        font-size:14px;
        height:30px;
        color:#000
    }
  .index{
        width:85px;
        font-family: Arial;
        background: #ffe9e9;
        text-align: center;
        font-weight: bold;        
        font-size:14px;
        height:30px;
    	color:#000
    }
    .name{
        width:280px;
        font-family: Arial;
        background: #ffe9e9;
        text-align: center;
        font-weight: bold;        
        font-size:14px;
        height:30px;
    	color:#000
    }
    .marks{
        width:65px;
        font-family: Arial;
        background: #ffe9e9;
        text-align: center;
        font-weight: bold;        
        font-size:14px;
        height:30px;
    	color:#000
    }
	#school_name{
        font-family:Verdana;
        font-size:20px;
        color:#205791;
        margin-left: 5px
    }
    h1{
        font-family:Verdana;
        margin-left:5px
    } 
    h2{
    	font-family:Calibri;
    	margin-left:5px;
    	margin-bottom:5px
    }
    #info{
        margin-left:5px;
        text-align:justify;
        margin-bottom:15px;
        padding:4px;
        font-family:Verdana;
        font-size:14px
    }
   table{
        margin-left: 5px;
        border-collapse:collapse
    }
    td{
        padding:2px;
        border:1px solid #cdcdcd;
    }
    .sno_data{
        text-align:center;
        width:40px
    }
    .name_data{
        text-align:left;
        width:280px;
    }
    .index_data{
        text-align:center;
    	width:85px;
    }
    .marks_data{
        text-align:center;
        width:55px;
    }
    #footer_top{
        margin-left:5px;
        border-top: 2px solid #8dc63f;
    }
    #footer{
        margin-top:1px;
        border-top:2px solid #fdc689;
        background:#f7f6f6;
        padding:5px;
        font-family:Georgia;
        color:#AAA9A9;
        font-size:13px
    }
    a{
        text-decoration:none;
        color:#0054a6
     }
    a:hover{
        text-decoration:underline;
        color:#3d91e3
    }
    tr:nth-child(even){
        background:#e9f2ff;
    }
    .under{
		line-height:2px;
		background:#7accc8;
		margin-bottom:15px;
		margin-left:5px;
		width:485px
	}
	.nope{
		color:#7accc8;
		font-size:1px
	}
	#congo{
		font-size:18px;
		color:#92278f;
		margin-bottom:2px
	}
	.nodata{
		margin-left:5px;
		width:440px;
		background:#fffce7;
		padding:2px;
		border:1px solid #ccc;
		padding-left:5px;
	}
    </style>
    """

html_data = html_data + html_style + "</head><body>"

# STARTING THE BODY
html_data = html_data + "<h1> Subject Toppers of ICSE 2013</h1> \n"

# WRITING THE SCHOOL NAME
c.execute("SELECT SCHOOL FROM Student_Result;")
row = c.fetchone()
j = row["SCHOOL"].split("\"")
html_data = html_data + "<div id=\"school_name\"> <b>{0}</b> </div> <br />".format(j[1])

# WRITING THE INFO
html_data = html_data + """<div id=\"info\">
							<div id=\"congo\">
							Congratulations!!!
							</div>
							All the students who have answered ICSE 2013, kudos to you! CISCE Board is one of the most 
							challenging in India. You have all done wonders in the examination.
							Many hours of hard work, dedication and frustration went into it. In the end you all have 
							emerged victorious. Hopes, Aspirations were touching sky high limits.
							The last minute nervousness, prayer to God before the results were declared found an echo 
							among you all. Some of the students along with their \'exceptional\'
							hard work and dedication lifted the Cup of Glory. The Cup of Glory for the year 2013 will 
							bear their name and it will remain there forever...
							</div>"""


# WRITING THE MAIN DATA
for i in range(0,8):
	c.execute("SELECT MAX({0}) FROM Student_Result;".format(subjects[i]))
	res = c.fetchone()
	html_data = html_data + "<h2> {0} </h2>".format(sub_full[(subjects[i])])
	html_data = html_data + "<div class=\"under\"><span class=\"nope\">*</span> &nbsp; </div>"
	if res[0]==0:
		html_data = html_data + "<div class=\"nodata\"> None </div>"
	else:
		c.execute("SELECT * FROM Student_Result WHERE {0}={1};".format(subjects[i],res[0]))
		html_data = html_data + """ <table class=\"toppers\">
								<tr>
								<td class=\"index\"> INDEX NO </td>
								<td class=\"name\"> NAME </td>
								<td class=\"marks\"> MARKS </td>
								</tr>"""
        rows = c.fetchall()
        sno = 0
        for row in rows:
			html_data = html_data + """<tr>
			<td class=\"index_data\">
			{0}
			</td>
			<td class=\"name_data\">
			{1}
			</td>
			<td class=\"marks_data\">
			{2}
			</td>
            </tr>""".format(row["INDEXNO"],row["NAME"],row[subjects[i]])
        html_data = html_data+"</table>"

# GETTING THE CURRENT DATE AND TIME
now = datetime.datetime.now()
current_date = now.strftime("%d %B,%Y")
current_time = now.strftime("%I:%M:%S %p")

# WRITING THE FOOTER
html_data = html_data + """</table><br />
    <div id="footer_top">
    <div id="footer">
    Generated by an automated Python script on {0} at {1}. <br />
    Coded by - <a href="http://sohamlive.wordpress.com" title="Soham's Blog">Soham Banerjee</a>
    </div>
    </div>
    <br />""".format(current_date,current_time)

# MAKING THE CODE PRETTIER :-P
soup = BeautifulSoup(html_data)
neat_data = soup.prettify()

# WRITING EVERYTHING TO THE HTML
html_doc.write(neat_data)

# CLOSING THE CURSOR
conn.close()

# OPEN HAPPINESS :-)) DONE!
print "*"*45
print "Cheers! The file is created successfully."

