import xml.etree.ElementTree as ET
import numpy as np

xregion = []
yregion = []

#define the boundary region, input list[x,y]
def initialNode(firstBoundaryNode, secondBoundaryNode):
    xregion.append(firstBoundaryNode[0])
    xregion.append(secondBoundaryNode[0])
    yregion.append(firstBoundaryNode[1])
    yregion.append(secondBoundaryNode[1])

#input list[x,y]
def checkNodeInRegion(firstBoundaryNode, secondBoundaryNode):
    if (firstBoundaryNode[0] >= xregion[0] and firstBoundaryNode[0]  <= xregion[1]) and \
        (firstBoundaryNode[1] >= yregion[0] and firstBoundaryNode[1] <= yregion[1]) and \
        (secondBoundaryNode[0] >= xregion[0] and secondBoundaryNode[0] <= xregion[1]) and \
        (secondBoundaryNode[1] >= yregion[0] and secondBoundaryNode[1] <= yregion[1]):
        #in the region
        return True
    else:
        # out of bound
        return False

def getViews(root, layer):
    returnList = []
    for child in root:
      returnList.append((child,layer))
      returnList.extend(getViews(child,layer+1))
    return returnList

def printTree(xmlList):
    for index,view in enumerate(xmlList):
        print "view" + str(index)
        for attr in view[0].attrib:
            print str(attr) +" = "+ str(view[0].attrib[attr])
        print " "
def removeNode():
    newxmlList = []
    #parse xml
    tree = ET.parse('UI.xml')
    root = tree.getroot()
    viewList = getViews(root, 1)

    #remove out of bound node
    initialNode([0,0], [1000,1500])
    for i, node in enumerate (viewList):
        listTempBounds = np.array([])
        bounds = node[0].attrib['bounds']
        replacebounds = bounds.replace('][', ',').replace('[','').replace(']','')
        tempbounds = replacebounds.split(',')
        for temp in tempbounds:
            listTempBounds = np.append(listTempBounds, int(temp))
        listBounds = np.reshape(listTempBounds,(2,2))
        if checkNodeInRegion(listBounds[0], listBounds[1]) == True:
            newxmlList.append(node)
    return newxmlList

def main():
    a = removeNode()
    printTree(a)

if __name__ == '__main__':
    main()