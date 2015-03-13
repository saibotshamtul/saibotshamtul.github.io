#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
#import cgitb
#cgitb.enable()

import pkgutil

print "Content-Type: text/plain;charset=utf-8"
print

print "Hello World!\n"

print "The following packages are installed:"
z = []
for x in pkgutil.iter_modules():
	z.append(x[1]+"("+str(x[2])[0:1]+")")

print z
print "\nDone!"
