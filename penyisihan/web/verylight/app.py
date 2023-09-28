from flask import Flask, request, render_template_string
import jinja2, re, hashlib

app = Flask(__name__)
app.secret_key = 'slashroot7{Fl49_p@l5u} slashroot7{Qmu_T3rtyPuuuuuu}'

@app.route('/')
def index():
	search = request.args.get('search') or None

	#simple filter
	blacklist = ["config", "self", "request", "[", "]", '"', "_", "+", " ", "join", "%", "%25"]
	if search == None: 
		return render_template_string(
			'''
		<html>
		<head>
			<title>Very Light</title>
		</head>
		<body>
			<marquee><h1>Very Very Light</h1></marquee>
			<!-- Parameter Name: search -->
			<!-- Method: GET -->
		</body>
		</html>
	''' .format(search))

	for x in blacklist:
		if x in search:
			return "hacking attempt {}".format(x), 400
	
	template = '''
		<html>
		<head>
			<title>Very Light</title>
		</head>
		<body>
			<marquee><h1>Very Very Light</h1></marquee>
			<h2>You searched for:</h2>
			<!-- Parameter Name: search -->
			<!-- Method: GET -->
		</body>
		</html>
		{}
	''' .format(search)

	return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20011)
