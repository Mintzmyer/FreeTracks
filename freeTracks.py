# Code and education taken
# from https://github.com/andyp123/mp4_to_mp3
#  and https://github.com/nficano/pytube

# This code inherits any of previous licenses
# any original content is licensed under the GPL

from __future__ import print_function 
from pytube import YouTube
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from subprocess import call
from sys import argv
import os

def main():
	saveDir = '/Users/<usr>/Music/8TracksVids'
	convDir = '/Users/<usr>/Music/8Tracks'
	with open('songs.csv') as f:
		for line in f:
			if (("Album:" not in line) and ("Year:" not in line)):
				getSong(line, saveDir)
	convert(saveDir, convDir)

def getSong(title, directory):
	print("Downloading " + title)
	url = (getUrls(title))
	print(url)
	try:
		yt = YouTube(url)
		yt.streams.filter(subtype='mp4').first().download(directory)
	except:
		print("Could not find a valid url for " + title)
		return

def getUrls(search):
	query = urllib.parse.quote(search)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		return 'https://www.youtube.com' + vid['href']

def convert(indir, outdir):
    try:
        # check specified folders exist
        if not os.path.exists(indir):
            exit("Error: Input directory \'" + indir + "\' does not exist. (try prepending './')")
        if not os.path.exists(outdir):
            exit("Error: Output directory \'" + outdir + "\' does not exist.")
        if not os.access(outdir, os.W_OK):
            exit("Error: Output directory \'" + outdir + "\' is not writeable.")

        print("[{0}/*.mp4] --> [{1}/*.mp3]".format(indir, outdir))
        files = [] # files for exporting
            
        # get a list of all convertible files in the input directory
        filelist = [ f for f in os.listdir(indir) if f.endswith(".mp4") ]
        for path in filelist:
            basename = os.path.basename(path) 
            filename = os.path.splitext(basename)[0]
            files.append(filename)
        # remove files that have already been outputted from the list
        files[:] = [f for f in files if not check_file_exists(outdir, f, ".mp3")]
    except OSError as e:
        exit(e)
    
    if len(files) == 0:
        exit("Could not find any files to convert that have not already been converted.")

    # convert all unconverted files
    for filename in files:
        print("-- converting {0}/{2}.mp4 to {1}/{2}.mp3 --".format(indir, outdir, filename))
        call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", indir + "/" + filename + ".mp4"])
        call(["lame", "-v", "audiodump.wav", outdir + "/" + filename + ".mp3"])
        os.remove("audiodump.wav")

def check_file_exists(directory, filename, extension):
    path = directory + "/" + filename + extension
    return os.path.isfile(path)
if __name__=="__main__":
    main()