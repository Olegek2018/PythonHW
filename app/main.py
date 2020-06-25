#import vlc, pafy



from lib.child import MainMovie



if __name__ == '__main__':

    am = MainMovie(' "Gone with the wind" ', 'avi', ' "Gone with the wind" ', 'avi', '*.mp3', ' "Gone with the wind.avi"', ' *.mpeg' )
    am.isMoving()


    
