#import requests
import json
#import requests_oauthlib 
from requests_oauthlib import OAuth2Session

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'anthem-private-key.json'
#VIEW_ID = '160918545' #All ANOC Live Website Data 
VIEW_ID = '160914767' #All eWK Live Website Data

client_id = "366643012552-a3p7mk041c5uehodlvv5bg4fginfjs40.apps.googleusercontent.com"

client_secret = "OH6MC4lS5lrg_2fsjGtlHHYi"

#redirect_uri = "https://841f3c0c.ngrok.io/"

redirect_uri = "https://twitter.com"


authorization_response = "4/AABrOZIfqKN0r_rxRHpapKTsuZHgogxDvy7QjXpWBitmV8nIZ2ZYWjIycwX0cwI7TxUu80dGQTvPVQbPbG0_LgU"

#authorization_response = "https://twitter.com/?state=f2cIumxe8zQBoA4vJY0dX1POkJPNFI&code=4/AABrOZIfqKN0r_rxRHpapKTsuZHgogxDvy7QjXpWBitmV8nIZ2ZYWjIycwX0cwI7TxUu80dGQTvPVQbPbG0_LgU"

url = "https://accounts.google.com/o/oauth2/auth"

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=SCOPES)

authorization_url, state = oauth.authorization_url(url, access_type="offline", prompt="select_account")

print ('Please go to %s and authorize access.' % authorization_url)

#authorization_response= '4/AADwogHMRTiX6_OBA1iGvU4Igrz-cPO_fvuB1EtxWU7Xkvwex56DIkgVmVntauB6zD-Um-bCDLKKcgMHIPE9OYQ'

#token = oauth.fetch_token('https://accounts.google.com/o/oauth2/token', client_secret=client_secret, authorization_response= authorization_response)


#token = oauth.fetch_token('https://accounts.google.com/o/oauth2/token', client_secret=client_secret, code= authorization_response)

r = oauth.post('https://analyticsreporting.googleapis.com/v4/reports:batchGet')

print(r.text)

"""

https://accounts.google.com/o/oauth2/v2/auth?
scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.metadata.readonly
&state=state_parameter_passthrough_value
&redirect_uri=http%3A%2F%2Flocalhost%2Foauth2callback
&access_type=offline
&response_type=code
&client_id=583306224539-atbcaa8ne8g85e8kc006o6vmq99qiid0.apps.googleusercontent.com
"""

"""
https://accounts.google.com/o/oauth2/auth?
response_type=code
&client_id=366643012552-a3p7mk041c5uehodlvv5bg4fginfjs40.apps.googleusercontent.com
&redirect_uri=https%3A%2F%2Ftwitter.com
&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fanalytics.readonly
&state=owW4iLeE08sB2PE7ZqbB22IVbEYIeE
&access_type=offline
&prompt=select_account
"""


"""

https://accounts.google.com/o/oauth2/auth?
response_type=code
&client_id=366643012552-a3p7mk041c5uehodlvv5bg4fginfjs40.apps.googleusercontent.com
&redirect_uri=https%3A%2F%2Ftwitter.com
&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fanalytics.readonly
&state=owW4iLeE08sB2PE7ZqbB22IVbEYIeE
&access_type=offline
&prompt=select_account
"""