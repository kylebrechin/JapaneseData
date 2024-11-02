from xml.etree import ElementTree as ET
import os
import platform

class bcolors:
    HEADER = '\033[95m'         # pink/purple
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if platform.system() == 'Darwin':
    tree = ET.parse("/Users/kyle/GitHub/JapaneseData/Data/JMDict/TEST_jmDict.xml")
if platform.system() == 'Windows':
    tree = ET.parse("/Users/HELLHEIM/Documents/JapaneseData/Data/JMDict/TEST_jmDict.xml")

root = tree.getroot()



# highest R_ELE and K_ELE are both 9

DICT_DEBUG_PRINT = True
JISHO_DEBUG = False




for entry in root[7:9]:
    r_el = []
    k_el = []
    g_el = []
    pos_el = []
    xref_el = []
    s_inf_el = []

    # special dictionary creation method

    # FIND READING
    ent_list = []

    reb_dict = {}
    re_nokanji_dict = {}
    re_restr_dict = {}
    re_inf_dict = {}



    reading_elements = entry.findall('r_ele')  # get all reading elements

    for count, reading in enumerate(reading_elements, start=1):




        # find everything based on tag
        for child in reading:
            if child.tag == 'reb':
                r_el.append(child.text)
                reb_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'reb {count}: ' + child.text)
            if child.tag == 're_nokanji':
                re_nokanji_dict[child.tag + ' ' + str(count)] = child.text
                # print('re_nokanji')
            if child.tag == 're_restr':
                re_restr_dict[child.tag + ' ' + str(count)] = child.text
                # print(f're_restr {count}: ' + child.text)
            if child.tag == 're_inf':
                re_inf_dict[child.tag + ' ' + str(count)] = child.text
                # print(f're_inf {count}: ' + child.text)

    # end READING elements
    # FIND KANJI
    keb_dict = {}
    ke_pri_dict = {}
    ke_inf_dict = {}

    kanji_elements = entry.findall('k_ele')  # get all kanji elements

    for count, kanji in enumerate(kanji_elements, start=1):
        for child in kanji:
            if child.tag == 'keb':
                k_el.append(child.text)
                keb_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'keb {count}: ' + child.text)
            if child.tag == 'ke_pri':
                ke_pri_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'ke_pri {count}: ' + child.text)
            if child.tag == 'ke_inf':
                ke_inf_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'ke_inf {count}: ' + child.text)

    # end KANJI elements

    # FIND SENSE
    gloss_dict = {}
    xref_dict = {}
    pos_dict = {}
    s_inf_dict = {}
    misc_dict = {}
    lsource_dict = {}
    field_dict = {}
    ant_dict = {}
    dial_dict = {}
    stagk_dict = {}
    stagr_dict = {}
    sense_elements = entry.findall('sense')  # get all sense elements

    for count, sense in enumerate(sense_elements, start=1):
        # find everything based on tag
        g_str = ""
        for child in sense:
            if child.tag == 'gloss':
                g_str += child.text + '; '
                # print(f'gloss {count}: ' + child.text)
            if child.tag == 'pos':
                pos_dict[child.tag + ' ' + str(count)] = child.text
                pos_el.append(child.text)
                # print(f'pos {count}: ' + child.text)
            if child.tag == 'misc':
                misc_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'misc {count}: ' + child.text)
            if child.tag == 'lsource':
                lsource_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'lsource {count}: ' + child.text)
            if child.tag == 's_inf':
                s_inf_dict[child.tag + ' ' + str(count)] = child.text
                s_inf_el.append(child.text)
                # print(f's_inf {count}: ' + child.text)
            if child.tag == 'xref':
                xref_dict[child.tag + ' ' + str(count)] = child.text
                xref_el.append(child.text)
                # print(f'xref {count}: ' + child.text)
            if child.tag == 'field':
                field_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'field {count}: ' + child.text)
            if child.tag == 'ant':
                ant_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'ant {count}: ' + child.text)
            if child.tag == 'dial':
                dial_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'dial {count}: ' + child.text)
            if child.tag == 'stagk':
                stagk_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'stagk {count}: ' + child.text)
            if child.tag == 'stagr':
                stagr_dict[child.tag + ' ' + str(count)] = child.text
                # print(f'stagr {count}: ' + child.text)

        # clean gloss, add to dictionary, and clear it
        gloss_dict['gloss ' + str(count)] = g_str.rstrip('; ')
        g_el = []

    # end SENSE elements

    # working !!
    if DICT_DEBUG_PRINT:
        if len(reb_dict):
            print(f'[{len(reb_dict)}] reb_dict: ' + str(reb_dict))
        if len(keb_dict):
            print(f'[{len(keb_dict)}] kab_dict: ' + str(keb_dict))
        if len(gloss_dict):
            print(f'[{len(gloss_dict)}] gloss_dict: ' + str(gloss_dict))
        if len(xref_dict):
            print(f'[{len(xref_dict)}] xref_dict: ' + str(xref_dict))
        if len(pos_dict):
            print(f'[{len(pos_dict)}] pos_dict: ' + str(pos_dict))
        if len(re_nokanji_dict):
            print(f'[{len(re_nokanji_dict)}] re_nokanji_dict: ' + str(re_nokanji_dict))
        if len(re_restr_dict):
            print(f'[{len(re_restr_dict)}] re_restr_dict: ' + str(re_restr_dict))
        if len(re_inf_dict):
            print(f'[{len(re_inf_dict)}] re_inf_dict: ' + str(re_inf_dict))
        if len(ke_pri_dict):
            print(f'[{len(ke_pri_dict)}] ke_pri_dict: ' + str(ke_pri_dict))
        if len(ke_inf_dict):
            print(f'[{len(ke_inf_dict)}] ke_inf_dict: ' + str(ke_inf_dict))
        if len(s_inf_dict):
            print(f'[{len(s_inf_dict)}] s_inf_dict: ' + str(s_inf_dict))
        if len(misc_dict):
            print(f'[{len(misc_dict)}] misc_dict: ' + str(misc_dict))
        if len(lsource_dict):
            print(f'[{len(lsource_dict)}] lsource_dict: ' + str(lsource_dict))
        if len(field_dict):
            print(f'[{len(field_dict)}] field_dict: ' + str(field_dict))
        if len(ant_dict):
            print(f'[{len(ant_dict)}] ant_dict: ' + str(ant_dict))
        if len(dial_dict):
            print(f'[{len(dial_dict)}] dial_dict: ' + str(dial_dict))
        if len(stagk_dict):
            print(f'[{len(stagk_dict)}] stagk_dict: ' + str(stagk_dict))
        if len(stagr_dict):
            print(f'[{len(stagr_dict)}] stagr_dict: ' + str(stagr_dict))

    # -----------------------------
    # pos
    # gloss
    # xref
    # s_inf

    # PRINT OUT EVERYTHING LIKE ON JISHO
    if JISHO_DEBUG:
        for idx, item in enumerate(gloss_dict):
            print(f"{bcolors.HEADER}pos: {bcolors.ENDC}", end='')
            print(pos_dict['pos ' + str(idx + 1)])
            print("\tgloss: " + str(gloss_dict['gloss ' + str(idx + 1)]))
            if 'xref ' + str(idx + 1) in xref_dict:
                print("\txref: " + xref_dict['xref ' + str(idx + 1)])
            if 's_inf ' + str(idx + 1) in s_inf_dict:
                print("\ts_inf: " + s_inf_dict['s_inf ' + str(idx + 1)])

    # PRINTOUT
    # print("############## PRINTOUTS ##############")
    # print(f'\t\treadings {len(r_el)}')
    # for count, r in enumerate(r_el, start=1):
    #     print(f'\t\t\t{count} {r}')

    # print(f'\t\tkanji {len(k_el)}')
    # for count, k in enumerate(k_el, start=1):
    #     print(f'\t\t\t{count} {k}')

    # print(f'\t\tpos {len(pos_el)}')
    # for count, pos in enumerate(pos_el, start=1):
    #     print(f'\t\t\t{count} {pos}')

    # print(f'\t\tgloss {len(g_el)}')
    # for count, g in enumerate(g_el, start=1):
    #     print(f'\t\t\t{count} {g}')

    # print(f'\t\txref {len(xref_el)}')
    # for count, x in enumerate(xref_el, start=1):
    #     print(f'\t\t\t{count} {x}')

    # print(f'\t\ts_inf_el {len(s_inf_el)}')
    # for count, s_inf in enumerate(s_inf_el, start=1):
    #     print(f'\t\t\t{count} {s_inf}')

    # print('^^^^^^^^^^^^^^ PRINTOUTS ^^^^^^^^^^^^^^\n\n')

    input("Press any key to continue...")

    # print out information

    # COLORED TEXT TEST
    # https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
    # print("\033[1;32mThis text is Bright Green  \n")

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
