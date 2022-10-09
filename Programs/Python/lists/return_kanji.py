''' This is a library of functions and variables that are helpful to have handy when manipulating Japanese text in
    python. This is optimized for Python 3.x, and takes advantage of the fact that all strings are unicode.'''

import re

# blocks
hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'
kanji = r'[㐀-䶵一-鿋豈-頻]'
radicals = r'[⺀-⿕]'
katakana_half_width = r'[｟-ﾟ]'
alphanum_full = r'[！-～]'
symbols_punct = r'[、-〿]'
misc_symbols = r'[ㇰ-ㇿ㈠-㉃㊀-㋾㌀-㍿]'
ascii_char = r'[ -~]'

# functions
# REGEX INFO - https://docs.python.org/3/library/re.html
# re.match(patern, string, flags=0) - returns None if no match

def extract_unicode_block(unicode_block, string):
    ''' extracts and returns all texts from a unicode block from string argument.
        Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.findall( unicode_block, string)

def remove_unicode_block(unicode_block, string):
    ''' removes all chaacters from a unicode block and returns all remaining texts from string argument.
        Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.sub( unicode_block, '', string)

def remove_kana(string):
    '''extracts all characters from a unicode block and returns all remaining texts from string argument.
       Note that you must use the unicode blocks defined above, or patterns of similar form '''
    hiragana_removed =          re.sub( hiragana_full, '', string)
    radicals_removed =          re.sub( radicals, '',hiragana_removed)
    katakana_half_removed =     re.sub( katakana_half_width, '',radicals_removed)
    alphanum_removed =          re.sub( alphanum_full, '',katakana_half_removed)
    symbols_removed =           re.sub( symbols_punct, '',alphanum_removed)
    misc_removed =              re.sub( misc_symbols, '',symbols_removed)
    asci_removed =              re.sub( ascii_char, '',misc_removed)
    return re.sub( katakana_full, '', asci_removed)

def kanji_in_sentence(string):
    sentence = remove_kana(string)
    in_sentence = ''
    if sentence == "":      # All Kanji removed, useless sentence
        return "NaN"
    sentence_len = len(sentence)-1
    for word in sentence:
        if sentence.index(word) != sentence_len:
            in_sentence += '"' + word + '",'
        else:   # last character
            in_sentence += '"' + word + '"'
    return in_sentence

# the list of the kanji found in the sentence
kanji_found = []
# LOAD
with open('data.txt', 'r', encoding="utf8") as in_file:
    for line in in_file:
        kanji_found.append(line.strip())

# for idx, line in enumerate(kanji_found):
#     print(str(idx+1) + "," + kanji_in_sentence(line))

with open('data_out.txt', 'w', encoding="utf8") as out_file:
    for idx, line in enumerate(kanji_found):
        out_file.write(str(idx+1) + "," + kanji_in_sentence(line) + "\n")






# EXAMPLES

#text = 'カイル初めての駅 自由が丘の駅で、大井町線から降りると、ママは、トットちゃんの手を引っ張って、改札口を出ようとした。ぁゟ゠ヿ㐀䶵一鿋豈頻⺀⿕｟ﾟabc！～、〿ㇰㇿ㈠㉃㊀㋾㌀㍿'

#print('Original text string:', text, '\n')
#print('All kanji removed:', remove_unicode_block(kanji, text))
#print('All hiragana in text:', ''.join(extract_unicode_block(hiragana_full, text)))
#print('All hiragana removed:', remove_unicode_block(hiragana_full, text))
#print('-------------------------')


#print('All kana removed: ', kanji_in_sentence(text))








# PRINT THE LINE
# for line in the_file[:5]:
#     print(line)

# ENUMERATION EXAMPLE TO GET INDED
# for idx, x in enumerate(xs):
#     print(idx, x)