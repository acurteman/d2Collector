#   Libraries
import requests, json, csv, time
from datetime import datetime


# import json
# import csv

# ----Functions relating to sequence number requests and managment----
################################################

# Requests a sequence of match data, and returns the results
def requestSequence(startNum, userKey):
    # API address and key
    key = '?key=' + userKey[:32]
    sequenceNum = '&start_at_match_seq_num=' + str(startNum)
    dotaAPI = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/'

    # Requests the data
    # print(dotaAPI + key + sequenceNum)
    dotaRequest = requests.get(dotaAPI + key + sequenceNum)

    return dotaRequest.text

# Request the most recent single match
def requestRecent(userKey):
    # API address and key
    key = '?key=' + userKey[:32]
    dotaAPI = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/'

    # Requests the data
    # print(dotaAPI + key + sequenceNum)
    dotaRequest = requests.get(dotaAPI + key)

    return dotaRequest.text

# Request dota data sequence
def reqSeqNow(userKey):

    # API address and key
    key = '?key=' + userKey[:32]
    dotaAPI = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/'

    # Requests the data
    # print(dotaAPI + key + sequenceNum)
    dotaRequest = requests.get(dotaAPI + key)

    return dotaRequest.text

# Reads most recent seqNum
def readSeqNum():
    # Aquire file name
    fileName = '.startingSeqNum'

    # Open file in given mode, copy data, then close file
    openFile = open(fileName, 'r')
    fileContent = openFile.read()
    openFile.close()

    # Return file content
    return fileContent


# Overwrite the past seq num with more recent number
def writeSeqNum(number):
    fileName = '.startingSeqNum'

    fileWrite = open(fileName, 'w')
    fileWrite.write(number)
    fileWrite.close()


# Obtain seq nums for data with desired values
def filterSeqNum(tempData):
    # Convert json data
    dotaData = json.loads(tempData)

    seqList = []
    length = len(dotaData.get('result').get('matches'))

    # print('Starting loop.')
    for x in range(0, length):
        if dotaData.get('result').get('matches')[x].get('human_players') == 10:
            if dotaData.get('result').get('matches')[x].get('duration') > 900:
                # print('Valid Match')
                # seqList.append(dotaData.get('result').get('matches')[x].get('match_seq_num'))
                seqList.append(x)

    return seqList


# ----Functions relating to file managment----
#############################

# Reads files and returns the content
def fileRead(fileName):
    # Aquire file name
    # fileName = input("File Name: ")

    # Open file in given mode, copy data, then close file
    openFile = open(fileName, 'r')
    fileContent = openFile.read()
    openFile.close()

    # Return file content
    return fileContent


# Takes data and appends it to a file
def fileAppend(fileName, data):
    # Aquire file name
    # print("Data will be appended to end of file.")
    # fileName = input("File Name: ")

    # Open file for appending, append, then close
    fileAppend = open(fileName, 'a')
    fileAppend.write(data)
    fileAppend.close()

    #print("File appended.")


# Takes data and writes it to a file
def fileWrite(fileName, data):
    # Aquire file name
    # print("Warning! Will overwrite existing files.")
    # fileName = input("File Name: ")

    # Create/open file for writing, writes, then closes file
    fileWrite = open(fileName, 'w')
    fileWrite.write(data)
    fileWrite.close()


# Takes data and writes it to a file named temp
def fileWriteTemp(data):
    # Aquire file name
    print("Writing data to temp file.")
    fileName = 'temp'

    # Create/open file for writing, writes, then closes file
    fileWrite = open(fileName, 'w')
    fileWrite.write(data)
    fileWrite.close()


# Takes data and appends it to a temp file
def fileAppendTemp(data):
    # Aquire file name
    print("Data will be appended to end of temp file.")
    fileName = 'temp'

    # Open file for appending, append, then close
    fileAppend = open(fileName, 'a')
    fileAppend.write(data)
    fileAppend.close()

    print("Temp file appended.")


