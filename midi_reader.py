import midi

pattern = midi.read_midifile("digimonbraveheart.mid")

#extract track files
tracklist = []
for i in range( len(pattern) ):
    if len(pattern[i]) > 20: tracklist.append(pattern[i]) 

#extract NoteOn & NoteOff events for each track
track_output = [ [] for i in tracklist]
for count in range(len(tracklist)): 
    for event in tracklist[count]:
        if str(type(event)) in ["<class 'midi.events.NoteOnEvent'>", "<class 'midi.events.NoteOffEvent'>"]:
            TYPE = 'on' if str(type(event)) == "<class 'midi.events.NoteOnEvent'>" else 'off'
            PITCH = event.get_pitch()-24 #unsure why need to reduce by 2 octaves
            TICK = event.tick
            if len(track_output[count]) != 0 and TICK == 0:
                track_output[count][-1][1].append([TYPE,PITCH]) #combine same tick events
            else:
                track_output[count].append([TICK,[[TYPE,PITCH]]])

# --- output ---
print "number of tracks: "+str(len(track_output))
for i in range( len(track_output) ):
    print "TRACK "+str(i+1)
    for j in track_output[i]:
        print j
    print "end TRACK "+str(i+1)


