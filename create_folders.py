import os, datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

d = datetime.date.today()
singleDay = datetime.timedelta(days=1)
targetYear = 2017

def dirPath(date):
	year = str(date.year)
	month = str(date.month) if date.month>9 else "0"+str(date.month)
	day = str(date.day) if date.day>9 else "0"+str(date.day)
	
	return dir_path+"/"+year+"/"+month+"/"+day

while(d.year==targetYear):
	if(not os.path.exists(dirPath(d))):
		os.makedirs(dirPath(d))
	d+=singleDay