# Sebastián Gracia
# Mercado Libre code challenge. Option 2
# https://github.com/sebasgraciavalderrama/codechallenge

import sqlite3
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
# I've created a dummy account to all the testing.
HOST = "imap.gmail.com"
USERNAME = "sebasgraciamercadolibre"
PASSWORD = "mercadolibre123"
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
for msgid, data in body: # It's a tuple
    envelope = data[b'ENVELOPE'] # We get the Envelope type data.
    ids.append(msgid) # We storage the ID of the message.
    subjects.append(envelope.subject.decode()) # We get the subject of the message.
    fromEmail.append(envelope.from_) # We get the sender email. We will come to this later.
    date.append(envelope.date) # We get the date.

# We have to iterate fromEmail since it has a different structure, we want to get the name and email of the sender in a single string.
for x in fromEmail:
   for y in x:
      finalSender.append(y) # We add the sender email to finalSender. i.e: 'Sebastian Gracia <sebastiangracia123@gmail.com>' 
      
    
# At this point we have checked if the word exists in the body of a message. We must check the envelope fetched from the subject and repeat the previous loop.
# It is important to mention that the word can be inside the subject and the body of the message. 
# That is why we must check if the record exist in the ids list and if it does exist we won't add it.
# If it does not exist we must add it. If we don't do this we will have duplicated records.
     
for msgid, data in subject: # It's a tuple
    envelope = data[b'ENVELOPE'] # We get the Envelope type data.
    for msgidBody in ids:
        if msgidBody != msgid:          
            ids.append(msgid) # We storage the ID of the message.
            subjects.append(envelope.subject.decode()) # We get the subject of the message.
            fromEmail.append(envelope.from_) # We get the sender email. We will come to this later.
            date.append(envelope.date) # We get the date.

# We now go through the lists and add each value to the table 'email'.
for (a, b, c, d) in zip(ids, finalSender, subjects, date):
    sql_command = insert_query.format(ids=a, fromEmail=b, subject=c, date=d)
    cursor.execute(sql_command) # We must execute the INSERT query for each set of values.


# We now fecth all the rows from the table.
sql_query = """ SELECT * FROM email""";
cursor.execute(sql_query)
result = cursor.fetchall() 

# We print them via console.
for r in result:
    print(r)
    print('\n')    
