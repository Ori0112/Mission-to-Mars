from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
import json 


app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

#Define HTML route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

#setup scraping route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    #mars_2=json.dumps(mars)
    mars.update({}, mars_data, upsert=True)
    
    #return(mars_2)
    return redirect('/', code=302)

if __name__ == "__main__":
   app.run(debug=True)