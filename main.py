import requests
import random
from config import config, headers
import time

#Get cookies to connect to Vinted API
def getCookies():
  auth = requests.get('https://www.vinted.com/', headers)
  print("Cookies response code : "+ str(auth.status_code))
  sesscookies = dict(auth.cookies)
  return sesscookies

def getUsername(sesscookies):
    userReq = requests.get("https://www.vinted.com/api/v2/users/"+config["username"], cookies=sesscookies)
    json_parsed = userReq.json()
    userIDs = json_parsed.get('user')
    userID = str(userIDs['id'])
    print("User: "+ config['username']+ " (" + userID+")")
    return userID

def getUserItems(userID, sesscookies):
    itemList = []
    itemsReq = requests.get("https://www.vinted.com/api/v2/users/"+userID+"/items?page=1&per_page=96&order=newest_first&currency=EUR", cookies=sesscookies)
    json_parsed = itemsReq.json()
    items = json_parsed.get('items')
    for i in items:
        itemList.append(i['url'])
    print(str(len(itemList))+ " items found on the profile\n")
    return itemList

def addViewsItems(itemList, cpt):
    count = 0
    for i in itemList:
        requests.get(i, headers)
        count += 1
        print("Item: "+str(count)+"/"+str(len(itemList))+" (Viewed: "+str(count+cpt)+")", end='\r')
    
       
print("┌────────────────────────┐\n│ Vinted Views Generator │\n│   github.com/lulucmy   │\n│     Initializing...    │\n└────────────────────────┘\n")
cpt = 0

sesscookies = getCookies()
userID = getUsername(sesscookies)
itemList = getUserItems(userID, sesscookies)

try:
    while True:
        addViewsItems(itemList, cpt)
        cpt += len(itemList)
        print("\nViewed "+str(cpt)+" items.")
        if (config['cooldown']):
            rand = random.randint(3, 9)
            print("Sleeping for "+str(rand)+"s")
            time.sleep(rand)
except KeyboardInterrupt:
    print('Goodbye!')