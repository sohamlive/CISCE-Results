#####################################
##      HTML RESULT GENERATOR      ##
#####################################
# Copyright (c) Soham Banerjee, 2013
# Email - < sohamlive@ymail.com >
# Date  - 23rd May,2013
# -----------------------------------
# << HTML.py >>

import os
import datetime
import sqlite3
from bs4 import *

os.system('cls')
print "-"*80
print " "*25+"HTML RESULT GENERATOR"
print "-"*80

# CONNECTING TO DATABASE
conn = sqlite3.connect('CISCE(X).db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# PRINTING SOME RUBBISH TO KILL TIME
print 
print "Please Wait while the RESULT.html file is generated."
print "Don't worry it will not take much time."

# CREATING THE HTML FILE
html_doc = open('RESULT.html' ,'a+')
html_data = "<!-- Coded by Soham Banerjee !-->"
html_style = ""

# WRITING THE HEADERS
html_data = html_data + "<html><head><title> ICSE RESULT 2013 </title>\n"

# BEAUTIFYING THE HTML :-)
html_style = html_style + """<style>
   table{
        margin-left: 5px
    }
    td{
        padding:2px;
        border:1px solid #cdcdcd;
    }
    .index{
        width:85px;
        font-family: Arial;
        background: #005826;
        text-align: center;
        font-weight: bold;
        border:1px solid #1d47b3 !important;
        font-size:14px;
        height:30px;
    color:#fff
    }
    .name{
        width:280px;
        font-family: Arial;
        background: #00aeef;
        text-align: center;
        font-weight: bold;
        border:1px solid #1d47b3 !important;
        font-size:14px;
        height:30px;
    color:#fff
    }
    .dob{
        width:90px;
        font-family: Arial;
        background: #603913;
        text-align: center;
        font-weight: bold;
        border:1px solid #1d47b3 !important;
        font-size:14px;
        height:30px;
    color:#fff
    }
    .marks{
        width:55px;
        font-family: Arial;
        background: #662d91;
        text-align: center;
        font-weight: bold;
        border:1px solid #1d47b3 !important;
        font-size:14px;
        height:30px;
    color:#fff
    }
    .index_data{
        text-align:center;
    width:85px;
    }
    .name_data{
        text-align:left;
        width:280px;
    }
    .dob_data{
        text-align:center;
        width:90px;
    }
    .marks_data{
        text-align:center;
        width:55px;
    }
    .data_table tr:nth-child(even){
        background:#FBFBEF;
    }
    .data_table tr:hover{
        background:#8A0829;
        color:#fff;
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
    #info{
        margin-left:5px;
        text-align:justify;
        margin-bottom:15px;
        padding:4px;
        font-family:Verdana;
        font-size:14px
    }
    li{
        list-style-type:square;
        margin-top:2px;
        margin-bottom:2px
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
  </style>"""

html_data = html_data + html_style + "</head><body>"

# STARTING THE BODY
html_data = html_data + "<h1> Result of ICSE 2013 </h1> \n"

# WRITING THE SCHOOL NAME
c.execute("SELECT SCHOOL FROM Student_Result;")
row = c.fetchone()
j = row["SCHOOL"].split("\"")
html_data = html_data + "<div id=\"school_name\"> School - <b>{0}</b> </div> <br />".format(j[1])

# WRITING THE INFO
html_data = html_data + """<div id="info">
    <li>This is the mark sheet of the students who appeared for ICSE 2013 Examination held in March,2013. There are a total of 
    8 Subjects out of which students have answered for <b>6</b> subjects. </li>
    <li>Students who have answered Science did not have Commercial Studies as a subject. Similarly students who have answered 
    for Computer Applications did not have Economic Applications and vice-versa. </li>
    <li> The subjects in which a candidate has scored 0 marks may mean that the candidate did not have the subject for
    ICSE or it may mean that the candidate has scored 0 marks in the exam, which is outgraciously impropable. </li>
    <li>The candidates who did not appear for the exam(ABSENT) although their Index No is listed have been here given 
    the mark 0.</li>
    </div>"""

# WRITING THE COLUMN NAMES
html_data = html_data + """<table>
  			<tr>
				<td class=\"index\"> INDEX NO </td>
				<td class=\"name\"> NAME </td> 
				<td class=\"dob\"> DOB </td> 
				<td class=\"marks\"> ENG </td>
				<td class=\"marks\"> HIN </td>
				<td class=\"marks\"> HCG </td>
				<td class=\"marks\"> MATH </td>
				<td class=\"marks\"> SCI </td>
				<td class=\"marks\"> CST </td> 
				<td class=\"marks\"> COMP </td>
				<td class=\"marks\"> EAS </td>
				</tr>
                </table>
                <table class=\"data_table\">"""

# SQL QUERY
c.execute("SELECT * FROM Student_Result;")
rows = c.fetchall()
for row in rows:

    # WRITING THE DATA
	html_data = html_data + """
                    <tr>
					<td class=\"index_data\"> {0} </td>
					<td class=\"name_data\"> {1} </td>
					<td class=\"dob_data\"> {2} </td>
					<td class=\"marks_data\"> {3} </td>
					<td class=\"marks_data\"> {4} </td>
					<td class=\"marks_data\"> {5} </td>
					<td class=\"marks_data\"> {6} </td>
					<td class=\"marks_data\"> {7} </td>
					<td class=\"marks_data\"> {8} </td>
					<td class=\"marks_data\"> {9} </td>
					<td class=\"marks_data\"> {10} </td> 
					</tr>
                    """.format(row["INDEXNO"], row["NAME"], row["DOB"], row["ENG"], row["HIN"], row["HCG"], row["MATH"], row["SCI"], row["CST"], row["COMP"], row["ECO"]) 
	
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
