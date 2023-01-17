# Get os and playsound
from os import sys, path
from vlc import MediaPlayer

def resource_path(relative_path):
    """ Get absolute path to resource"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath('.')

    return path.join(base_path, relative_path)

def playSong(game):
    if game == 1:
        # Get directory
        directory = resource_path('')
        stillAlive = MediaPlayer(f'{directory}StillAlive.mp3')

        stillAlive.play()

    elif game == 2:

        # Get user's directory
        directory = resource_path('')
        wantYouGone = MediaPlayer(f'{directory}WantYouGone.mp3')

        wantYouGone.play()
        