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
# #                  Fix Double Kana - START
# ####-------------------------------------------------####

##############
#             Initialize Variables
##############
TYPES_OF_GRAMMAR = ["Adjective", "Adjectival Noun", "Adverb", "Noun", "Interrogative", "Verbal Noun",
                     "Verb", "Interjection", "Phrase", "Pronoun"]
# used to set current_line_being_read if one sentence
ONE_S_SPACING = 8               # 7
# used to set current_line_being_read if two sentences
TWO_S_SPACING = 11              # 10
# used in checking from GRAMMAR line if next has single sentences, with or without a corrected kana
ONE_S_NO_KANA = 7       # 6
ONE_S_WITH_KANA = 8     # 7
# used in checking from GRAMMAR line if next has double sentences, with or without a corrected kana
TWO_S_NO_KANA = 10      # 9
TWO_S_WITH_KANA = 11    # 10
# ^ these two no longer used

# +1 to find line in Sublime from here
# -1 to find line from Sublime from here
current_line = 0                            # this like should have the kanji ( DEFAULT - 0)
kana_insert_idx = current_line + 1          # where to insert the kana
kana_line = current_line + 1                # this like should have the kana
grammar_line = current_line + 3             #  this line should have the grammar
sentence_insert_idx = grammar_line + 1

# debug lines
grammar_check_line_1 = grammar_line + TWO_S_NO_KANA
grammar_check_line_2 = grammar_line + TWO_S_WITH_KANA

def DebugLines():
    print("{0:>27}{1:>10}".format("Line", "Content"))
    print("{0:<23}{1:<7}{2}".format("Cur. Line - Kanji", (current_line + 1), (filedata[current_line].strip())))
    print("{0:<23}{1:<7}{2}".format("Kana", (kana_line + 1), (filedata[kana_line].strip())))
    print("{0:<23}{1:<7}{2}".format("Grammar", (grammar_line + 1), (filedata[grammar_line].strip())))
    print("{0:<23}{1:<7}".format("Sentence Insert", (sentence_insert_idx + 1)))
    print("{0:<23}{1:<7}{2}".format("Grammar Checks", (grammar_check_line_1), (grammar_check_line_2)))
    for idx, item in enumerate(filedata[current_line:current_line + 20]):
        print(f"{idx + 1}:\t{item}", end='')


with open('sentences_different.txt', 'r', encoding="utf8") as in_file:
    filedata = in_file.readlines()
    last = False
    while current_line < len(filedata):

        # *** DEBUG INFO ***
        try:
            DebugLines()
        except:
            sentence_insert_idx = grammar_line + 1

        # Check if a kana comes after a kanji, if not: there is no kana, so insert one
        #try:
        if filedata[grammar_line].strip()  in TYPES_OF_GRAMMAR:
            print("kana is correct")
            # write the kana into the file
        else:
            print("\nkana is NOT correct")
            print("-- inserting kana --\n")
            filedata.insert(kana_insert_idx, filedata[current_line])
            DebugLines()
        input("")
        #except IndexError:
            #print("IndexError::No more lines to read")


        ####-------------------------------------------------####
        #        Check if one or two sentence
        ####-------------------------------------------------####
        try:    # TODO: search single sentence instead, essential swap the if/else
            if filedata[(grammar_line + ONE_S_NO_KANA)].strip() not in TYPES_OF_GRAMMAR and \
                    filedata[(grammar_line + ONE_S_WITH_KANA)].strip() not in TYPES_OF_GRAMMAR:
                #print("Should be two sentence -- inserting count")
                filedata.insert(sentence_insert_idx, "2\n")
                current_line += TWO_S_SPACING
            else:
                #print("Should be one sentence -- inserting count")
                filedata.insert(sentence_insert_idx, "1\n")
                current_line += ONE_S_SPACING
        except IndexError: # do the last!
            print("IndexError::EOF - Should be one sentence")
            last = True
            print(f'Count insert: {sentence_insert_idx + 1}')
            filedata.insert(sentence_insert_idx, "1\n")
            current_line += ONE_S_SPACING

        ####-------------------------------------------------####
        #                   Update Counters
        ####-------------------------------------------------####
        kana_insert_idx = current_line + 1
        kana_line = current_line + 1  # this like should have the kana
        grammar_line = current_line + 3  # this line should have the grammar
        sentence_insert_idx = grammar_line + 1
        # debug lines
        grammar_check_line_1 = grammar_line + TWO_S_NO_KANA
        grammar_check_line_2 = grammar_line + TWO_S_WITH_KANA

    print(" -- finished fixing kana --")

# # ---------- SAVE FILE ----------
with open('sentences_numbered.txt', 'w', encoding="utf8") as out_file:
    for line in filedata:
        out_file.write(line)

# ####-------------------------------------------------####
# #                  Put into Excel - START
# ####-------------------------------------------------####
