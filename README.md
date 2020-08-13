![](https://storage.googleapis.com/twg-content/original_images/why-airbnb-takes-a-customer-centric-approach-to-adwords_case-studies_lg.png)

# 0x02. [AirBnB](https://www.airbnb.com) clone - MySQL

## Background Context
Welcome to the [AirBnB clone project Second Part](https://intranet.hbtn.io/concepts/74)! (The Holberton B&B)
Before starting, please read the AirBnB concept page and watch [this video](https://youtu.be/fb2zxES7ROU) from [Bobby Yang](https://twitter.com/bobstermyang), talking about how HBNB project abstracts the storage part: FileStorage and DBStorage.

In this project we must do::

* Replace the file storage by a Database storage
* Map your models to a table in database by using an O.R.M.

This repository contains the second stage of a student project to build a clone of the AirBnB website. 

Environment variables will be your best friend for this project!

* HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
* HBNB_MYSQL_USER: the username of your MySQL
* HBNB_MYSQL_PWD: the password of your MySQL
* HBNB_MYSQL_HOST: the hostname of your MySQL
* HBNB_MYSQL_DB: the database name of your MySQL
* HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)

See to the following picture:

<p>
<img src="https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Airbnb%20clone%20website.png" width="80%" height="80%">
</p>

AirBnb Clone is a project that consists of several stages linked together, which will be developed step by step:

* The Console
* Web Static
* MySQL storage
* Web framework - templating
* RESTful API
* Web dynamic

### Diagram AirBnB  clone (MySQL storage)
![](https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Flow%20Airbnb%20clone.png)

## Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

* Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
* Provide default value of any attribute
* In the future, provide the same model behavior for file storage or database storage

### Files in This Repository:

| File | File Hierarchy | Description |
| :---: | :---: | :---: |
| `console.py` | [console.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/console.py) | The main console file |
| `amenity.py` | [models/amenity.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/amenity.py) | The amenity subclass |
| `base_model.py` | [models/base_model.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/base_model.py) | The base model superclass |
| `city.py` | [models/city.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/city.py) | The city subclass | 
| `place.py` | [models/place.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/place.py) | Te place subclass |
| `review.py` | [models/review.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/review.py) | Te review subclass |
| `state.py` | [models/state.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/state.py) | Te state subclass |
| `user.py` | [models/user.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/user.py) | Te user subclass |
| `file_storage.py` | [models/engine/file_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | The file storage class |
| `db_storage.py` | [models/engine/db_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) | The DB storage class |
| `test_amenity.py` | [tests/test_amenity.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_amenity.py) | The unittest module for amenity |
| `test_base_model.py` | [tests/base_model.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_base_model.py) | The unittest module for base model |
| `test_city.py` | [tests/city.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_city.py) | The unittest module for city |
| `test_place.py` | [tests/place.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_place.py) | The unittest module for place |
| `test_review.py` | [tests/review.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_review.py) | The unittest module for review |
| `test_state.py` | [tests/state.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_state.py) | The unittest module for state |
| `test_user.py` | [tests/user.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_user.py) | The unittest module for user |
| `test_file_storage.py` | [tests/test_models/test_engine/test_file_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_engine/test_file_storage.py) | The unittest module for file storage |
| `test_db_storage.py` | [tests/test_models/test_engine/test_db_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_engine/test_db_storage.py) | The unittest module for DB storage |
| `test_console.py` | [tests/console.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_console.py) | The unittest module for console |
| `setup_mysql_test.sql` | [setup_mysql_test.sql](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/setup_mysql_test.sql) | Create database and test user |
| `setup_mysql_dev.sql` | [setup_mysql_dev.sql](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) | Create database |


### Usage
### Basic usage of The Console

| Command | Usage | Example | Functionality |
| :---: | :---: | :---: | :---: |
| `help` | `help` | help | displays a list of the commands |
| `create` | `create <class>` | create BaseModel | Create a new instance |
| `show` | `show <class> <id>` | show BaseModel 787fds-fdf665-fdf843a1 | Shows a specific instance |
| `destroy` | `destroy <class> <id>` | destroy BaseModel 787fds-fdf665-fdf843a1 | Deletes a specific instance |
| `all` | `all` or `all <class>` | all BaseModel | Shows all instance or class |
| `update` | `update <class> <id> <attribute> <value>` | update BaseModel 787fds-fdf665-fdf843a1 name Maria | Update an attribute in an instance |
| `quit` | `quit` | quit | Quits the console |



1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>