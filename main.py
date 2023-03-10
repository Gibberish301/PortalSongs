# Import play song functions from each of them and sleep to wait
from stillAlive import playSongSA
from wantYouGone import playSongWYG
from time import sleep
from os import system, sys

# Intro sequence
system('cls')
print('Startup Initialized')

for _ in range(10):
    print('.', end = '', flush = True)
    sleep(0.5)

sleep(0.5)
system('cls')

print('Welcome to the Apeture Science Special Audio Recordings Archive')
sleep(3)
print('There are currently only:')
sleep(1)
print('2')
sleep(0.5)
print('Special Audios in our library. Please choose between:')
sleep(3)

# Get the song the user wants by asking them
while True:

    while True:
        songChoice = input('\"still alive\" or \"want you gone\"?: ')

        if songChoice.lower() == 'still alive' or songChoice.lower() == 'want you gone' or songChoice == '1' or songChoice == '2':
            break
        else:
            print('Invalid choice')
            sleep(1)

    print('Excellent choice')

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