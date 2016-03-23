from tabulate import tabulate
import random
import time
import math

nextRound = 1
YourLogo = "YourLogo.jpg"
leftLogo = YourLogo
rightLogo = YourLogo

def tic():
	return time.time()

def toc(a):
	b = time.time() - a
	return b

def getWins(item):
	return item[2]
	
def getTables(item):
	return item[0]

def isEven(number):
	nf = math.floor(0.5*number)
	nc = math.ceil(0.5*number)
	return nf == nc
	
def getClub(variable):
	# Get which club they are in and check if they are still playing.
	# 0 if they have dropped, string or 1 if still playing.
	# String is the club.
	# Returns (stillPlaying,club)
	try:
		# This will catch 0s and 1s. If 0, the rest of the program will skip this player. If 1, return a random string for the club so their club won't match any other club.
		stillPlaying = int(variable)
		club = "%0.20f" % random.random()
	except:
		# If it is a string, it'll fail. But it also means they are still playing so return a 1 and their club.
		stillPlaying = 1
		club = variable
	return (stillPlaying, club)
	#return isinstance(variable, basestring) # Python 2.x
	#return isinstance(variable, str) # Python 3.x

fo = open('aaRound '+str(nextRound)+' Draw.txt','r')
pairsS = fo.read().splitlines()
pairs = []
for n in range(len(pairsS)):
	players = pairsS[n].split('\t')
	pairs.append([n+1,players[0],players[1]])
	print(pairs[n])

pairHeaders = ["Table","Player 1","Player A"]
printingString = tabulate(pairs, headers=pairHeaders, tablefmt="simple")
print(printingString)
displayFileObject = open("zzRound "+str(nextRound)+" Draw.txt","w")
displayFileObject.write(printingString)

htmlTable = tabulate(pairs, headers=pairHeaders, tablefmt="html")

splitTable = htmlTable.split()

for n in range(len(splitTable)):
	if splitTable[n] == 'right;">':
		splitTable[n] = 'center;">'

htmlTable = ' '.join(splitTable)

logoWidth = 150

#for n in range(len(htmlLogos)):
leftLogo = 'YourLogo.jpg'
rightLogo = 'YourLogoMirror.jpg'
htmlStartString = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"><html><head><title>Round %d Draw</title><style type="text/css">\nbody {\n	font-family: Georgia, "Times New Roman", Times, serif;\nbackground-color: #111;\n}\nh2 {\ncolor: #fff;}\ntable {\nborder: 1px solid black;\nborder-collapse: collapse;\nfloat: center\n}\nth, td {\ntext-align: left;\nborder: 1px solid black;\npadding: 5px;\n}\ntr:nth-child(odd) {\nbackground-color: #ccc;\n}\ntr:nth-child(even) {\nbackground-color: #fff;\n}\nth {\ncolor: white;\nbackground-color: #444;\n}\n</style><meta http-equiv="refresh" content="10"></head><body><center><h2>Round %d Draw</h2><p style="vertical-align:top;">' % (nextRound,nextRound)
htmlString2 = '<table style="width:100%%;border:0;"><tr><td style="width:20%%;border:0;background-color:#111;text-align:right;vertical-align:top;"><img src="%s" width="%d"></td><td style="width:40%%;border:0;background-color:#111;vertical-align:top;"><center>' % (leftLogo,logoWidth)
htmlString3 = '</center></td><td style="width:20%%;border:0;background-color:#111;text-align:left;vertical-align:top;"><img src="%s" width="%d"></td></tr></table>' % (rightLogo,logoWidth)
htmlEndString = '</p></center></body></html>'
htmlFileObject = open("RefreshingRoundDrawLogo.html","w")
htmlFileObject.write(htmlStartString + htmlString2 + htmlTable + htmlString3 + htmlEndString)
htmlFileObject.close()

htmlFileObject = open("RefreshingRoundDrawNoLogo.html","w")
htmlFileObject.write(htmlStartString + htmlTable + htmlEndString)
htmlFileObject.close()
