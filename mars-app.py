#Dependencies
import sys
from flask import Flask, render_template
import pymongo
import scrape_mars

#Instance of Flask
app = Flask(__name__)

#Pymongo Connection
mars_data = pymongo.MongoClient().mars_db
collection = mars_data.mars_facts_data

###Website Routing

#Scrape Route
@app.route('/scrape')
def scrape():
    #query Mongo database and pass mars data into HTML template
    mars_info = scrape.scrape()
    mars_data.collection.insert_one(mars_info)
    #Return template
    return render_template('scrape.html')

#Root Route
@app.route('/')
def index():
    #list pymongo mars_data
    mars = list(mars_data.mars_facts_data.find())
    print(mars)
    #Return template
    return render_template('index.html', mars_info=mars_info)

#Initialize the program
if __name__ == '__main__':
    app.run(debug=True)
