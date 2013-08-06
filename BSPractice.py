from bs4 import BeautifulSoup
import urllib
from twilio.rest import TwilioRestClient

#twilio setup
account_sid = "AC07fbb49cf96f6a00b02b7a4a4ed24791"
auth_token = "398ff9cf83a11f36ddbbc8914a20d1c9"
client = TwilioRestClient(account_sid, auth_token)

# setup htmldoc
html = urllib.urlopen('http://goo.im/devs/aokp/d2vzw').read()
soup = BeautifulSoup(html)

# print title of page
print soup.title.string
print "\n"

# (obsolete) print the class of all 'td's on page that have one
for td in soup.find_all('td'):
  if 'class' in td:
    print td

# read lines into variable DBlines
DB = open('DataBase.txt', 'r')
DBlines = DB.readlines()
DB.close()

# for each td with class
# add to file if isn't already and send sms
for td in soup.find_all('td'):
  if td.get('class') != None:
    theclass = td.get('class')
    
    found = False
    for line in DBlines:
      if str(theclass) in line:
        found = True
        
    if not found:
      print theclass
      DB = open('DataBase.txt', 'a')
      DB.write(str(theclass)+'\n')
      DB.close()
      message = client.sms.messages.create(to="+15306131989", from_="+19177461990", body="New Build!!")
