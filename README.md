# FreeTracks
A (hastily hacked) implementation for downloading lists of songs

This program was pulled together to satisfy two purposes:
 1 - Experiment with pytube and some other code repos
 2 - Solve the following problem: If the user has enumerated
        a list of uncopywritten, 'open source' music, how 
        can the process of acquiring that list be automated

This was truly for my own interest and satisfaction, but
I'm making it public (and perhaps find motivation to polish
it a bit) in the event someone else finds it educational

 - -  Overview  - -

    PyTube searches YouTube for each element in the user's list
    thus this program is no better at finding content than
    YouTube's algorithm

    It selects the first (best?) result returned and downloads
    the movie version of the file. Although pyTube has the
    ability to directly download audio-only files, I found in
    practice that they were less commonly available. Hence..

    Finally, mp4_to_mp3 converts the movie file to an mp3.
    One nice feature they provide is checking the directories
    for pre-existing converted files, avoiding duplicating
    files that have already been converted


 - -   Instructions  - -   

 A. Use a spreadsheet like Numbers or Excel to organize a list
    of songs, and then export to the comma-separated values
    file named Songs.csv

 B. Modify the saveDir and convDir variables in freeTracks.py
    to point to the directories to save the movies, and to
    save the converted mp3's.

 C. Run freeTracks.py
