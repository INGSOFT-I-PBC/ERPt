# ERP Template with Django Framework

This repository contains the base configuration
for an ERP with the Django Framework and the implementation
for an API REST implementation

## Installing dependencies

To install the dependencies of python whe must run the next command:

#### GNU/Linux / MacOS

```
$ python -m pip install -r requirements.txt
```

Or

```
$ pip3 install -r requirements.txt
```

#### Windows

```
> py -m pip install -r requirements
```

Or

```
> pip install -r requirements
```

## Django Backend

### General Configuration

Before using the system we need to create the `.env` file where
the configurations will be setting up, to create a `.env` copy the file
`.env.example` and remove the `.example` extension.

### Database

After that we need the creation of the database that will hold all the information,
to create this database we need to run:

```
> python manage.py migrate
```

This command will create all the base structure of the database, included the base data needed to manage the roles, permission and users.

### User creation

To start using the backend we need an admin user, to create a new
superuser run the next command:

```
> python manage.py createuser --admin
```

To create a normal/manual user run without `--admin` switch. Like:

```
> python manage.py createuser
```

Also, you can provide the username without the need to write on the
terminal form:

```
> python manage.py createuser [--admin] --username <Username>
```

If the creation of the user was sucessfully the next message will be
shown:

```
> python manage.py createuser --username 'Super admin'
...
Successfully created the user 'super_admin'
```

### Run server

To run the Django's server we start the server with the following options

```
> python manage.py runserver [<ip/hostname>:<port>]
```
