import json
import requests



def auth(url):
	headers = { "Content-Type": "application/json; charset=utf-8"}
	VIEW_ID = '160914767'
 	body = {
 	'reportRequests':[{
	            'viewId': VIEW_ID,
	            'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
	            'metrics': [{'expression': 'ga:pageviews'}, {'expression': 'ga:uniquePageviews'},'expression': 'ga:avgTimeOnPage'], 
	            'dimensions': [{'name': 'ga:pagePath'}, {'name': 'ga:sourceMedium'}],
	            'orderBys': [{'fieldName': 'ga:pageviews', 'sortOrder': 'DESCENDING'}]
	        					}
						    	]
	 							   }
          

	body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:country'}]
        }]
      }

    print(type(body))


	data = json.loads(body)

	print(type(data))

	response = requests.request("POST", url, headers=headers, data= data) 

	print(response.text)









def main():

	url = "https://analyticsreporting.googleapis.com/v4/reports:batchGet"

	auth(url)

	client_id = "366643012552-a3p7mk041c5uehodlvv5bg4fginfjs40.apps.googleusercontent.com"
	client_secret = "OH6MC4lS5lrg_2fsjGtlHHYi"


if __name__=="__main__":
	main()
