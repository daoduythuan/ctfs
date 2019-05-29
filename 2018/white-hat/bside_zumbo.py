'''import flask, os, sys
import requests
app = flask.Flask(__name__)



counter = 12345672

@app.route('/<path:page>')
def custome_page(page):
	if page == 'favicon.ico': return ''
	global counter
	counter += 1
	try:
		template = open(page).read()
	except Exception as e:
		template = str(e)
	template += "\n<!-- page: %s, src: %s -->\n" % (page, __file__)
	return flask.render_template_string(template, name='test', counter=counter)


@app.route('/')
def home():
	return flask.redirect('/index.template')

if __name__ == '__main__':
	app.debug=True
	flag1 = "flag1:this_is_flag1"
	with open('/flag','w+') as f:
		flag2 = f.read()
	app.run(host='0.0.0.0')'''
from flask import Flask, request
from jinja2 import Environment

app = Flask(__name__)
Jinja2 = Environment()

@app.route("/page")
def page():

    name = request.values.get('name')
    
    # SSTI VULNERABILITY
    # The vulnerability is introduced concatenating the
    # user-provided `name` variable to the template string.
    output = Jinja2.from_string('Hello ' + name + '!').render()
    
    # Instead, the variable should be passed to the template context.
    # Jinja2.from_string('Hello {{name}}!').render(name = name)

    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)