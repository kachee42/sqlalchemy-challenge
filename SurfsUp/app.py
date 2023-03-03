import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify

# Setup database
# Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database onto new model
Base = automap_base()

# Reflect Tables
Base.prepare(engine=engine, reflect=True)

# Save references to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#Flask setup
app = Flask(__name__)

#Flask Routes
@app.route("/")
def home():
    """List all available api routes"""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start-date<br/>"
        f"/api/v1.0/start-date/end-date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # create session from python to DB
    session = Session(engine)

    """Returns JSON list of last 12 months of rain data"""
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= dt.date(2016,8,23)).all()
    
    session.close()

    rain_dict = {}
    for date, prcp in results:
        rain_dict[date] = prcp

    return jsonify(rain_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    """Returns JSON list of weather stations"""
    results = session.query(Station.station, Station.name).all()

    session.close()

    all_stations = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temp_data():
    session = Session(engine)

    """Returns JSON list of temp data for the most active station during the most recent year of data"""
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(desc(func.count(Measurement.station))).first()[0]
    
    results = session.query(Measurement.date, Measurement.tobs, Station.name).\
        filter(Measurement.date >= dt.date(2016,8,23)).\
        filter(Measurement.station == Station.station).\
        filter(Measurement.station == most_active_station).all()
    
    session.close()

    all_temps = []
    for date, tobs, station in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["temperature"] = tobs
        temp_dict["station_name"] = station
        all_temps.append(temp_dict)

    return jsonify(all_temps)

@app.route("/api/v1.0/<start_date>")
def start_date(start_date):
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    
    session.close()
    
    start_date_temp = []

    for temp_min, temp_max, temp_avg in results:
        temp_dict = {}
        temp_dict["min_temp"] = temp_min
        temp_dict["max_temp"] = temp_max
        temp_dict["avg_temp"] = temp_avg
        start_date_temp.append(temp_dict)



    return jsonify(start_date_temp)

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end_date(start_date, end_date):
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()
    
    session.close()
    
    start_date_temp = []

    for temp_min, temp_max, temp_avg in results:
        temp_dict = {}
        temp_dict["min_temp"] = temp_min
        temp_dict["max_temp"] = temp_max
        temp_dict["avg_temp"] = temp_avg
        start_date_temp.append(temp_dict)

    return jsonify(start_date_temp)

if __name__ == '__main__':
    app.run(debug=True)