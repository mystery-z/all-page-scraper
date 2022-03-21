import requests
from datetime import date
import threading
import time

################################# CONFIGURATION OPTIONS ##############################################
# Debug is just to print errors if theyre thrown otherwise dont
debug=False
# Print output from urls (status code url etc) you may want to set this to false if using multithreading
printOutput = False

# how many tries createLogFile can have to create a log file (refer to above function)
logFileRetrys = 10
# how many words from whatever wordlist to attempts
countOfWords = 37000

maxThreads = 200
wordlist = "./words.txt"
#######################################################################################################

today = date.today()
d1 = today.strftime("%d-%m-%Y")
## recursive function for creating logFile if one already exists
# create file if theres an error try create another until retryLimit is exceeded 
def createLogFile(retry):
    if(retry >= logFileRetrys): return None
    fileString = ""
    try:
        fileString = d1+"-output "+str(retry)+".txt"
        open(fileString, 'x').close()
        return fileString  
    except Exception as e:
        if(debug): print(e)
        return createLogFile(retry+1)

## Open wordlist read it and return
# breaking this out into a function makes code (in my opinion ) more neat
# and simpler to follow / change
def getWords(wordList):
    file = open(wordList, "rt")
    wordList = file.readlines()
    file.close()
    return wordList





file = createLogFile(0)
readList = getWords(wordlist)




terminatedThreads = 0
openedThreads = 0






def getUrl(word):
    ## include as a global so it can be accessed outside the current thread
    # to be honest the network adapter of the machine will limit the speed of this but
    # better something then nothing
    global terminatedThreads
    try:
        link = "http://"+word+'.com/'
        r = requests.get(link)     
        status_code = str(r.status_code)
        f = open(file,"a")
        
        f.write(link + ":" + status_code + "\n")
        f.close()
        if(printOutput):
            print(link)
            print(r.status_code)
            print("----------")
        # this lets the program keep track of how many queries its completed
        # also allows a thread cap to be implemented
        terminatedThreads=terminatedThreads+1
        return 0
    except Exception as e:
        if(debug): print(e)
        terminatedThreads=terminatedThreads+1
        return 0

i = 0
while i<countOfWords:
    # the difference between openedThreads and terminatedThreads is the amount of currently running threads
    if(openedThreads-terminatedThreads < maxThreads):
        word = readList[i]
        word = word.replace("\n","")
        # create new thead and start it
        threading.Thread(target=getUrl,args=(word,)).start()
        ## increment opened threads so the program knows how many threads have been opened in total
        openedThreads=openedThreads+1
        i+=1
    else:
        # this could be put into a seperate thread and timed so the console doenst get nuked but 
        print("Completed : " + str(terminatedThreads) + " querys out of " + str(countOfWords))
