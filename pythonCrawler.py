import httplib
import re

str1 = "http://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Illuminati&namespace=0&limit=50000"
con1 = httplib.HTTPConnection("en.wikipedia.org")
con1.connect()
pathToTool = "/w/index.php?title=Special:WhatLinksHere/"
keyword = "Illuminati"
namespaceStr = "&namespace="
namespace = 0
limitStr = "&limit="
limit = 50000
con1.putrequest("GET",pathToTool + keyword + namespaceStr + str(namespace) + limitStr + str(limit))

response = con1.getresponse()

#print response.read()
