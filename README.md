# Mp3 Converter

    source env/bin/activate

## (1) Managing Files

> (1) Put all Mp3 Files on the [RawMp3](/AlbumEditor/Rawmp3/)

## Note: before running the Code!

- - Change Prefered Album, Artist, Genre CheckIfMp3(`ALBUM`,¸`JCD'`,`Genre`).CheckMp3()

> Current Albums:
>
> - Religious
>   > - CheckIfMp3('Hymns','JCD','Religious Songs').CheckMp3()
> - Non-Religious
>   > - CheckIfMp3('Love Songs','JCD','Love').CheckMp3()

### Below the code file [AlbumEditor.py](/albumeditor)

    python3 AlbumEditor.py

### it will separate Mp3 to not Mp3

- Nt Mp3 will be moved in [mp4Files_dir](/mp4Files_dir/)

* Mp3 will be moved in [FolderForMp3](/AlbumEditor/FolderForMp3/)

## Ready For [Export](/AlbumEditor/ReadyToExportmp3/)

# Converting mp4 files

put all mp4 files in [mp4Files_dir](/mp4Files_dir/) and run

    audioconvert --verbose convert mp4Files_dir  AlbumEditor/Rawmp3  --output-format .mp3

### Converted files will go [Rawmp3](/AlbumEditor/Rawmp3/)

> Accepted Formats
>
> - .mp3
> - .flac
> - .aiff
> - .mp4
> - .m4a
> - .wav
> - .ogg
