from flask import Flask,json
from flask import render_template
from flask import request
import requests
 

key = 'key-a86332885c717e1bc26dc139bc514146'
sandbox = 'sandboxf03f54d1e3a54f80bff0240c02c57478.mailgun.org'

app=Flask("HelloApp1")


@app.route("/")
def hello():
#    return "Hello Everyone!"
    return render_template("index.html")

@app.route("/about")
def about():
#    return "Hello Everyone!"
    return render_template("about.html")

@app.route("/contact")
def contact_page():
#    return "Hello Everyone!"
	return render_template("contact.html")

@app.route("/<name>")
def hello_name(name):
#    return "Hello {0}!".format(name.title())
    return render_template("template.html",name=name.title())

@app.route("/q", methods=['GET', 'POST']) 
def search_result(name):
#    tried to do a search, but it didn't work
    return render_template("template.html",name=name.title())



@app.route("/message", methods=['POST'])
def contact():
	form_data= request.form

	#Get form data
	name = form_data['name']
	message = form_data['message']
	email = form_data['Email']

	print(name, message, email)

	#email message
	subject = "Hello from Test"
	body = "Hi there, this is a test email."

	sender = 'vanissa@gmail.com'

	#sending message
	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)

	email_request = requests.post(request_url, auth=('api', key), data={
		'from': sender,
		'to': email,
		'subject': subject,
		'text': body
		})

	# checking email status
	print('Status:{0}'.format(email_request.status_code))
	print('Body: {0}'.format(email_request.text))


	return render_template("message.html",name=name.title())

 
if __name__=="__main__":
    app.run()