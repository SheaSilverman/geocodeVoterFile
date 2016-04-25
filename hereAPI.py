import csv
import requests

# County,VoterID,Last Name,Suffix,First Name,Middle Name,Exempt,Address 1,Address 2,City,State,Zipcode,Mailing1,Mailing2,Mailing3,MailingCity,MailingState,MailingZip,MailingCountry,Gender,Race,DOB,Registration,Party,Precinct,Group,Split,Suffix,Status,Congress,House,Senate,Commision,SchoolBoard,AreaCode,PhoneNumber,Extension,email


APP_ID = ''
APP_CODE = ''
SOURCE_FILE = '/path/to/file.csv'
DESTINATION_FILE '/path/to/new_file.csv'

source= csv.reader( open(SOURCE_FILE,"rU") )
dest= csv.writer( open(DESTINATION_FILE,"wb+") )
counter = 0
for row in source:
	address = row[7] + " " + row[8] + " " + row[9] + " " + row[10] + " " + row[11] + " " + row[12]
	url = "https://geocoder.cit.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s&gen=8" % (address, APP_ID, APP_CODE)
	#print url
	r = requests.get(url)
	#print r.json()
	try:
		if r.json():
			if r.json()['Response']['View'] != []:
				#print r.json()['Response']['View']
				latitude = r.json()['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
				longitude = r.json()['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
				print latitude, longitude, counter
				result= row[0:] + [latitude] + [longitude]
				dest.writerow( result )
				counter += 1
	except:
		print "bad data", url
