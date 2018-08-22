import os
from time import gmtime, strftime
import json
import geojson
import time
import threading
import urllib
import urllib2
import requests


url = 'https://municipal.systems/v1/data?key=80c8a4a0-bc70-43f5-820b-ea96eaed310f' #keyData is your Data Source Key. Generate this on the Source Page.

         
os.system('clear') #clear the terminal (optional)
         
# class GpsPoller(threading.Thread):
#           def __init__(self):
#             threading.Thread.__init__(self)
#             global gpsd #bring it in scope
#             gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
#             self.current_value = None
#             self.running = True #setting the thread running to true
         
#           def run(self):
#             global gpsd
#             while gpsp.running:
#               gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
         
if __name__ == '__main__':
          # gpsp = GpsPoller() # create the thread
          try:
            # gpsp.start() # start it up
            while True:
              #It may take a second or two to get good data
         
              os.system('clear')

              location = geojson.Point(((-74.09115314483641 40.71384197546361)))
              speed = '8 KM/H'
              routeId = 'AV Pilot Vehicle Route 2'
              manufacturedAt = '2017-01-01' #Use ISO 8601 syntax YYYY-MM-DD 
              manufacturer = 'Ford'
              model = 'Fusion'
              color = 'Oxford White'
              vin = '1HGCM12345A006789'
              plate = '12345NJ' 
              type = 'AV Shuttle Bus'
              active: TRUE
              id = 'Pilot AV 1' + strftime("%H:%M:%S")

         	
              print
              print ' GPS reading'
              print '----------------------------------------'
              print 'location    ' , location
              print 'speed       ' , speed

              payload = {'location':location, 'speed':speed, "routeId":routeId, "manufacturedAt":manufacturedAt, "manufacturer":manufacturer, "model":model 
              "color":color, "vin":vin, "plate":plate, 'type':type, 'id':id, 'active':active}

              r = requests.post(url, json=payload)
              print r.content #200 = successful http request. 400 = bad request; check your syntax.  500 = server error, check stae status page.
         
              time.sleep(10) #default value will send GPS data every 10 seconds. use faster speeds for faster or right-of-way vehicles.
         
          except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
            print "\nStopping GPS program..."
            # gpsp.running = False
            # gpsp.join() # wait for the thread to finish what it's doing
          print "Done.\nExiting."
