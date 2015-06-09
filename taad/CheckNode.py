import xml.etree.ElementTree as ET
import numpy as np

class CheckNode:
    xregion = []
    yregion = []

    def __init__(self, inputxml, initialnode):
        self.inputxml = inputxml
        self.initialnode = initialnode

    #define the boundary region, input list[x,y]
    def initialNode(self):
        listTempBounds = []
        bounds = self.initialnode
        replacebounds = bounds.replace('][', ',').replace('[','').replace(']','')
        tempbounds = replacebounds.split(',')
        for temp in tempbounds:
            listTempBounds = np.append(listTempBounds, int(temp))
        self.xregion.append(listTempBounds[0])
        self.xregion.append(listTempBounds[2])
        self.yregion.append(listTempBounds[1])
        self.yregion.append(listTempBounds[3])

    #input list[x,y]
    def checkNodeInRegion(self, firstBoundaryNode, secondBoundaryNode):
        if (firstBoundaryNode[0] >= self.xregion[0] and firstBoundaryNode[0]  <= self.xregion[1]) and \
            (firstBoundaryNode[1] >= self.yregion[0] and firstBoundaryNode[1] <= self.yregion[1]) and \
            (secondBoundaryNode[0] >= self.xregion[0] and secondBoundaryNode[0] <= self.xregion[1]) and \
            (secondBoundaryNode[1] >= self.yregion[0] and secondBoundaryNode[1] <= self.yregion[1]):
            #in the region
            return True
        else:
            # out of bound
            return False

    def getViews(self, root, layer):
        returnList = []
        for child in root:
          returnList.append((child,layer))
          returnList.extend(self.getViews(child,layer+1))
        return returnList

    def printTree(self, xmlList):
        for index,view in enumerate(xmlList):
            print "view" + str(index)
            for attr in view[0].attrib:
                print str(attr) +" = "+ str(view[0].attrib[attr])
            print " "

    def removeNode(self):
        newxmlList = []
        #parse xml
        tree = ET.parse(self.inputxml)
        root = tree.getroot()
        viewList = self.getViews(root, 1)

        #remove out of bound node
        self.initialNode()
        for i, node in enumerate (viewList):
            listTempBounds = np.array([])
            bounds = node[0].attrib['bounds']
            replacebounds = bounds.replace('][', ',').replace('[','').replace(']','')
            tempbounds = replacebounds.split(',')
            for temp in tempbounds:
                listTempBounds = np.append(listTempBounds, int(temp))
            listBounds = np.reshape(listTempBounds,(2,2))
            if self.checkNodeInRegion(listBounds[0], listBounds[1]) == True:
                newxmlList.append(node)
        return newxmlList

if __name__ == '__main__':
    x = CheckNode('UI.xml','[0,0][1000,1500]')
    a = x.removeNode()
    x.printTree(a)