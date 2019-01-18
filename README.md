<!-- [![Build Status](https://travis-ci.org/nanfuka/ireporter-api.svg?branch=162823442-user-able-get-all-redflags)](https://travis-ci.org/nanfuka/ireporter-api)
[![Coverage Status](https://coveralls.io/repos/github/nanfuka/ireporter-api/badge.svg?branch=162823442-user-able-get-all-redflags)](https://coveralls.io/github/nanfuka/ireporter-api?branch=162823442-user-able-get-all-redflags)
[![Maintainability](https://api.codeclimate.com/v1/badges/aacc695e602d9e473552/maintainability)](https://codeclimate.com/github/nanfuka/ireporter-api/maintainability)

ireporter-api
# i-reporter

# description
I-reporter is the localised solution to the corruption problem in Africa. With this application, every citizen can  bring any form of corruption to the notice of the appropriate authorities. These have been termed as redflags in this application.     Users can also report on things that needs government intervention

## Project Features
- Create a ​red-flag​​ record
- Get all ​red-flag
​- records○Get a specific ​red-flag​​ record
- Edit a specific ​red-flag​​ record
- Delete a ​red-flag​​ record

##heroku
- The app is hosted om heroku at [ireporter-api](https://reporterss.herokuapp.com/)

## gh-pages 
- Go to [I-reporter](https://nanfuka.github.io/iReporter/)

## API endpoints for the application
Request|URL|Description
---|---|---
GET /red-flags/<red-flag-id>Fetch a specific ​red-flag​​ record
**GET**|`api/v1/red-flags`|Fetch all ​red-flag ​​records
**GET**|`api/v1/red-flags/<red-flag-id>`|Fetch a specific ​red-flag​​ record
**POST**|`/red-flags`|Create a ​red-flag​​ record
**PATCH**|`/red-flags/<red-flag-id>/location`|Edit the location of a specific red-flag record
**PATCH**|`red-flags/<red-flag-id>/comment`|Edit the comment of a specific red-flag record
**DELETE**|`/red-flags/<red-flag-id>`|Delete a specific red flag record


## Instalation
- first of all you should install python 3.7 or anyother version upwards in case you do have    it
- Clone the GitHub repo: git clone https://github.com/nanfuka/ireporter-api.git`
- git checkout 162823442-user-able-get-all-redflags
- install a virtualenviroment with these commands (virtualenv venv)
- move into the virtual enviroment.
- install the requred packages which are in the requrements.txt file by following these        commands in your tarminal(pip install -r requirements.txt)
- run the app (python run.py)


## Contributors
* Deborah Kalungi

## How to Contribute
1. Download and install Git
2. Clone the repo `https://github.com/nanfuka/ireporter-api.git` -->


[![Build Status](https://travis-ci.org/nanfuka/ireporter-api.svg?branch=162823442-user-able-get-all-redflags)](https://travis-ci.org/nanfuka/ireporter-api)
[![Coverage Status](https://coveralls.io/repos/github/nanfuka/ireporter-api/badge.svg?branch=162823442-user-able-get-all-redflags)](https://coveralls.io/github/nanfuka/ireporter-api?branch=162823442-user-able-get-all-redflags)
[![Maintainability](https://api.codeclimate.com/v1/badges/aacc695e602d9e473552/maintainability)](https://codeclimate.com/github/nanfuka/ireporter-api/maintainability)

# i-reporter

# description
I-reporter is the localised solution to the corruption problem in Africa. With this application, every citizen can  bring any form of corruption to the notice of the appropriate authorities. These have been termed as redflags in this application. With this application, the general public can also report interventions to the concerned authorities. Interventions can include issues such as a collapsed bridge.

## Project Features
- Create a ​red-flag​​ record
- Get all ​red-flag
​- Get a specific ​red-flag​​ record
- Edit a specific ​red-flag​​ record
- Delete a ​red-flag​​ record

## heroku
The app is hosted om heroku at [ireporter-api] (https://reportth.herokuapp.com/)

## gh-pages 
- Go to [I-reporter](https://nanfuka.github.io/iReporter/)

## API endpoints for the application

| METHOD   | URL  | FUNCTIONALITY |
|---|---|---|
| GET |  `api/v1/red-flags` | Fetch all ​red-flag ​​records |
| GET | `api/v1/red-flags/<redflag_id>`| Fetch a specific ​red-flag​​ record |
| POST |  `api/v1/red-flags` | Create a ​red-flag​​ record |
| PATCH |  `api/v1/red-flags/<red-flag_id>/location` | Edit the location of a specific red-flag |
| PATCH |  `api/v1/red-flags/<red-flag_id>/comment` | Edit the comment of a specific red-flag record|
| DELETE | `api/v1/red-flags/<red-flag_id>/redflag` | Delete a specific red flag record
| POST |  `api/v1/signup` | Add user | 
| POST |  `api/v1/login` | login user |


## Instalation
- first of all you should install python 3.7 or anyother version upwards in case you do have    it
- Clone the GitHub repo: git clone https://github.com/nanfuka/ireporter-api.git`
- git checkout develop
- install a virtualenviroment with these commands (virtualenv venv)
- move into the virtual enviroment.
- install the requred packages which are in the requrements.txt file by following these         commands in your tarminal(pip install -r requirements.txt)
- run the app (python run.py)


## Contributors
* Deborah Kalungi

## How to Contribute
1. Download and install Git
2. Clone the repo `https://github.com/nanfuka/ireporter-api.git`