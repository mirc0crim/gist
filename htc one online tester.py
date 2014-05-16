#!C:/Python27/python.exe -u

import mechanize
import re

fust = "http://www.fust.ch/de/nav/shop/online-shop/category/handy/product/htc-8.html?cHash=f0aa3eee7194cf1a9430b9790b54dede"
interdiscount = "http://www.interdiscount.ch/idshop/product/Telefone_Mobile/897927_ER-8810785046529/HTC_One_silver/detail.jsf"
digitec = "https://www.digitec.ch/ProdukteDetails2.aspx?Reiter=Details&Artikel=265446"
mediamarkt = "http://shop.mediamarkt.ch/de/computer-telefonie/telefonie/handys-smartphones/htc-one-silber/idp5i1s4iopq"
steg = "http://www.steg-electronics.ch/de/article/htc-one-silver-756200.aspx"
brack = "http://www.brack.ch/htc-one-32gb-galacial-silver-239573"

browser = mechanize.Browser()
# I guess I'm allowed to pare a publicly available document twice a day. The robots
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
    m = re.search("CHF \d{3}\.(\d{2}|-)", str(resp))
    return m.group().replace("-", "00")

print
print "fust", parseCHF(getPage(fust)), "and 10% off"
print "interdiscount", parseCHF(getPage(interdiscount)), "and 10% off"
print "digitec", parseCHF(getPage(digitec))
print "mediamarkt", parseCHF(getPage(mediamarkt))

print "steg", re.search("\d{3}\.\d{4}", str(getPage(steg))).group().replace("00", "0")
print "brack", re.search("\d{3}\.\d{2}", str(getPage(brack))).group(), "and 1% off"
