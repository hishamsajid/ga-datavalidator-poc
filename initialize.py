import argparse
import cmd

from apiclient.discovery import build
#from oauth2client.service_account import ServiceAccountCredentials

import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

class Initialize:
  
  SCOPES = ['https://www.googleapis.com/auth/analytics.readonly',
            'https://www.googleapis.com/auth/tagmanager.readonly']
  DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
  CLIENT_SECRETS_PATH = '/client_secrets.json' # Path to client_secrets.json file.
  
  #UNCOMMENT IF INTERACTIVE INPUT IS DISABLED
  VIEW_ID = '#########' #8 Digit View ID
  ACCOUNT_ID = '########' #8 Digit Account ID
  WEB_PROPERTY_ID = '#########' #9 Digit Web Property ID

  #UNCOMMENT IF INTERACTIVE INPUT IS ENABLED
  # VIEW_ID =  raw_input('Enter VIEW_ID from GA Account: ') #87922352 
  # ACCOUNT_ID = raw_input('Enter ACCOUNT_ID from GA Account: ') #18735851
  # WEB_PROPERTY_ID = raw_input('Enter WEB_PROPERTY_ID from GA Account: ') #UA-18735851-5
  print 'Processing Requests...'

  def initialize_analyticsreporting(self):
    """Initializes the analyticsreporting service object.

    Returns:
      analytics an authorized analyticsreporting service object.
    """
    #Parse command-line arguments.
    parser = argparse.ArgumentParser(
      formatter_class=argparse.RawDescriptionHelpFormatter,
      parents=[tools.argparser])
    flags = parser.parse_args([])

    #Set up a Flow object to be used if we need to authenticate.
    flow = client.flow_from_clientsecrets(
      self.CLIENT_SECRETS_PATH, scope=self.SCOPES,
      message=tools.message_if_missing(self.CLIENT_SECRETS_PATH))

    #Prepare credentials, and authorize HTTP object with them.
    #If the credentials don't exist or are invalid run through the native client
    #flow. The Storage object will ensure that if successful the good
    #credentials will get written back to a file.
    storage = file.Storage('analyticsreporting.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
      credentials = tools.run_flow(flow, storage, flags)
    http = credentials.authorize(http=httplib2.Http())

  # Build the service object.
    analytics_v4 = build('analytics', 'v4', http=http, discoveryServiceUrl=self.DISCOVERY_URI)
    analytics_v3 = build('analytics', 'v3', http=http)
    gtm = build('tagmanager','v2', http = http)
    analytics = {'analytics_v3': analytics_v3, 'analytics_v4': analytics_v4, 'gtm':gtm}
    return analytics
