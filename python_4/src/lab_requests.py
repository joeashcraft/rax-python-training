#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_requests` -- interacting with REST
=========================================

LAB_REQUESTS Learning Objective: Learn to interact with RESTful APIs using requests library
::

 a. Using requests, HTTP GET the initial page from the url given to you by the instructor.

 b. Using the JSON you receive from the server, determine the next url you are to open.
    Use HTTP POST to send the `token` you received from the initial page back to the server
    at the next url to load the second page.

    The returned JSON object will be in the form: {'<some_key>': url, 'token': <your_token>}
    where <some_key> will change for each access and <your_token> will be the same token you
    sent to the server.

    Your post JSON should be only one element: {'token': <your_token> }

 c. Continue the pattern from step b until you get a JSON response that contains the element
    called `answer`.  Print out the final object you recieved from the server.

 Note: the token has a short timeout, so you will have to pull all the steps in a loop,
       otherwise the token will invalidate due to timeout

"""
import requests  # noqa
import json


# Load the first page using an HTTP GET
start = "http://104.239.140.190"
response = json.loads(requests.get(start).content.decode())
# json.loads(response)

finished = False
# Begin loop:
while not finished:
    #     parse the JSON object to find the next url
    for ii in response:
        if ii == "token":
            token = response[ii]
            continue
        if ii == "answer":
            print(ii, response[ii])  # we're done
            answer = response[ii]
            finished = True
            break
        else:
            next_url = response[ii]

    json_data = dict(token=token)
    response = json.loads(requests.post(next_url, json=json_data).content.decode())
    #     load the url using an HTTP POST
    #     stop the loop when the JSON object has the key: "answer"
    # Print the final JSON response

# Note: if you need to debug your HTTP connection info, call the following
# function before you do any http calls with requests:


def debug_mode():
    import logging
    from http.client import HTTPConnection
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
