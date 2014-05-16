#!C:/Python27/python.exe -u

import mechanize
import re

browser = mechanize.Browser()

myURL = "http://bigbangtrans.wordpress.com"
infoResp = browser.open(myURL).read()
m = re.findall(">Series.*?</a>", str(infoResp))
print "Total", len(m)
s = m[-1][1:]
print s[:(s.index("The")-9)]

raw_input("Finished")
