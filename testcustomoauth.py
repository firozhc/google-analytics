import requests
import json


def auth():

	"""
		auth_url = "https://accounts.google.com/o/oauth2/v2/auth"

		response_type = "code"

		client_id="366643012552-a3p7mk041c5uehodlvv5bg4fginfjs40.apps.googleusercontent.com"

		redirect_uri="https%3A%2F%2Ftwitter.com"

		scope= "https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fanalytics.readonly"

		access_type= "offline"

		params = "response_type="+response_type+"&client_id="+client_id+"&redirect_uri="+redirect_uri+"&scope="+scope+"&access_type="+access_type

		url = auth_url+"?"+params


		#r =	requests.request("GET", auth_url, params=params)

		#print(r.url)

		#print(r.text)		

		#code="4/AACfTsEjsHZh9pIKqGdscuA6HjHsNIUkVUB58fLXd60dUq1yzYRpXxmRJjXXHLYgcpwlV0VhioUNZAsDKJEICSo"




		token_url = "https://www.googleapis.com/oauth2/v4/token"

		client_secret = "OH6MC4lS5lrg_2fsjGtlHHYi"


		grant_type= "authorization_code"


		#data = "client_secret="+client_secret+"&client_id="+client_id+"&grant_type="+grant_type+"&redirect_uri="+redirect_uri+"&code="+code

		
		data = "code="+code+"&client_id="+client_id+"&client_secret="+client_secret+"&redirect_uri="+redirect_uri+"&grant_type="+grant_type



	#	response = requests.request("POST",token_url, params=data)



	https://accounts.google.com/o/oauth2/auth?
	response_type=code
	&client_id=366643012552-a3p7mk041c5uehodlvv5bg4fginfjs40.apps.googleusercontent.com
	&redirect_uri=https%3A%2F%2Ftwitter.com
	&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fanalytics.readonly
	&state=owW4iLeE08sB2PE7ZqbB22IVbEYIeE
	&access_type=offline
	&prompt=select_account

	{
	 "access_token": "ya29.GlvjBW3t4OfccNrp3hpAH8ZRtKaZjTujV5AowYRE0uKpvRAz6b51OPnSU4m29mwqymADfno1QFUUgZZKPEEqNXYvAGxeP_-cuZsQR27s9GCX4258PC9RKof-Oo17",
	 "token_type": "Bearer",
	 "expires_in": 3546
	}


	"""

	durl = "https://analyticsreporting.googleapis.com/v4/reports:batchGet"
	payload = "{\r\n\t\"reportRequests\": [\r\n        {\r\n          \"viewId\": \"160914767\",\r\n          \"dateRanges\": [{\"startDate\": \"67daysAgo\", \"endDate\": \"today\"}],\r\n          \"metrics\": [{\"expression\": \"ga:sessions\"}],\r\n          \"dimensions\": [{\"name\": \"ga:country\"}]\r\n        }\r\n       ]\r\n}"
	headers = {
	    'Content-Type': "application/json",
	    'Authorization': "Bearer ya29.GlvjBW3t4OfccNrp3hpAH8ZRtKaZjTujV5AowYRE0uKpvRAz6b51OPnSU4m29mwqymADfno1QFUUgZZKPEEqNXYvAGxeP_-cuZsQR27s9GCX4258PC9RKof-Oo17"
	    }

	response = requests.request("POST", durl, data=payload, headers=headers)

	print(response.text)


def main():
	auth()




if __name__=="__main__":
	main()


