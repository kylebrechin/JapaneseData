#########################################
#     COMPLETED PROGRAM
#########################################
# IMPORT
import re, os, sys



####-------------------------------------------------####
#                  Remove Newlines - START
####-------------------------------------------------####



# ---------- OPEN FILE ----------
# Open the file and store the information into a variable
# -------------------------------
with open('/content/sample_data/sentences_different.txt', 'r') as in_file:
    filedata = in_file.readlines()

# ---------- SAVE FILE ----------
# Open the file and dump everything in the variable holding it
# into the out_file to override it
# -------------------------------
# put file back together
with open('/content/sample_data/sentences_different.txt', 'w') as out_file:
    for line in filedata:
        if line is not '\n':
            out_file.write(line)

####-------------------------------------------------####
#                  Remove Brackets - START
####-------------------------------------------------####
with open('/content/sample_data/sentences_different.txt', 'r') as in_file:
    filedata = in_file.readlines()

with open('/content/sample_data/sentences_different.txt', 'w') as out_file:
    for line in filedata[:1]:
        if '[' in line:
            print("Found a [")                                                          # TODO: remove this debug line
            print(f"Searching: {repr(line)}")                                           # TODO: remove this debug line

            # find the index of the left and right bracket
            left_index = line.index(' [')
            right_index = line.index(']')
            # splice the kanji off, add newline, and save it
            line_kanji = line[:left_index] + '\n'
            # splice the kana out with bracket and newline
            line_kana = line[left_index + 2:right_index] + '\n'
            out_file.write(line_kanji)
            out_file.write(line_kana)
        else:
            print("Did not find [")                                                     # TODO: remove this debug line
