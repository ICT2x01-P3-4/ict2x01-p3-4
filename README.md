# ICT2x01 Team Project

This is a team project for ICT2101/2201.

## Setting Up

### Requirements:

1. Pip
2. Python

### Set up

1. git clone the repository
2. Set up virtual env with `python -m venv venv` on the terminal. *IMPT MAKE SURE YOU ARE IN THE CORRECT REPO DIRECTORY WHEN CREATING*
3. To activate the virtual environment type `venv\Scripts\activate.bat` in your terminal for Windows, and `source venv/bin/activate` for Linux or MacOS
4. Install the dependencies with `pip install -r requirements.txt`
5. Copy these 2 commands and execute it in your terminal

```
// For Windows CMD
set FLASK_APP=carstep
set FLASK_ENV=development

// For UNIX-like systems using Bash
export FLASK_APP=carstep
export FLASK_ENV=development
```

6. Once all these are set up, you just run the and debug the program but typing `flask run` in the terminal

## Development Workflow
### Default branches  

**master branch**: Only codes that are ready to deploy will be merged here.  

**dev branch**: This is where codes are being developed.

### Workflow
1.  All developers will branch off from the **dev** branch and create a feature branch following this naming convention: **feature/\<featurename>** 
2.  Implementation and testing will be done on the feature branchs.
3. Once a feature is done, a PR into the dev branch will need to be created and a reviewer needs to be assigned to  the PR for code reviewing.
4. The reviewer will then merge the PR into the **dev** branch once all code quality and conventions are satisfied.
## TODO

- Organise Working directory for repository
- Plan app routes for flask frontend
- Backend APIs, how to get data??

## Reference

1. [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
2. [Git CLI guide](https://github.com/alphonsekoh/UltimateGitResource/tree/main)
3. [Setting up MongoDB with Flask](https://www.mongodb.com/compatibility/setting-up-flask-with-mongodb)
