import httplib
import urllib
import base64
import json
import pandas as pd
import numpy as np
import requests
import time
from credentials import key

_url = 'https://api.projectoxford.ai/emotion/v1.0/recognizeInVideo'
_key = key
_maxNumRetries = 10

#paramsPost = urllib.urlencode({'outputStyle': 'perFrame',
#                               'file': 'video_michel_temer.mp4'})

paramsPost = urllib.urlencode({'file': 'video_michel_temer.mp4'})

headersPost = dict()
#headersPost['Ocp-Apim-Subscription-Key'] = _key
headersPost['content-type'] = 'application/octet-stream'
headersPost['content-type'] = 'application/json'
jsonGet = {}
headersGet = dict()
headersGet['Ocp-Apim-Subscription-Key'] = _key
paramsGet = urllib.urlencode({})


responsePost = requests.request('POST', _url + "?" + paramsPost,
                                data=open('video_michel_temer.mp4', 'rb').read(),
                                headers=headersPost)

print "Operation status code: ", responsePost.status_code

videoIDLocation = responsePost.headers['Operation-Location']

print "Waiting 2 minutes to get response from server."
time.sleep(120)

getResponse = requests.request('get', videoIDLocation, json=jsonGet,
                               data=None, headers=headersGet, params=paramsGet)

print json.loads(getResponse.text)['status']