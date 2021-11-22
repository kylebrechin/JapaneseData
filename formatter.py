#########################################
#     COMPLETED PROGRAM
#########################################
# IMPORT
import re, os, sys, time
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
#print(" -- finished removing newlines --")
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
#print(" -- finished removing brackets --")
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
# used in checking from GRAMMAR line if next has single sentences, with or without a corrected kana
ONE_SENTENCE_SPACING_MISSING_KANA = 6
ONE_SENTENCE_SPACING_WITH_KANA = 7
# used in checking from GRAMMAR line if next has double sentences, with or without a corrected kana
TWO_SENTENCE_SPACING_MISSING_KANA = 9
TWO_SENTENCE_SPACING_WITH_KANA = 10
# ^ these two no longer used

# +1 to find line in Sublime
# -1 to find line from Sublime
current_line_being_read = 0                             # this like should have the kanji ( DEFAULT - 0)
kana_insert_point = current_line_being_read + 1
kana_line_being_read =  current_line_being_read + 1     # this like should have the kana
grammar_line_being_read = current_line_being_read + 3   #  this line should have the grammar

# debug lines
grammar_check_line_1 = grammar_line_being_read + TWO_SENTENCE_SPACING_WITH_KANA
grammar_check_line_2 = grammar_line_being_read + TWO_SENTENCE_SPACING_MISSING_KANA


with open('sentences_different.txt', 'r', encoding="utf8") as in_file:
    filedata = in_file.readlines()

    while current_line_being_read < len(filedata):
        # for current line position check if grammar is set up right
        # if not, kana missing
        if filedata[grammar_line_being_read].strip() not in TYPES_OF_GRAMMAR:
            #print(f"----> Grammar:\t\t\t{filedata[grammar_line_being_read]}", end='')
            # insert kana
            filedata.insert(kana_insert_point, filedata[current_line_being_read])
        # print debug info
        print(f"\n\nProcessing from line {current_line_being_read+1}")
        print(f"Kanji:\t\t\t{filedata[current_line_being_read]}"
              f"Kana:\t\t\t{filedata[kana_line_being_read]}"
              f"Grammar:\t\t{filedata[grammar_line_being_read]}",end='')
        print(f"kanji_line {current_line_being_read+1}\tkana_line {kana_line_being_read+1}\tgrammar_line {grammar_line_being_read+1}\t\t"
              f"grammar_check_line_1 {grammar_check_line_1}\t\tgrammar_check_line_2 {grammar_check_line_2}")
        #time.sleep(.1)     # so I can read it as it scrolls
        ####-------------------------------------------------####
        #        Check if one or two sentence - START
        ####-------------------------------------------------####
        try:    # TODO: search single sentence instead, essential swap the if/else
            if filedata[(grammar_line_being_read + ONE_SENTENCE_SPACING_MISSING_KANA)].strip() not in TYPES_OF_GRAMMAR and \
                    filedata[(grammar_line_being_read + ONE_SENTENCE_SPACING_WITH_KANA)].strip() not in TYPES_OF_GRAMMAR:
                print("Should be two sentence")
                current_line_being_read += LINE_TWO_SENTENCE_SPACING
            else:
                    print("Should be one sentence")
                    current_line_being_read += LINE_ONE_SENTENCE_SPACING
        except IndexError: # do the last!
            current_line_being_read += LINE_ONE_SENTENCE_SPACING

        ####-------------------------------------------------####
        #                   Update Counters
        ####-------------------------------------------------####
        print("Updating all counting variables")
        kana_insert_point = current_line_being_read + 1
        kana_line_being_read = current_line_being_read + 1  # this like should have the kana
        grammar_line_being_read = current_line_being_read + 3  # this line should have the grammar
        # debug lines
        grammar_check_line_1 = grammar_line_being_read + TWO_SENTENCE_SPACING_WITH_KANA
        grammar_check_line_2 = grammar_line_being_read + TWO_SENTENCE_SPACING_MISSING_KANA
    print(" -- finished fixing kana --")
# # ---------- SAVE FILE ----------
with open('sentences_different.txt', 'w', encoding="utf8") as out_file:
    for line in filedata:
        out_file.write(line)

# ####-------------------------------------------------####
# #                  Put into Excel - START
# ####-------------------------------------------------####
