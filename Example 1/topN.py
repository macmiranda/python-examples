#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Marco Aurelio Miranda <macmiranda@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from sys import argv
txt = open(argv[1])
topN = int(argv[2])

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setPrevious(self,newprevious):
        self.previous = newprevious


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
	self.count = 0

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() <= item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
	    if current != None:
	        current.setPrevious(temp)
	    else:
		self.tail = temp
	    self.count = self.count + 1
        elif current != None:
            temp.setNext(current)
            temp.setPrevious(previous)
	    current.setPrevious(temp)
            previous.setNext(temp)
	    self.count = self.count + 1
        elif self.count < topN:
	    temp.setNext(None)
            temp.setPrevious(previous)
            previous.setNext(temp)
	    self.tail = temp
	    self.count = self.count + 1

        if self.count > topN:
            self.tail = self.tail.getPrevious()
	    self.tail.setNext(None)
	    self.count = self.count - 1

    def isEmpty(self):
        return self.head == None

    def printL(self):
        current = self.head
        while current != None:
	    print current.getData()
            current = current.getNext()

mylist = OrderedList()
for line in txt:
   mylist.add(int(line))

mylist.printL()
