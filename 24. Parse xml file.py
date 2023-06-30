import xml.etree.ElementTree as ET

#with open("webfile.xml", "r") as file:
#    xmldata = file.read()
#    print(xmldata)

tree = ET.parse("webfile.xml")
root = tree.getroot()
#print(root.tag, root.attrib)
#print(root[1][2].text)


#for child in root:
#    print(child.tag, child.attrib)
#    for innerchild in child:
#        print(innerchild.tag, innerchild.attrib)

#for neighbor in root.iter("neighbor"):
    #if neighbor.attrib in 'Austria':
#    print(neighbor.attrib)

#for country in root.findall('country'):
#    rank = country.find('rank').text
#    name = country.get('name')
#    print(name, rank)

#x = 0
#for child in root:
#    print(f"This is the child No. {x+1} with attribute: {child.attrib}")
#    x += 1

#for child in root:
#    if child.attrib['name'] == 'Liechtenstein':
#        print(f"Attribute found: {child.attrib['name']}")

#find best (lowest number) rank
# sum all ranks
#for child in root:
#    for inner in child:
#        print(inner.tag, inner.text)

#max = 0
#min = 1
#sum = 0
#for child in root:
#    for inner in child.iter('rank'):
#        if int(inner.text) <= int(min):
#            min = inner.text
#            best = (child.attrib['name'])
            #print(best)
#        if int(inner.text) > int(max):
#            max = inner.text
#            worst = (child.attrib['name'])
#            sum = int(sum) + int(inner.text)
            #print(worst)
            #print(f"sum is {sum}.")


#print(f"Best rank (No.{min}) has country {best}.")
#print(f"Worst rank (No. {max}), has country {worst}.")
#print(f"Rank sum is {sum}.")

#how many austria is there
count = 0

for child in root.iter('neighbor'):
    #print(child.attrib['name'])
    if child.attrib['name'] == 'Austria':
        count += 1
print(f"Austria is mentioned {count} times.")
