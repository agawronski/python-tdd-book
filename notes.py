#-------------------------------------------------------------------------------
# https://www.obeythetestinggoat.com/book/chapter_01.html
# make a virtualenv
cd python-tdd-book
python3.6 -m venv virtualenv

# activate a virtualenv
cd ~/Documents/python-tdd-book
source virtualenv/bin/activate

# Installing Django and Selenium
(virtualenv) $ pip install "django<1.12" "selenium<4"

# Getting Django Up and Running
$ django-admin.py startproject superlists .
├── functional_tests.py
├── geckodriver.log
├── manage.py
├── superlists
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── virtualenv
    ├── [...]


# start the Django app
python manage.py runserver

# run functional tests
python functional_tests.py


# initialize a git repo
ls
# db.sqlite3
# functional_tests.py
# geckodriver.log
# manage.py
# superlists
# virtualenv

git init .
# Initialised empty Git repository in ...python-tdd-book/.git/

echo "db.sqlite3" >> .gitignore
echo "geckodriver.log" >> .gitignore
echo "virtualenv" >> .gitignore

git add .
git status
# On branch master
#
# No commits yet
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#         new file:   .gitignore
#         new file:   functional_tests.py
#         new file:   manage.py
#         new file:   superlists/__init__.py
#         new file:   superlists/__pycache__/__init__.cpython-36.pyc
#         new file:   superlists/__pycache__/settings.cpython-36.pyc
#         new file:   superlists/__pycache__/urls.cpython-36.pyc
#         new file:   superlists/__pycache__/wsgi.cpython-36.pyc
#         new file:   superlists/settings.py
#         new file:   superlists/urls.py
#         new file:   superlists/wsgi.py

git rm -r --cached superlists/__pycache__
# rm 'superlists/__pycache__/__init__.cpython-36.pyc'
# rm 'superlists/__pycache__/settings.cpython-36.pyc'
# rm 'superlists/__pycache__/urls.cpython-36.pyc'
# rm 'superlists/__pycache__/wsgi.cpython-36.pyc'
echo "__pycache__" >> .gitignore
echo "*.pyc" >> .gitignore

git add .gitignore
git commit

# run unit tests
python manage.py test



https://www.obeythetestinggoat.com/book/chapter_philosophy_and_refactoring.html
































#-------------------------------------------------------------------------------
