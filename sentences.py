#! python3

import argparse
from pydub import *
import pydub

parser = argparse.ArgumentParser(description='Generate an audio sentence from a written one, given a folder full of individual word audio clips (in mp3).')

parser.add_argument('words', metavar='word', type=str, nargs='+', help='The words (or sentences) to be converted')
parser.add_argument('--outfile', default='sentence.mp3', type=str, help='The file to write out the audio to, defaults to "sentence.mp3"', nargs='?')

args = parser.parse_args()
words = args.words
print('Converting "' + (' '.join(words)) + '" to audio')

audio_parts = list()

for word in words:
    audio_parts.append(AudioSegment.from_mp3(word+'.mp3'))

result = audio_parts.pop(0)
for part in audio_parts:
    result = result + part.strip_silence()

result = result.compress_dynamic_range()
outfile = args.outfile
if ( not outfile.endswith('.mp3') ):
    outfile = outfile + '.mp3'

print('Writing out audio to ' + outfile)
result.export(outfile)

