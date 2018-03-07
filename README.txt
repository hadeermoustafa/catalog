This project is a part of udacity nanodegree program

The project is about building a web app catalog that extract some categories and subcategories for each category. Each subcategory has its own describtion and name. This project is runing on localhost http://localhost:5050/

The aim of this project is to use authentication, authorization , CURD and JSON endpoint

Please notice that i used a very minimal stylings as the main purpose of the project is the fucntionality, and I relied on the course stylings

"catalog" is the project folder

The project folder contains 2 folders and 7 files

1)static folder (contains the style css file)
2)Templates folder ( contain the .html templates files to be read by flask)
3)catalog.db (The database file the contains the categories and its subs)
4)client_secrets.json (google authentication file)
5)database_setup.py ( Python file that contains a classes to contect the project file with the database)
6)listofcategories.py( file contains categories list)
7)fb_clients_secret.json ( facebook authentication code)
8)project.py( the project main file)
9)Readme.txt(informations and instructions about the programe)

** How to run the programe file?

- Open git bash
- run the following code to open the contain folder:
   $cd catalog
- then:
   $vagrant up ("to run the VM")
- then:
   $vagrant ssh
- now open the vagrant: 
   $cd /vagrant/catalog
- now lets run the server
   $cd python project.py
- open http://localhost:5050/
- To access any category just click on its name
- Subcategories page will open with the name and describtion
- To add a new category you need to login ( click the login button on the top right or visit : http://localhost:5050/login)
- Choose a login option (Google or facebook)
- After login successfully you will be redirect to categories page
- Now you can add/edit or delete categories and items.
- To view Json endpoint you need to access (http://localhost:5050/category/<category_id>/item/JSON, ex: http://localhost:5050/category/1/item/JSON) 

