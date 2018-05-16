import json

class Audits:
  def check_adwordsLink(self,management_get):
    """ 
    Function that checks whether adwords account is linked or not
    """
    linked_dict = management_get['adwords_linked']
    #print type(linked_dict)
    linked_list = linked_dict['items']
    if(len(linked_list) == 0):
      print 'No AdWords account linked'
      return json.dumps({"Adwords Link" : 1})
    else:
      print 'AdWords account(s) linked' 
      return json.dumps({"Adwords Link" : 0})
    
    

  def check_medium(self,useful_values):
    """
    Function which checks if any Mediums are not set
    """
    itr = 0
    medium_list = useful_values['medium_list']
    for medium in medium_list:
    
      if (str(medium) == '(not set)'):
        itr += 1 
    print 'Medium not set for ' + str(itr) + ' sources'
    return json.dumps({'unset_mediums' : itr})


  def check_totalValue(self,useful_values):
    totalValue = useful_values['totalValue']
    if(totalValue > 0):
      print totalValue


  def check_siteSearch(self,useful_values):
    searchSessions = useful_values['searchSessions']
    print searchSessions
    if(searchSessions>0):
      print "Site Search active, total Site Searches in last 7 days: " + str(searchSessions)
    else:
      print "Site search not active"

  def check_selfReferral(self,url,useful_values):
    flag = False
    str_referrer = []
    fullReferrer_list = useful_values['fullReferrer_list']
    for reference in fullReferrer_list:
      reference = str(reference)
      if(reference == url):
        print "URL '" + url + "' exists, self refferal happening"
        flag = True
    if(flag == False):
      print 'URL does not exist, self refferal is happening'

  def check_eventTracking(self,useful_values):
    totalEvents = useful_values['totalEvents']
    if(totalEvents>0):
      print "Evet tracking active, total Events in last 7 days: " + str(totalEvents)
    elif(totalEvents == 0):
      print "Event tracking not active"

  def check_customDimensions(self,management_get):
    custom_dimensions = management_get['customDimensions_list']
    if(len(custom_dimensions)>0):
      print 'Custom Dimensions exist, total custom dimensions: ' + str(len(custom_dimensions))

  def check_gtm(self,accounts):
    n_accounts = len(accounts)

    if(n_accounts == 0):
      print 'GTM is not set up'
    elif(n_accounts > 0):
      i = 0
      while(i<n_accounts):
        print 'GTM set up, the following account(s) exist: \n' + accounts['account'][0]['name']
        i += 1
  
  def check_goals(self,management_get):
    goals = management_get['goals_list']
    print 'total goals: ' + str(len(goals))
    for goal in goals:
      print goal

  def check_customMetrics(self,management_get):
    custom_metrics = management_get['customMetrics_list']
    
    if(len(custom_metrics) == 0):
      print 'No custom metrics have been created'
    else:
      print 'The following custom metrics exist: '
      for metric in custom_metrics:
        print metric
    