import requests
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d-%m-%Y")
 
file = open("words.txt", "rt")
readList = file.readlines()
file.close()

saver = open(d1+ "-output.txt", 'x')
saver = open(d1+ "-output.txt", 'w')


a=0
while a<3:
	word = readList[a]
	word = word.replace("\n","")
	print(word+":")
	saver.write(word+":")
	try:
		link = "http://"+word+'.com/'
		print(link)
		saver.write(link)
		r = requests.get(link)
		print(r.status_code)
		status_code = str(r.status_code)
		saver.write(status_code)
		print(r.text+"\n\n")
		status_text = str(r.text)
		status_text = status_text+"\n\n"
		saver.write(status_text)
		a = a+1 
	except:
		print("error\n\n")
		saver.write("error\n\n")
		a = a+1
saver.close()
