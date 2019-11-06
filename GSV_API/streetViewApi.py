import pandas as pd
import google_streetview.api


csvExport = pd.read_csv("./DVA_Group_Project/Data/TransBase/geo_st_intrsctn.csv", sep = ",",usecols = ["latitude","longitude"])
#print(csvExport)
params=[]
count=0
for index, rows in csvExport.iterrows(): 
   latitude =rows.latitude
   longitude= rows.longitude
   input_array= {
	'size': '600x300', 
	'location': ''+str(latitude)+','+str(longitude)+'',
	'heading': '151.78',
	'pitch': '-0.76',
	'key': 'AIzaSyB0NpeNQgVuTxfHdkxw2lhl7WCvpWN6GXc'
}
   count+=1
   print(count)
   print(latitude,longitude)
   params.append(input_array)
print(count)
results = google_streetview.api.results(params)
# Preview results
#results.preview()

# Download images to directory 'downloads'
results.download_links('downloads')

# Save links
results.save_links('links.txt')

# Save metadata
results.save_metadata('metadata.json')

#print(params)

#latitude=37.70941911820
#longitude=-122.38250569300
#input_array= {
#	'size': '600x300', 
#	'location': ''+str(latitude)+','+str(longitude)+'',
#	'heading': '151.78',
#	'pitch': '-0.76',
#	'key': 'AIzaSyB0NpeNQgVuTxfHdkxw2lhl7WCvpWN6GXc'
#}
#params.append(input_array)



#params = [{
#	'size': '600x300', # max 640x640 pixels
#	'location': '37.70941911820,-122.38250569300',
#    ##'46.414382,10.013988',
#	'heading': '151.78',
#	'pitch': '-0.76',
#	'key': 'AIzaSyB0NpeNQgVuTxfHdkxw2lhl7WCvpWN6GXc'
#}]
#
#results = google_streetview.api.results(params)
#
## Download images to directory 'downloads'
#results.download_links('downloads')