import sqlite3
import pymysql
from imapclient import IMAPClient

# Database config
connection = sqlite3.connect("mercadolibre.db")
cursor = connection.cursor()

cursor.execute("""DROP TABLE email;""")

sql_command = """
CREATE TABLE email (
id INTEGER PRIMARY KEY,
fromEmail VARCHAR(30),
subject VARCHAR(30),
date DATE);"""

cursor.execute(sql_command)


# Gmail account info
HOST = "imap.gmail.com"
USERNAME = "sebastiangracia123"
PASSWORD = "SEBASTIAN1994Qwerty"
ssl = True

## Connect we connect to the IMAPClient server, login and the select INBOX folder.
server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)
select_info = server.select_folder('INBOX', readonly=True)

# We then proceed to search for all emails that have the word 'DevOps' either in the subject and the body.
messagesBody = server.search(['BODY' ,'DevOps'])
messagesSubject =server.search(['SUBJECT' ,'DevOps'])

body = server.fetch(messagesBody, ['ENVELOPE']).items();
subject = server.fetch(messagesSubject, ['ENVELOPE']).items();


# We declare 3 lists; one for the date field, from and subject.
date = []
fromEmail = []
finalSender = []
subjects = []
ids = []


## We extract from the Envelope the subject, from and date fields and insert them in to the preovious declared lists.


insert_query = """INSERT INTO email (id, fromEmail, subject, date) 
                VALUES ("{ids}", "{fromEmail}", "{subject}", "{date}");"""


## We iterate the body 
for msgid, data in body: ## Is a tuple
    envelope = data[b'ENVELOPE']
    ids.append(msgid)
    subjects.append(envelope.subject.decode())
    fromEmail.append(envelope.from_)
    date.append(envelope.date)    
    ## Now we insert the fields into the table

for x in fromEmail:
   for y in x:
      finalSender.append(y)
      
for x in finalSender:
    print(x)      

for (a, b, c, d) in zip(ids, finalSender, subjects, date):
    sql_command = insert_query.format(ids=a, fromEmail=b, subject=c, date=d)
    cursor.execute(sql_command)

sql_query = """ SELECT * FROM email""";
cursor.execute(sql_query)
result = cursor.fetchall() 
for r in result:
    print(r)
    print('\n')    
 

 
 ##print('\n')
 ##for x in date:
 ##    print(x)
 ##print('\n')
##for x in subject:
##   print(x)
##   print('\n')


##print(len(messagesBody))
##print('\n')
##print(fromHeader)
##print('\n')


##print('%d messages in BODY' % len(messagesBody))