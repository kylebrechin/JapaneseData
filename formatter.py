#########################################
#     COMPLETED PROGRAM
#########################################
# IMPORT
import re, os, sys
#
# ####-------------------------------------------------####
# #                  Remove Newlines - START
# ####-------------------------------------------------####
#
# # ---------- OPEN FILE ----------
# # Open the file and store the information into a variable
# # -------------------------------
# with open('sentences_different.txt', 'r', encoding="utf8") as in_file:
#     filedata = in_file.readlines()
#
# # ---------- SAVE FILE ----------
# # Open the file and dump everything in the variable holding it
# # into the out_file to override it
# # -------------------------------
# # put file back together
# with open('sentences_different.txt', 'w', encoding="utf8") as out_file:
#     for line in filedata:
#         if line != '\n':
#             out_file.write(line)
#
# ####-------------------------------------------------####
# #                  Remove Brackets - START
# ####-------------------------------------------------####
# with open('sentences_different.txt', 'r', encoding="utf8") as in_file:
#     filedata = in_file.readlines()
#
# with open('sentences_different.txt', 'w', encoding="utf8") as out_file:
#     for line in filedata:
#         if '[' in line:
#             #print("Found a [")                                                          # TODO: remove this debug line
#             #print(f"Searching: {repr(line)}")                                           # TODO: remove this debug line
#
#             # find the index of the left and right bracket
#             left_index = line.index(' [')
#             right_index = line.index(']')
#             # splice the kanji off, add newline, and save it
#             line_kanji = line[:left_index] + '\n'
#             # splice the kana out with bracket and newline
#             line_kana = line[left_index + 2:right_index] + '\n'
#             out_file.write(line_kanji)
#             out_file.write(line_kana)
#         else:
#             #print("Did not find [")                                                     # TODO: remove this debug line
#             out_file.write(line)
#
# ####-------------------------------------------------####
# #                  Fix Double Kana - START
# ####-------------------------------------------------####

##############
#             Initialize Variables
##############
TYPES_OF_GRAMMAR = ["Adjective", "Adjectival Noun", "Adverb", 'Noun', "Interrogative", "Verbal Noun",
                     "Verb", "Interjection", "Phrase", "Pronoun"]
# used to set current_line_being_read if one sentence
LINE_ONE_SENTENCE_SPACING = 7
# used to set current_line_being_read if two sentences
LINE_TWO_SENTENCE_SPACING = 10
# used in checking from GRAMMAR line if next has double sentences, with or without a corrected kana
TWO_SENTENCE_SPACING_MISSING_KANA = 9
TWO_SENTENCE_SPACING_WITH_KANA = 10

# this stores if the line is a double line or not
is_double_line = False

# +1 to find line in Sublime
# -1 to find line from Sublime
current_line_being_read = 693                             # this like should have the kanji ( DEFAULT - 0)
kana_insert_point = current_line_being_read + 1
kana_line_being_read =  current_line_being_read + 1     # this like should have the kana
grammar_line_being_read = current_line_being_read + 3   #  this line should have the grammar






with open('sentences_different.txt', 'r', encoding="utf8") as in_file:
    filedata = in_file.readlines()
    set_EOF_found_next_loop = False
    EOF_found = False

    while not EOF_found:

        # END CATCHER:
        # If this is executing, check the next set to see if kana needs to be written, write it all, then save the terminate
        # this is the completion of the program
        if set_EOF_found_next_loop:
            print("Check for kana, write it all, and exit")
        # for current line position check if grammar is set up right
        # if not, kana missing
        if filedata[grammar_line_being_read].strip() not in TYPES_OF_GRAMMAR:
            print(f"----> Grammar:\t\t\t{filedata[grammar_line_being_read]}", end='')
            # insert kana
            filedata.insert(kana_insert_point, filedata[current_line_being_read])
        else:
            print("----> Grammer check OK")

        # check Kanji does not have two sentences (9 if no kana, 10 if kana)
        try:
            if filedata[grammar_line_being_read + TWO_SENTENCE_SPACING_MISSING_KANA].strip() not in TYPES_OF_GRAMMAR:
                if filedata[grammar_line_being_read + TWO_SENTENCE_SPACING_WITH_KANA].strip() not in TYPES_OF_GRAMMAR:
                    print("must be single sentence")

            else:
                    print("must be double sentences")
                    current_line_being_read += LINE_TWO_SENTENCE_SPACING
        except IndexError:
            print("EOF_Found::Single sentence remaining\nEOF_Found::Next is last")
            #TODO: this will catch the EOF error from the TRY section, need to make this break after reading last bit of info
            current_line_being_read += LINE_ONE_SENTENCE_SPACING
            EOF_found = True                    # TODO: remove after finishing the TODO below this, new while loop: while True:
            set_EOF_found_next_loop = True      # TODO: will I even use this varriable?


    # ------ DEBUG
    # print(f"{current_line_being_read + 1}. Kanji:\t\t\t{filedata[current_line_being_read]}", end='')
    # print(f"{kana_line_being_read + 1}. Kana:\t\t\t{filedata[kana_line_being_read]}", end='')
    # print(f"{grammar_line_being_read + 1}. Grammar:\t\t\t{filedata[grammar_line_being_read]}", end='')


    # for data in filedata[:14]:
    #     print(data, end='')
    print(f'{current_line_being_read}. Next kanji: {filedata[current_line_being_read]}')
