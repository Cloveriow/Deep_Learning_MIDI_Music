import py_midicsv as pm

# Load the MIDI file and parse it into CSV format
name="is name"
csv_string = pm.midi_to_csv(name+".mid")
with open(name+"_out.csv", "w") as f:
    f.writelines(csv_string)

# Parse the CSV output of the previous command back into a MIDI file
midi_object = pm.csv_to_midi(csv_string)

# Save the parsed MIDI file to disk
with open(name+"_out.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)