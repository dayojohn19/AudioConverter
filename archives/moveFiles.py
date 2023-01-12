
import os
from os.path import isfile, join
import shutil
x = '/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/RAW Files'
y= '/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/converted'

def MoveFiles(fromDir, toDir):
    files = [f for f in os.listdir(fromDir) if isfile(join(fromDir, f))]
    for f in files:
        print(f)
        shutil.move(fromDir+'/'+f,toDir)
MoveFiles(x,y)
