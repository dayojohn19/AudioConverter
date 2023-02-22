# Mp3 Converter

## Step1: Open Environment

> - pip3 install -r requirements.txt
>   - To install dependencies

    source env/bin/activate

---

## Step2: Managing Files

- (1) Put all Mp3 Files on the [RawMp3](/AlbumEditor/Rawmp3/)

- Change Prefered Album, Artist, Genre

      CheckIfMp3(`YOUR_ALBUM`,¸`JCD'`,`Genre`).CheckMp3()

> Current Albums:
>
> - Religious
>   > CheckIfMp3('Hymns','JCD','Religious Songs').CheckMp3()
> - Non-Religious
>   > CheckIfMp3('Love Songs','JCD','Love').CheckMp3()

---

## Step: 3 Below the code file [AlbumEditor.py](/albumeditor)

    python3 AlbumEditor.py

> It will separate Mp3 to not Mp3
>
> - Not Mp3 will be moved in [mp4Files_dir](/mp4Files_dir/)
>   - Run step 4 again and back to Step 3
> - Mp3 will be moved in [FolderForMp3](/AlbumEditor/FolderForMp3/) and Ready For [Export](/AlbumEditor/ReadyToExportmp3/)

---

## Step4: Converting mp4 files

From [mp4Files_dir](/mp4Files_dir/) To [Rawmp3](AlbumEditor/Rawmp3) - [Documetation][mp4tomp3]

    audioconvert --verbose convert mp4Files_dir  AlbumEditor/Rawmp3  --output-format .mp3

### Converted files will go [Rawmp3](/AlbumEditor/Rawmp3/)

`Go back to Step 3`

---

## Final Step:

### Ready For [Export](/AlbumEditor/ReadyToExportmp3/ "Open and Automatically moved to music and delete the original File") to Music or Copy to External Storage

| Syntax    | Description                                 | asdasd |
| --------- | ------------------------------------------- | ------ |
| Header    | Title                                       | asdas  |
| Paragraph | First paragraph. <br><br> Second paragraph. | asda   |

[mp4tomp3]: https://pypi.org/project/AudioConverter/
