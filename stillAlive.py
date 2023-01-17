# Import functions from libraries/modules/whatever else because I dont know
from time import sleep
from termcolor import colored
from os import system
from playSongs import playSong

# Print things letter by letter instead of a whole sentence function
def pLine(string, waitTime = 0.06, newLine = True):
    for i in string:
        print(colored(i, 'yellow'), end = '', flush = True)
        sleep(waitTime)

    # If the line ends there
    if newLine:
        print('')

# Top functions
def top1():
    # Print out top part
    pLine('Forms FORM-29827281-12:', 0.05)
    pLine('Test Assesment Report', 0.05)

    # Make 3 new lines
    print('')
    print('')
    print('')

def top2():
    # Print out top part
    pLine('Forms FORM-55551-5:', 0.03)
    pLine('Personnel File Addendum:', 0.03)
    print('')
    pLine('Dear <<Subject Name Here>>,')
    print('')
    print('')
    sleep(0.5)

def top3():
    # Print out top part
    pLine('Forms FORM-55551-6:', 0.03)
    pLine('Personnel File Addendum Addendum', 0.03)
    print('')
    print('')
    sleep(5)

# Verse functions
def verse1():
    pLine('This was a triumph.')
    sleep(2.5)
    pLine('I\'m making a note here:')
    sleep(0.75)
    pLine('HUGE SUCCESS.', 0.07)
    sleep(1.5)
    pLine('It\'s hard to ', 0.07, False)
    pLine('overstate', 0.1)
    sleep(0.5)
    pLine('my satisfaction.', 0.15)
    sleep(2.5)
    pLine('Apeture Science.', 0.07)
    sleep(3)
    pLine('We do what we must,')
    sleep(0.5)
    pLine('because we can.', 0.1)
    sleep(2)
    pLine('For the good of all of us.', 0.1)
    sleep(1)
    pLine('Except the ones who are dead.')
    print('')

def verse2():
    pLine('But there\'s no sense crying')
    sleep(0.5)
    pLine('over every mistake.')
    sleep(0.5)
    pLine('You just keep on trying.')
    sleep(0.5)
    pLine('Till\' you run out of cake.')
    sleep(0.5)
    pLine('And the Science gets done.')
    sleep(0.5)
    pLine('And you make a neat gun.')
    sleep(0.5)
    pLine('For the people who are')
    sleep(0.5)
    pLine('still alive.', 0.1)

def verse3():
    pLine('I\'m not even angry.', 0.07)
    sleep(2.5)
    pLine('I\'m being so ', 0.07, False)
    sleep(0.5)
    pLine('sincere right now.', 0.1)
    sleep(2)
    pLine('Even though you broke my heart.', 0.1)
    sleep(0.5)
    pLine('And killed me.')
    sleep(2.5)
    pLine('And tore me to pieces.')
    sleep(2.5)
    pLine('And threw every piece ', 0.07, False)
    sleep(0.5)
    pLine('into ', 0.2, False)
    sleep(0.5)
    pLine('a fire.', 0.07)
    sleep(1.5)
    pLine('As they burned it hurt because', 0.08)
    sleep(0.5)
    pLine('I was so happy for you!', 0.07)

def verse4():
    pLine('Now these points of data')
    sleep(0.5)
    pLine('Make a beatuiful line.')
    sleep(0.5)
    pLine('And we\'re out of beta.')
    sleep(0.5)
    pLine('We\'re releasing on time.')
    sleep(0.5)
    pLine('So I\'m GLaD I got burned.')
    sleep(0.5)
    pLine('Think of all the things we learned.')
    sleep(0.5)
    pLine('For the people who are')
    sleep(0.5)
    pLine('still alive.', 0.1)

def verse5():
    pLine('Go ahead and leave me.', 0.1)
    sleep(1)
    pLine('I think I prefer to stay inside.', 0.1)
    sleep(2.5)
    pLine('Maybe you\'ll find someone else', 0.1)
    pLine('to help you.', 0.1)
    sleep(2.5)
    pLine('Maybe Black Mesa.', 0.1)
    sleep(1.5)
    pLine('THAT WAS A JOKE. ', 0.07, False)
    sleep(2)
    pLine('FAT CHANCE.')
    sleep(1.5)
    pLine('Anyways, ', 0.07, False)
    sleep(0.5)
    pLine('this cake is great.')
    sleep(0.5)
    pLine('It\'s so delicious and moist!')

def verse6():
    pLine('Look at me still talking.')
    sleep(0.5)
    pLine('When there\'s science to do.')
    sleep(0.5)
    pLine('When I look out there,')
    sleep(0.5)
    pLine('It makes me GLaD I\'m not you.')
    sleep(0.5)
    pLine('I\'ve experiments to run.')
    sleep(0.5)
    pLine('There is research to be done.')
    sleep(0.5)
    pLine('On the people who are')
    sleep(0.5)
    pLine('still alive.', 0.1)
    
def verse7():
    pLine('PS: And believe me I am')
    pLine('still alive.')
    print('')
    sleep(1)
    pLine('PPS: I\'m doing Science and I\'m')
    pLine('still alive.')
    print('')
    sleep(0.5)
    pLine('PPPS: I feel FANTASTIC and I\'m')
    pLine('still alive.')
    print('')
    sleep(1)
    pLine('FINAL THOUGHT: While you\'re dying I\'ll be')
    pLine('still alive.')
    print('')
    sleep(0.5)
    pLine('FINAL THOUGHT PS: And when you\'re dead I will be')
    pLine('still alive.')
    sleep(1.5)
    print('')
    print('')
    pLine('STILL ALIVE', 0.1)

# Main code (the song)
def playSongSA():
    # Clear terminal, play song, and make top part
    system('cls')
    top1()

    # Play song
    playSong(1)

    # Wait for song to start
    sleep(2.5)    

    # Begin typing out the lines of the songs

    verse1()
    sleep(0.5)
    verse2()
    sleep(1.5)
    system('cls')
    sleep(1)

    top2()
    verse3()
    sleep(0.5)
    verse4()
    sleep(0.5)
    system('cls')

    top3()
    verse5()
    sleep(1)
    verse6()
    sleep(0.5)
    system('cls')
    sleep(1)

    print('')
    print('')
    print('')
    verse7()
    sleep(1)
    system('cls')
    sleep(3)