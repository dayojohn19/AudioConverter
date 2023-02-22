from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import shutil
import time
"""

HOW TO USE
From TERMINAL cd Directory and Copy
Arguments :
(1) File Directories 
(2) Export Directories
(3) Convert Format (.mp3)

Execute
```
    from getFileList import ConvertAll
    Convertall(1,2,3)
```


To Easy Run, Put all files on FILES and MP3 will put putted on AlbumEditor and Successful converted file will be moved to converted files
"""
FromDIR='/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/RAW Files'
MoveDIR='/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/converted'
# FailedDir='/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/convertedFailed'

class ConvertAll():
    def __init__(self, FilesDirectories,MoveDIRF, exportDirectories,convertFormat):
        # FilesDirectories = 
        dir = FilesDirectories.replace('\ ', " ")
        self.convertFormat = convertFormat
        self.exportFrom = dir
        self.exportTo = exportDirectories
        self.countN = 0
        self.MoveDIR = MoveDIRF
        self.GetFiles()
        self.FailedDir = '/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/convertedFailed'
        

    def GetFiles(self):
        self.FileList = [f for f in listdir(self.exportFrom) if isfile(join(self.exportFrom, f))]
        for eachFile in self.FileList:
            time.sleep(0.2)
            try:
                # print(eachFile)
                # fileType = eachFile.split('.')[1]
                fileType = eachFile[-3:]
                # print(eachFile,fileType)
                self.convertFile(eachFile,fileType)

            except Exception as e:
                    print(e)
                    pass
            print('\n')

    def convertFile(self,fileName,fileType):
        try:
            # print(join(self.exportFrom,fileName),'\n')
            # print(join(self.exportFrom,fileName), fileType )
            
            convertedFile = AudioSegment.from_file(join(self.exportFrom,fileName), format=fileType )
            # print(convertedFile)
            print('Success: Converted',fileType)
            # print(fileName)
            # print(fileName[:-3])
            # print(self.convertFormat)
            # print(join(self.exportTo,fileName[:-3])+self.convertFormat)
            # print()
            convertedFile.export(join(self.exportTo,fileName.split('.')[0])+'.'+self.convertFormat, format=self.convertFormat)
            # print('Initial Convertion Done',convertedFile)
            # ****
            # convertedFile.export(join(self.exportTo,fileName[:-3])+self.convertFormat, format=self.convertFormat)
            print('     Success Exported')
            return
            print('Moving..')
            self.countN+=1
            shutil.move(self.exportFrom+'/'+fileName,MoveDIR)
            print('Done', self.countN)
        except Exception as e:
            print('Failed: ',fileType)
            # print('\nFailed',e)
            # shutil.move(self.exportFrom+'/'+fileName,self.FailedDir)

ConvertAll(FromDIR,MoveDIR,'/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/ExportedFiles','mp3')