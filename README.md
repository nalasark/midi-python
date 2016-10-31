# Midi-Readable Python
convert midi into human-readable note-events

## IMPORTANT

### 1. Installation

pip install python-midi

package github: https://github.com/vishnubob/python-midi

### 2. Modify package

python -> open module -> midi.constants

update file with the provided file

(What does this do? Adds a dictionary NOTE_MAP that maps pitch to note)

## OUTPUT

list of tracks each containing list of ticks with on/off pitch events

track_output = [ track1, track2, track3, ... ]

trackx = [ [tick, [event1, event2, event3, ... ] ], [tick, [event1, event2, event3, ... ] ], ... ]

eventx = [ [ on/off, pitch], [ on/off, pitch], ... ]

### NOTE

pitch is NOT note frequency

midi.NOTE_MAP[pitch] = note
