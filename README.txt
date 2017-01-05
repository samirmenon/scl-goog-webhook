This will set up a web interface for allowing scl to receive google action commands.


There are a few components:

****************
1. Google Action
****************

The high level goal is to use the google natural language api to
support human-robot natural language interaction.

       ------------------------------------------------------
       
1.a) Api.ai Natural Language Action Specification (api.ai)

The api.ai system allows one to broadly define an intent-to-json schema.
It enables setting up high level natural language communication.

There is a straightforward tutorial at : https://www.youtube.com/watch?v=9SUAuy9OJg4
Set up a basic app and control it at the console.api.ai website.

       ------------------------------------------------------
       
1.b) Google Action integration (developers.google.com/actions)

This is required to connect an api.ai bot to some device (or simulator).
For now, it seems like there is an option to either connect it to a google home
device or to the web simulator.

The web simulator is here : https://developers.google.com/actions/tools/web-simulator
Once you publish an api.ai action, you can connect it to the simulator (top right).

There is also an option to integrate with a "webhook" (todo : more about this).

       ------------------------------------------------------
       
1.c)


****************
2. Webhook
****************

Our high level goal is to communicate with a google device. As such, we
need to eat the json and return json with ack responses.

       ------------------------------------------------------
       
2.a) Heroku webhook

Google recommends this as a default. We'll try it out. For now, it seems to allow you to set up
web access through a variety of different programming languages.

2017/01/04 : The default integration is funky and doesn't work...

       ------------------------------------------------------
       
2.b) Python Flask program to process api.ai POST messages 

The api.ai system webhooks use POST messaging to send/recv stuff from a web service:
https://docs.api.ai/docs/webhook

So we basically have to write a small program that can run a server to send/recv these
JSON messages.

MESSAGE FROM GOOG:
Goog will POST a message to your web service with the following json format:
https://docs.api.ai/docs/query#response

MESSAGE TO GOOG:
Goog asks for you to send a json message with the followinig format:
https://docs.api.ai/docs/webhook#section-format-of-response-from-the-service 

DEBUGGING:
It's annoying to debug the app through the web framework (for now, say we're using heorku).
So we have a few test things:
2.b.i) First run the app locally using python+flask
$ phon scl_goog_webhook.py
2.b.ii) Run another python shell and send POST requests locally.
$ ipython
import requests as r
req = {'question':'what is the answer?'}
req = {'result': {'parameters': {'primitive-type':"move"}}};
rr = r.post('http://localhost:5000/scl_webhook', json=req); print rr.text 

*******************
3. Running the app
*******************

