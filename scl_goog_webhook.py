#!/usr/bin/env python

# An application to support webhooks with the api.ai framework.
# Processes requests and parses them into messages that can be translated into
# robot commands
# For more, see scl documentation

# Author : Samir Menon
# 2017-01-04 : Basic application created

from flask import Flask
from flask import request
from flask import make_response

# Import a few useful libraries
import json
import os

# Flask app should start in global layout
# The flask framework requires this specific init to work.
app = Flask(__name__);

# This is the function that we'll trigger with our natural language API.
# This particular implementation is for Google's api.ai action framework.
@app.route('/webhook', methods=['POST'])
def scl_webhook():
    # Get a hold of the Goog action POST request.
    req = request.get_json(silent=True, force=True);
    # First we parse the Goog action POST request. And get a JSON object back.
    result_json = processRequest(req);
    # Next we convert the JSON object into a proper return response
    retval = make_response(result_json);
    retval.headers['Content-Type'] = 'application/json';
    # Finally, we send the response back to the Goog action.
    return retval;

# This is just a random function to see if the service is up.
@app.route('/webhook-info')
def webhookTester():
    return '<h2>SCL Google Action Responder</h2><br /> <br />Version 0.1, 2017-01 <br /> Author : Samir Menon';

# This parses the request and adds a response.
# Returns : A json object with the message to return to the Goog action service
def parseRequest(req):
    if req.get("result").get("parameters").get("primitive-type") != "move":
        return json.dumps({});
    # Google requires the following fields
    dd = {};
    dd['speech'] = "Robot moved";
    dd['displayText'] = dd['speech'];
    # For now we won't add any data to the return response.
    dd['data'] = {};
    dd['contextOut'] = [];
    dd['source'] = "SCL";
    # Now we'll convert the object into a json structure.
    data = json.dumps(dd);
    return data;

# This starts the app..
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
