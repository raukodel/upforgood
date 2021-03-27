# Project
This project use Flask for backend and React for frontend. <br />

# Python 3
Enviroment
```
$ pip3 install virtualenv
$ virtualenv name_of_env
$ source env/bin/activate
$ deactivate
```

Install dependencies
```
$ pip3 install -r requirements.txt
```
Run Linux
```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```
Run Windows
```
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
$ flask run
```

# React
Need Node.js to run.

Install dependencies
```
$ npm init -y
$ npm i webpack webpack-cli webpack-dev-server html-webpack-plugin --save-dev
$ npm i react react-dom --save
$ npm i @babel/core @babel/preset-env @babel/preset-react babel-loader --save-dev
$ npm install --save redux react-redux
$ npm install --save react-redux-toastr
$ npm install --save-dev mini-css-extract-plugin
```
Run
```
$ npm run build
$ npm start
```
