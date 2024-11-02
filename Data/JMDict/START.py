from xml.etree import ElementTree as ET
import platform

tags = ['reb ', 're_restr ', 're_pri ', 'keb ', 'k_pri ']

if platform.system() == 'Darwin':
    tree = ET.parse("/Users/kyle/GitHub/JapaneseData/Data/JMDict/TEST_jmDict.xml")
if platform.system() == 'Windows':
    tree = ET.parse("/Users/HELLHEIM/Documents/JapaneseData/Data/JMDict/TEST_jmDict.xml")

root = tree.getroot()

for entry in root[:10]:
    reb_dict = {}
    keb_dict = {}
    sense_dict = {}

    reading_elements = entry.findall('r_ele')  # get all reading elements
    for count, reading in enumerate(reading_elements, start=1):
        for child in reading:
            if child.tag == 'reb':
                reb_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 're_nokanji':
                reb_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 're_restr':
                reb_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 're_inf':
                reb_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 're_pri':
                reb_dict[str(child.tag) + ' ' + str(count)] = child.text
            else:
                print('ERROR' + child.tag + ' not found')


    kanji_elements = entry.findall('k_ele')  # get all kanji elements
    for count, kanji in enumerate(kanji_elements, start=1):
        for child in kanji:
            if child.tag == 'keb':
                keb_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'ke_pri':
                keb_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'ke_inf':
                keb_dict[str(child.tag) + ' ' + str(count)] = child.text
            else:
                print('ERROR' + child.tag + ' not found')

    sense_elements = entry.findall('sense')  # get all sense elements
    for count, sense in enumerate(sense_elements, start=1):
        g_str = ""
        for child in sense:
            if child.tag == 'gloss':
                g_str += child.text + '; '
            elif child.tag == 'pos':
                sense_dict[child.tag + ' ' + str(count)] = child.text
                #pos_el.append(child.text)
            elif child.tag == 'misc':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'lsource':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 's_inf':
                sense_dict[child.tag + ' ' + str(count)] = child.text
                #s_inf_el.append(child.text)
            elif child.tag == 'xref':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
                #xref_el.append(child.text)
            elif child.tag == 'field':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'ant':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'dial':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'stagk':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'stagr':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            else:
                print('ERROR' + child.tag + ' not found')
        sense_dict['gloss ' + str(count)] = g_str.rstrip('; ')








    print(reb_dict)
    print(keb_dict)
    print(sense_dict)
    print('----------')
