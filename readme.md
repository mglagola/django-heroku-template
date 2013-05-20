# Django + Heroku Template
This template was only tested with and only works with *Mountain Lion OS X* (Mac).  This may change in the future.

See a full, in depth tutorial on how to use the template [HERE](http://markglagola.com/post/django-heroku-template-depth-tutorial/)

### Why use it?
This template simplifies the setup process of creating a Django project that's ready to be pushed to Heroku with Amazon S3 support.

- It takes **about 3 minutes** to setup and run a **local** django project using this template.

- It takes **under 10 minutes** to setup and run a django project using this template **on Heroku** (Following this [Tutorial](http://markglagola.com/post/django-heroku-template-depth-tutorial/)).  Setting up and install requirements on Heroku for the first time is what takes the most time!


## Requirements
- OS X
- virtualenv
- [heroku toolbelt](https://toolbelt.heroku.com/)
- git
- Amazon S3 Account (Get AWS Keys Ready!)

## Setup
Below is a brief overview on how to setup the template.  I recommend going through a more in depth tutorial [HERE](http://markglagola.com/post/django-heroku-template-depth-tutorial/).

1. Download .zip and extract it to your desired directory.
2. Rename the root folder to whatever you like.  **DO NOT** modify any other files.
2. `cd` into your recently renamed root folder.
3. Run `git init` in terminal.
4. run `virtualenv .env` in terminal (You may name your virtualenv anything you like).
5. Activate your virtual environment by running `source .env/bin/activate` in terminal.
6. run `pip install -r requirements.txt` in terminal (~1min).
7. run `python setup.py` in terminal. Follow the prompts and make sure to have your amazon S3 keys ready.
8. reactivate your virtual environment by running  `source .env/bin/activate`

- Your project is now setup.  You can test locally by running `python manage.py syncdb` and then `python manage.py runserver` in terminal.
- You could also test it on the herokuapp site.  Just make sure you run `syncdb` on your heroku app.

## License is MIT
Copyright (c) 2013 Mark Glagola.
See [License.txt](https://github.com/mglagola/django-heroku-template/blob/master/License.txt)
