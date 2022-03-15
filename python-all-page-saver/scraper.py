import requests
 
file = open("words.txt", "rt")
readList = file.readlines()
file.close()

a=0
while a<370103:
	word = readList[a]
	word = word.replace("\n","")
	print(word+":")
	try:
		link = "http://"+word+'.com/'
		print(link)
		r = requests.get(link)
		print(r.status_code)
		print(r.text+"\n\n")
		a = a+1 
	except:
		print("error\n\n")
		a = a+1
