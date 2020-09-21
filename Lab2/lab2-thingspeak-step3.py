import urllib.request
import requests
import threading
import json

import random

def read_data_thingspeak():
    URl='https://api.thingspeak.com/channels/1151983/feeds.json?results=2'
    KEY='CKQC28N0E0QCQOJZ'
    HEADER='&results=2'
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    
    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    
    channel_id=get_data['channel']['id']
    
    field1 = get_data['feeds']
    #print(field1)
    
    t=[]
    for x in field1:
        t.append(x['field1'])
        
    print(t)
    
    
    
if __name__ == '__main__':
    read_data_thingspeak()