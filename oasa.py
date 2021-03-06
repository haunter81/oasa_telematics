#import urllib.request, json
#import pandas as pd
import requests

#stops = ['060814','340060','340061','340101','40115' ,'170022']
stops = ['340060','340061','40115','060814']

for t in range(len(stops)):
    stopnum = stops[t]
    #vrisko to onoma tis stasis
    stopnamelink="http://telematics.oasa.gr/api/?act=getStopNameAndXY&p1="+stopnum
    r = requests.get(stopnamelink)
    table3=r.json()
    #print(table3)
    print("--------------")
    print ("*"+table3[0]['stop_descr']+"*")

######
###### vrisko to lineid px 218
    linenamelink="http://telematics.oasa.gr/api/?act=webRoutesForStop&p1="+stopnum
    r = requests.get(linenamelink)
    table4=r.json()
    #print(table4) ##debug
######
    link="http://telematics.oasa.gr/api/?act=getStopArrivals&p1="+stopnum
    r = requests.get(link)
    table=r.json()
    #print(table)
    #print(r) gia na do response
    #length = len(table)
    if table != None:
       for i in range(len(table)):
          #print (table)
          #print(table[i]['route_code'])
          routecode=table[i]['route_code']
          time=table[i]['btime2']
          #print (length)
          #print (routecode)
          link2="http://telematics.oasa.gr/api/?act=getRouteName&p1="+routecode
          r = requests.get(link2)
          #print(r)
          table2=r.json()
          #print (table)
          linename=table2[0]['route_descr']
          #####dokimi gia lineid
          linenumber = ""
          for e in range(len(table4)):
             if routecode==table4[e]['RouteCode']:
                linenumber=table4[e]['LineID']
          print ("["+linenumber+"] "+linename+" σε "+time+" λεπτα!")

