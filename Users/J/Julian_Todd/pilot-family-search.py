import scraperwiki
import re
import sys

sys.exit(0)

mainurl = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/0"
htmlParishes = scraperwiki.scrape(mainurl)

# loop over all Parishes
parishes = re.findall('<waypoint levelOrder="1".*?id="(\d*)" collectionId="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishes)
for idParish, collectionId, nameParish in parishes[:1]:  # first one only
    #print nameParish, "ID: ", idParish
    urlParishEvents = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/%s" % idParish
    htmlParishEvents = scraperwiki.scrape(urlParishEvents)
    
    # loop over all the events for this parish
    parishEvents = re.findall('<waypoint levelOrder="2".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEvents)
    for idEvent, nameEvent in parishEvents:
        #print nameEvent, "ID: ", idEvent
        urlParishEventYears = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idEvent)
        htmlParishEventYears = scraperwiki.scrape(urlParishEventYears)
        
        # loop over all the years for this event
        parisheventYears = re.findall('<waypoint levelOrder="3".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEventYears)
        for idYear, nameYear in parisheventYears:
            urlYear = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idYear)
            htmlYear = scraperwiki.scrape(urlYear)
            imageCount = int(re.findall('<waypoint levelOrder="3" leaf="true".*?imageCount="(\d*)".*?>', htmlYear)[0])
            #print nameYear, " ID: ", idYear, imageCount
            
            # extract the image URLs
            image = 0
            while image < imageCount :
                #print "image: ", image, ": imageCount: ", imageCount
                urlImages = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s/image?offset=%s" %(collectionId, idYear, image)
                htmlImages = scraperwiki.scrape(urlImages)
                #print htmlImages
                images = re.findall('<waypointImage offset="(\d*)".*?<url>(.*?)</url>', htmlImages)
                for offset, url in images:
                    if int(offset) + 1 > image:
                        #print "Image: ", offset, ": ", url
                        image = int(offset) + 1
                        url = re.sub("&amp;", "&", url)
                        data = {"Parish":nameParish, "Event":nameEvent, "Year":nameYear, "offset":offset, "imageCount":imageCount, "url":url }
                        scraperwiki.datastore.save(unique_keys=["url"], data=data)
                                           
        
import scraperwiki
import re
import sys

sys.exit(0)

mainurl = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/0"
htmlParishes = scraperwiki.scrape(mainurl)

# loop over all Parishes
parishes = re.findall('<waypoint levelOrder="1".*?id="(\d*)" collectionId="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishes)
for idParish, collectionId, nameParish in parishes[:1]:  # first one only
    #print nameParish, "ID: ", idParish
    urlParishEvents = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/%s" % idParish
    htmlParishEvents = scraperwiki.scrape(urlParishEvents)
    
    # loop over all the events for this parish
    parishEvents = re.findall('<waypoint levelOrder="2".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEvents)
    for idEvent, nameEvent in parishEvents:
        #print nameEvent, "ID: ", idEvent
        urlParishEventYears = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idEvent)
        htmlParishEventYears = scraperwiki.scrape(urlParishEventYears)
        
        # loop over all the years for this event
        parisheventYears = re.findall('<waypoint levelOrder="3".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEventYears)
        for idYear, nameYear in parisheventYears:
            urlYear = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idYear)
            htmlYear = scraperwiki.scrape(urlYear)
            imageCount = int(re.findall('<waypoint levelOrder="3" leaf="true".*?imageCount="(\d*)".*?>', htmlYear)[0])
            #print nameYear, " ID: ", idYear, imageCount
            
            # extract the image URLs
            image = 0
            while image < imageCount :
                #print "image: ", image, ": imageCount: ", imageCount
                urlImages = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s/image?offset=%s" %(collectionId, idYear, image)
                htmlImages = scraperwiki.scrape(urlImages)
                #print htmlImages
                images = re.findall('<waypointImage offset="(\d*)".*?<url>(.*?)</url>', htmlImages)
                for offset, url in images:
                    if int(offset) + 1 > image:
                        #print "Image: ", offset, ": ", url
                        image = int(offset) + 1
                        url = re.sub("&amp;", "&", url)
                        data = {"Parish":nameParish, "Event":nameEvent, "Year":nameYear, "offset":offset, "imageCount":imageCount, "url":url }
                        scraperwiki.datastore.save(unique_keys=["url"], data=data)
                                           
        
import scraperwiki
import re
import sys

sys.exit(0)

mainurl = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/0"
htmlParishes = scraperwiki.scrape(mainurl)

# loop over all Parishes
parishes = re.findall('<waypoint levelOrder="1".*?id="(\d*)" collectionId="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishes)
for idParish, collectionId, nameParish in parishes[:1]:  # first one only
    #print nameParish, "ID: ", idParish
    urlParishEvents = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/%s" % idParish
    htmlParishEvents = scraperwiki.scrape(urlParishEvents)
    
    # loop over all the events for this parish
    parishEvents = re.findall('<waypoint levelOrder="2".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEvents)
    for idEvent, nameEvent in parishEvents:
        #print nameEvent, "ID: ", idEvent
        urlParishEventYears = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idEvent)
        htmlParishEventYears = scraperwiki.scrape(urlParishEventYears)
        
        # loop over all the years for this event
        parisheventYears = re.findall('<waypoint levelOrder="3".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEventYears)
        for idYear, nameYear in parisheventYears:
            urlYear = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idYear)
            htmlYear = scraperwiki.scrape(urlYear)
            imageCount = int(re.findall('<waypoint levelOrder="3" leaf="true".*?imageCount="(\d*)".*?>', htmlYear)[0])
            #print nameYear, " ID: ", idYear, imageCount
            
            # extract the image URLs
            image = 0
            while image < imageCount :
                #print "image: ", image, ": imageCount: ", imageCount
                urlImages = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s/image?offset=%s" %(collectionId, idYear, image)
                htmlImages = scraperwiki.scrape(urlImages)
                #print htmlImages
                images = re.findall('<waypointImage offset="(\d*)".*?<url>(.*?)</url>', htmlImages)
                for offset, url in images:
                    if int(offset) + 1 > image:
                        #print "Image: ", offset, ": ", url
                        image = int(offset) + 1
                        url = re.sub("&amp;", "&", url)
                        data = {"Parish":nameParish, "Event":nameEvent, "Year":nameYear, "offset":offset, "imageCount":imageCount, "url":url }
                        scraperwiki.datastore.save(unique_keys=["url"], data=data)
                                           
        
import scraperwiki
import re
import sys

sys.exit(0)

mainurl = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/0"
htmlParishes = scraperwiki.scrape(mainurl)

# loop over all Parishes
parishes = re.findall('<waypoint levelOrder="1".*?id="(\d*)" collectionId="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishes)
for idParish, collectionId, nameParish in parishes[:1]:  # first one only
    #print nameParish, "ID: ", idParish
    urlParishEvents = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/%s" % idParish
    htmlParishEvents = scraperwiki.scrape(urlParishEvents)
    
    # loop over all the events for this parish
    parishEvents = re.findall('<waypoint levelOrder="2".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEvents)
    for idEvent, nameEvent in parishEvents:
        #print nameEvent, "ID: ", idEvent
        urlParishEventYears = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idEvent)
        htmlParishEventYears = scraperwiki.scrape(urlParishEventYears)
        
        # loop over all the years for this event
        parisheventYears = re.findall('<waypoint levelOrder="3".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEventYears)
        for idYear, nameYear in parisheventYears:
            urlYear = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idYear)
            htmlYear = scraperwiki.scrape(urlYear)
            imageCount = int(re.findall('<waypoint levelOrder="3" leaf="true".*?imageCount="(\d*)".*?>', htmlYear)[0])
            #print nameYear, " ID: ", idYear, imageCount
            
            # extract the image URLs
            image = 0
            while image < imageCount :
                #print "image: ", image, ": imageCount: ", imageCount
                urlImages = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s/image?offset=%s" %(collectionId, idYear, image)
                htmlImages = scraperwiki.scrape(urlImages)
                #print htmlImages
                images = re.findall('<waypointImage offset="(\d*)".*?<url>(.*?)</url>', htmlImages)
                for offset, url in images:
                    if int(offset) + 1 > image:
                        #print "Image: ", offset, ": ", url
                        image = int(offset) + 1
                        url = re.sub("&amp;", "&", url)
                        data = {"Parish":nameParish, "Event":nameEvent, "Year":nameYear, "offset":offset, "imageCount":imageCount, "url":url }
                        scraperwiki.datastore.save(unique_keys=["url"], data=data)
                                           
        
import scraperwiki
import re
import sys

sys.exit(0)

mainurl = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/0"
htmlParishes = scraperwiki.scrape(mainurl)

# loop over all Parishes
parishes = re.findall('<waypoint levelOrder="1".*?id="(\d*)" collectionId="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishes)
for idParish, collectionId, nameParish in parishes[:1]:  # first one only
    #print nameParish, "ID: ", idParish
    urlParishEvents = "http://pilot.familysearch.org/recordsearch/v1/collection/1416598/waypoint/%s" % idParish
    htmlParishEvents = scraperwiki.scrape(urlParishEvents)
    
    # loop over all the events for this parish
    parishEvents = re.findall('<waypoint levelOrder="2".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEvents)
    for idEvent, nameEvent in parishEvents:
        #print nameEvent, "ID: ", idEvent
        urlParishEventYears = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idEvent)
        htmlParishEventYears = scraperwiki.scrape(urlParishEventYears)
        
        # loop over all the years for this event
        parisheventYears = re.findall('<waypoint levelOrder="3".*?id="(\d*)".*?>\s*<label>(.*?)</label>', htmlParishEventYears)
        for idYear, nameYear in parisheventYears:
            urlYear = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s" % (collectionId, idYear)
            htmlYear = scraperwiki.scrape(urlYear)
            imageCount = int(re.findall('<waypoint levelOrder="3" leaf="true".*?imageCount="(\d*)".*?>', htmlYear)[0])
            #print nameYear, " ID: ", idYear, imageCount
            
            # extract the image URLs
            image = 0
            while image < imageCount :
                #print "image: ", image, ": imageCount: ", imageCount
                urlImages = "http://pilot.familysearch.org/recordsearch/v1/collection/%s/waypoint/%s/image?offset=%s" %(collectionId, idYear, image)
                htmlImages = scraperwiki.scrape(urlImages)
                #print htmlImages
                images = re.findall('<waypointImage offset="(\d*)".*?<url>(.*?)</url>', htmlImages)
                for offset, url in images:
                    if int(offset) + 1 > image:
                        #print "Image: ", offset, ": ", url
                        image = int(offset) + 1
                        url = re.sub("&amp;", "&", url)
                        data = {"Parish":nameParish, "Event":nameEvent, "Year":nameYear, "offset":offset, "imageCount":imageCount, "url":url }
                        scraperwiki.datastore.save(unique_keys=["url"], data=data)
                                           
        
