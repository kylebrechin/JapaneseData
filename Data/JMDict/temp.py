from xml.etree import ElementTree as ET

tree = ET.parse("/Users/kyle/GitHub/JapaneseData/Data/JMDict/TEST_jmDict.xml")
root = tree.getroot()


def FindReadingElements():
    reading_elements = entry.findall('r_ele')       # get all reading elements

    for reading in reading_elements:
        # find everything based on tag
        for child in reading:
            if child.tag == 'reb':
                print('reb: ' + child.text)
            if child.tag == 're_nokanji':
                print('re_nokanji')
            if child.tag == 're_restr':
                print('re_restr: ' + child.text)
            if child.tag == 're_inf':
                print('re_inf: ' + child.text)
            if child.tag == 'r_ele':
                print("still in r_ele")



def FindKanjiElements():
    kanji_elements = entry.findall('k_ele')       # get all kanji elements

    for kanji in kanji_elements:
        for child in kanji:
            if child.tag == 'keb':
                print('keb: ' + child.text)
            if child.tag == 'ke_pri':
                print('ke_pri: ' + child.text)
            if child.tag == 'ke_inf':
                print('ke_inf: ' + child.text)
            if child.tag == 'k_ele':
                print("still in kanji element")


def FindSenseElements():
    sense_elements = entry.findall('sense')   # get all sense elements

    for sense in sense_elements:
        # find everything based on tag
        for child in sense:
            if child.tag == 'pos':
                print('pos: ' + child.text)
            if child.tag == 'gloss':
                print('gloss: ' + child.text)
            if child.tag == 'misc':
                print('misc: ' + child.text)
            if child.tag == 'lsource':
                print('lsource: ' + child.text)
            if child.tag == 's_inf':
                print('s_inf: ' + child.text)
            if child.tag == 'xref':
                print('xref: ' + child.text)
            if child.tag == 'field':
                print('field: ' + child.text)
            if child.tag == 'reb':
                print('reb: ' + child.text)
            if child.tag == 're_pri':
                print('re_pri: ' + child.text)
            if child.tag == 'ant':
                print('ant: ' + child.text)
            if child.tag == 'dial':
                print('dial: ' + child.text)
            if child.tag == 'stagk':
                print('stagk: ' + child.text)
            if child.tag == 'stagr':
                print('stagr: ' + child.text)
            if child.tag == 'sense':
                print("still in sense")

        print('\t-----')




for entry in root[:10]:
    #find all reading_elements
    FindReadingElements()
    FindKanjiElements()
    FindSenseElements()
    print('--------------------------------------------')


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


