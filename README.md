# Flask
Flask simple example

# Usage

### 1. install virtualenv
```sh
$ pip install virtualenv
$ mkdir venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### 2. set environment
| Name                | Description                      |
| ------------------- | -------------------------------- |
| APP_MODE            | choose from production, development, testing |
| APP_HOST            | ip address                       |
| APP_PORT            | port number                      |
| MYSQL_USER_NAME     | mysql user name                  |
| MYSQL_USER_PASSWD   | mysql user password              |
| MYSQL_HOST          | mysql host                       |
| MYSQL_DB_NAME       | mysql db name                    |
| REDIS_HOST          | redis ip address                 |
| REDIS_PASSWD        | redis password                   |

### 3. init
```sh
$ python manage.py init
```
init db tables

### 4. run test code
```sh
$ python manage.py test
```

### 5. run flask server
```sh
$ python manage.py runserver
```
if you do not install database you can get the database connection error

# Command

### runserver
```sh
$ python manage.py runserver
```
run flask server

### test
```sh
$ python manage.py test
```
run test code with unittest2

### init
```sh
$ python manage.py init
```
init db tables
