``` bash
virtualenv mywebsite
cd mywebsite
source bin/activate
pip install Django
django-admin.py startproject mywebsite .
python manage.py migrate
python manage.py startapp pythonapp
vim mywebsite/settings.py
touch pythonapp/urls.py
mkdir pythonapp/templates
mkdir pythonapp/templates/pythonapp
touch pythonapp/templates/pythonapp/index.html
python manage.py runserver 0.0.0.0:8080
```