#! /usr/bin/python3
import re
import requests
from bs4 import BeautifulSoup as bs

numbered = re.compile("\n\d{1,3}\.")
page = requests.get("https://archive.org/stream/poorrichardsalma00franrich/poorrichardsalma00franrich_djvu.txt")
almanack = bs(page.content, 'html.parser')

newquotes = []
for line in numbered.split(almanack.find("pre").contents[0]):
    fixed = line.replace("\n","").replace('*','').replace('- ','')
    fixed = re.sub("\d{0,3} POOR RICHAR[DP]'S ALMANACK\. ?\d{0,3}", "", fixed)
    # Yes, there are TYPOS in the source. I will not try to fix those in the aphorisms.
    # 'The most exquisite folly is made of wisdom spun too fine.'
    newquotes.append( fixed.strip() )
        
# newquotes[0] contains all the front matter. The rest are the aphorisms.
print([x for x in newquotes[1:] if "money" in x.lower()])
