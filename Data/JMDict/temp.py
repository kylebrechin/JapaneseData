from xml.etree import ElementTree as ET
import platform

if platform.system() == 'Darwin':
    tree = ET.parse("/Users/kyle/GitHub/JapaneseData/Data/JMDict/TEST_jmDict.xml")
if platform.system() == 'Windows':
    tree = ET.parse("/Users/HELLHEIM/Documents/JapaneseData/Data/JMDict/TEST_jmDict.xml")

root = tree.getroot()

# highest R_ELE and K_ELE are both 9


def FindReadingElements():
    reading_elements = entry.findall('r_ele')       # get all reading elements

    for count, reading in enumerate(reading_elements, start=1):
        # find everything based on tag
        for child in reading:
            if child.tag == 'reb':
                print(f'reb {count}: ' + child.text)
            if child.tag == 're_nokanji':
                print('re_nokanji')
            if child.tag == 're_restr':
                print(f're_restr {count}: ' + child.text)
            if child.tag == 're_inf':
                print(f're_inf {count}: ' + child.text)
            if child.tag == 'r_ele':
                print("still in r_ele")




def FindKanjiElements():
    kanji_elements = entry.findall('k_ele')       # get all kanji elements

    for count, kanji in enumerate(kanji_elements, start=1):
        for child in kanji:
            if child.tag == 'keb':
                print(f'keb {count}: ' + child.text)
            if child.tag == 'ke_pri':
                print(f'ke_pri {count}: ' + child.text)
            if child.tag == 'ke_inf':
                print(f'ke_inf {count}: ' + child.text)
            if child.tag == 'k_ele':
                print("still in kanji element")


def FindSenseElements():
    g_el = []
    sense_elements = entry.findall('sense')   # get all sense elements

    for count, sense in enumerate(sense_elements, start=1):
        # find everything based on tag
        g_str = ""
        for child in sense:
            if child.tag == 'pos':
                print(f'pos {count}: ' + child.text)
            if child.tag == 'gloss':
                g_str += child.text + '; '
                print(f'gloss {count}: ' + child.text)
            if child.tag == 'misc':
                print(f'misc {count}: ' + child.text)
            if child.tag == 'lsource':
                print(f'lsource {count}: ' + child.text)
            if child.tag == 's_inf':
                print(f's_inf {count}: ' + child.text)
            if child.tag == 'xref':
                print(f'xref {count}: ' + child.text)
            if child.tag == 'field':
                print(f'field {count}: ' + child.text)
            if child.tag == 'ant':
                print(f'ant {count}: ' + child.text)
            if child.tag == 'dial':
                print(f'dial {count}: ' + child.text)
            if child.tag == 'stagk':
                print(f'stagk {count}: ' + child.text)
            if child.tag == 'stagr':
                print(f'stagr {count}: ' + child.text)
            if child.tag == 'sense':
                print("still in sense")

            # CHECK THESE TWO TAGS ARE SUPPOSED TO BE HERE
            if child.tag == 'reb':
                print(f'reb {count}: ' + child.text)
            if child.tag == 're_pri':
                print(f're_pri {count}: ' + child.text)
            # ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
        g_el.append(g_str.rstrip('; '))
        print(g_el)
        print('\t-----')




for entry in root[5:10]:
#for count, entry in enumerate(root[5:10]):
    # print(count+1)
    # find all reading_elements
    FindReadingElements()
    FindKanjiElements()
    FindSenseElements()
    #print('--------------------------------------------')

# ALL AVAILABLE TAGS

# r_ele
    # reb
    # re_nokanji
    # re_restr
    # re_inf

# k_ele
    # keb
    # ke_pri
    # ke_inf

# sense
    # pos
    # gloss
    # misc
    # lsource
    # s_inf
    # xref
    # field
    # reb
    # re_pri
    # ant
    # dial
    # stagk
    # stagr


