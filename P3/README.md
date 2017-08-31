# P3 - Logs Analysis

Reporting tool that prints out plain text reports based on data from a PostgreSQL database written in Python that utilising the psycopg2 module to connect to the database.

## Prerequisites

This program was created on a Linux VM and to run it successfully you will require the following - 

  - Python2.7
  - VirtualBox
  - Vagrant

## Setting up the Project

1 - Download and install the correct platform package for your OS of VirtualBox from here - [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2 - Download and install the correct platform package for your OS of Vagrant from here - [Vagrant](https://www.vagrantup.com/downloads.html)
3 - Clone the VM Configuration from here - [VM Configuration Data](https://github.com/udacity/fullstack-nanodegree-vm)
4 - Download the data for the program here - [Project Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5 - Unzip the Data into your repository

## Launching the VM

From within the Vagrant sub-directory of your repository using the Terminal launch the VM using the command:
'''vagrant up'''

Log in to Vagrant using the command:
'''vagrant ssh'''

Move yourself into the \vagrant directory and view the files using the command:
'''cd \vagrant'''
'''ls'''

## Setting up the Database

Load the data into the database by using the command:
'''psql -d news -f newsdata.sql'''

The database is now created. Three tables were created, their names are - Articles, Authors & Log. In order to view the schema of the database and it's tables, run the following commands to connect to the database and explore - 

'''psql -d news'''
'''\dt'''
'''\d articles'''
'''\d authors'''
'''\d log'''

### Creating the necessary views within the database for running the Program

In order to run the program it is necessary to create a couple of views in the database. The first view is used to view data related to articles it's authors and counts the views of each article. The second view combines data to calculate the error percentage of article requests.

To create the article_views view run the command:
'''create view article_views as select title, author, count(*) as views from articles, log where log.path like concat('%',articles.slug_ group by articles.title, articles.author order by views desc;'''

To create the error_log view run the command:
'''create view error_log as select date(time), round(100.0 * sum(case log.status when '404 NOT FOUND' then 1 else 0 end)/count(log.status),2) as error_rate from log group by date(time);'''

This will create the following views to query against in the table - 

**article_views**
| Column   | Data Type |
| -------- |:---------:|
| title    | text      |
| author   | text      |
| views    | integer   |

**error_log**
| Column     | Data Type |
| ---------- |:---------:|
| date       | date      |
| error_rate | float     |


## Running the program and generating the Logs

Exit out of the database by using the command: '''\q'''

Then run the program using the command: '''python logs.py'''

## License
This project is licensed under the MIT License
