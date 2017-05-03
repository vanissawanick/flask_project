from flask import Flask,json
from flask import render_template
from flask import request
import requests
 

key = 'xxxxx' #had to change it
sandbox = 'xxxxx'

app=Flask("HelloApp1")

@app.route("/")
def hello():
#    return "Hello Everyone!"
    return render_template("hello.html")

@app.route("/<name>")
def hello_name(name):
#    return "Hello {0}!".format(name.title())
    return render_template("hello.html",name=name.title())

@app.route("/contact", methods=['POST'])
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


	return render_template("contact.html",name=name.title())

 
if __name__=="__main__":
    app.run()
