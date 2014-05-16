#!C:/Python27/python.exe -u

import mechanize
import re

m8 = "https://www.digitec.ch/ProdukteDetails2.aspx?Reiter=Details&Artikel=298690"
dotView = "https://www.digitec.ch/ProdukteDetails2.aspx?Reiter=Details&Artikel=300186"

browser = mechanize.Browser()
# I guess I'm allowed to parse a publicly available document twice a day. The robots
# RFC states it very clearly that it is outside the scope of its memo.
browser.set_handle_robots(False)

def getPage(link):
        s = ""
        try:
            s = browser.open(link).read()
        except mechanize.HTTPError:
            s = "not available"
        return s

def parseCHF(resp):
    if resp == "not available":
        return resp
    m = re.search("CHF \d{2,3}\.(\d{2}|-)", str(resp))
    return m.group().replace("-", "00")

print
print "m8", parseCHF(getPage(m8))
print "dotView", parseCHF(getPage(dotView))
print

raw_input("Finished")
