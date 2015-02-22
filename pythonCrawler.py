import httplib
import re
import urllib
import json

def getWikipediaLinkedPage(keyword):
	url = "http://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/"+keyword+"&namespace=0&limit=50000"
	search_response = urllib.urlopen(url)
	search_results = search_response.read()
	return search_results

def getWikipediaLinkedPageTitles(keyword):
	webpage = getWikipediaLinkedPage(keyword)
	webpageSplit = webpage.split("<li><a")
	search = re.compile(">\w*\s*\w*<")
	found = ""
	allFound = []
	for eachItem in webpageSplit:
		if eachItem[0:4] == " hre":
			found = search.findall(eachItem)[0]
			if not("links" in found):
				allFound.append(found[1:-1])
	return allFound

def expandPath(path):
	newPaths = []
	linkedTitles = getWikipediaLinkedPageTitles(path[0])
	for eachTitle in linkedTitles:
		newPaths.append([eachTitle] + path)
	return newPaths

allPaths = [["Illuminati"],["Triangle"],["Eye"],["Pyramid"],["Person"]]
newAllPaths = []
numPathsDone = 0
for i in range(5):
	for eachPath in allPaths:
		newAllPaths += expandPath(eachPath)
	allPaths = newAllPaths
	newAllPaths = []
	print "Finished Layer"
f = open("resultsFull.txt","w")
for eachResult in allPaths:
	f.write(str(eachResult)+"\n")


#print search.findall(webpage)
#print re.findall("<a>",webpage)
