# WebTechnology_Project
 Have to do:-

1. Make a CURD Application.
2. At least having 5 database table.
3. Visualizing Data from minimun 3 table using query.
4. Insert data to at least 2 table at a time.
5. Using Frontend, Backend and Database.

<h1 align="center">
Food Order 
</h1>

The main idea of "Food Order" is to maintain customer's orders. The system offers to the user to manage their customer's profile and their order. 
Using Python Framework(Django) at backend, SQLite as database with HTML, CSS, Javascript and bootstrap at the frontend. 

***

### Requirements:
 * #### [Python 3.8 or up](https://www.python.org/downloads/release/python-372/)
 * #### [Django 3.2.7](https://www.djangoproject.com/) 
 * #### Database : [SQLite](https://www.sqlite.org/index.html/)
 


***
### How to work:
 * Clone the project
 * Open command line in project base dir and install all dependency
   > `pip install -r requirements.txt`

 * To run the project in localhost:
   > `python manage.py runserver`

   
***   
### Database setup:
By default we are using SQLite. For using any other relational database please install the package of that database
for django and change the database dependency on `settings.py`.

***
### Some django keyword:
* To migrations the model:
  > `python manage.py makemigrations [app_name]`
 
* To migrate the models to Database:
  > `python manage.py migrate`
  
***

