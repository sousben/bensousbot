import urllib2
import json
import os

from django.shortcuts import render
from django.http import HttpResponse

###VARIABLES THAT YOU NEED TO SET MANUALLY IF NOT ON HEROKU#####
try:
	CLIENT_ID = os.environ['SLACK_CLIENT_ID'] 
	CLIENT_SECRET = os.environ['SLACK_CLIENT_SECRET']
except:
	CLIENT_ID = 'Manually set the Message if youre not running through heroku or have not set vars in ENV'
	CLIENT_SECRET = 'Manually set the API Token if youre not running through heroku or have not set vars in ENV'
###############################################################

def oauth(request):
    print 'new app install what else'
    print request.GET
    getDict = request.GET
    code = getDict.get('code','0')
    print code
    
    url = 'https://slack.com/api/oauth.access?client_id='+CLIENT_ID+'&client_secret='+CLIENT_SECRET+'&code='+code
    serialized_data = urllib2.urlopen(url).read()
    data = json.loads(serialized_data)
    
    print 'Request successful with result:' 
    err = data.get('error','')
    print err
    
    if (err == ''):
      return HttpResponse('Installation Successful!')
    else:
      return HttpResponse('Installation Unsuccessful with error: ' + err)

    # https://slack.com/api/oauth.access?

def poll(request, pollName):
    print 'user requested poll page with name ' + pollName
    print type(request)
    print request.GET
    return render(request, 'index.html')

