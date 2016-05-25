# -*- coding: utf-8 -*-


class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None

    def setLeftBranch(self, node):
        self.leftBranch = node
        
        self.rightBranch = node
        self.parent = 