#python script to change the xmltag path in the .xml files

import os
import sys
import xml.etree.ElementTree as ET


outputFolderPath = "C:\\"

tree = ET.parse("C:\\Users\\lokesh.koshale\\Desktop\\lokesh\\Data\\DataSet\\cat_book2.xml")

root = tree.getroot()
path = root.find('path')
name = tree.find('filename')
n_str = name.text
n_str = n_str.split('.', 1)[0]

path.text = str(outputFolderPath)

tree.write('modified_xml\\'+n_str+'.xml')

print(n_str)