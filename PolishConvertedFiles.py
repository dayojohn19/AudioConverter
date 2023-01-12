from mutagen.easyid3 import EasyID3
import mutagen
import shutil
from os import listdir
from os.path import  join, isfile, isdir
import re
import os
# audio = EasyID3("AlbumEditor/03 Sam Concepcion, Tippy Dos Santos and Quest Dati Official Music Video Philpop 2013.mp3")
# audio['title'] = u"Example Title2"
# audio['album'] = u"My album"
# print(audio['title'])
# print(audio)
# audio.save()

# shutil.move("AlbumEditor/test1.mp3", "AlbumEditor/moved")

class PolishMp3():
    def __init__(self, album=None, artist=None):
        self.baseDir = "AlbumEditor/Rawmp3"
        # self.baseDir = "/Users/nhoj/Desktop/audios/musicdesktop/classic"
        self.MoveDir = "AlbumEditor/ReadyToExportmp3"
        # self.MoveDir = "/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/AlbumEditor/moved   "
        print(self.baseDir)
        print('\n\n')
        self.album = album
        self.artist = artist
        self.getList()


    def getList(self):

        with os.scandir(self.baseDir) as entries:
            for entry in entries:
                if isfile(entry):
                    # os.system('chflags nouchg {}'.format(entry.path))
                    print('Done\n\n')
                    try:
                        print('YES')
                        print(self.baseDir)
                        print(entry.path)
                        # self.checkIfLocked(entry.name)
                        self.checkIfLocked(entry)
                        print('Done Checking Locked Status',entry.name)
                        audio = EasyID3(entry.path)
                        # audio['title'] =  ''.join([i for i in entry.name[:-4] if not i.isdigit()]).lstrip(' ')
                        # audio['title'] =  ''.join([i for i in re.sub("\s\s+", " ",re.sub('[^a-zA-Z0-9 \n\.]', ' ', entry.name[:-4])) if not i.isdigit()]).lstrip(' ').rstrip()
                        audio['title'] =  ''.join([i for i in re.sub("\s\s+", " ",re.sub(r'[^a-zA-Z0-9 \n\.]', ' ', entry.name[:-4])) if not i.isdigit()]).lstrip(' ').rstrip()
                        if self.album is not None:
                            audio['album'] = self.album    
                        else:
                            audio['album'] = 'From Lenovo'
                        # audio['artist'] = 'Old Laptop'
                        if self.artist is not None:
                            audio['albumartist'] = self.artist
                        else:
                            audio['albumartist'] = 'Lenovo'
                        audio.save()
                        old_file = os.path.join(entry.path)
                        new_file = os.path.join(self.MoveDir, audio['title'][0]+entry.name[-4::])
                        os.rename(old_file, new_file)
                        print(audio['title'][0])
                        print(audio)
                        
                    except Exception as e:

                        print('Fail')
                        print(e,'\n\n')
                        pass
                print(entry)
                print('\n')


    def checkIfLocked(self,locked_filename):
        print('checking.....',locked_filename)
        print('Dir: ',self.baseDir)
        print("TYPE: ",type(locked_filename))

        # x= os.stat(self.baseDir+'/'+locked_filename).st_flags
        try:
            x= os.stat(locked_filename).st_flags
            print('FIles is Locked: ' ,x)
            # os.stat(locked_filename).st_flags=0
            # print(os.stat(locked_filename).__format__)
            xx = os.system('chflags nouchg {}'.format(locked_filename))
        except Exception as e:
            print("Fail to Check")
            # print(e)
            pass
        # xx = os.system('chflags nouchg {}'.format(self.baseDir+'/'+locked_filename))
        print('Unlocked',os.stat(locked_filename).st_flags)
        


    def moveMp3(self,fileToMove):
        # shutil.move(fileToMove,self.MoveDir)
        shutil.copy(fileToMove,self.MoveDir)

PolishMp3('My First Album', 'Me Myself and I')