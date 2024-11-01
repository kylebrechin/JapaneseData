from xml.etree import ElementTree as ET
import platform

if platform.system() == 'Darwin':
    tree = ET.parse("/Users/kyle/GitHub/JapaneseData/Data/JMDict/TEST_jmDict.xml")
if platform.system() == 'Windows':
    tree = ET.parse("/Users/HELLHEIM/Documents/JapaneseData/Data/JMDict/TEST_jmDict.xml")

root = tree.getroot()

# highest R_ELE and K_ELE are both 9




for entry in root[5:10]:
    r_el = []
    k_el = []
    g_el = []
    pos_el = []
    xref_el = []
    s_inf_el = []

    # special dictionary creation method
        # ent_list = []
        # ent_dict = {}

    # in -- for child in x ---
        # ent_dict[child.tag + ' ' + str(count)] = child.text
        # ele_name = ''
        # ele_name = child.tag + ' ' + str(count)


    # FIND READING
    reading_elements = entry.findall('r_ele')  # get all reading elements

    for count, reading in enumerate(reading_elements, start=1):
        # find everything based on tag
        for child in reading:
            if child.tag == 'reb':
                r_el.append(child.text)
                print(f'reb {count}: ' + child.text)
            if child.tag == 're_nokanji':
                print('re_nokanji')
            if child.tag == 're_restr':
                print(f're_restr {count}: ' + child.text)
            if child.tag == 're_inf':
                print(f're_inf {count}: ' + child.text)
            if child.tag == 'r_ele':
                print("still in r_ele")
    # end READING elements

    # FIND KANJI
    kanji_elements = entry.findall('k_ele')       # get all kanji elements

    for count, kanji in enumerate(kanji_elements, start=1):
        for child in kanji:
            if child.tag == 'keb':
                k_el.append(child.text)
                print(f'keb {count}: ' + child.text)
            if child.tag == 'ke_pri':
                print(f'ke_pri {count}: ' + child.text)
            if child.tag == 'ke_inf':
                print(f'ke_inf {count}: ' + child.text)
            if child.tag == 'k_ele':
                print("still in kanji element")
    # end KANJI elements

    # FIND SENSE
    sense_elements = entry.findall('sense')   # get all sense elements

    for count, sense in enumerate(sense_elements, start=1):
        # find everything based on tag
        g_str = ""
        for child in sense:
            if child.tag == 'gloss':
                g_str += child.text + '; '
                print(f'gloss {count}: ' + child.text)
            if child.tag == 'pos':
                pos_el.append(child.text)
                print(f'pos {count}: ' + child.text)
            if child.tag == 'misc':
                print(f'misc {count}: ' + child.text)
            if child.tag == 'lsource':
                print(f'lsource {count}: ' + child.text)
            if child.tag == 's_inf':
                s_inf_el.append(child.text)
                print(f's_inf {count}: ' + child.text)
            if child.tag == 'xref':
                xref_el.append(child.text)
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

        g_el.append(g_str.rstrip('; '))
        print('\t-----')
        # end SENSE elements
    print("***************")

    # PRINTOUT
    print("############## PRINTOUTS ##############")
    print(f'\t\treadings {len(r_el)}')
    for count, r in enumerate(r_el, start=1):
        print(f'\t\t\t{count} {r}')

    print(f'\t\tkanji {len(k_el)}')
    for count, k in enumerate(k_el, start=1):
        print(f'\t\t\t{count} {k}')

    print(f'\t\tpos {len(pos_el)}')
    for count, pos in enumerate(pos_el, start=1):
        print(f'\t\t\t{count} {pos}')

    print(f'\t\tgloss {len(g_el)}')
    for count, g in enumerate(g_el, start=1):
        print(f'\t\t\t{count} {g}')

    print(f'\t\txref {len(xref_el)}')
    for count, x in enumerate(xref_el, start=1):
        print(f'\t\t\t{count} {x}')

    print(f'\t\ts_inf_el {len(s_inf_el)}')
    for count, s_inf in enumerate(s_inf_el, start=1):
        print(f'\t\t\t{count} {s_inf}')

    print('^^^^^^^^^^^^^^ PRINTOUTS ^^^^^^^^^^^^^^\n\n')

    # print out information

            # COLORED TEXT TEST
            # https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
            # print("\033[1;32mThis text is Bright Green  \n")


# ALL AVAILABLE TAGS

# r_ele         - 'reb', 're_nokanji', 're_pri', 're_inf', 're_restr'
    # reb
    # re_nokanji
    # re_restr
    # re_inf

# k_ele
    # keb
    # ke_pri
    # ke_inf

# sense         - 'ant', 'pos', 'lsource', 'field', 'gloss', 'dial', 'stagk', 'misc', 's_inf', 'stagr', 'xref'
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


