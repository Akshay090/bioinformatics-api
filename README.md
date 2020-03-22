# Overview
Flask application which serves data from bioinformatics_posts_se.xml ingested into 
sqlite database 

## How to Run

Prerequisite : 
Install Sqlite

Basic setup:
    

    $ git clone https://Akshay900@bitbucket.org/Akshay900/bioinformatics-api.git 
    $ cd bioinformatics-api
    $ pip install pipenv
    $ pipenv shell
    $ pipenv install
    
Setup Database

    $ flask db init
    $ flask db migrate
    $ flask db upgrade  

Run Flask application:

    $ flask run
    
Run Test 

    $ pytest

This application is written using Python 3.7.

# Api endpoints 

```
GET http://127.0.0.1:5000/questions/1
GET http://127.0.0.1:5000/questions/1?orderby=score
GET http://127.0.0.1:5000/questions/1?orderby=views
GET http://127.0.0.1:5000/question/11075
GET http://127.0.0.1:5000/search_q?q=the genome
GET http://127.0.0.1:5000/search_a?q=the genome

```

