import os
from bottle import route, run, static_file, view

@route("/")
@view("index")
def index():
	pass

@route("/contacts")
@view("contacts")
def contacts():
	pass

@route("/css/<filename>")
def send_css(filename):
	return static_file(filename, root='static/css')

@route("/js/<filename>")
def send_js(filename):
	return static_file(filename, root='static/js')

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)