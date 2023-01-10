# Import functions from libraries/modules/whatever else because I dont know
from time import sleep
from termcolor import colored
from os import system, path, sys
from vlc import MediaPlayer

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)

# Print things letter by letter instead of a whole sentence function
def pLine(string, waitTime = 0.08, newLine = True, afterWaitTime = 0.5):
    for i in string:
        print(colored(i, 'yellow'), end = '', flush = True)
        sleep(waitTime)

    # If the line ends there
    if newLine:
        print('')

    sleep(afterWaitTime)

# Top functions

def top1():
    pLine('Forms FORM-29827281-12-2:')
    pLine('Notice of Dismissal')
    print('')

def top2():
    print(colored('Severance Package Details:', 'yellow'))
    print('')

# Verse functions

def verse1():
    pLine('Well here we are again')
    pLine('It\'s always such a pleasure')
    pLine('Remember when you tried')
    pLine('to kill me twice?')
    sleep(0.5)
    pLine('Oh how we laughed and laughed')
    pLine('Except I wasn\'t laughing')
    pLine('Under the circumstances')
    pLine('I\'ve been shockingly nice')

    sleep(0.5)
    system('cls')

def verse2():
    pLine('You want your freedom?')
    pLine('Take it', 0.1)
    sleep(1)
    pLine('That\'s what I\'m counting on')
    print('')
    sleep(2)
    pLine('I used to want you dead', 0.1)
    pLine('but')
    pLine('Now I only want you gone', 0.1)

    sleep(4)
    system('cls')

def verse3():
    pLine('She was a lot like you')
    pLine('(Maybe not quite as heavy)')
    pLine('Now little Caroline ', 0.08, False)
    pLine('is in here too')
    sleep(1)
    pLine('One day they woke me up')
    pLine('So I could live forever')
    pLine('It\'s such a shame the same')
    pLine('will never happen to you')

    sleep(0.5)
    system('cls')

def verse4():
    pLine('You\'ve got your', 0.05)
    pLine('short sad')
    pLine('life ', 0.15, False)
    pLine('left', 0.2)
    sleep(1)
    pLine('That\'s what I\'m counting on')
    sleep(1)
    pLine('I\'ll let you get right to it')
    pLine('Now I only want you gone')

    sleep(4)
    system('cls')

def verse5():
    pLine('Goodbye my only friend')
    pLine('Oh, did you think I meant you?', 0.08)
    pLine('That would be funny', 0.08)
    pLine('if it weren\'t ', 0.08, False)
    pLine('so sad', 0.2)
    pLine('Well you have been replaced')
    pLine('I dont\'t need anyone now')
    pLine('When I delete you maybe')
    pLine('[REDACTED]', 0.5)

    sleep(0.5)
    system('cls')

def verse6():
    pLine('Go make some new ', 0.1, False)
    pLine('disaster', 0.2)
    sleep(1)
    pLine('That\'s what I\'m counting on')
    sleep(1)
    pLine('You\'re someone else\'s problem', 0.1, True, 0)
    pLine('Now I only want you gone')
    pLine('Now I only want you gone')
    pLine('Now I only want you')

def end():
    for _ in range(5):
        print('')
    pLine('gone', 0.5)

# Main code
def playSongWYG():

    # Clear terminal
    system('cls')

    # Get user's directory
    directory = resource_path('.')

    # Use directory to get song for VLC
    wantYouGone = MediaPlayer(f'{directory}/WantYouGone.mp3')

    # Wait for song to start
    wantYouGone.play()
    sleep(0.5)
    
    # Make top part
    top1()

    # Start verses

    verse1()

    verse2()

    sleep(0.5)
    verse3()

    top2()
    verse4()

    verse5()

    verse6()
    end()
    sleep(1)
    system('cls')