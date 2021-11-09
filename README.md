# AGH Rentals

## _About The Project_:
&emsp;&emsp;&emsp;AGH Rentals Is The Project Based On The Real World Domain Rental Systems. This Project Is Made With The Python Full Stack Development[PFSD] Tech Stack

## _Getting Started_:
&emsp;&emsp;&emsp;A rental system Project Written in Django.

## **Installation**

**clone repo**

	git clone https://github.com/pamarthiabhinav/AGH-Rentals.git
	

**Go Into Repo**

	
	cd AGH-Rentals\aghrentals
	

**Make A Virtual Environment**

	
	virtualenv django (pip install virtualenv)
	

**Start The Environment[django]**
	
	django\Scripts\activate
	

**Install The Requirements**
	
	pip install -r requirements.txt
	

**Now Make the database migrations**
	
	python manage.py makemigrations
	
**Now run the database migrations**
	
	python manage.py migrate
	

**Now run the server**
	
	python manage.py runserver
	

**Head to** `http://127.0.0.1:8000/`


----------------------
**Stop the Running server**
	
	ctrl + c
	
**Admin Site**

Create superuser for admin site

	
	python manage.py createsuperuser
	
	

**Now run the server Again**
	
	python manage.py runserver


**Head to** `http://127.0.0.1:8000/aghar` The Admin Url Has Been Modified from admin to aghar

----------------------
**Note** : Although **Heading to The** `http://127.0.0.1:8000/admin` Will Also Show The Same Admin Panel But It Won't Give Any Response For Your Login Credentials. This Is Because Of django-Honeypot Which I Have Added Into The Project To Trick The Users With The Admin Panel


### &copy; [Abhinav Pamarthi](https://github.com/pamarthiabhinav) &copy;
