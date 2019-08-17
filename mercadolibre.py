import sqlite3
import pymysql
from imapclient import IMAPClient

# Database config
connection = sqlite3.connect("mercadolibre.db")
cursor = connection.cursor()

# Delete the table to prevent corrupted data.
cursor.execute("""DROP TABLE email;""")

# Query for the creation of the table:
# Field: ID, Type: Integer: PRIMARY KEY - Represents de ID of the email.
# Field: fromEmail, Type: VARCHAR - Represents the sender of the email.
# Field: subject, Type: VARCHAR - Represents the subject of the email.
# Field: date, Type: DATE - Represents the email send date.
sql_command = """
CREATE TABLE email (
id INTEGER PRIMARY KEY,
fromEmail VARCHAR(30),
subject VARCHAR(30),
date DATE);"""


# We now execute the SQL sentence.
cursor.execute(sql_command)

# Gmail account info
HOST = "imap.gmail.com"
USERNAME = "sebastiangracia123"
PASSWORD = "SEBASTIAN1994Qwerty"
ssl = True

# We connect to the IMAPClient server, login and the select INBOX folder.
server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)
select_info = server.select_folder('INBOX', readonly=True)

# We then proceed to search for all emails that have the word 'DevOps' in the subject and the body of the message.
messagesBody = server.search(['BODY' ,'DevOps'])
messagesSubject =server.search(['SUBJECT' ,'DevOps'])


# We now fetch both body and subject using the data type Envelope.
body = server.fetch(messagesBody, ['ENVELOPE']).items();
subject = server.fetch(messagesSubject, ['ENVELOPE']).items();


# We declare 4 lists; one for the date field, from, subject and finalSender that will store the sender email in a more 'human' structure.
date = []
fromEmail = []
finalSender = []
subjects = []
ids = []


# We create the INSERT SQL sentence that will allow us to persist the information of the message into the DB.
# We use prepared statements.

insert_query = """INSERT INTO email (id, fromEmail, subject, date) 
                VALUES ("{ids}", "{fromEmail}", "{subject}", "{date}");"""


# We iterate the body 
for msgid, data in body: # Is a tuple
    envelope = data[b'ENVELOPE'] # We get the Envelope type data.
    ids.append(msgid) # We storage the ID of the message.
    subjects.append(envelope.subject.decode()) # We get the subject of the message.
    fromEmail.append(envelope.from_) # We get the 
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