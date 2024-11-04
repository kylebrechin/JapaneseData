from xml.etree import ElementTree as ET
import platform

class bcolors:
    HEADER = '\033[95m'         # pink
    OKBLUE = '\033[94m'         # blue
    OKCYAN = '\033[96m'         # cyan
    OKGREEN = '\033[92m'        # green
    WARNING = '\033[93m'        # yellow
    FAIL = '\033[91m'           # red
    ENDC = '\033[0m'            # end color
    BOLD = '\033[1m'            # bold
    UNDERLINE = '\033[4m'       # underline


if platform.system() == 'Darwin':
    tree = ET.parse("/Users/kyle/GitHub/JapaneseData/Data/JMDict/JMdict_e.xml")
if platform.system() == 'Windows':
    tree = ET.parse("/Users/HELLHEIM/Documents/JapaneseData/Data/JMDict/TEST_jmDict.xml")



root = tree.getroot()

for entry in root[:10000]:
    reb_dict = {}
    keb_dict = {}
    sense_dict = {}

    reading_elements = entry.findall('r_ele')  # get all reading elements
    for count, reading in enumerate(reading_elements, start=1):
        if count > 2:
            break
        for child in reading:
            if child.tag == 'reb':
                reb_dict[str(child.tag) + ' ' + str(count)] = child.text

    kanji_elements = entry.findall('k_ele')  # get all kanji elements
    for count, kanji in enumerate(kanji_elements, start=1):
        if count > 2:
            break
        for child in kanji:
            if child.tag == 'keb':
                keb_dict[str(child.tag) + ' ' + str(count)] = child.text

    sense_elements = entry.findall('sense')  # get all sense elements
    for count, sense in enumerate(sense_elements, start=1):
        g_str = ""
        l_str = ""
        for child in sense:
            if child.tag == 'gloss':
                g_str += child.text + '; '
            elif child.tag == 'pos':
                sense_dict[child.tag + ' ' + str(count)] = child.text
                #pos_el.append(child.text)
            elif child.tag == 'misc':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 's_inf':
                sense_dict[child.tag + ' ' + str(count)] = child.text
                #s_inf_el.append(child.text)
            elif child.tag == 'xref':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
                #xref_el.append(child.text)
            elif child.tag == 'field':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            elif child.tag == 'lsource':
                for name, value in child.attrib.items():
                    l_str += f'{name}="{value}"; '
                sense_dict['lsource ' + str(count)] = l_str.rstrip('; ')
            elif child.tag == 'dial':
                sense_dict[str(child.tag) + ' ' + str(count)] = child.text
            # else:
            #     print('ERROR ' + child.tag + ' not found')

        sense_dict['gloss ' + str(count)] = g_str.rstrip('; ')

    # restructure data to be used






    # print(reb_dict)
    # print(keb_dict)
    print(sense_dict)
    # for key, value in sense_dict.items():
    #     print(f'{key}: {value}')
    # print('----------')


