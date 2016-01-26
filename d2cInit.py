# Script to create files needed to run dotaCollector.py

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
    print('4: Exit.')

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