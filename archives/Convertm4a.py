import os
import glob
from pydub import AudioSegment

video_dir = 'RAW FILES'  # Path where the videos are located
extension_list = ('*.mp3', '*.flv')

# os.chdir(video_dir)
print(len(video_dir))
for x in video_dir:
    print(x)
for extension in extension_list:
    print(extension)
    # for video in glob.glob(extension):
    #     mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
    #     AudioSegment.from_file(video).export(mp3_filename, format='mp3')

