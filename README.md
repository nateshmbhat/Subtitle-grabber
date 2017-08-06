# Subtitle-grabber

Gets the subtitles for the video file or multiple videos in a specified directory.
___________

Features :-
---------
+ Relatively faster when compared to some of the other subtitle retreiving codes out there.
+ Gets the subtitle based on the Hash value of the video file. So the subtitles are very accurate.
+ Users can specify the path of the video file as an argument while running from the console.
+ Can also take direcotories as path and gets the subtitles for all the video files if found , inside any subfolder or folder within the given path.
+ After successful retrieval of the subtitle , the subtitle file is automatically renamed to the same name as that of the corresponding video file.


Supported languages :-
------------------------
+ English 'en'
+ Portuguese 'pt'
+ Spanish 'es'
+ French 'fr'
+ Italian 'it'
+ Dutch 'nl'
+ Polish 'pl'
+ Romanian 'ro'
+ Swedish 'sv'
+ Turkish 'tr'

Limitation :-
--------------
+ Since the video file is checked using its hash , for some of the video files , the subtitles won't be available if the video file hash is not present in the Subtitle server's list.



Usage :-
------------------
```
import Subtitle_grabber
Subtitle_grabber.get_subtitle(filepath , lan="en") ; 

#The argument lan refers to the two character language code for the corresponding languages as shown above.

#If the subtitle exists , then it automatically downloads it and renames it to that of the videofile.


#If a directory containing multiple files has to be specified, use the get_batch_sub( ) method.

Subtitle_grabber.get_batch_sub(directorypath , lan="en") ;

```
