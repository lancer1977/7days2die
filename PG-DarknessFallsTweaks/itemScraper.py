# Python code to 
# demonstrate readlines() 
import os
import xml.etree.ElementTree as ET
prefix = '<set xpath="/items/item[@name=\''
suffix = '\']/property[@name=\'Stacknumber\']/@value">50</set>'
tree = ET.parse('items.xml.orig')
root = tree.getroot()
 
L = [] 
# Using readlines() 
for item in root.iter('item'):
    #print("tag:{} attrib:{}".format( item.tag, item.attrib))   
    name =  item.get('name') 
    merge = "{}{}{}".format(prefix,name, suffix)
    if "food" in name:
        merge = merge.replace('50','250')
    if "resource" in name:
        merge = merge.replace('50','500')
    L.append(merge + '\n')
file2 = open('fielog.txt', 'w',encoding="utf8") 
file2.writelines(L) 
file2.close() 