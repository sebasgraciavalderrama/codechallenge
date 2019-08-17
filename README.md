# Mercado Libre Code Challenge - Sebastián Gracia - Option 2 :game_die:
Welcome to my code challenge for Mercado Libre.

## BACKGROUND: :email: :inbox_tray:
Access a Gmail account and look for the word 'DevOps' inside the Subject and the Body of a message.
After finding the messages with the specified word, create a DB in MySQL and persist the following fields into the a table:
1. Sender email.
2. Subject of the message.
3. Date of the message.

## CONSTRAINTS: :no_entry_sign:
1. Free choice of programing language.
2. Database must be MySQL.
3. Email account must be a Gmail valid account.
4. Must be submitted to the recruiter email before Friday, August 16th midnight.
5. Must be public for further analysis.

## DEVELOPMENT: :computer:
I've decided to develop the software in Python3 using Anaconda environment - Spyder IDE.
There are 2 ways of solving this challenge:
1. Using libraries such as: IMAPCLient, POP, IMAP, etc.
2. Using Google Gmail API Services.

I chose the option number 2 for the following reason:
**Time** The recruiter gave enough me time to develop the challenge but due to other commitments that required my full attention I was unable to study and fully understand the documentation provided by Google Developer site.
Using Google Gmail API Services would have been the most organized and well structured way of solving this challenge. However a series of prerequisites and installation of Google libraries made the process a little more longer than using libraries embedded into Python3 package.

## NOTE TO DEVELOPERS :notebook:

The code in this repository can be optimized in different ways (Using Google Gmail API services, Better data structures, etc).

## COMPLEXITY :chart_with_upwards_trend:
It is important to analyze the complexity of the algorithms used to find the *msgid*.

Since I am using nested loops, the complexity is **O(n^2)**. The issue with this complexity is that the execution time and resource consumption will significantly increase if the size of the input (N) is greater and greater each time the algorithm executes (Think about having +25000 messages in the INBOX folder :astonished:).
From a graphical point of view, the representation of this algorithm would be a quadratic function.
This can be improved by using other data structures, recursion, different programing paradigm, etc. However, this is out of scope and this is going to be categorized as 'Future improvements' (Section down below).

## FUTURE IMPROVEMENTS :telescope:
1. Research which type of data structures can be used to improve complexity and execution time.
2. Research if any other programming paradigms can be used to address this challenge.
3. ¿Use a different programing language?.

## RESOURCES :open_file_folder:
1. https://docs.python.org/2/tutorial/datastructures.html#sets
2. https://www.python-course.eu/sql_python.php
3. https://imapclient.readthedocs.io/en/2.1.0/api.html
4. https://imapclient.readthedocs.io/en/2.1.0/api.html#imapclient.IMAPClient.fetch
5. https://imapclient.readthedocs.io/en/2.1.0/
