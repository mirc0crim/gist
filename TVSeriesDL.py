#!C:/Python27/python.exe -u
 
import mechanize
import re
import webbrowser
import datetime
import os
 
username = "u"
password = "pw"
 
basedlURL = "http://hralinks.info/viewtopic.php?f=3&t="
dl = {"ng": "253", "tbbt": "54", "tm": "55", "taahm": "18", "got": "93", "2bg": "270", "ts": "83", "caso": "737"}
baseinfoURL = "http://services.tvrage.com/feeds/episodeinfo.php?sid="
info = {"ng": "28304", "tbbt": "8511", "tm": "18967", "taahm": "6454", "got": "24493", "2bg": "28416", "ts": "6190", "caso": "29336"}
 
loginURL = "http://hralinks.info/ucp.php?mode=login"
 
# Mo = 0; Su = 6
dayinweek = datetime.datetime.today().weekday()
 
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.set_handle_equiv(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
 
def login():
    print "Login to hralinks..."
    browser.open(loginURL)
    browser.select_form(nr=0)
    browser["username"] = username
    browser["password"] = password
    browser.new_control("HIDDEN", "action", {})
    control = browser.form.find_control("action")
    control.readonly = False
    browser["action"] = "login"
    browser.method = "POST"
    browser.action = loginURL
    response = browser.submit()
 
def download(name):
    print "Fetching dl link..."
    myURL = basedlURL + dl[name]
    dlResp = browser.open(myURL).read()
    m = re.search("http://ul\.to/.{5,10}<", dlResp)
    if m:
        link = m.group().replace("<", "")
        print link
        webbrowser.open(link)
    else:
        print "Link not found"
 
def setClipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
 
def getLatestNumber(name):
    myURL = baseinfoURL + info[name]
    infoResp = browser.open(myURL).read()
    m = re.search("<number>.*?</number>", str(infoResp))
    number = m.group().replace("<number>", "").replace("</number>", "")
    n = number.replace(number[0:3], "")
    print "Latest Number: " + n
    return n
 
def getLatestTitle(name):
    myURL = baseinfoURL + info[name]
    infoResp = browser.open(myURL).read()
    m = re.search("<title>.*?</title>", str(infoResp))
    t = m.group().replace("<title>", "").replace("</title>", "")
    print "Latest Title: " + t
    return t
 
 
seriesName = []
if dayinweek == 1:
    #seriesName.append("2bg")
    print "2bg -> september 2014"
if dayinweek == 2:
    #seriesName.append("ng")
    print "ng -> september 2014"
if dayinweek == 4:
    #seriesName.append("tbbt")
    print "tbbt -> september 2014"
    #seriesName.append("taahm")
    print "taahm -> september 2014"
if dayinweek == 0:
    seriesName.append("tm")
    print "tm"
    seriesName.append("ts")
    print "ts"
    seriesName.append("got")
    print "got"
    seriesName.append("caso")
    print "caso"
 
if len(seriesName) != 0:
    for s in seriesName:
        print "Checking " + s
        if seriesName.index(s) == 0:
            login()
        download(s)
        try:
            setClipboard(getLatestNumber(s) + " " + getLatestTitle(s))
        except:
            print "name/number not loaded"
        if len(seriesName) > 1:
            raw_input("Enter for next")
 
raw_input("Finished")
