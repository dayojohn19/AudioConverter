from pydub import AudioSegment
from mutagen.easyid3 import EasyID3
import mutagen

fpath = '/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/AlbumEditor/Rawmp3/fault in the stars.m4a'
# faudio = EasyID3()
try:
    faudio = EasyID3(fpath)
except Exception as e:
    faudio = mutagen.File(fpath, easy=True)
    faudio.keys()
    # faudio.add_tags()
print('Audio: ',type(faudio))

# AudioSegment.from_file("/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/AlbumEditor/Rawmp3/fault in the stars.m4a").export("/Volumes/version2/Third/Visual Studio Code /Python/audioConvert/AlbumEditor/FolderForMp3/fault in stars.mp3", format="mp3")