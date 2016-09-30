from flask import Flask
from flask import render_template
from flask import request
import yaml


app = Flask(__name__)

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/compute', methods=['GET', 'POST'])
def compute():
	if request.method == 'GET':
		    return render_template('compute.html')
	else:
		app.logger.debug(request.form['message'])
		yamlInput = yaml.safe_load(request.form['message'])
		app.logger.debug(yamlInput)
		print yamlInput
		searchword = request.args.get('key', '')
		#print searchword
		#app.logger.debug(searchword)		
		result = yamlInput.keys()[0]  # root
		return render_template('compute.html', result=result)
