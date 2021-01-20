from flask import Flask, render_template, request
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/send_sms", methods=['POST'])
def send_sms():
  if request.method == "POST":
    # strip out form data from the request
    phone_number = request.form['phone']
    form_message = request.form['message']

    # bring in env variables for twilio account
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')

    # Create the connection to Twilio and send the message
    client = Client(account_sid, auth_token)    
    message = client.messages \
                    .create(
                      body=f"{form_message}",
                      from_="+16204004157",
                      to=f"+1{phone_number}"
                    )

    print(account_sid, auth_token)

    return render_template("message_sent.html")
  return home()


if __name__ == "__main__":
  app.run(debug=True)