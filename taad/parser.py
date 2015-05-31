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

def removeNode():
    #parse xml
    tree = ET.parse('UI.xml')
    root = tree.getroot()
    initialNode([0,0], [3000,5000])
    #find all node in tree
    for node in root.iter('node'):
        listTempBounds = np.array([])
        bounds = node.get('bounds')
        replacebounds = bounds.replace('][', ',').replace('[','').replace(']','')
        tempbounds = replacebounds.split(',')
        for temp in tempbounds:
            listTempBounds = np.append(listTempBounds, int(temp))
        listBounds = np.reshape(listTempBounds,(2,2))
        #fisrtNode = listBounds[0], secondNode = listBounds[1]
        if checkNodeInRegion(listBounds[0], listBounds[1]) == True:
            root.remove(node)
    tree.write('outputUI.xml')

def main():
    removeNode()

if __name__ == '__main__':
    main()