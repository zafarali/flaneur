from flask import Flask 
from mealGetter import hello1

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world"

@app.route("/location/<lat>/<longi>")
def location(lat, longi):

	# i'm providing you with lat and long
	# use function to get the real city name
	# return to me a STRING with the city name
	return hello1(lat, longi)
	pass

@app.route("/feelinglucky/<lat>/<longi>")
def feelingLucky(lat, longi):

	# this function will return JSON in the following form:
	"""
	# result : {
		breakfast: <name of place>, <exact location>, <rating>, <price range>, any other data (image_url)
		morning activity: 
		lunch: same as above
		afternoon activity
		dinner: same as above
		night life
	}	

	"""

	pass



@app.route("/restaurants/<long>/<lat>")
def restuarants():
	# make a call here to another file that 
	print ("4")
	hello1()

if __name__ == "__main__":
	app.run()