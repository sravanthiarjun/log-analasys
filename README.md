# log_analysis
About Queries in postgres database
This Log analysis project is third project of Udacity Full Stack Nanodegree course:
## To do this project we must install certain softwares as:
     virtualBox
     vagrant
     postgres database
     python
## vagrant:
##### This vagrant is used to run different operating system environment in on single OS.
##### This project is completely based on Ubuntu operating system.
##### After installing vagrant we should create a folder name vagrant in our directory.Later we open the command propmt or terminal in        the vagrant folder path.
## Then,we should run some commands as:
      vagrant -v
      vagrant init ubuntu/trusty64( or some other vagrant environment for ubuntu)
      Vagrant up
      vagrant ssh
 we must install psycopg2 by having command : sudo apt-get install python-psycopg2 
 To change to postgres folder we should run command : sudo -i -u postgres
 Then after we should connect to  postgres database by having command psql.
To display files in our directory we should use command : \l
## Then,after we create user with some password by having command:
     create user username with password 'something'
     To see the roles command : \du
## To make a database user with different roles:
     alter user username with Superuser;
     alter user username with Createrole;
     alter user username with CreateDB; 
#### To get exit we have command:\q or exit
#### Now we should a database as vagarnt : sudo -i -u vagrant
#### next command : Createdb vagrant 
#### Now we should create database to our project name news by using following commands:
     run psql command.After that we must create database name news by using:\c news
     Then we get message as that you are connected to news database from vagrant..
#### To fetch the data for our project we use the command that already discuused in the udacity course tutorials : psql -d news -f            filename.sql (This Zip file we get download from the udacity full stack course of log analysis project)
#### Then after we use different queries to get data to certain neccessary question that aksed in the project.
#### In this news data base we have three tables named:
      articles
      authors
      log
 ## The first query is most popular three articles of all time:
 ### For this  I have created a view as  article_view
     create  view  article_view as select title,count(*) as likes from articles,log where  log.path like concat('%',articles.slug) group by articles.title,articles.author order by likes desc;
## The second query is most popular article all the time:
### For this I have created a views as authors_view
     create  view  authors_view as select name,count(*) as views from articles,authors,log where authors.id=articles.author and  log.path like concat('%',articles.slug) group by name order by views desc;
## The third query is based on which day did more than 1% of requests lead to errors:
### For  this I have created three views:
#### 1.error_view : this view gives the number of errors that not found.
     create view error_view as select date(time),count(*) as errors  from log where log.status like concat('404 NOT FOUND') group by date(time) order by errors desc;
#### 2.total_view: this view gives the total views
     create view total_view as select date(time),count(status) as total_errors from log group by date(time)  order by total_errors desc;
#### 3. log_view:this view gives the percentage of errors
     create view log_view as select total_view.date as date,((100.00*errors)/(total_errors)) as percentage_errors from error_view natural join total_view where error_view.date=total_view.date group by total_view.date,percentage_errors order by percentage_errors desc;
## Queries:
 open the file and write the queries based on given conditions and save that file in the vagrant directory with .py extension.
## To run:
In the vagrant folder directory run the file using python filename.py
#### Then I had checked my code in pep8 online checker.
##### By this we can complete the loganalysis project.
 
