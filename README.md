# Sentences.py

Quick and dirty script to join a bunch of individual audio words to create a sentence.

## Instructions

Get some individual words of recorded audio (in mp3, or change two lines of code in this file)
forvo.com seems to be a good source for these
Rename all the audio files in the pattern [word it says].mp3
Pick a sentence, using only words you have files for in the folder.
Run, like
``` python sentences.py [--outfile save-to.mp3] these are some words ```
...wait...
BAM! You have the audio equivalent of one of those ransom notes you see in the movies

### Dependencies

jiaaro/pydub (with commit 1362a77e55) - This will hopefully be merged soon
