# ICT2x01 Team Project

This is a team project for ICT2101/2201.

## Setting Up

### Requirements:

1. Install MySQL Workbench, MySQL Server
2. Pip
3. Python

### Set up

1. git clone the repository
2. Set up virtual env with `python -m venv venv` on the terminal. IMPT MAKE SURE YOU ARE IN THE CORRECT REPO DIRECTORY WHEN CREATING
3. To activate the virtual environment type `venv\Scripts\activate.bat` in your terminal for Windows, and `source venv/bin/activate` for Linux or MacOS
4. Install the dependencies with `pip install -r requirements.txt`
5. Copy these 2 commands and execute it in your terminal [For Windows CMD]

```
set FLASK_APP=CarStep
```

and

```
set FLASK_ENV=development
```

5.  Copy these 2 commands and execute it in your terminal [For UNIX-like systems using Bash]

```
export FLASK_APP=CarStep
```

and

```
export FLASK_ENC=development
```

6. Once all these are set up, you just run the and debug the program but typing `flask run` in the terminal

## TODO

- Organise Working directory for repository
- Plan app routes for flask frontend
- Backend APIs, how to get data??

## Reference

1. [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
2. [Git CLI guide](https://github.com/alphonsekoh/UltimateGitResource/tree/main)
