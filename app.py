from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/pandemic_final.db")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
#######QUERY FROM DATABASE fOR THIS ROUTE ####### 
    return render_template('index.html')
 
@app.route("/charts")
def charts():

    return render_template('charts.html')

@app.route("/globe")
def globe():

    return render_template('globe.html')

@app.route("/about")
def about():
    return render_template('about.html')
 

@app.route("/api/v1.0/pandemic")
def pandemic():
   # Read data from database and store in JSON format in \Dashboard_Files\data\pandemic_final

    """ Query all Pandemics for 'Pandemic', 'Country', 'Year', 'Cases', 'Deaths', 'Lon', 'Lat', 'population'"""
    #results_old = session.query(pandemic_table.Pandemic, pandemic_table.Country, pandemic_table.Year, pandemic_table.Cases, pandemic_table.Deaths, pandemic_table.Lon, pandemic_table.Lat, pandemic_table.population).all()
    query ='SELECT "Pandemic", "Country", "Year", "Cases", "Deaths", "Lon", "Lat", "population" from "pandemic_final";'
    
    results = pd.read_sql(query, con=engine)

    all_pandemics = results.to_dict(orient="records")

    # Grab list of pandemic names
    pandemic_names = list(results.Pandemic.unique())

    # Mimic the pandemic_final.json structure for the graphs to work
    pandemics_final = {
        'names': pandemic_names,
        'pandemics':  all_pandemics
    }

    return jsonify(pandemics_final)

if __name__ == "__main__":
    app.run(debug=True)
