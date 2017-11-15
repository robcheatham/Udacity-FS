# P3 - Build an Item Catalog Application

Application that provides a list of items within a variety of categories as well as a User Authentication system. Upon authentication additional functionality is granted to add, edit and delete their own items.



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
```
vagrant up
```

Log in to Vagrant using the command:
```
vagrant ssh
```

Move yourself into the \vagrant directory and view the files using the command:
```
cd \vagrant
```



## Setting up the Database


Establish the database and populate it with data by running the following commands in your terminal:
```
python db_setup.py
```
```
python db_population.py
```

The database is now created and populated. The terminal should provide feedback that reflects this.


## Running the Application

You are now ready to run the application. To start the application run the following command in your terminal:
```
python project.py
```

You can now access the application at the following link - [http://localhost:5000](http://localhost:5000)

## JSON Endpoints

The following API Endpoints are available publicly:

All Categories, displays all categories available by adding this to the localhost:5000 URL - `/api/v1/category/JSON`
All Products in a specific Category, display all products from within a category by adding this to the localhost:5000 URL - `/api/v1/category/<url_name>/products/JSON`
Individual Product, displays an individual Product by adding this to the localhost:5000 URL - `/api/v1/category/<url_name>/products/<product_id>/JSON`

url_names and product_id included in the initial db_population script are as follows - 

**JSON Parameters**

url_name | product_id
--- | ---
outerwear | 1 to 5
tshirts | 6 to 10
activewear | 11 to 15
hikinggear | 16 to 20
snowrange | 21 to 25
running | 26 to 30



## License
This project is licensed under the MIT License
