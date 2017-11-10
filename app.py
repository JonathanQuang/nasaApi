from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)


@my_app.route('/')
def root():
	u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=r2kYH40AWn48f7czaQYLmk34h1GMzBX5JKtXPCRX')
	data=u.read()
	dict=json.loads(data)
	return render_template("default.html",date=dict["date"],explanation=dict["explanation"],hdurl=dict["hdurl"])


if __name__ == '__main__':
	my_app.debug = True
	my_app.run()