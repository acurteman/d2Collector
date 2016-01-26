# Manages to collection of API data
# Created 18 September 2015

# Libraries
# from requestSequence import requestSequence
# from manageSeqNum import readSeqNum, writeSeqNum, filterSeqNum
# from fileManager import fileWrite, fileRead, fileAppend
# from csvWriter import csvWrite, simpleCSVWrite
from dcFunctions import *
import json

# Get starting sequence number
startSeqNum = readSeqNum()
# print('Starting sequence number: ' + str(startSeqNum))

# Request initial data
apiKey = getKey()
print('Requesting data.')
tempData = requestSequence(startSeqNum, apiKey)
print('Request completed.')

# Convert json data
# print('Converting json data')
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
    print('Number of matches in result: ' + str(length))

    # Get last seq_num
    lastMatchSeqNum = dotaData.get('result').get('matches')[length - 1].get('match_seq_num')
    # print('Last sequence number: ' + str(lastMatchSeqNum))

    # Save most recent sequence number
    writeSeqNum(str(lastMatchSeqNum))
    # print('Last sequence number saved.')

    # Filter unwanted data out. Removes matches shorter than 15 mins and fewer than 10 players
    seqList = filterSeqNum(tempData)
    print('Number of valid matches: ' + str(len(seqList)))

    # Convert data to .csv
    fileName = getFileName()
    simpleCSVWrite(dotaData, seqList, fileName)
    print('Data written to csv file.')