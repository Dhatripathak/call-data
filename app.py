# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

call = client.calls.create(
  url=os.getenv("URL"),
  to="+918604059177",
  from_="+17622466952"
)

print(call.sid)