# Takes input of dotaData and selected values and writes them to a .csv
def csvWrite(dotaData, selection):
    writeData = []

    # Creating Header
    header = ['matchSeqNum', 'radiantWin', 'duration', 'firstBloodTime', 'lobbyType', 'gameMode',
              'p1accountID', 'p1Slot', 'p1HeroID', 'p1Item0', 'p1Item1', 'p1Item2', 'p1Item3', 'p1Item4', 'p1Item5',
              'p1Kills', 'p1Deaths', 'p1Assists', 'p1LeaverStatus', 'p1Gold', 'p1LastHits', 'p1Denies', 'p1GPM',
              'p1XPM', 'p1GoldSpent', 'p1HeroDamage', 'p1TowerDamage', 'p1HeroHealing', 'p1Level',
              'p2accountID', 'p2Slot', 'p2HeroID', 'p2Item0', 'p2Item1', 'p2Item2', 'p2Item3', 'p2Item4', 'p2Item5',
              'p2Kills', 'p2Deaths', 'p2Assists', 'p2LeaverStatus', 'p2Gold', 'p2LastHits', 'p2Denies', 'p2GPM',
              'p2XPM', 'p2GoldSpent', 'p2HeroDamage', 'p2TowerDamage', 'p2HeroHealing', 'p2Level',
              'p3accountID', 'p3Slot', 'p3HeroID', 'p3Item0', 'p3Item1', 'p3Item2', 'p3Item3', 'p3Item4', 'p3Item5',
              'p3Kills', 'p3Deaths', 'p3Assists', 'p3LeaverStatus', 'p3Gold', 'p3LastHits', 'p3Denies', 'p3GPM',
              'p3XPM', 'p3GoldSpent', 'p3HeroDamage', 'p3TowerDamage', 'p3HeroHealing', 'p3Level',
              'p4accountID', 'p4Slot', 'p4HeroID', 'p4Item0', 'p4Item1', 'p4Item2', 'p4Item3', 'p4Item4', 'p4Item5',
              'p4Kills', 'p4Deaths', 'p4Assists', 'p4LeaverStatus', 'p4Gold', 'p4LastHits', 'p4Denies', 'p4GPM',
              'p4XPM', 'p4GoldSpent', 'p4HeroDamage', 'p4TowerDamage', 'p4HeroHealing', 'p4Level',
              'p5accountID', 'p5Slot', 'p5HeroID', 'p5Item0', 'p5Item1', 'p5Item2', 'p5Item3', 'p5Item4', 'p5Item5',
              'p5Kills', 'p5Deaths', 'p5Assists', 'p5LeaverStatus', 'p5Gold', 'p5LastHits', 'p5Denies', 'p5GPM',
              'p5XPM', 'p5GoldSpent', 'p5HeroDamage', 'p5TowerDamage', 'p5HeroHealing', 'p5Level',
              'p6accountID', 'p6Slot', 'p6HeroID', 'p6Item0', 'p6Item1', 'p6Item2', 'p6Item3', 'p6Item4', 'p6Item5',
              'p6Kills', 'p6Deaths', 'p6Assists', 'p6LeaverStatus', 'p6Gold', 'p6LastHits', 'p6Denies', 'p6GPM',
              'p6XPM', 'p6GoldSpent', 'p6HeroDamage', 'p6TowerDamage', 'p6HeroHealing', 'p6Level',
              'p7accountID', 'p7Slot', 'p7HeroID', 'p7Item0', 'p7Item1', 'p7Item2', 'p7Item3', 'p7Item4', 'p7Item5',
              'p7Kills', 'p7Deaths', 'p7Assists', 'p7LeaverStatus', 'p7Gold', 'p7LastHits', 'p7Denies', 'p7GPM',
              'p7XPM', 'p7GoldSpent', 'p7HeroDamage', 'p7TowerDamage', 'p7HeroHealing', 'p7Level',
              'p8accountID', 'p8Slot', 'p8HeroID', 'p8Item0', 'p8Item1', 'p8Item2', 'p8Item3', 'p8Item4', 'p8Item5',
              'p8Kills', 'p8Deaths', 'p8Assists', 'p8LeaverStatus', 'p8Gold', 'p8LastHits', 'p8Denies', 'p8GPM',
              'p8XPM', 'p8GoldSpent', 'p8HeroDamage', 'p8TowerDamage', 'p8HeroHealing', 'p8Level',
              'p9accountID', 'p9Slot', 'p9HeroID', 'p9Item0', 'p9Item1', 'p9Item2', 'p9Item3', 'p9Item4', 'p9Item5',
              'p9Kills', 'p9Deaths', 'p9Assists', 'p9LeaverStatus', 'p9Gold', 'p9LastHits', 'p9Denies', 'p9GPM',
              'p9XPM', 'p9GoldSpent', 'p9HeroDamage', 'p9TowerDamage', 'p9HeroHealing', 'p9Level',
              'p10accountID', 'p10Slot', 'p10HeroID', 'p10Item0', 'p10Item1', 'p10Item2', 'p10Item3', 'p10Item4',
              'p10Item5', 'p10Kills', 'p10Deaths', 'p10Assists', 'p10LeaverStatus', 'p10Gold', 'p10LastHits',
              'p10Denies', 'p10GPM', 'p10XPM', 'p10GoldSpent', 'p10HeroDamage', 'p10TowerDamage', 'p10HeroHealing',
              'p1L0evel']

    for x in range(0, len(selection)):
        # Create a string with relevant match information
        matchData = [str(dotaData.get('result').get('matches')[selection[x]].get('match_seq_num')),
                     dotaData.get('result').get('matches')[selection[x]].get('radiant_win'),
                     str(dotaData.get('result').get('matches')[selection[x]].get('duration')),
                     dotaData.get('result').get('matches')[selection[x]].get('first_blood_time'),
                     str(dotaData.get('result').get('matches')[selection[x]].get('lobby_type')),
                     str(dotaData.get('result').get('matches')[selection[x]].get('game_mode'))]

        # Create a string with all relevant player information
        for y in range(0, 10):
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
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get(
                                  'leaver_status')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('gold')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('last_hits')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('denies')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get(
                                  'gold_per_min')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('xp_per_min')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('gold_spent')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('hero_damage')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get(
                                  'tower_damage')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get(
                                  'hero_healing')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('level'))]

            # Append player data to match data
            matchData += playerData

        # Append match data to writeData
        writeData.append(matchData)

    # Testing
    # print(writeData)

    # Writing to CSV file
    b = open('test.csv', 'w')
    a = csv.writer(b)
    a.writerow(header)
    a.writerows(writeData)
    b.close()


