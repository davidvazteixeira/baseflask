# Base Flask App

**UPDATE 12-10-2022**

> Heroku **FREE PLANS IS NO MORE**! There's a new section to deploy to Render. The Heroku sections still works, but you must sign a non free plan.

The idea of this repository is that you simply clone it and start your development.

This code is a starting basis for creating projects in Flask. It already comes with a minimal application that "just works" without you having to write a single line of code. It has a **suggested** folder structure to simplify your life and is already configured to be used on the Heroku server or Render.

**If you're new to GIT, Heroku or Render**, keep reading for an **extremely straightforward tutorial** on how to install and configure both, which you'll need in development. **If you already know**, skip directly to [Sugested steps to deploy your app to Render](#render) or [Sugested steps to deploy your app to Heroku](#heroku).
 
At the end, under [Useful Links](#useful-links), there is a small list of documentation and links to Python, Flask, HTML, Javascript and CSS.

* Version: Python3
* Main packages: flask, gunicorn
* Tools: heroku-cli, git

# Contents

* [Introduction](#base-flask-app)
* [Install](#install)
* [Git](#git)
* [Run in localhost](#run-in-localhost)
* [Suggested steps to deploy your app](#suggested-steps-to-deploy-your-app)
    * [Render](#render)
      * [Render Account](#render-account)
      * [Render Deploy](#render-deploy)
    * [Heroku](#heroku)
      * [Heroku Tools](#heroku-tools)
      * [Heroku Deploy](#heroku-deploy)
* [Future App Updates](#future-app-updates)
* [Recommended: Python version](#recommended-python-version)
* [Useful Links](#useful-links)
    * [Python](#python)
    * [Virtual Environments](#virtual-environments)
    * [Flask](#flask)
    * [Frontend](#frontend)
* [What is missing?](#what-is-missing)

# Install

## Using pip+venv (Linux) 

You must have:

* git: To clone this project (or you can download the zip from Git Hub)
* Python 3: The main server language
* pip: To install Python packages
* Python Packages: venv

```bash
  $ git clone https://github.com/davidvazteixeira/baseflask.git   # Clone this rep
  $ cd baseflask                                                  # go to folder
  $ python3 -m venv .env                                          # Create environment in folder .env
  $ source .env/bin/activate                                      # Activate your environment
  $ pip install -r requirements.txt                               # Install required packages
  $ flask run                                                     # Start server
```

After these steps, your server will be running in localhost:5000

## Using Anaconda

You must have:

* Anaconda distribution installed [(link)](https://www.anaconda.com/products/distribution
)

Steps:

* Create a new environment: "baseflask_env"
  * Choose the latest Python 3.x version
* Open terminal in baseflask_env environment
* Install pip

```bash
  C:\> conda install pip
```

* Create a folder and clone the repository in that folder:

```bash
  C:\> cd [your folder]                                                                 # go to folder
  C:\[your folder]> git clone https://github.com/davidvazteixeira/baseflask.git         # Download project files in baseflask
```

A new subfolder "baseflask" will be created inside [your folder].

* Go to the "baseflask" folder inside [your folder]
* Install projects packages using pip

```bash
  C:\[your folder]\baseflask> pip install -r requirements.txt                           # Install additional Python packages
```

* Run server

```bash
  C:\[your folder]\baseflask> python3 -m flask run                                      # Start server!
```

After these steps, your server will be running in localhost:5000. Test in your browser.

> Note: localhost:5000 no working? try 127.0.0.1:5000

# Git

**Install git**

* Download: <https://git-scm.com/downloads>

**Git First-Time setup**

Generally you just need theses commands:

```bash
  $ git config --global user.name "Your name"
  $ git config --global user.email your_email@mail.com
```

* Full documentation: <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

# Run in localhost

localhost is the machine you are on.

* If you want to use an environment (venv, virtualenv, conda etc), create it with python3 bindings.
* Install project packages:
  * flask, gunicorn
  * (preferably) install packages defined in requirements.txt file and update it every time you add a new package.
    * Note: requirements.txt is the output of "pip freeze"

If everything was set correctly, test locally with:

Development webserver 

```bash
  $ flask run                   # Or ...
  $ python -m flask run
```

or a more robust webserver (same running in Heroku):

```bash
  $ gunicorn app:app            # Or ...
  $ python -m gunicorn app:app
```

And your app will be running at URL:

  * flask run: <http://localhost:5000> or <http://127.0.0.1:5000>
  * gunicorn:  <http://localhost:8000> or <http://127.0.0.1:8000>

If you got "flask/gunicorn not found" than you forgot to: 1) activate your Python environment or 2) install flask or gunicorn.

# Suggested steps to deploy your app

## Render

https://render.com

### Render Account
  
* Create an account in render.com
* Optionally, connect your Git Hub account to your Render account

### Render Deploy

* Go to dash board https://dashboard.render.com/
  * Click button "New+"
  * Choose "Webservice"
* Connect a repository
  * You can:
    * use your own GitHub repository (public or private)
    * test this repository (just use: git@github.com:davidvazteixeira/baseflask.git)
* Configure some params:
  * Name:
    * this name must be unique in Render.
    * Will be your address: name.onrender.com
  * Root: leave blank
  * Environment: Python 3
  * Region: choose any
  * branch: master
  * build command: keep "pip install -r requirements.txt"
  * start command: keep "gunicorn app:app"
    * This will run the project with gunicorn server, not "flask run"
  * Plans: choose Free
  * Avanced:
    * Here you can set useful things like environment variables
    * For now, just skip
  * Click "Create Web Service"

After this you will see a datetime and "in progress..." animation. When ready, the "in progress" will change to "Live" At the time of this writing, the free plan deployed in 6 minutes. In this screen you can check your web server link in the form https://name.onrender.com

This project is onrender at: https://baseflask.onrender.com

> Note: Oh no! 404 error!?

The first time you deploy an app, Render.com can delay and additional 20 minutes to update the routing after you see the "Live". In the application screen, see the "logs". If it's ok like above, just wait a little and try again.

```
Oct 12 03:02:30 PM  ==> Starting service with 'gunicorn app:app'
Oct 12 03:02:34 PM  [2022-10-12 18:02:34 +0000] [52] [INFO] Starting gunicorn 20.1.0
Oct 12 03:02:34 PM  [2022-10-12 18:02:34 +0000] [52] [INFO] Listening at: http://0.0.0.0:10000 (52)
Oct 12 03:02:34 PM  [2022-10-12 18:02:34 +0000] [52] [INFO] Using worker: sync
Oct 12 03:02:34 PM  [2022-10-12 18:02:34 +0000] [55] [INFO] Booting worker with pid: 55
# blank after this? Wait a little for the router and try the address again.
```

## Heroku

> Note: Heroku has **NO FREE PLAN ANYMORE!** 

https://www.heroku.com

### Heroku Tools

Heroku has CLI tool that helps the process of deploy.

<https://devcenter.heroku.com/articles/heroku-cli>

**Check your installation:**

```bash
  $ heroku --version
```

If you see a version information the installation is right.

**Connect with your Heroku account**

```bash
  $ heroku login
```

A new browser window will open. Just login with your Heroku login/pass. After logon, return to terminal and if everything was right you will see something like this:

```bash
  $ heroku login
  heroku: Press any key to open up the browser to login or q to exit
   ›   Warning: If browser does not open, visit
   ›   https://cli-auth.heroku.com/auth/browser/***
  heroku: Waiting for login...
  Logging in... done
  Logged in as YOUR_HEROKU_LOGIN
```

### Heroku Deploy

```bash
  $ git clone https://github.com/davidvazteixeira/baseflask.git   # Clone this rep
  $ cd baseflask                                                  # go to folder
  $ heroku create YOUR_NEW_APP_NAME                               # create a heroku app
  $ git push heroku master                                        # push modifications to server

  # ... Many output lines here! Check for errors!
    
  $ heroku ps:scale web=1               # create 1 free dyno to run your app (dyno ~ processor)
  $ heroku open                         # open link in a browser window
```

Note: If "heroku open" don't start your browser, your application link will be:

<https://YOUR_NEW_APP_NAME.herokuapp.com>

# Future App Updates

> Note: This is an oversimplified scenario that "just works" for a git newbie.

After you make changes in some files you will need to push this "new version" of the code to the server.

Go back to terminal in the root folder of your project and:

```bash
  $ git status                      # just to see all new and modified files
  $ git add -A                      # Mark all modifications for commit
  $ git commit -m 'some message'    # Apply the commit, with a message
  $ git push SERVER master          # Push all commits to the server
```

> Note: SERVER here is the name of the server that host your code.

* Heroku:
  * likes to keep the code in his own base.
  * Use "heroku" in place of SERVER
  * After *EVERY* push, Heroku CLI will show some information. Always check the output for errors!
* Render:
  * In render, you can use the same github.
  * probably the server is just "origin", so use in place of SERVER

> Note: Return to browser and check your updated website.

# Recommended: Python version

There is no guarantee that the Python version installed locally will be the same one used by Heroku. Also, the server has some versions available and, if not specified, it will use some default version.

To avoid unpleasant surprises, the ideal is to always **use the same version in development and in the server**.

In the main project folder, create a **runtime.txt** file and add just one line:

```
python-3.8.13
```

You can check your development version by running:

```bash
  $ python -V      # generally under environment
  $ python3 -V     # generally under system environment
```

The command you return something like:

**Python 3.8.13**

> Note: Pay attention in the difference between the output and the form that needs to be placed in the **runtime.txt** file. You can check the Documentation below "Python Support".

* Documentation: https://devcenter.heroku.com/articles/python-support
* Documentation: https://devcenter.heroku.com/articles/python-runtimes

# Useful Links
  
## Python

* Tutorial: https://www.w3schools.com/python/
* Tutorial: https://realpython.com/
* Tutorial: https://www.tutorialspoint.com/python3/index.htm
* Tutorial: https://www.javatpoint.com/python-tutorial
* Documentation: https://docs.python.org/3/

## Virtual Environments

* Tutorial: https://realpython.com/python-virtual-environments-a-primer/

## Flask
  
* Project
    * Page: https://flask.palletsprojects.com
    * Quickstart: https://flask.palletsprojects.com/en/2.1.x/quickstart/
    * Documentation: https://flask.palletsprojects.com/en/2.1.x/tutorial/
* Tutorial: https://overiq.com/flask-101/ 
* Tutorial: https://realpython.com/tutorials/flask/
* Tutorial: https://www.tutorialspoint.com/flask/index.htm
* Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* Tutorial (extension): https://flask-restful.readthedocs.io/en/latest/

## Frontend

* HTML
  * https://www.w3schools.com/html/default.asp
* CSS Tutorial:
  * https://www.w3schools.com/css/
  * https://www.tutorialspoint.com/css/index.htm
  * https://www.javatpoint.com/css-tutorial
* Boostrap (CSS Framework) Tutorial:
  * https://www.w3schools.com/bootstrap/
  * https://www.tutorialspoint.com/bootstrap/index.htm
  * https://www.javatpoint.com/bootstrap-tutorial
* Javascript Tutorial:
  * https://www.w3schools.com/js/
  * https://www.tutorialspoint.com/javascript/index.htm
  * https://www.javatpoint.com/javascript-tutorial
* jQuery (JS library) Tutorial:
  * https://www.w3schools.com/jquery/default.asp
  * https://www.tutorialspoint.com/jquery/index.htm
  * https://www.javatpoint.com/jquery-tutorial

# What Is Missing?

  * Database. You must find you way to include it. You can start from here:
    * SQLite: https://flask.palletsprojects.com/en/2.2.x/tutorial/database
    * MySQL: https://flask-mysql.readthedocs.io/en/stable
    * MariaDB: https://mariadb.com/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-1
    * PostgreSQL: https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
    * MongoDB: https://flask.palletsprojects.com/en/2.2.x/patterns/mongoengine

