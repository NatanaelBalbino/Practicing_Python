#v0.2
#Add #CHARACTER REMOVER
#Removed the line when the code turn the variable text in a new file

#coding: 'iso_8859_1'
import re
import hashlib
from lxml import etree


parser = etree.XMLParser(remove_blank_text=True,) # lxml.etree only!
root = etree.XML(open("xml_converter.xml", ).read(), parser)
file = str(etree.tostring(root))

print(file)
print("-----------------")
print("-----------------")
print("-----------------")

#CHARACTER REMOVER - removing the caracters "b''" recived the etree code
pretext = file.replace(file[0], '')
finaltext = pretext.replace(file[1], '')

#XML TAGS REMOVER
text = re.sub('<[^<]+>', "", finaltext)

print("-----------------")
print("XML Tags Removed!")
print(text)
print("-----------------")

# Hash enconde
str2hash = text

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode("ISO-8859-1"))

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())