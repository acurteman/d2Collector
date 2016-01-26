#   Libraries
import requests, json, csv
from datetime import datetime
#import json
#import csv

#----Functions relating to sequence number requests and managment----
################################################

#Requests a sequence of match data, and returns the results
def requestSequence(startNum, userKey):

    #API address and key
    key = '?key=' + userKey[:32]
    sequenceNum = '&start_at_match_seq_num=' + str(startNum)
    dotaAPI = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/'

    #Requests the data
    print(dotaAPI + key + sequenceNum)
    dotaRequest = requests.get(dotaAPI + key + sequenceNum)

    return dotaRequest.text

#Reads most recent seqNum
def readSeqNum():

    #Aquire file name
    fileName = '.startingSeqNum'

    #Open file in given mode, copy data, then close file
    openFile = open(fileName, 'r')
    fileContent = openFile.read()
    openFile.close()

    #Return file content
    return fileContent

#Overwrite the past seq num with more recent number
def writeSeqNum(number):

    fileName = '.startingSeqNum'

    fileWrite = open(fileName, 'w')
    fileWrite.write(number)
    fileWrite.close()

#Obtain seq nums for data with desired values
def filterSeqNum(tempData):

    #Convert json data
    dotaData = json.loads(tempData)

    seqList = []
    length = len(dotaData.get('result').get('matches'))

    #print('Starting loop.')
    for x in range(0,length):
        if dotaData.get('result').get('matches')[x].get('human_players') == 10:
            if dotaData.get('result').get('matches')[x].get('duration') > 900:
                #print('Valid Match')
                #seqList.append(dotaData.get('result').get('matches')[x].get('match_seq_num'))
                seqList.append(x)

    return seqList



#----Functions relating to file managment----
#############################

#Reads files and returns the content
def fileRead(fileName):

    #Aquire file name
    #fileName = input("File Name: ")

    #Open file in given mode, copy data, then close file
    openFile = open(fileName, 'r')
    fileContent = openFile.read()
    openFile.close()

    #Return file content
    return fileContent

#Takes data and appends it to a file
def fileAppend(fileName, data):

    #Aquire file name
    #print("Data will be appended to end of file.")
    #fileName = input("File Name: ")

    #Open file for appending, append, then close
    fileAppend = open(fileName, 'a')
    fileAppend.write(data)
    fileAppend.close()

    print("File appended.")

#Takes data and writes it to a file
def fileWrite(fileName, data):

    #Aquire file name
    #print("Warning! Will overwrite existing files.")
    #fileName = input("File Name: ")

    #Create/open file for writing, writes, then closes file
    fileWrite = open(fileName, 'w')
    fileWrite.write(data)
    fileWrite.close()
    
#Takes data and writes it to a file named temp
def fileWriteTemp(data):

    #Aquire file name
    print("Writing data to temp file.")
    fileName = 'temp' 

    #Create/open file for writing, writes, then closes file
    fileWrite = open(fileName, 'w')
    fileWrite.write(data)
    fileWrite.close()

#Takes data and appends it to a temp file
def fileAppendTemp(data):

    #Aquire file name
    print("Data will be appended to end of temp file.")
    fileName = 'temp'

    #Open file for appending, append, then close
    fileAppend = open(fileName, 'a')
    fileAppend.write(data)
    fileAppend.close()

    print("Temp file appended.")

