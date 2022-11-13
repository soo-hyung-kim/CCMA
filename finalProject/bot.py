from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

STATE = 0
REQUEST = None

@app.route('/bot', methods=['POST'])

def bot():
    global STATE

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if STATE == 0:
        [advance_state, response] = respond_to_request_type(incoming_msg)
        STATE += advance_state
        msg.body(response)

    elif STATE == 1:
        [advance_state, response] = respond_to_broad_location(incoming_msg)
        STATE += advance_state
        msg.body(response)

    elif STATE == 2:
        [advance_state, response] = respond_to_specific_location(incoming_msg)
        STATE += advance_state
        msg.body(response)

    #    msg.body("Sorry, this automated system only knows how to deal with\
    #              rapid tests, meals, and masks. To get in touch with someone,\
    #              feel free to reach out to...")
    return str(resp)


def respond_to_request_type(msg):
    advance_state = 1
    if 'rapid' in msg:
        response = "Rapid test coming :) To which dorm & floor would you like that delivered?"
    elif 'meal' in msg:
        response = "Meal coming up :) To which dorm & floor would you like that delivered?"
    elif 'mask' in msg:
        response = "Masks coming up :) To which dorm & floor would you like that delivered?"
    else:
        response = "Sorry, I didn't understand that request. Try again?"
        advance_state = 0
    return [advance_state, response]


def respond_to_broad_location(msg):
    response = "Cool! And which room, specifically? This will only " +\
               "be shared with whoever takes on your request."
    return [1, response]


def respond_to_specific_location(msg):
    response = "Sounds great. We just notified our available peer volunteers "+\
               "to ask if they can help you at your dorm! "+\
               "We'll let you know as soon as someone accepts the request :)"
    return [1, response]


if __name__ == '__main__':
    app.run()
    
    