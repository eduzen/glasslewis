# Python2.7 and Django 1.9.1 - web application test

The web application uses django and bootstrap for the front end. The database is a sqlite, because it's easy to send it through email with a minimum amount of data. I  worked in a virtual environment with the specific dependencies installed on it, as it is usual for projects in python.
I have attached the code, but it can also be downloaded from github:

https://github.com/eduzen/glasslewis

Then you need to create an virtualenv:
(https://virtualenv.readthedocs.org/en/latest/installation.html)

Linux:
```
$ virtualenv myenv
```
Windows:
```
C:\Users\Name\glasslewis> C:\Python27\python -m venv myvenv
```

You can activate the env on linux doing:
```
$ source myenv/bin/activate
```
Windows
```
C:\Users\Name\glasslewis> myvenv\Scripts\activate
```

Then you need to install django and pillow (Pillow needs some dependecies which you can see on http://pillow.readthedocs.org/en/3.0.x/installation.html )

Linux:
```
$ pip install django pillow
or pip install -r requirements.txt
```

Windows
```
C:\Users\Name\glasslewis> pip install -r requirements.txt
```
Once the virtualenv is activated, start the app by running:

Linux: 
```
$python testproject/manage.py runserver
```

Windows: 
```
C:\Users\Name\glasslewis\testproject> python manage.py runserver 0:8000
```

Then you can see the web application on:

```
http://127.0.0.1:8000/
```

If you want to add new companies or contacts, go to:

```
http://127.0.0.1:8000/admin
``` 
(It’s an admin view where you can easily add new contacts and companies.)


username: shiva

password: Glasslewis


