#python code to read url and extract data

import urllib, urlparse, string, mysql.connector
url=request.get('url')

def getPage(theURL):
  page = urllib.urlopen(theURL)
	theHTML = page.read()
	return theHTML
def extractTitle(theLine):
	
	titleStart = theLine.find("<title>")
	if titleStart > -1:
		titleStart = titleStart + 7
		titleEnd = theLine.find("</title>")
		theTitle = theLine[titleStart:titleEnd]
		theTitle = theTitle.strip() 
	else:
		theTitle = ""
		
	return(theTitle)

thePageHTML = getPage(url)
theTitle = extractTitle(thePageHTML)
print theTitle




con = mysql.connector.connect(user='myapp', password='',host='127.0.0.1',database='myapp')
                              
cur = con.cursor()
cur.execute("DELETE * FROM MYAPP");
cur.execute("INSERT INTO MYAPP(TITLE)VALUES (theTitle)");

print "Do u wish to update(Y/N) :";
in=raw_input();
if in=='Y'||in=='y'
   cur.execute("UPDATE MYAPP SET TITLE = '%s' "% (in));

print "Do u want to view databse:(Y/N)";
in1=raw_input();
if in1=='Y'||in1=='y'
   cur.execute("SELECT * FROM MYAPP");
   results = cursor.fetchall()
   for row in results:
      title = row[0]
      print "Title: %s:" %(title)


   
