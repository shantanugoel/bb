import json
import requests
import datetime
import time
import sys

time_to_sleep_sec = 30

telegram_url = "https://api.telegram.org/bot[YOURBOTAPIKEY]/sendMessage?chat_id=@bbslotsnotifier&text='Slots Available'"



cookies = {
        # Your own cookies
}

headers = {
        # Your Headers
}

data = {
  'addr_id': '[Address id]'
}

print("##########################")
sys.stdout.flush()
while (1):
  print("====")
  sys.stdout.flush()
  print(datetime.datetime.now())
  sys.stdout.flush()
  response = requests.post('https://www.bigbasket.com/co/update-po/', headers=headers, cookies=cookies, data=data)
  body = response.json()
  print(body)
  sys.stdout.flush()
  if body['status'].lower() != "failure":
    response = requests.get(telegram_url)
    print(response)
    sys.stdout.flush()
  else:
    print("Slot Not available")
    sys.stdout.flush()
  time.sleep(time_to_sleep_sec)