#Takes input of dotaData and selected values and writes them to a .csv
def csvWrite(dotaData, selection):
    writeData = []

    #Creating Header
    header = ['matchSeqNum', 'radiantWin', 'duration', 'firstBloodTime', 'lobbyType', 'gameMode',
              'p1accountID','p1Slot', 'p1HeroID', 'p1Item0', 'p1Item1', 'p1Item2', 'p1Item3', 'p1Item4', 'p1Item5', 'p1Kills', 'p1Deaths', 'p1Assists', 'p1LeaverStatus', 'p1Gold', 'p1LastHits', 'p1Denies', 'p1GPM', 'p1XPM', 'p1GoldSpent', 'p1HeroDamage', 'p1TowerDamage', 'p1HeroHealing', 'p1Level',
              'p2accountID','p2Slot', 'p2HeroID', 'p2Item0', 'p2Item1', 'p2Item2', 'p2Item3', 'p2Item4', 'p2Item5', 'p2Kills', 'p2Deaths', 'p2Assists', 'p2LeaverStatus', 'p2Gold', 'p2LastHits', 'p2Denies', 'p2GPM', 'p2XPM', 'p2GoldSpent', 'p2HeroDamage', 'p2TowerDamage', 'p2HeroHealing', 'p2Level',
              'p3accountID','p3Slot', 'p3HeroID', 'p3Item0', 'p3Item1', 'p3Item2', 'p3Item3', 'p3Item4', 'p3Item5', 'p3Kills', 'p3Deaths', 'p3Assists', 'p3LeaverStatus', 'p3Gold', 'p3LastHits', 'p3Denies', 'p3GPM', 'p3XPM', 'p3GoldSpent', 'p3HeroDamage', 'p3TowerDamage', 'p3HeroHealing', 'p3Level',
              'p4accountID','p4Slot', 'p4HeroID', 'p4Item0', 'p4Item1', 'p4Item2', 'p4Item3', 'p4Item4', 'p4Item5', 'p4Kills', 'p4Deaths', 'p4Assists', 'p4LeaverStatus', 'p4Gold', 'p4LastHits', 'p4Denies', 'p4GPM', 'p4XPM', 'p4GoldSpent', 'p4HeroDamage', 'p4TowerDamage', 'p4HeroHealing', 'p4Level',
              'p5accountID','p5Slot', 'p5HeroID', 'p5Item0', 'p5Item1', 'p5Item2', 'p5Item3', 'p5Item4', 'p5Item5', 'p5Kills', 'p5Deaths', 'p5Assists', 'p5LeaverStatus', 'p5Gold', 'p5LastHits', 'p5Denies', 'p5GPM', 'p5XPM', 'p5GoldSpent', 'p5HeroDamage', 'p5TowerDamage', 'p5HeroHealing', 'p5Level',
              'p6accountID','p6Slot', 'p6HeroID', 'p6Item0', 'p6Item1', 'p6Item2', 'p6Item3', 'p6Item4', 'p6Item5', 'p6Kills', 'p6Deaths', 'p6Assists', 'p6LeaverStatus', 'p6Gold', 'p6LastHits', 'p6Denies', 'p6GPM', 'p6XPM', 'p6GoldSpent', 'p6HeroDamage', 'p6TowerDamage', 'p6HeroHealing', 'p6Level',
              'p7accountID','p7Slot', 'p7HeroID', 'p7Item0', 'p7Item1', 'p7Item2', 'p7Item3', 'p7Item4', 'p7Item5', 'p7Kills', 'p7Deaths', 'p7Assists', 'p7LeaverStatus', 'p7Gold', 'p7LastHits', 'p7Denies', 'p7GPM', 'p7XPM', 'p7GoldSpent', 'p7HeroDamage', 'p7TowerDamage', 'p7HeroHealing', 'p7Level',
              'p8accountID','p8Slot', 'p8HeroID', 'p8Item0', 'p8Item1', 'p8Item2', 'p8Item3', 'p8Item4', 'p8Item5', 'p8Kills', 'p8Deaths', 'p8Assists', 'p8LeaverStatus', 'p8Gold', 'p8LastHits', 'p8Denies', 'p8GPM', 'p8XPM', 'p8GoldSpent', 'p8HeroDamage', 'p8TowerDamage', 'p8HeroHealing', 'p8Level',
              'p9accountID','p9Slot', 'p9HeroID', 'p9Item0', 'p9Item1', 'p9Item2', 'p9Item3', 'p9Item4', 'p9Item5', 'p9Kills', 'p9Deaths', 'p9Assists', 'p9LeaverStatus', 'p9Gold', 'p9LastHits', 'p9Denies', 'p9GPM', 'p9XPM', 'p9GoldSpent', 'p9HeroDamage', 'p9TowerDamage', 'p9HeroHealing', 'p9Level',
              'p10accountID','p10Slot', 'p10HeroID', 'p10Item0', 'p10Item1', 'p10Item2', 'p10Item3', 'p10Item4', 'p10Item5', 'p10Kills', 'p10Deaths', 'p10Assists', 'p10LeaverStatus', 'p10Gold', 'p10LastHits', 'p10Denies', 'p10GPM', 'p10XPM', 'p10GoldSpent', 'p10HeroDamage', 'p10TowerDamage', 'p10HeroHealing', 'p1L0evel']


    for x in range(0, len(selection)):
        #Create a string with relevant match information
        matchData = [str(dotaData.get('result').get('matches')[selection[x]].get('match_seq_num')),
                          dotaData.get('result').get('matches')[selection[x]].get('radiant_win'),
                          str(dotaData.get('result').get('matches')[selection[x]].get('duration')),
                          dotaData.get('result').get('matches')[selection[x]].get('first_blood_time'),
                          str(dotaData.get('result').get('matches')[selection[x]].get('lobby_type')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('game_mode'))]

        #Create a string with all relevant player information
        for y in range(0,10):
            playerData = [str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('account_id')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('player_slot')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('hero_id')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('item_0')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('item_1')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('item_2')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('item_3')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('item_4')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('item_5')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('kills')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('deaths')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('assists')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('leaver_status')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('gold')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('last_hits')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('denies')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('gold_per_min')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('xp_per_min')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('gold_spent')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('hero_damage')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('tower_damage')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('hero_healing')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('level'))]

            #Append player data to match data
            matchData += playerData

        #Append match data to writeData
        writeData.append(matchData)

    #Testing    
    #print(writeData)

    #Writing to CSV file
    b = open('test.csv', 'w')
    a = csv.writer(b)
    a.writerow(header)
    a.writerows(writeData)
    b.close()
