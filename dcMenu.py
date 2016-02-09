from dcFunctions import *

validSelection = False
selection = 0

while validSelection == False or selection != 5:
    print('--- Dota2 Collector ---')
    print('1: Create or update api key or sequence number files.')
    print('2: Bulk data collection.')
    print('3: Continuous data collection.')
    print('4: Create or update hero data sheet from JankDota')
    print('5: Exit.')

    try:
        selection = int(input('Enter selection number (1-5): '))

    except:
        print('Please enter a number between 1 and 5.')

    if selection > 0 and selection < 5:
        validSelection = True

    else:
        print('Please enter a number between 1 and 5')

    if selection == 1:
        manageInit()

    elif selection == 2:
        requestCount = int(input('How many data requests?'))
        bulkCollect(requestCount)

    elif selection == 3:
        contCollect()

    elif selection == 4:
          getHeroData()

    else:
          print('Good bye')
