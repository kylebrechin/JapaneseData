from xml.etree import ElementTree as ET


tree = ET.parse("/Users/HELLHEIM/Downloads/TEST_jmDict.xml")
root = tree.getroot()




print(root.tag)

def FindReadingElements():
    r_el = entry.findall('r_ele')
    print(r_el)

def FindKanjiElements():
    k_el = entry.findall('k_ele')
    if k_el:    # for empty check code: if not k_el
        print(k_el)

def FindSenseElements():
    sense_el = entry.findall('sense')
    print(sense_el)
    
    
    
    
    
for entry in root[:10]:
    #find all reading_elements
    FindReadingElements()
    FindKanjiElements()
    FindSenseElements()
    print('\n\n')
    
    
    
    

elemList = []

for elem in tree.iter():
    elemList.append(elem.tag)

# now I remove duplicities - by convertion to set and back to list
elemList = list(set(elemList))

# Just printing out the result
print(elemList)



#   'lsource', 'ant', 'JMdict', 'r_ele', 'entry', 're_inf', 'stagr', 're_pri', 
#   're_restr', 'dial', 'field', 'ke_inf', 'k_ele', 're_nokanji', 'gloss', 
#   'pos', 'misc', 's_inf', 'ke_pri', 'xref', 'reb', 'keb', 'stagk', 'sense'