import csv

#Takes input of dotaData and selected values and writes them to a .csv
def simpleCSVWrite(dotaData, selection, fileName):
    writeData = []

    #Creating Header
    header = ['matchSeqNum', 'radiantWin', 'duration', 'lobbyType', 'gameMode',
              'p1HeroID', 'p1LeaverStatus',
              'p2HeroID', 'p2LeaverStatus',
              'p3HeroID', 'p3LeaverStatus',
              'p4HeroID', 'p4LeaverStatus',
              'p5HeroID', 'p5LeaverStatus',
              'p6HeroID', 'p6LeaverStatus',
              'p7HeroID', 'p7LeaverStatus',
              'p8HeroID', 'p8LeaverStatus',
              'p9HeroID', 'p9LeaverStatus',
              'p10HeroID', 'p10LeaverStatus']


    for x in range(0, len(selection)):
        #Create a string with relevant match information
        matchData = [str(dotaData.get('result').get('matches')[selection[x]].get('match_seq_num')),
                          dotaData.get('result').get('matches')[selection[x]].get('radiant_win'),
                          str(dotaData.get('result').get('matches')[selection[x]].get('duration')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('lobby_type')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('game_mode'))]

        #Create a string with all relevant player information
        for y in range(0,10):
            playerData = [str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('hero_id')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('leaver_status'))]

            #Append player data to match data
            matchData += playerData

        #Append match data to writeData
        writeData.append(matchData)

    #Testing    
    #print(writeData)

    #Writing to CSV file
    b = open((fileName + '.csv'), 'w')
    a = csv.writer(b)
    a.writerow(header)
    a.writerows(writeData)
    b.close()

#Generates a filename using the current date and time
def getFileName():
    currTime = datetime.now()
    fileName = str(currTime.date()) + str(currTime.time())
    fileName = 'd2c' + fileName[:-7]

    return fileName
    
#Reads most recent seqNum
def getKey():

    #Aquire file name
    fileName = '.apiKey'

    #Open file in given mode, copy data, then close file
    openFile = open(fileName, 'r')
    fileContent = openFile.read()
    openFile.close()

    #Return file content
    
    return fileContent
