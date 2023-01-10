# Import play song functions from each of them and sleep to wait
from stillAlive import playSongSA
from wantYouGone import playSongWYG
from time import sleep
from os import system, sys

# Get the song the user wants by asking them
while True:

    while True:
        songChoice = input('\"still alive\" or \"want you gone\"?: ')

        if songChoice.lower() == 'still alive' or songChoice.lower() == 'want you gone' or songChoice == '1' or songChoice == '2':
            break
        else:
            print('Invalid choice')

    if songChoice.lower() == 'still alive' or songChoice == '1':
        sleep(2)
        playSongSA()
    else:
        sleep(2)
        playSongWYG()

    while True:
        endProgram = input('End? (Y/N): ')
        if endProgram.upper() == 'Y' or endProgram.upper() == 'N':
            break
        else:
            print('Invalid choice')

    if endProgram.upper() == 'Y':
        print('Goodbye')
        sleep(1)
        sys.exit()
    else:
        print('Alright then,')