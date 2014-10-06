#python code to read url and extract data

import urllib
def everything_between(text,begin,end):
    idx1=content.find(begin)
    idx2=content.find(end,idx1)
    return content[idx1+len(begin):idx2].strip()
sock = urllib.urlopen("https://www.google.com")
content = sock.read()
sock.close()
title=everything_between(content,'<title>','</title>')
print title



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


   
