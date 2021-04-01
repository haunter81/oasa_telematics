import requests

stops = ['340060','340061','40115','060814']

for t in range(len(stops)):
    stopnum = stops[t]
    #vrisko to onoma tis stasis
    stopnamelink="http://telematics.oasa.gr/api/?act=getStopNameAndXY&p1="+stopnum
    r = requests.get(stopnamelink)
    table3=r.json()
    print("--------------")
    print ("*"+table3[0]['stop_descr']+"*")
###### vrisko to lineid px 218
    linenamelink="http://telematics.oasa.gr/api/?act=webRoutesForStop&p1="+stopnum
    r = requests.get(linenamelink)
    table4=r.json()
######
    link="http://telematics.oasa.gr/api/?act=getStopArrivals&p1="+stopnum
    r = requests.get(link)
    table=r.json()
    if table != None:
       for i in range(len(table)):
          routecode=table[i]['route_code']
          time=table[i]['btime2']
          for t in range(len(table4)):
             if routecode==table4[t]['RouteCode']:
                linename=table4[t]['RouteDescr']
                linenumber=table4[t]['LineID']
          print ("["+linenumber+"] "+linename+" σε "+time+" λεπτα!")
