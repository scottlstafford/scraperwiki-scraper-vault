# -*- coding: UTF-8 -*-

import scraperwiki
import json
from BeautifulSoup import BeautifulSoup
import datetime
import dateutil.parser
import lxml.html
import resource
import sys
import urlparse
import re

# Make sure Scraperwiki believe this is the source from this database
scraperwiki.scrape("http://www.kafjord.kommune.no/postlister.18590.no.html")

lazycache=scraperwiki.swimport('lazycache')
postlistelib=scraperwiki.swimport('postliste-python-lib')

agency = 'Kåfjord kommune'

def report_errors(errors):
    if 0 < len(errors):
        print "Errors:"
        for e in errors:
            print e
        raise ValueError("Something went wrong")

def out_of_cpu(arg, spent, hard, soft):
    report_errors(arg)

def process_pdf(parser, pdfurl, errors):
    postlistelib.exit_if_no_cpu_left(0, out_of_cpu, errors)
    try:
        pdfcontent = scraperwiki.scrape(pdfurl)
        parser.preprocess(pdfurl, pdfcontent)
        pdfcontent = None
    except ValueError, e:
        errors.append(e)
    except IndexError, e:
        errors.append(e)

def process_page_queue(parser, errors):
    try:
        parser.process_pages()
        postlistelib.exit_if_no_cpu_left(0, out_of_cpu, errors)
    except scraperwiki.CPUTimeExceededError, e:
        errors.append("Processing pages interrupted")

def process_journal_pdfs(parser, listurl, errors):
#    print "Finding PDFs on " + listurl
#    u = urllib.parse.urlparse(listurl)
    html = scraperwiki.scrape(listurl)
    root = lxml.html.fromstring(html)
    html = None
    for ahref in root.cssselect("table a"):
        href = ahref.attrib['href']
        url = urlparse.urljoin(listurl, href)
        if -1 != href.find("file://") or -1 == url.find("/postliste-"):
#            print "Skipping non-http URL " + url
            continue
        if parser.is_already_scraped(url):
            True
#            print "Skipping already scraped " + url
        else:
#            print "Will process " + url
            process_pdf(parser, url, errors)
    # Follow the "next page" link to the end
    for ahref in root.cssselect("center a"):
        href = ahref.attrib['href']
        url = urlparse.urljoin(listurl, href)
        print ahref.text, url
        if -1 != ahref.text.find("Neste side"):
            process_journal_pdfs(parser, url, errors)

def test_small_pdfs(parser):
    # Test with some smaller PDFs
    errors = []
    process_pdf(parser, "http://www.kafjord.kommune.no/postliste-03-07-12.5071007-18590.html", errors)
    process_page_queue(parser, errors)
    report_errors(errors)
    exit(0)

errors = []
parser = postlistelib.PDFJournalParser(agency=agency)

#test_small_pdfs(parser)

process_page_queue(parser, errors)
process_journal_pdfs(parser, "http://www.kafjord.kommune.no/postlister.18590.no.html", errors)
process_page_queue(parser, errors)
report_errors(errors)