#import csv


# Takes input of dotaData and selected values and writes them to a .csv
def simpleCSVWrite(dotaData, selection, fileName):
    writeData = []

    # Creating Header
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
        # Create a string with relevant match information
        matchData = [str(dotaData.get('result').get('matches')[selection[x]].get('match_seq_num')),
                     dotaData.get('result').get('matches')[selection[x]].get('radiant_win'),
                     str(dotaData.get('result').get('matches')[selection[x]].get('duration')),
                     str(dotaData.get('result').get('matches')[selection[x]].get('lobby_type')),
                     str(dotaData.get('result').get('matches')[selection[x]].get('game_mode'))]

        # Create a string with all relevant player information
        for y in range(0, 10):
            playerData = [str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('hero_id')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get(
                                  'leaver_status'))]

            # Append player data to match data
            matchData += playerData

        # Append match data to writeData
        writeData.append(matchData)

    # Testing
    # print(writeData)

    # Writing to CSV file
    b = open((fileName + '.csv'), 'w')
    a = csv.writer(b)
    a.writerow(header)
    a.writerows(writeData)
    b.close()


# Takes input of dotaData and selected values and writes them to a .csv
def simpleCSVAppend(dotaData, selection, fileName):
    writeData = []

    for x in range(0, len(selection)):
        # Create a string with relevant match information
        matchData = [str(dotaData.get('result').get('matches')[selection[x]].get('match_seq_num')),
                     dotaData.get('result').get('matches')[selection[x]].get('radiant_win'),
                     str(dotaData.get('result').get('matches')[selection[x]].get('duration')),
                     str(dotaData.get('result').get('matches')[selection[x]].get('lobby_type')),
                     str(dotaData.get('result').get('matches')[selection[x]].get('game_mode'))]

        # Create a string with all relevant player information
        for y in range(0, 10):
            playerData = [str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get('hero_id')),
                          str(dotaData.get('result').get('matches')[selection[x]].get('players')[y].get(
                                  'leaver_status'))]

            # Append player data to match data
            matchData += playerData

        # Append match data to writeData
        writeData.append(matchData)

    # Testing
    # print(writeData)

    # Writing to CSV file
    b = open((fileName + '.csv'), 'a')
    a = csv.writer(b)
    a.writerows(writeData)
    b.close()


# Generates a filename using the current date and time
def getFileName():
    currTime = datetime.now()
    fileName = str(currTime.date()) + '_' + str(currTime.time())
    fileName = 'd2c_' + fileName[:-7]

    return fileName


