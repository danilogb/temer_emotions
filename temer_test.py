########### Python 2.7 #############
import httplib, urllib, base64, json, requests

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'cf409a7f89634260b43da6901ff681dd',
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'https://github.com/danilobrandao/video_emotions/blob/master/video_michel_temer.mp4' }"

try:
    #conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognizeinvideo?%s" % params, body, headers)
    response = conn.getresponse()
    location = response.getheader('operation-location')
    data = response.read()
    #responseObject = json.loads(data)
    print data
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

print location
jsonGet = {}
getResponse = requests.request('get', location, json=jsonGet,
                               data=None, headers=headers, params=params)

print json.loads(getResponse.text)['status']

"""
#body = "{'url': location}"
try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    #conn.request("GET", "/emotion/v1.0/operations/{oid}?%s" % params, "{body}", headers)
    conn.request("GET", location, params, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
"""