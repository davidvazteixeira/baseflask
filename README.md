# Mininum Flask App

Minimun working Flask app to run in Heroku server. Just clone and use heroku-cli.
  
* Version: Python3
* Packages: Flask
* Tools: heroku-cli

# Git and Heroku CLI

New to git? New to Heroku? 

## Git

**Install git**

* Download: <https://git-scm.com/downloads>

**Git First-Time setup**

Generally you just need theses commands:

```bash
  git config --global user.name "Your name"
  git config --global user.email your_email@mail.com
```

* Full documentation: <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## Heroku-CLI

**Install heroku-cli**

<https://devcenter.heroku.com/articles/heroku-cli>

**Check your instalation**

```bash
  heroku --version
```

If you see a version information the installation is right.

**Connect with your Heroku account**

```
  heroku login
```

A new browser window will open. Just login with your Heroku login/pass. After logon, return to terminal and if everything was right you will see something like this:

```
  heroku: Press any key to open up the browser to login or q to exit
   ›   Warning: If browser does not open, visit
   ›   https://cli-auth.heroku.com/auth/browser/***
  heroku: Waiting for login...
  Logging in... done
  Logged in as YOUR_HEROKU_LOGIN
```

# Sugested steps to deploy your app in Heroku server

```bash
  git clone GITLINK                   # Here you are cloning this base app
  cd GITLINK                          # go to cloned project folder
  heroku create YOUR_NEW_APP_NAME     # create a new heroku app in your account
  git add -A                          # add the files to commit
  git commit -m 'Initial Commit'      # commit
  git push heroku master              # push modifications to server

  #... many outout lines here!
    
  heroku open                         # open the link in a browser window
```

Note: If "heroku open" don't start your browser, your application link will be:

<https://YOUR_NEW_APP_NAME.herokuapp.com>

# Test locally

* If you use environments (venv, virtualenv, conda etc), create your environment with python3 bindings.
* Install project packages:
  * flask
  * (preferably) install packages defined in requirements.txt file and update it every time you add a new package.

If everything was set, test locally with:

```
flask run
```

And you app will be running the he URL: <http://localhost:5000> or <http://127.0.0.1:5000>

If you got "flask not found" than you forgot to: 1) activate your python environment or 2) install flask

# Future app updates

> Note: This is an oversimplified scenario that is "just good" for a git newbie.

After you make change in some files, you will need to push this "new version" of the server. Back to terminal, in the root folder of your project:

```
git status                    # just to see all new and modified files
git add -A                    # Add every modification listed for the commit
git commit -m 'some message'  # Apply the commit
git push heroku master        # Push all commits to the server
```

> Note: After *EVERY* git push, the Heroku server will automatically re deploy. Check the output for errors!

Return to browser and check you updated website.
