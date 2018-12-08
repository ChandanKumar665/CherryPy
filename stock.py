import urllib.request, shutil
from zipfile import *
import csv
import redis
zip_file_url='https://www.bseindia.com/download/BhavCopy/Equity/EQ051218_CSV.ZIP'
file_name=zip_file_url.split('/')[-1]
row=[]
fields=[]
file_list=[]
redis_db=redis.Redis(host='localhost',port=6379,db=0)
try:
	with urllib.request.urlopen(zip_file_url) as response, open(file_name, 'wb') as out_file:
	    shutil.copyfileobj(response, out_file)
	with ZipFile(file_name) as zf:
		zf.extractall()
		file_list=zf.namelist()
	print(file_list)    
	with open(file_list[0],'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		print(csv_reader.line_num)
		for obj in csv_reader:
			row.append(obj)
	print('Fields: '+' '.join(x for x in row[0]))
	# last=len(row[0])
	
	for obj in row[1:5]:
		i=0
		for col in obj:
			redis_db.set(row[0][i],col)
			print(col,end=' ')
			# print(row[0][i])
			i+=1
		print('\n')
	# for key in redis_db.scan_iter():
	# 	print(key,redis_db.get(key))	
	# print(redis_db.get(row[0][0]))			
except Exception as e:
	raise e
else:
	print('file downloaded')	
finally:
	pass