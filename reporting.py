from apiclient.discovery import build
#from oauth2client.service_account import ServiceAccountCredentials

import json
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from initialize import Initialize

class Reporting:
  IN_initialize = Initialize()
  VIEW_ID = IN_initialize.VIEW_ID
  ACCOUNT_ID = IN_initialize.ACCOUNT_ID
  WEB_PROPERTY_ID = IN_initialize.WEB_PROPERTY_ID

  def get_gtm(self,analytics):
    gtm = analytics['gtm']
    accounts = gtm.accounts().list().execute()
    return accounts

  def get_management(self,analytics):
    #API V4 does not have management resource so we use V3 for this

    analytics_v3 = analytics['analytics_v3']
  
    custom_dimensions = analytics_v3.management().customDimensions().list(
      accountId =  self.ACCOUNT_ID, 
      webPropertyId = self.WEB_PROPERTY_ID
    ).execute() 

    custom_metrics = analytics_v3.management().customMetrics().list(
      accountId = self.ACCOUNT_ID,
      webPropertyId = self.WEB_PROPERTY_ID
    ).execute()

    adwords_linked = analytics_v3.management().webPropertyAdWordsLinks().list(
      accountId = self.ACCOUNT_ID,
      webPropertyId = self.WEB_PROPERTY_ID 
    ).execute()

    goals = analytics_v3.management().goals().list(
      accountId = self.ACCOUNT_ID,
      webPropertyId = self.WEB_PROPERTY_ID,
      profileId = self.VIEW_ID
    ).execute()
    
    #print json.dumps(custom_metrics,sort_keys=True,indent=2)
    
    customMetrics_list = []

    for metric in custom_metrics.get('items',[]):
      metric_name = metric.get('name')
      print metric_name
      customMetrics_list.append(metric_name)

    customDimensions_list = []
    for dimension in custom_dimensions.get('items',[]):
      Cdimension_name = dimension.get('name')
      customDimensions_list.append(Cdimension_name)
    
    goals_list = []
    for goal in goals.get('items',[]):
      goal_name = goal.get('name')
      goals_list.append(goal_name)    

    managemnt_get = {'customDimensions_list':customDimensions_list, 'adwords_linked':adwords_linked,
                      'goals_list':goals_list, 'customMetrics_list':customMetrics_list}
    
    return managemnt_get


  def get_report(self,analytics):
    """Using the Analytics Service Object to query the Analytics Reporting API V4.
    """
    #VIEW_ID = IN_initialize.VIEW_ID
  
    analytics_v4 = analytics['analytics_v4']
  
    report = analytics_v4.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': self.VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:searchSessions'}, {'expression': 'ga:totalEvents'},
          {'expression':'ga:totalValue'}]
        },
        
        {
          'viewId': self.VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'dimensions': [{'name': 'ga:fullReferrer'}, {'name': 'ga:medium'}]
        }  
        ]
        }
    ).execute()

    return report


  def print_response(self,response):
    """Parses and prints the Analytics Reporting API V4 response"""
    fullReferrer_list = []
    medium_list = []
    for report in response.get('reports', []):
      columnHeader = report.get('columnHeader', {})
      dimensionHeaders = columnHeader.get('dimensions', [])
      metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
      rows = report.get('data', {}).get('rows', [])

      for row in rows:
        dimensions = row.get('dimensions', [])
        dateRangeValues = row.get('metrics', [])

        for header, dimension in zip(dimensionHeaders, dimensions):
          #global fullReferrer_list
          if(header == 'ga:fullReferrer'):
            fullReferrer_list.append(dimension)
          if(header == 'ga:medium'):
            #global medium_list
            medium_list.append(dimension)
          #print header + ': ' + dimension

        for i, values in enumerate(dateRangeValues):
          #print 'Date range (' + str(i) + ')'
          for metricHeader, value in zip(metricHeaders, values.get('values')):
            #print metricHeader.get('name') + ': ' + value
            if(metricHeader.get('name') == 'ga:searchSessions'):
            #global searchSessions
              searchSessions = value
            if(metricHeader.get('name') == 'ga:totalEvents'):
              #global totalEvents
              totalEvents = value
            if(metricHeader.get('name') == 'ga:totalValue'):
              #global totalValue
              totalValue = value

    useful_values = {'searchSessions':searchSessions,'totalEvents':totalEvents,
                   'totalValue':totalValue, 'fullReferrer_list':fullReferrer_list, 
                   'medium_list':medium_list}
    return useful_values  