# Reads most recent seqNum
def getKey():
    # Aquire file name
    fileName = '.apiKey'

    # Open file in given mode, copy data, then close file
    openFile = open(fileName, 'r')
    fileContent = openFile.read()
    openFile.close()

    # Return file content

    return fileContent

# Creates and manages the needed initiation files
def manageInit():
    # Print menu options

    print('Create/Overwrite files needed to run dotaCollector.py')
    print('The apiKey file will contain your unique api key from Valve.')
    print('The startSeqNum file will contain the sequence number of the first match request.')
    print('')

    validSelection = False
    while validSelection == False:

        print('1: Create/Overwrite both apiKey and startSeqNum files.')
        print('2: Create/Overwrite apiKey file.')
        print('3: Create/Overwrite startSeqNum file.')
        print('4: Return.')

        # Process menu options
        try:
            selection = int(input('Enter selection number (1-4): '))

        except:
            print('Please enter a number between 1 and 4.')

        if selection > 0 and selection < 5:
            validSelection = True

        else:
            print('Please enter a number between 1 and 4.')

    # Create/Overwrite needed files

    if selection == 1 or selection == 2:

        # Create/Overwrite apiKey file with user input
        fileName = '.apiKey'
        seqNum = input('Enter api key: ')

        fileWrite = open(fileName, 'w')
        fileWrite.write(seqNum)
        fileWrite.close()


    if selection ==1 or selection == 3:

        # Create/Overwrite startSeqNum
        fileName = '.startingSeqNum'
        seqNum = input('Enter starting sequence number: ')

        fileWrite = open(fileName, 'w')
        fileWrite.write(seqNum)
        fileWrite.close()


# Dota collector script for bulk collection

def bulkCollect(collCount):

    fileName = getFileName()

    for x in range(0, collCount):
        print('Request {0}/{1}'.format(x+1,collCount))
        # Get starting sequence number
        startSeqNum = readSeqNum()
        print('Starting sequence number: ' + str(startSeqNum))

        # Request initial data
        apiKey = getKey()
        #print('Requesting data.')
        tempData = requestSequence(startSeqNum, apiKey)
        #print('Request completed.')

        # Convert json data
        # print('Converting json data')
        try:
            dotaData = json.loads(tempData)

            # Check the status of the request
            status = dotaData.get('result').get('status')

            # Check if request was succesful
            if status != 1:
                print('Error with data request.')

            # If succesful, continue
            else:

                # Get length of results
                length = len(dotaData.get('result').get('matches'))
                #print('Number of matches in result: ' + str(length))

                # Get last seq_num
                lastMatchSeqNum = dotaData.get('result').get('matches')[length - 1].get('match_seq_num')
                # print('Last sequence number: ' + str(lastMatchSeqNum))

                # Save most recent sequence number
                writeSeqNum(str(lastMatchSeqNum))
                # print('Last sequence number saved.')

                # Filter unwanted data out. Removes matches shorter than 15 mins and fewer than 10 players
                seqList = filterSeqNum(tempData)
                #print('Number of valid matches: ' + str(len(seqList)))

                # Write data to .csv
                # If first time through loop, write header
                if x == 0:
                    simpleCSVWrite(dotaData, seqList, fileName)

                # Else just append data
                else:
                    simpleCSVAppend(dotaData, seqList, fileName)

                print('Data written to csv file.')

                time.sleep(3)

        except:
            print('Error with request, trying again.')
            time.sleep(3)


