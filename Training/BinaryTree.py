#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 二叉树是节点拥有 Next, Previous节点位置类型的数据？
#! 是left和right的树状结构


# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

# 前序遍历指的是从左下角的结点开始往右遍历？
# 中序和后序不记得了
#! 二叉树的遍历分成三种，按照根节点的访问先后分为：
#!先序遍历（先根遍历）：先访问根节点，然后访问左子树， 最后访问右子树。
#!中序遍历（中根遍历）：先访问左子树，然后访问根节点， 最后访问右子树。
#!后序遍历（后根遍历）：先访问左子树，然后访问右子树， 最后访问根节点。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return int整型一维数组
#

from typing import List

class Solution:
    def preorderTraversal(self , root) -> List[int]:
        # write code here
        re = []
        self.recursion(re, root)
        print(re)
        
    def recursion(self, re, root):
        re.append(root.val) #! 错误在于:不论是开始还是结尾输出终止条件，都需要逻辑上对应，否则会变成root.val为None的情况先append，再return。
        if re.left:
            self.recursion(re.left)
        elif re.right:
            self.recursion(re.right)
        else:
            return
        
# def preorder(self, list: List[int], root: TreeNode):   #! Solution where return is in order first, no filtering of root node in the code.
        # 遇到空节点则返回
        if root == None:
            return
        # 先遍历根节点
        list.append(root.val)
        # 再去左子树
        self.preorder(list, root.left)
        # 最后去右子树
        self.preorder(list, root.right)
    
s = Solution()
s.preorderTraversal()