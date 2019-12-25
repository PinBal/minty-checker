import urllib2
import json

codes = []

with open('codes.txt', 'r') as filehandle:
    codes = [codes.rstrip() for codes in filehandle.readlines()]


for z in codes:
    #print z
    response = urllib2.urlopen('https://www.epicgames.com/fortnite/ajax/redemption/validate-redemption-code?redeem-code=')
    data = response.read()
    y = json.loads(data)
    status = y["isSuccess"]
    if status == False:
        print "Code " + z + " Is not working!"
    else:
        print "Code " + z + " Is working go and RiDdIm it! xsdxd"
    
    
    response.close()