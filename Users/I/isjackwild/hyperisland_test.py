import scraperwiki

search = scraperwiki.swimport('twitter_search_extended').search

search(['#hyperisland'], num_pages=15)
