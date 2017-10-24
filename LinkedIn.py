CONSUMER_KEY = '9pux1XcwXXXXXXXXXX'     # This is api_key
CONSUMER_SECRET = 'brtXoXEXXXXXXXXXXXXX'   # This is secret_key

USER_TOKEN = '27138ae8-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXb'   # This is oauth_token
USER_SECRET = 'ca103e23-XXXXXXXXXXXXXXXXXXXXXXXX7bba512625e'   # This is oauth_secret
RETURN_URL = 'http://localhost:8000'

from linkedin import linkedin
from oauthlib import *

# Define CONSUMER_KEY, CONSUMER_SECRET,
# USER_TOKEN, and USER_SECRET from the credentials
# provided in your LinkedIn application

# Instantiate the developer authentication class

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
                                                      USER_TOKEN, USER_SECRET,
                                                      RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

g = application.get_profile()
print g