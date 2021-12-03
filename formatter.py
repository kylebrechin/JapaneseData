#########################################
#     COMPLETED PROGRAM
#########################################
# IMPORT
# import re, os, sys, time
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
# print(" -- finished removing newlines --")
# # ####-------------------------------------------------####
# # #                  Remove Brackets - START
# # ####-------------------------------------------------####
# with open('sentences_different.txt', 'r', encoding="utf8") as in_file:
#     filedata = in_file.readlines()
#
# with open('sentences_different.txt', 'w', encoding="utf8") as out_file:
#     for line in filedata:
#         if '[' in line:
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
#             out_file.write(line)
#
# print(" -- finished removing brackets --")

# ####-------------------------------------------------####
# #                  Fix Only Kana - START
# ####-------------------------------------------------####
#   This section actually has to take care of a few things.
#
#   We need to find if there is only a kana for the sentence,
#   from there we input the kana we found onto the next line.
#   Then we check to see if there is only one sentence for the word
#   by getting the grammar for the word and comparing it to
#   where the next grammar type should be based on index
#   if the next word has a kana or not
# ####-------------------------------------------------####

##############
#             Initialize Variables
##############
TYPES_OF_GRAMMAR = ["Adjective", "Adjectival Noun", "Adverb", "Noun", "Interrogative", "Verbal Noun",
                     "Verb", "Interjection", "Phrase", "Pronoun"]
# the current line being read
current_line = 0
# set to where the grammar should be if there is a kana in the words data set
grammar_line = 0
not_finished = True

def isGrammarType(to_check):
    return to_check in TYPES_OF_GRAMMAR

with open('data.txt', 'r', encoding="utf8") as in_file:

    filedata = in_file.readlines()                                      # read in a list of all the data in the file

    # while NOT last_line or current_line > len(filedata)
    while not_finished or current_line < len(filedata):
        current_line_data = filedata[current_line].strip()                  # data stored in the current line, stripped to remove \n
        grammar_line = current_line + 3
        grammar_data = filedata[grammar_line].strip()                       # data stored in the grammar line, stripped to remove \n


        # Check to see if word set has a kana
        # This is done by checking to see if the grammar type
        # matches any of the available types
            # True = kana is on 2nd line
            # False = there is currently no kana
        if not isGrammarType(grammar_data):                                 # no kana found: perform kana insertion operation
            filedata.insert(current_line + 1, current_line_data+'\n')       # insert the 2nd kana into the list

        # We're going to assume this word set only has one sentence
        # so we're going to look for:
            # check_1: grammar if no kana
            # check_2: grammar if has kana
        try:
            check_1 = filedata[current_line + 9].strip()
            check_2 = filedata[current_line + 10].strip()
        except IndexError:
            not_finished = False

        try:    # get sentence count
            if isGrammarType(check_1):
                sentence_count = 1
                filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
            elif isGrammarType(check_2):
                sentence_count = 1
                filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
            else:
                sentence_count = 2
                filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
        except IndexError:
            sentence_count = 1
            filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
            print("GrammarCheck::IndexError:")

        if sentence_count == 1:
            current_line += 8
        elif sentence_count == 2:
            current_line += 11
        else:
            print("InvalidValue::sentence_count")

# # ---------- SAVE FILE ----------
with open('data_out.txt', 'w', encoding="utf8") as out_file:
    for line in filedata:
        out_file.write(line)

# ####-------------------------------------------------####
# #                  Put into Excel - START
# ####-------------------------------------------------####
