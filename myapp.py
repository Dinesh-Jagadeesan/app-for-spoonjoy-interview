#python code to read url and extract data

import urllib ,mysql.connector
def everything_between(text,begin,end):
    idx1=content.find(begin)
    idx2=content.find(end,idx1)
    return content[idx1+len(begin):idx2].strip()
url=request.get('url')    
sock = urllib.urlopen(url)
content = sock.read()
sock.close()
title=everything_between(content,'<title>','</title>')
print title



con = mysql.connector.connect(user='myapp', password='',host='127.0.0.1',database='myapp')
                              
cur = con.cursor()
cur.execute("DELETE * FROM MYAPP");
cur.execute("INSERT INTO MYAPP(TITLE)VALUES (theTitle)");

print "Do u wish to update(Y/N) :";
inq=raw_input();
if inq=='Y'or inq=='y'
   cur.execute("UPDATE MYAPP SET TITLE = '%s' "% (in));

print "Do u want to view databse:(Y/N)";
inw=raw_input();
if inw=='Y'or inw=='y'
   cur.execute("SELECT * FROM MYAPP");
   results = cursor.fetchall()
   for row in results:
      title = row[0]
      print "Title: %s:" %(title)


   
