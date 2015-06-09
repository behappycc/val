import CheckNode as CN

#constructor first argument guixml, second argument initial bounds
x = CN.CheckNode('UI.xml','[0,0][1000,1500]')
a = x.removeNode()
x.printTree(a)