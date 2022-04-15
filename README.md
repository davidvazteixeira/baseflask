# Base Flask App

The idea of this repository is that you simply clone it and start your development.

This code is a starting base for creating projects in Flask. It already comes with a minimal application that "just works" without you having to write a single line of code. It has a **suggested** folder structure to simplify your life and is already configured to be used on the Heroku server.

**If you're new to GIT or Heroku**, keep reading for an **extremely straightforward tutorial** on how to install and configure both, which you'll need in development. **If you already know**, skip directly to [Sugested steps to deploy your app in Heroku](#sugested-steps-to-deploy-your-app-in-heroku).

At the end, under [Useful Links](#useful-links), there is a small list of documentation and links to Python, Flask, HTML, Javascript and CSS.

* Version: Python3
* Main packages: flask, gunicorn
* Tools: heroku-cli, git

# Contents

* [Base Flask App](#base-flask-app)
* [Git and Heroku CLI](#git-and-heroku-cli)
    * [Git](#git)
    * [Heroku-CLI](#heroku-cli)
* [Sugested steps to deploy your app in Heroku](#sugested-steps-to-deploy-your-app-in-heroku)
* [Run in localhost](#run-in-localhost)
* [Future app updates](#future-app-updates)
* [Recommended: Python version](#recommended-python-version)
* [Useful Links](#useful-links)
    * [Python](#python)
    * [Virtual Environments](#virtual-environments)
    * [Flask](#flask)
    * [Frontend](#frontend)

# Git and Heroku CLI

## Git

**Install git**

* Download: <https://git-scm.com/downloads>

**Git First-Time setup**

Generally you just need theses commands:

```bash
  $ git config --global user.name "Your name"
  $ git config --global user.email your_email@mail.com
```

* Full documentation: <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## Heroku-CLI

**Install heroku-cli**

<https://devcenter.heroku.com/articles/heroku-cli>

**Check your installation:**

```bash
  $ heroku --version
```

If you see a version information the installation is right.

**Connect with your Heroku account**

```
  $ heroku login
```

A new browser window will open. Just login with your Heroku login/pass. After logon, return to terminal and if everything was right you will see something like this:

```
  $ heroku login
  heroku: Press any key to open up the browser to login or q to exit
   ›   Warning: If browser does not open, visit
   ›   https://cli-auth.heroku.com/auth/browser/***
  heroku: Waiting for login...
  Logging in... done
  Logged in as YOUR_HEROKU_LOGIN
```

# Sugested steps to deploy your app in Heroku

```bash
  $ git clone https://github.com/davidvazteixeira/baseflask.git   # Clone this rep
  $ cd baseflask                                                  # go to folder
  $ heroku create YOUR_NEW_APP_NAME                               # create a heroku app
  $ git push heroku master                                        # push modifications to server

  # ... Many output lines here! Check for erros!
    
  $ heroku ps:scale web=1               # create 1 free dyno to run your app (dyno ~ processor)
  $ heroku open                         # open link in a browser window
```

Note: If "heroku open" don't start your browser, your application link will be:

<https://YOUR_NEW_APP_NAME.herokuapp.com>

# Run in localhost

localhost is the machine you are on.

* If you want to use an environment (venv, virtualenv, conda etc), create it with python3 bindings.
* Install project packages:
  * flask, gunicorn
  * (preferably) install packages defined in requirements.txt file and update it every time you add a new package.
    * Note: requirements.txt is the output of "pip freeze"

If everything was set correctly, test locally with:

Development webserver 
```
  $ flask run                   # Or ...
  $ python -m flask run
```

or a more robust webserver (same running in Heroku):

```
  $ gunicorn app:app            # Or ...
  $ python -m gunicorn app:app
```

And your app will be running at URL:

  * flask run: <http://localhost:5000> or <http://127.0.0.1:5000>
  * gunicorn:  <http://localhost:8000> or <http://127.0.0.1:8000>

If you got "flask/gunicorn not found" than you forgot to: 1) activate your Python environment or 2) install flask or gunicorn.

# Future app updates

> Note: This is an oversimplified scenario that "just works" for a git newbie.

After you make changes in some files you will need to push this "new version" of the code to the server.

Go back to terminal in the root folder of your project and:

```
git status                      # just to see all new and modified files
git add -A                      # Mark all modifications for commit
git commit -m 'some message'    # Apply the commit, with a message
git push heroku master          # Push all commits to the server
```

> Note: After *EVERY* push, Heroku server will automatically deploy again your app. Always check the output for errors!

Return to browser and check your updated website.

# Recommended: Python version

There is no guarantee that the Python version installed locally will be the same one used by Heroku. Also, the server has some versions available and, if not specified, it will use some default version.

To avoid unpleasant surprises, the ideal is to always **use the same version in development and in the server**.

In the main project folder, create a **runtime.txt** file and add just one line:

```
python-3.8.13
```

You can check your development version by running:

```
  python -V      # generally under environment
  python3 -V     # generally under system environment
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
