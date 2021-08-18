from flask import Flask,  render_template ,request
from flask_login import LoginManager  
from flask import request 
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
import requests
import json 
from website import create_app

    

if __name__ == "__main__":
    app= create_app()
 
    app.run(debug = True)  
