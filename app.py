from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)


@my_app.route('/')
def root():
	u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=r2kYH40AWn48f7czaQYLmk34h1GMzBX5JKtXPCRX')
	data=u.read()
	dict=json.loads(data)
	return render_template("default.html",date=dict["date"],explanation=dict["explanation"],hdurl=dict["hdurl"])

@my_app.route('/second')
def secondApi():
    u = urllib2.urlopen('http://api.followthemoney.org/?law-eid=4764641&gro=d-ccb&APIKey=a975fbe4aa68e017785f48ba78bea504&mode=json')
    data=u.read()
    dict=json.loads(data)
    return render_template('secondTemplate.html',theDict=dict)


if __name__ == '__main__':
	my_app.debug = True
	my_app.run()
