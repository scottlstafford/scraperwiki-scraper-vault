#import scraperwiki
#html = scraperwiki.scrape("http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm")

#import lxml.html
#root = lxml.html.fromstring(html)
#for tr in root.cssselect("div[align='left'] tr.tcont"):
#    tds = tr.cssselect("td")
#    data = {
#      'country' : tds[0].text_content(),
#      'years_in_school' : int(tds[4].text_content())
#    }
#    scraperwiki.sqlite.save(unique_keys=['country'], data=data)

import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://scraperwiki.com/")
root = lxml.html.fromstring(html)

for el in root.cssselect("div.tags a"):
    print lxml.html.tostring(el)
#import scraperwiki
#html = scraperwiki.scrape("http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm")

#import lxml.html
#root = lxml.html.fromstring(html)
#for tr in root.cssselect("div[align='left'] tr.tcont"):
#    tds = tr.cssselect("td")
#    data = {
#      'country' : tds[0].text_content(),
#      'years_in_school' : int(tds[4].text_content())
#    }
#    scraperwiki.sqlite.save(unique_keys=['country'], data=data)

import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://scraperwiki.com/")
root = lxml.html.fromstring(html)

for el in root.cssselect("div.tags a"):
    print lxml.html.tostring(el)
