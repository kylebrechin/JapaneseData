#########################################
#     COMPLETED PROGRAM
#########################################
import pandas as pd
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

# #############
#             Initialize Variables
# #############
# TYPES_OF_GRAMMAR = ["Adjective", "Adjectival Noun", "Adverb", "Noun", "Interrogative", "Verbal Noun",
#                      "Verb", "Interjection", "Phrase", "Pronoun"]
# # the current line being read
# current_line = 0
# # set to where the grammar should be if there is a kana in the words data set
# grammar_line = 0
# not_finished = True
#
# def isGrammarType(to_check):
#     return to_check in TYPES_OF_GRAMMAR
#
# with open('data.txt', 'r', encoding="utf8") as in_file:
#
#     filedata = in_file.readlines()                                      # read in a list of all the data in the file
#
#     # while NOT last_line or current_line > len(filedata)
#     while not_finished or current_line < len(filedata):
#         current_line_data = filedata[current_line].strip()                  # data stored in the current line, stripped to remove \n
#         grammar_line = current_line + 3
#         grammar_data = filedata[grammar_line].strip()                       # data stored in the grammar line, stripped to remove \n
#
#
#         # Check to see if word set has a kana
#         # This is done by checking to see if the grammar type
#         # matches any of the available types
#             # True = kana is on 2nd line
#             # False = there is currently no kana
#         if not isGrammarType(grammar_data):                                 # no kana found: perform kana insertion operation
#             filedata.insert(current_line + 1, current_line_data+'\n')       # insert the 2nd kana into the list
#
#         # We're going to assume this word set only has one sentence
#         # so we're going to look for:
#             # check_1: grammar if no kana
#             # check_2: grammar if has kana
#         try:
#             check_1 = filedata[current_line + 9].strip()
#             check_2 = filedata[current_line + 10].strip()
#         except IndexError:
#             not_finished = False
#
#         try:    # get sentence count
#             if isGrammarType(check_1):
#                 sentence_count = 1
#                 filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
#             elif isGrammarType(check_2):
#                 sentence_count = 1
#                 filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
#             else:
#                 sentence_count = 2
#                 filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
#         except IndexError:
#             sentence_count = 1
#             filedata.insert(grammar_line + 1, str(sentence_count) +'\n')
#             print("GrammarCheck::IndexError:")
#
#         if sentence_count == 1:
#             current_line += 8
#         elif sentence_count == 2:
#             current_line += 11
#         else:
#             print("InvalidValue::sentence_count")

# # ---------- SAVE FILE ----------
# with open('data_out.txt', 'w', encoding="utf8") as out_file:
#     for line in filedata:
#         out_file.write(line)

# ####-------------------------------------------------####
# #                  Put into Excel - START
# ####-------------------------------------------------####
# put list into list
# then put into DataFrame

current_line = 0
COLS=['word_kanji', 'word_kana', 'word_meaning', 'word_grammar', 'sentence_count', 'sentence_1_kanji',
      'sentence_1_kana', 'sentence_1_meaning', 'sentence_2_kanji', 'sentence_2_kana', 'sentence_2_meaning',
      'from', 'part', 'word_audio', 'audio_sentence_1', 'audio_sentence_2', 'audio-tag', 'sentence_1_tag',
      'sentence_2_tag']     # for pandas data frame
not_finished = True

# initializlers for string that might not be filled
data_S2_kanji = ''
data_S2_kana = ''
data_S2_meaning = ''

with open('data_out.txt', 'r', encoding="utf8") as in_file:
    filedata = in_file.readlines()

    data = []

    while not_finished or current_line < len(filedata):
        # get data

        try:

            data_kanji              = filedata[current_line].strip()
            data_kana               = filedata[current_line + 1].strip()
            data_meaning            = filedata[current_line + 2].strip()
            data_grammar            = filedata[current_line + 3].strip()
            data_count              = filedata[current_line + 4].strip()
            data_S1_kanji           = filedata[current_line + 5].strip()
            data_S1_kana            = filedata[current_line + 6].strip()
            data_S1_meaning         = filedata[current_line + 7].strip()

            if data_count == '2':
                data_S2_kanji       = filedata[current_line + 8].strip()
                data_S2_kana        = filedata[current_line + 9].strip()
                data_S2_meaning     = filedata[current_line + 10].strip()
        except IndexError:
            not_finished = False

        try:
            if data_count == '1':
                row = [data_kanji, data_kana, data_meaning, data_grammar, data_count,
                       data_S1_kanji, data_S1_kana, data_S1_meaning, '', '', '', '', '', '', '', '', '', '', '']
                data.append(row)
                current_line += 8
            elif data_count == '2':
                row = [data_kanji, data_kana, data_meaning, data_grammar, data_count,
                       data_S1_kanji, data_S1_kana, data_S1_meaning,
                       data_S2_kanji, data_S2_kana, data_S2_meaning, '', '', '', '', '', '', '', '']
                data.append(row)
                current_line += 11
        except IndexError:
            not_finished = False
            print("Error")

    #create data frame
    df = pd.DataFrame(data, columns=COLS, index=None)


with pd.ExcelWriter('new.ods', engine='odf') as doc:
    df.to_excel(doc, sheet_name="Sheet1", index=False)






