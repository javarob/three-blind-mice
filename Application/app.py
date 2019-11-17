import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import psycopg2

app = Flask(__name__)


#################################################
# Database Setup
#################################################

conn = psycopg2.connect(host="localhost", database="tbm",
                        user="postgres", password="Issimo86*")

# engine = create_engine("postgresql://postgres:" + password + "@localhost:5432/Homework09")
# connection = engine.connect()

##################################################

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Stock_Data = Base.classes.stock_data


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
