import httplib
import re

str1 = "http://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Illuminati&namespace=0&limit=50000"
con1 = httplib.HTTPConnection("en.wikipedia.org")
pathToTool = "/w/index.php?title=Special:WhatLinksHere/"
keyword = "Illuminati"
namespaceStr = "&namespace="
namespace = 0
limitStr
limit = 50000
con1.putrequest("POST",pathToTool + keyword + namespaceStr + str(namespace) + )