# Dota collector script for continuous collection
def contCollect():

    fileName = getFileName()
    logName = 'log_' + fileName
    apiKey = getKey()
    contCount = 0
    totalMatches = 0

    # Create log file
    fileWrite(logName, 'Request started on {0}'.format(str(datetime.now())))

    # Get most recent sequence numnber
    startSeqNum = getRecSeqNum()
    fileAppend(logName, 'Starting sequence number: {0}'.format(startSeqNum))
    print('Waiting 1 minute for matches...')
    time.sleep(60)

    # Loop for 24 hours
    while contCount < 288:
        print('Request {0}'.format(contCount+1))

        # Request initial data
        tempData = requestSequence(startSeqNum, apiKey)

        # Convert json data, then write to .csv
        try:
            dotaData = json.loads(tempData)

            # Check the status of the request
            status = dotaData.get('result').get('status')

            # Check if request was succesful
            if status != 1:
                print('Error with data request.')
                fileAppend(logName, '\nError with request at {0}'.format(str(datetime.now().time())))
                time.sleep(3)

            # If succesful, continue
            else:

                # Get length of results
                length = len(dotaData.get('result').get('matches'))
                #print('Number of matches in result: ' + str(length))

                # Filter unwanted data out. Removes matches shorter than 15 mins and fewer than 10 players
                seqList = filterSeqNum(tempData)
                totalMatches += len(seqList)
                #print('Number of valid matches: ' + str(len(seqList)))

                # Write data to .csv
                # If first time through loop, write header
                if contCount == 0:
                    simpleCSVWrite(dotaData, seqList, fileName)
                    contCount += 1

                # Else just append data
                else:
                    simpleCSVAppend(dotaData, seqList, fileName)
                    contCount += 1

                print('Data for request {0} written to csv file at {1}.'.format(contCount, str(datetime.now().time())))
                fileAppend(logName, '\nData for request {0} written to .csv file. Number of valid matching this request: {1}. New total: {2}'.format(contCount+1, len(seqList), totalMatches))

                # Get most recent sequence numnber
                startSeqNum = getRecSeqNum()
                fileAppend(logName, 'Next starting sequence number: {0}'.format(startSeqNum))

                time.sleep(300)

        except:
            print('Error with request, trying again.')
            fileAppend(logName, '\nError with request at {0}'.format(str(datetime.now().time())))
            time.sleep(3)

# Get most recent match sequence number:
def getRecSeqNum():

    apiKey = getKey()
    success = False
    failCount = 0

    while success == False and failCount < 10:

        # Request most recent match
        tempData = requestRecent(apiKey)

        try:
            dotaData = json.loads(tempData)

            # Check the status of the request
            status = dotaData.get('result').get('status')

            # Check if request was succesful
            if status != 1:
                print('Error with most recent match request.')
                failCount += 1
                time.sleep(2)

            else:
                # Get length of results
                length = len(dotaData.get('result').get('matches'))

                # Get last seq_num
                lastMatchSeqNum = dotaData.get('result').get('matches')[length - 1].get('match_seq_num')

                success = True

        except:
            print('Error with most recent match request.')
            failCount += 1
            time.sleep(2)

    return lastMatchSeqNum

# This function requests hero data from JankDota, and creates a .csv file with the returned data
def getHeroData():

    # Request data from JankDota
    api = 'http://api.herostats.io/heroes/all'
    heroRequest = requests.get(api)

    # Convert json data
    heroData = json.loads(heroRequest.text)

    # Create filename for .csv
    currTime = datetime.now()
    fileName = 'heroData_' + str(currTime.date())

    # Create header for .csv file
    header = ['ID', 'Name', 'Movespeed', 'MaxDmg', 'MinDmg', 'HP', 'HPRegen', 'Mana', 'ManaRegen',
              'Armor', 'Range', 'BaseStr', 'BaseAgi', 'BaseInt', 'StrGain', 'AgiGain', 'IntGain', 'PrimaryStat',
              'BaseAttackTime']

    heroList = []

    for x in range(1,(len(heroData)+1)):
        heroLine = [heroData[str(x)]['ID'], heroData[str(x)]['Name'], heroData[str(x)]['Movespeed'],
                    heroData[str(x)]['MaxDmg'], heroData[str(x)]['MinDmg'], heroData[str(x)]['HP'],
                    heroData[str(x)]['HPRegen'], heroData[str(x)]['Mana'], heroData[str(x)]['ManaRegen'],
                    heroData[str(x)]['Armor'], heroData[str(x)]['Range'], heroData[str(x)]['BaseStr'],
                    heroData[str(x)]['BaseAgi'], heroData[str(x)]['BaseInt'], heroData[str(x)]['StrGain'],
                    heroData[str(x)]['AgiGain'], heroData[str(x)]['IntGain'], heroData[str(x)]['PrimaryStat'],
                    heroData[str(x)]['BaseAttackTime']]

        heroList.append(heroLine)

    # Writing to CSV file
    b = open((fileName + '.csv'), 'w')
    a = csv.writer(b)
    a.writerow(header)
    a.writerows(heroList)
    b.close()

    print('Data written to file: {0}'.format(fileName + '.csv'))
