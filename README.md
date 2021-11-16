# ICT2x01 Team Project

Welcome to Project CarStep! 🚗 🦶🏻

## Team Members
| [<img src="https://avatars.githubusercontent.com/u/16801537?v=4" style="border-radius: 50%" width="75px;"/><br /><sub><b>Koh Huan Yin</b></sub>](https://github.com/alphonsekoh)<br/>Team Lead | [<img src="https://avatars.githubusercontent.com/u/19357352?v=4" style="border-radius: 50%" width="75px;"/><br /><sub><b>Ng Han Yi</b></sub>](https://github.com/hanyi97)<br />Fullstack Developer| [<img src="https://avatars.githubusercontent.com/u/61367983?v=4" style="border-radius: 50%" width="75px;"/><br /><sub><b>Lim Shu Fen</b></sub>](https://github.com/shufenlim)<br />Security Specialist| [<img src="https://avatars.githubusercontent.com/u/73699421?v=4" style="border-radius: 50%" width="75px;"/><br /><sub><b>Low Yong Lin</b></sub>](https://github.com/lowyl)<br />Security Specialist
| :---: | :---: | :---: | :---: |

---


## Requirements:

- Pip >= 21.x
- Python >= 3.x
- Node >= 15.x
  
## Set up
### Clone the repository
1. Navigate to desired directory and open a new terminal window
2. Run the following command: `git clone https://github.com/ICT2x01-P3-4/ict2x01-p3-4.git`

### Configure project and install dependencies
1. Navigate to the root directory of the project
2. Set up virtual env with `python -m venv venv` on the terminal.
3. To activate the virtual environment type `venv\Scripts\activate.bat` in for **Windows**, and `source venv/bin/activate` for **Linux or MacOS**
4. Install the dependencies with `pip install -r requirements.txt`
5. Create a `.env` file and copy other the content from `.env.example` (the values will be shared privately within the group)
6. Copy these 2 commands and execute it in your terminal
```
# For Windows CMD
set FLASK_APP=carstep
set FLASK_ENV=development

# For UNIX-like systems using Bash
export FLASK_APP=carstep
export FLASK_ENV=development
```

### Run the application
1. Navigate to the root directory of the project
2. Execute the command `flask run` in your terminal
3. Open the browser and navigate to http://localhost:5000

---

## Development Workflow
### Default branches  

`master`: Only codes that are ready to deploy will be merged here.  

`dev`: This is where codes are being developed.

### Note
Any development **MUST** be done in the `feature` branches first before merging to the `dev` branch. Merging to `master` branch will only be done when all codes are ready to deploy.

### Feature Branches
1. All new feature branches should be created in the `dev` branch.
2. Follow this naming convention: `feature/<feature-name>`.

### Development Branch
1. Only **COMPLETED** feature branches can be merged into the `dev` branch.
2. Pull Requests (PR) should be created before any merging takes place.
3. The rest of the team members should be assigned as a reviewer for the PR.
4. PRs should be approved by **AT LEAST ONE** team member before merging.

### Master Branch
1. Only **COMPLETED AND DEPLOYABLE** codes from `dev` branch should be merged into the `master` branch.
2. PRs should be created before any merging takes place.
3. PRs should be created by the **Team Lead** and all team members should be assigned as a reviewer.
4. PRs should be approved by **ALL** team members before merging.
### Workflow
1. Create a feature branch by branching off the `dev` branch.
```
git checkout -b feature/<feature-name> dev
```
2. Push the new feature branch to the remote repository.
```
git push -u origin feature/<feature-name>
```
3. Save the progress
```
# Add all files to staging area
git add .

# Double check if everything added is correct
git status

# Commit the changes
# Commit messages should be in imperative: "Fix bug" and not "Fixed bug" or "Fixes bug"
git commit -m "<commit message>"

# Push changes to the corresponding branch in the remote repository
git push
```
4. Create a new pull request to merge the completed feature into the `dev` branch. **MAKE SURE `dev` IS SELECTED AS `base`!**
5. The reviewer will then merge the PR into the `dev` branch once all code quality and conventions are satisfied.
---
## User Acceptance Test

---
## Whitebox Testing

---
## Reference

1. [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
2. [Git CLI guide](https://github.com/alphonsekoh/UltimateGitResource/tree/main)
3. [Setting up MongoDB with Flask](https://www.mongodb.com/compatibility/setting-up-flask-with-mongodb)
