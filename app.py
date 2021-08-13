#Note: Upload this script onto OSSIM and execute it from OSSIM. Select the option of generate alert when the script is executed.
#Have any questions? Open a issue :)
import requests
import sys
import json
import time
import uuid
import re
import argparse
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact, CustomFieldHelper

THEHIVE_URL = 'Put your hive url here'
THEHIVE_API_KEY = 'Put your hive api key here'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)
parser = argparse.ArgumentParser()
parser.add_argument('--DSTIP', type=str, required=True)
parser.add_argument('--SRCIP', type=str, required=True)
#parser.add_argument('--DSTHOST', type=str, required=True)
#parser.add_argument('--SRCHOST', type=str, required=True)
parser.add_argument('--RSK', type=str, required=True)
parser.add_argument('--USRDATA1', type=str, required=True)
parser.add_argument('--USRDATA2', type=str, required=True)
#parser.add_argument('--FILE', type=str, required=True)
args = parser.parse_args()
ip=args.DSTIP
srcip=args.SRCIP
#dsthostname=args.DSTHOST
#srchostname=args.SRCHOST
userdata1=args.USRDATA1
userdata2=args.USRDATA2
rsk=args.RSK
if rsk == 'Low':
    tlpset=1
elif rsk == 'Medium':
    tlpset=2
else:
    tlpset=3

#filename=args.FILE
# Prepare observables
#inmemory_file = open('sample.txt', 'rb')
artifacts = [
    AlertArtifact(dataType='ip', data=ip),
    AlertArtifact(dataType='srcip', data=srcip),
    AlertArtifact(dataType='domain', data='testing.com'),
    AlertArtifact(dataType='MAC address', data=userdata1),
    AlertArtifact(dataType='Machine Name', data=userdata2)
   # AlertArtifact(dataType='file', data=filename)
]

# Prepare custom fields
#customFields = CustomFieldHelper()\
    #.add_string('Destination Hostname', dsthostname)\
    #.add_string('Source Hostname', srchostname)\
    #.add_string('business-impact', 'HIGH')\
    #.add_date('occur-date', int(time.time())*1000)\
    #.add_number('cvss', 6)\
    #.build()

# Prepare the sample Alert
sourceRef = str(uuid.uuid4())[0:6]
alert = Alert(title='New Alert from STIP',
    tlp=tlpset,
    tags=['TheHive4Py', 'sample'],
    description='N/A',
    type='external',
    source='STIP',
    sourceRef=sourceRef,
    artifacts=artifacts,
    #customFields=customFields
)

# Create the alert
try:
  response = api.create_alert(alert)

  # Print the JSON response
  print("JSON response")
  print(json.dumps(response.json(), indent=4, sort_keys=True))

except AlertException as e:
  print("In alert exception!")
  print("Alert create error: {}".format(e))

#inmemory_file.close()

# Exit the program
sys.exit(0)
