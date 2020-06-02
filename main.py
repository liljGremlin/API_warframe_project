
import json
import requests
import time



url = 'https://api.warframestat.us/ps4/fissures'
current_survivals = [] # hold current survivals until new once appear
ids_sent = []
#execute every 5 sec

while True:
    raw_data = requests.get(url)
    fissures_data = json.loads(raw_data.text)

    # I have to clear to get rid of the old id's
    current_survivals.clear()

    print()
    for x in fissures_data:
        print(x['missionType'])
    print()
    # add 
    for mission in fissures_data:
        if mission['missionType'] == 'Capture':
            # add to current_survivals
            current_survivals.append(mission['id'])

    # Makes sure not to send an email twice 
    for x in current_survivals:
        if x in ids_sent:
            print("Email already sent.")
        else:
            ids_sent.append(x)
            print("Sent Email")
            # send an email 
    
    print("Current_survivals: " + str(current_survivals))
    print("ids_sent: " + str(ids_sent) + "\n")


    time.sleep(60) #will run agian after 1 minute
