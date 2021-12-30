# ----- This is a console application to find information from the
#       WaniKani html files to display in an easily readable format
#       in the console
from bs4 import BeautifulSoup
from pathlib import Path
from sys import platform

# set path based on operating system
if platform == 'darwin':
    Vocab_Path = Path("/Users/kyle/GitHub/JapaneseData/Data/WaniKani/vocabulary/")
    Kanji_Path = Path("/Users/kyle/GitHub/JapaneseData/Data/WaniKani/kanji/")
elif platform == 'win32':
    pass
else:
    print("Invalid OS detected")
    quit()

def find_kanji_in_file(vocab_path, kanji_path, file):
    if (vocab_path / file).is_file():
        return (vocab_path / file)
    elif  (kanji_path / file).is_file():
        return (kanji_path / file)
    else:
        print("Not found")
        quit()





kanji_to_find = input("Word: ")
file_name = kanji_to_find + '.html'

found_html_file = find_kanji_in_file(Vocab_Path, Kanji_Path, file_name)

# open the found file and store the contents into doc variable
with open(found_html_file.as_posix(), 'r') as f:
    soup = BeautifulSoup(f, "html.parser")


p = soup.find_all('section', {'id':'meaning'})

#print(doc.prettify())




#
#
# spreadsheet_path = Path(path_raw) / "spreadsheets" / file_level /
#
#
#
#
#
# with open("index.html", 'r') as f:
#     doc = BeautifulSoup(f, "html.parser")
#
# print(doc.title.string)
