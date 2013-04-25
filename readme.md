# Django + Heroku Template
This template was only tested with *Mountain Lion OS X* (Mac)
I will refer to *"Mac"* as if its the only device supported for the template.  That's not *really* the case.  Its just the only device I tested the template with.

It **may** work on *linux* distributions, but my concern is that the `setup.py` script may cause some issues.  If you have an edit for the setup.py, feel free to issue a pull request.  If it works on linux or windows, let me know!

Fork it!..

## Requirements
These must be installed on your Mac:
- virtualenv
- pip
- [heroku toolbelt](https://toolbelt.heroku.com/)
- git
- [heroku accounts](https://github.com/ddollar/heroku-accounts.git) - You must have an account setup
- Experience setting up a herokuapp with django (this is helpful to understand what's going on!)

## Setup
1. Either download the .zip or clone this template to your desired directory.  If you download the .zip, extract it…
2. `cd` into the template directory you just cloned or extracted.  Change the top folder name if you like, but don't change the project name.  That will be handled in the `setup.py` script.
3. Either run `git init` in terminal.
4. run `virtualenv .env` in terminal. You don't have to name it `.env`, but this is **required** if you want to use the setup.py script (specifically the amazon S3 setup section).
5. run `source .env/bin/activate` in terminal.  This activates your virtual environment.
6. run `pip install -r requirements.txt` in terminal.  This installs all the requirements needed for django, amazon S3, and heroku.
7. run `python setup.py` in terminal. This is a handy script that will setup your project to be heroku and S3 ready.  It will even change your project name from "*project_name*" to whatever you like.  **DO NOTE:** the script is not perfect.  It was created quickly and **does not** handle errors!

- Your project is now setup.  You can test locally by running `python manage.py syncdb` and then `python manage.py runserver` in terminal.
- You could also test it on the herokuapp site.  Just make sure you run `syncdb` on your heroku app.

## License is MIT
Copyright (c) 2013 Mark Glagola.

See License.txt
