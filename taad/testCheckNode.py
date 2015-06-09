import CheckNode as CN

x = CN.CheckNode('UI.xml','[0,0][1000,1500]')
a = x.removeNode()
x.printTree(a)