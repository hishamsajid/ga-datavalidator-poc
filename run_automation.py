from initialize import Initialize
from reporting import Reporting
from audits import Audits
import json

def main():
  IN_initialize = Initialize()
  IN_reporting = Reporting()
  IN_audits = Audits()

  Output = []

  analytics = IN_initialize.initialize_analyticsreporting()
  response = IN_reporting.get_report(analytics)
  management_get = IN_reporting.get_management(analytics)
  useful_values = IN_reporting.print_response(response)
  accounts = IN_reporting.get_gtm(analytics)
  
  print "######"
  IN_audits.check_siteSearch(useful_values)
  print "_______"
  Output.append(IN_audits.check_medium(useful_values))
  #check_totalValue()
  print "_______"
  IN_audits.check_customDimensions(management_get)
  print "_______"
  #url = raw_input('Enter URL for self-Referral check: ')
  IN_audits.check_selfReferral('yandex',useful_values)
  print "_______"
  IN_audits.check_eventTracking(useful_values)
  print "_______"
  Output.append(IN_audits.check_adwordsLink(management_get))
  print "_______"
  IN_audits.check_gtm(accounts)
  print "_______"
  IN_audits.check_goals(management_get)
  print "_______"
  IN_audits.check_customMetrics(management_get)
  print "######"
  print Output
  with open('data.json', 'w') as djson:
    json.dump(Output,djson)
  
  #print set(fullReferrer_list)
  # if(searchSessions>0):
  #     print "Site Search active"

if __name__ == '__main__':
  main()