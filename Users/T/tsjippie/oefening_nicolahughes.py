import scraperwiki
from bs4 import BeautifulSoup #de goeie versie kiezen

search_page = "http://www.contractsfinder.businesslink.gov.uk/Search%20Contracts/Search%20Contracts%20Results.aspx?site=1000&lang=en&sc=3fc5e794-0cb4-4c10-be10-557f169c4c92&osc=db8f6f68-72d4-4204-8efb-57ceb4df1372&rb=1&ctlPageSize_pagesize=200&ctlPaging_page="

html = scraperwiki.scrape(search_page + "1")
soup = BeautifulSoup(html)
#print soup

max = soup.find(id="resultsfound").get_text()
num = int(max.split(" ")[2])
#print num

# Let's calculate the number of the last page

if num % 200 != 0:
    last_page = (num/200) + 1
else:
    last_page = num/200
#print last_page

for n in range(1, last_page + 1):
    html = scraperwiki.scrape(search_page + str(n))

    soup = BeautifulSoup(html)
    
    links = soup.find_all("a", "notice-title")
    #print links

    counter = (n-1)*200 + 1

    for link in links:
        url = link["href"]
        #print url
        data = {"URL": url, "id": counter}
        scraperwiki.sqlite.save(["URL"], data)
        counter+=1

#search_page = "http://www.contractsfinder.businesslink.gov.uk/Search%20Contracts/Search%20Contracts%20Results.aspx?site=1000&lang=en&sc=3fc5e794-0cb4-4c10-be10-557f169c4c92&osc=db8f6f68-72d4-4204-8efb-57ceb4df1372&rb=1&ctlPageSize_pagesize=200&ctlPaging_page=" #it has to be a string

#html = scraperwiki.scrape(search_page + "1")
#soup = BeautifulSoup(html)
#print soup

#max = soup.find(id="resultsfound").get_text() #find html element, it will give me the first one, id's are unique, zie regel 400 in broncode
#num = int(max.split (" ")[2])
#print num

#cal the number on the last page

#if num % 200 != 0:
 #   last_page = (num/200) + 1
#else:
 #   last_page = num/200
#print last_page

#for n in range(1, last_page + 1):
 #   html = scraperwiki.scrape(search_page + str(n))

#  soup = BeautifulSoup(html)
    
#    links = soup.find_all("a", "notice-title") #a tag with class notice_title tag - find_all("tag", "class)
    #print links

#   counter = (n-1)+200 + 1 #teller zodat bijgehouden wordt hoever je bent wanneer het scrapen afgebroken wordt

#    for link in links:
#        url = link("href")
#        #print url
#        data = {"URL": url, "id": counter} 
#        scraperwiki.sqlite.save(["URL"], data)
#        counter+=1 #tot hier alles om de urls te plukken

import scraperwiki
from bs4 import BeautifulSoup #de goeie versie kiezen

search_page = "http://www.contractsfinder.businesslink.gov.uk/Search%20Contracts/Search%20Contracts%20Results.aspx?site=1000&lang=en&sc=3fc5e794-0cb4-4c10-be10-557f169c4c92&osc=db8f6f68-72d4-4204-8efb-57ceb4df1372&rb=1&ctlPageSize_pagesize=200&ctlPaging_page="

html = scraperwiki.scrape(search_page + "1")
soup = BeautifulSoup(html)
#print soup

max = soup.find(id="resultsfound").get_text()
num = int(max.split(" ")[2])
#print num

# Let's calculate the number of the last page

if num % 200 != 0:
    last_page = (num/200) + 1
else:
    last_page = num/200
#print last_page

for n in range(1, last_page + 1):
    html = scraperwiki.scrape(search_page + str(n))

    soup = BeautifulSoup(html)
    
    links = soup.find_all("a", "notice-title")
    #print links

    counter = (n-1)*200 + 1

    for link in links:
        url = link["href"]
        #print url
        data = {"URL": url, "id": counter}
        scraperwiki.sqlite.save(["URL"], data)
        counter+=1

#search_page = "http://www.contractsfinder.businesslink.gov.uk/Search%20Contracts/Search%20Contracts%20Results.aspx?site=1000&lang=en&sc=3fc5e794-0cb4-4c10-be10-557f169c4c92&osc=db8f6f68-72d4-4204-8efb-57ceb4df1372&rb=1&ctlPageSize_pagesize=200&ctlPaging_page=" #it has to be a string

#html = scraperwiki.scrape(search_page + "1")
#soup = BeautifulSoup(html)
#print soup

#max = soup.find(id="resultsfound").get_text() #find html element, it will give me the first one, id's are unique, zie regel 400 in broncode
#num = int(max.split (" ")[2])
#print num

#cal the number on the last page

#if num % 200 != 0:
 #   last_page = (num/200) + 1
#else:
 #   last_page = num/200
#print last_page

#for n in range(1, last_page + 1):
 #   html = scraperwiki.scrape(search_page + str(n))

#  soup = BeautifulSoup(html)
    
#    links = soup.find_all("a", "notice-title") #a tag with class notice_title tag - find_all("tag", "class)
    #print links

#   counter = (n-1)+200 + 1 #teller zodat bijgehouden wordt hoever je bent wanneer het scrapen afgebroken wordt

#    for link in links:
#        url = link("href")
#        #print url
#        data = {"URL": url, "id": counter} 
#        scraperwiki.sqlite.save(["URL"], data)
#        counter+=1 #tot hier alles om de urls te plukken

