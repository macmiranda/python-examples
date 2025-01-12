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
from heapq import nlargest, nsmallest

def get_top_n(filename, n):
    with open(filename) as f:
        numbers = map(int, f)
        return nlargest(n, numbers)

def get_bottom_n(filename, n):
    with open(filename) as f:
        numbers = map(int, f)
        return nsmallest(n, numbers)

if __name__ == "__main__":

    topN = int(argv[2])
    top_n_list = get_top_n(argv[1], topN)
    bottom_n_list = get_bottom_n(argv[1], topN)
    for num in top_n_list:
        print(num)
    print("---")
    for num in reversed(bottom_n_list):
        print(num)
