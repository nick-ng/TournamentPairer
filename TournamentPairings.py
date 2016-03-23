from tabulate import tabulate
import random
import time
import math
import collections

TournamentDate = 20160312 # Enter first day of the tournament date as yyyymmdd
seedAdjustment = 0 # Emergency use. Usually doesn't need changing
YourLogo = "YourLogo.jpg"
leftLogo = YourLogo
rightLogo = YourLogo

fullRandom = False

print(1*"\n")
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

# 0            1                2        3            4    
# Player,    Still Playing,    Wins,    Opponent 1,    Opponent 2, etc. (Old version)
# Player,    Club,            Wins,    Opponent 1,    Opponent 2, etc.
pairingDataFilename = "PairingData.txt"
#pairingDataFile = open(pairingDataFilename)
#pairingDataRaw = pairingDataFile.read()
#pairingDataSplit = pairingDataRaw.split("\t")

# Read previous round draws from .txt file
with open(pairingDataFilename,'r') as f:
    pairingDataWithHeaders = f.read().splitlines()
    for n in range(len(pairingDataWithHeaders)):
        pairingDataWithHeaders[n] = pairingDataWithHeaders[n].split('\t')

# Set up win bracket
#playersPerWinBracket = []
#for n in range(nextRound):
#    playersPerWinBracket.append(0)

#pairingData = [pairingDataWithHeaders[0]]
pairingData = []
listOfClubs = []
for n in range(1,len(pairingDataWithHeaders)):
#    random.seed(pairingSeed)
    #randomWin =  random.random() / 10
    #print randomWin
    #pairingDataWithHeaders[n][1] = int(pairingDataWithHeaders[n][1]) # Club. Used to be "Still Playing"
    temp = getClub(pairingDataWithHeaders[n][1]) # Get club
    stillPlaying = temp[0] # Check if still playing
    pairingDataWithHeaders[n][1] = temp[1] # Re-assign club
    listOfClubs.append(temp[1]) # Add club to listOfClubs
    numberOfWins = int(pairingDataWithHeaders[n][2]) # Legacy. I used to care about the number of wins.
    pairingDataWithHeaders[n][2] = numberOfWins # Wins
    
    if stillPlaying: # Include only players who haven't dropped (still playing != 0)
        pairingData.append(pairingDataWithHeaders[n])
        #playersPerWinBracket[numberOfWins] = playersPerWinBracket[numberOfWins] + 1

pairingData = sorted(pairingData, key=getWins, reverse=1) # Sort from most to fewest wins

nextRound = 0
#print(pairingData)
# Remove #N/A
for n in range(len(pairingData)):
    hasNA = True
    #print(pairingData[n])
    while hasNA:
        try:
            pairingData[n].remove('#N/A')
        except ValueError:
            hasNA = False
    nextRound = max([nextRound,len(pairingData[n])])
    
# Set up seed so pairings are consistent
nextRound = nextRound - 2
#pairingSeed = TournamentDate * (1+nextRound) + seedAdjustment
#random.seed(pairingSeed)

numberOfPlayers = len(pairingData)
print("Number of Players: %d" % numberOfPlayers)
print("Next Round: %d" % nextRound)
clubCollection = collections.Counter(listOfClubs)
temp = clubCollection.most_common(1) # Get most common club.
print(temp[0][0]+" is the most common club (%d members)" % temp[0][1])
mostClub = temp[0][1]
# Figure out how many rounds there are.
#maxRounds = math.ceil(math.log(numberOfPlayers,2))
clubRounds = math.floor(numberOfPlayers / mostClub) # Number of rounds to avoid club pairings. math.floor just in case.
forbidSameClub = 1
# if nextRound < clubRounds:
    # forbidSameClub = 1
# else:
    # forbidSameClub = 0
# print("Avoiding same club pairings for %d rounds" % clubRounds)

#print playersPerWinBracket
clubDrawTime = 2. # How long to attempt pairings while avoiding the same club.
anyDrawTime = clubDrawTime + 5. # How long after that while allowing the same club.
fullRandomTime = anyDrawTime + clubDrawTime # How long to draw without respect to wins but with respect to clubs.
maxDrawTime = fullRandom + anyDrawTime # Attempt to pair players for that many seconds
undrawn = 1
draws = 0
a = tic()
lenPairingData0 = len(pairingData[0])
addedAGhost = 0
# Add a bye if there are an odd number of players
if not isEven(numberOfPlayers):
    byeList = ["-Bye-",1,-1]
    for n in range(3,lenPairingData0):
        byeList.append("No one would have a name this long")
    pairingData.append(byeList)

