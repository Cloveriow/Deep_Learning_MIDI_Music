import py_midicsv as pm

# Load the MIDI file and parse it into CSV format
name="mymusic11"

midi_object = pm.csv_to_midi(name+".csv")

# Save the parsed MIDI file to disk
with open(name+"_out.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)