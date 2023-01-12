import os
from os import listdir
from os.path import join
import shutil
from mutagen.easyid3 import EasyID3
import re
import mutagen
import time


class CheckIfMp3():
    def __init__(self,album=None):
        self.album = album
        self.BaseDir = 'AlbumEditor/Rawmp3'
        self.NoIDFolder = 'AlbumEditor/FolderForMp3/NoID'
        self.mp3Folder = 'AlbumEditor/FolderForMp3'
        self.NotMp3Folder = 'RAW Files'
        self.MoveDir = 'AlbumEditor/ReadyToExportmp3'
        self.GetMp3()
        self.CheckMp3()

    def CheckMp3(self):
        FileList = [f for f in listdir(self.mp3Folder)]
        for f in FileList:
            fname=f[:-4]
            fpath=join(self.mp3Folder,f)
            if f.startswith('.'):
                continue
            rpath = self.CheckMp3ID(fpath,fname)
            if rpath is not None:
                self.RenameMp3(rpath[0],rpath[1])
            time.sleep(0.2)

    def CheckMp3ID(self,mp3Path,fname):
        try:
            faudio = EasyID3(mp3Path)
        except Exception as e:
            try:
                faudio = mutagen.File(mp3Path, easy=True)
                faudio.add_tags()
            except Exception as e:
                print(e)
                time.sleep(5)
                return None
        print('\n\n\nFAUDIO',faudio)
        if fname is not None:
            faudio['title']=fname
        else:
            faudio['title']='Unknown Title'
        if self.album is not None:
            faudio['album'] = self.album
        else:
            faudio['album'] = 'My Decade Old Songs'
        faudio['artist'] = 'JCD'
        faudio['albumartist'] = 'JCD'
        newTitle = ''.join([i for i in re.sub("\s\s+", " ",re.sub(r'[^a-zA-Z0-9 \n\.]', ' ', faudio['title'][0])) if not i.isdigit()]).lstrip(' ').rstrip()
        faudio['title'] = re.sub(r"\.",'',newTitle)
        if faudio['title'][0] == '':
            faudio['title'][0] = 'Unknown Title'
        mp3Name = faudio['title'][0]
        faudio.save()
        return [mp3Path,mp3Name]
            # ************************
        # except Exception as e:
        # except mutagen.id3.ID3NoHeaderError:
            # try:
            #     shutil.move(mp3Path,self.NoIDFolder)
            # except Exception as e:
            #     print(e, '00000-----------')
                # print('aready Exist\n\n')
            # return None
            

    def RenameMp3(self,oldName,NewName):
        os.rename(oldName, join(self.mp3Folder,NewName)+oldName[-4:])
        try:
            shutil.move(join(self.mp3Folder,NewName)+oldName[-4:],self.MoveDir)
        except Exception as e:
            print(e)
            # print('aready Exist\n\n')

        # print(NewName)
        pass






    def GetMp3(self):
        FileList = [f for f in listdir(self.BaseDir)]
        mp3N=0
        notAudioMp3=0
        for f in FileList:
            if f.endswith(".mp3"):
                mp3N+=1
                self.MoveMp3(join(self.BaseDir,f))
            else:
                notAudioMp3+=1
                # FOR DS_STORE already exist
                try:
                    shutil.move(join(self.BaseDir,f),self.NotMp3Folder)
                except:
                    pass
        print('Mp3 N: ',mp3N)
        print('Not: ',notAudioMp3)
        time.sleep(3)
        

    def MoveMp3(self,fromDir):
        try:
            shutil.move(fromDir,self.mp3Folder)
        except Exception as e:
            print(e,'\n\n')

# CheckIfMp3()
CheckIfMp3('Lucban Best').CheckMp3()