pairHeaders = ["Table","Player 1","Player A"]
print("Making round pairings")
while undrawn:
    b = toc(a)
    draws = draws + 1
    # Add random amount to each player's wins so they get drawn randomly within their win bracket
    pairs = []
    for n in range(len(pairingData)):
        if fullRandom:
            randomWin = random.random() * 10.
        else:
            randomWin = random.random() / 10.
        pairingData[n][2] = math.floor(pairingData[n][2]) + randomWin
    pairingDataB = sorted(pairingData, key=getWins, reverse=0) # Sort list from fewest to most wins.
    redraw = 0
    #print("Attempt %d, (random %0.5f, %0.1f seconds elapsed)" % (draws,randomWin,b))
    while len(pairingDataB) > 1: # Iterate through the list backwards
        p1 = len(pairingDataB) - 1
        p2 = p1 - 1
        #print "p1 = %d, p2 = %d" % (p1,p2)
        playedBefore = 0
        # Compare player 1's club with player 2's club
        if forbidSameClub and (pairingDataB[p1][1] == pairingDataB[p2][1]):
            redraw = 1
        # Compare player 2 with player 1's previous opponents
        for n in range(3,lenPairingData0):
            if pairingDataB[p2][0] == pairingDataB[p1][n]:
                redraw = 1
            if pairingDataB[p1][0] == pairingDataB[p2][n]:
                redraw = 1
        if redraw:
            break
        else:
            # Assign that pair a random table number
            pairs.append([random.random(),pairingDataB[p1][0],pairingDataB[p2][0]])
            pairingDataB.pop(p1)
            pairingDataB.pop(p2)
            #print(tabulate(pairs, headers=pairHeaders, tablefmt="simple")+"\n")
    if redraw:
        if (b > clubDrawTime) & forbidSameClub:
            forbidSameClub = 0
            print("Allowing same club pairings.")
        if (b > anyDrawTime) & (not fullRandom):
            fullRandom = True
            forbidSameClub = 1
            print("Couldn't pair players within win brackets. Ignoring win brackets.")
        if (b > fullRandomTime) & forbidSameClub:
            fullRandom = True
            forbidSameClub = 0
            print("Allowing same club pairings.")
        if b > maxDrawTime:
            break
    else:
        undrawn = 0
        print("Had to draw %d times" % draws)

pairs = sorted(pairs, key=getTables, reverse=0)

# Change table numbers to integers and write text file for spreadsheet administration.
adminFileObject = open("aaRound "+str(nextRound)+" Draw.txt","w")
adminString = ""
for n in range(len(pairs)):
    pairs[n][0] = n+1
    adminString = adminString+pairs[n][1]+"\t"+pairs[n][2]+"\n"   #"\r\n"
adminFileObject.write(adminString)
#print(pairs)
printingString = tabulate(pairs, headers=pairHeaders, tablefmt="simple")
#print("Debug stuff above")
if undrawn:
    print("Couldn't pair players after %d attempts." % draws)
else:
    print(1*"\n")
    if not forbidSameClub:
        print("Allowed same club pairings\n")
    if fullRandom:
        print("Ignored wins when pairing. Probably due to too many rounds being played")
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

htmlStartString = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"><html><head><title>Round %d Draw</title><style type="text/css">\nbody {\n    font-family: Georgia, "Times New Roman", Times, serif;\nbackground-color: #111;\n}\nh2 {\ncolor: #fff;}\nh3 {\ncolor: #fff;}\ntable {\nborder: 1px solid black;\nborder-collapse: collapse;\nfloat: center\n}\nth, td {\ntext-align: left;\nborder: 1px solid black;\npadding: 5px;\n}\ntr:nth-child(odd) {\nbackground-color: #ccc;\n}\ntr:nth-child(even) {\nbackground-color: #fff;\n}\nth {\ncolor: white;\nbackground-color: #444;\n}\n</style><meta http-equiv="refresh" content="10"></head><body><center><h2>Round %d Draw</h2><p style="vertical-align:top;">' % (nextRound,nextRound)
htmlString2 = '<table style="width:100%%;border:0;"><tr><td style="width:20%%;border:0;background-color:#111;text-align:right;vertical-align:top;"><img src="%s" width="%d"></td><td style="width:40%%;border:0;background-color:#111;vertical-align:top;"><center>' % (leftLogo,logoWidth)
htmlString3 = '</center></td><td style="width:20%%;border:0;background-color:#111;text-align:left;vertical-align:top;"><img src="%s" width="%d"></td></tr></table>' % (rightLogo,logoWidth)
htmlEndString = '</p></center></body></html>'
htmlFileObject = open("RefreshingRoundDrawLogo.html","w")
htmlFileObject.write(htmlStartString + htmlString2 + htmlTable + htmlString3 + htmlEndString)
htmlFileObject.close()

htmlFileObject = open("RefreshingRoundDrawNoLogo.html","w")
htmlFileObject.write(htmlStartString + htmlTable + htmlEndString)
htmlFileObject.close()
