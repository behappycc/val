import xml.etree.ElementTree as ET
import sys

def getViews(root,layer):
    returnList = []
    for child in root:
      returnList.append((child,layer))
      returnList.extend(getViews(child,layer+1))
    return returnList

def main():
    #Path = sys.argv[1]
    #xml = ET.parse(Path)
    xml = ET.parse('UI.xml')
    root = xml.getroot()
    viewList = getViews(root,1)

    for index,view in enumerate(viewList):
        print("view"+str(index),"=")
        for attr in view[0].attrib:
            print(str(attr)+"="+str(view[0].attrib[attr]),end="  ")
        print("")
        print("")

if __name__ == '__main__':
    main()
