import os
grammar_type_list = ["Adjective", "Adjectival Noun", "Adverb",
                     "Noun", "Interrogative", "Verbal Noun",
                     "Verb", "Interjection", "Phrase", "Pronoun"]
word = os.environ['KMVAR_grammar_check_word']
def Check():
    return (word in grammar_type_list)

print(Check())
