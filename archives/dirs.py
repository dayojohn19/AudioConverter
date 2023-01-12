from os import listdir
from os.path import isfile, join,isdir

# rawDirectory = '/Users/nhoj/Music/Music/Media.localized/Music/Alan\ Jackson/Precious\ Memories'
rawDirectory = '/Users/nhoj/Music/Music/Media.localized/Music/Alan\ Jackson/'
dir = rawDirectory.replace('\ ', " ")
print(isdir(dir))
# 
# .replace(r'/DIR/', '\\\\MYDIR\\data\\')