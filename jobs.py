#!/usr/bin/env python
# coding: utf-8
# Author: Pablo Iranzo Gomez (Pablo.Iranzo@gmail.com)
# Description: RSS Feed parser from RH Jobs portal

import feedparser
import datetime

url = "http://redhat.jobs/feed/rss"
feed = feedparser.parse(url)

# Countries to consider in our interest region
countries = ["GBR", "ESP", "CZE", "RUS", "BEL", "CHE", "DEU", "IRL", "FRA", "FIN", "ITA", "NLD", "SWE"]
# countries=[]
excluded = []
# If last_days is defined we will show only the jobs posted not older that it
last_days = 0
jobs = []
for item in reversed(feed["items"]):
    if len(countries) == 0 or (item["title"][1:4] in countries):
        title = item["title"][1:]
        date = datetime.datetime.strptime(item["published"][:16], "%a, %d %b %Y")
        if last_days == 0 or (date > datetime.datetime.now() - datetime.timedelta(days=last_days)):
            jobs.append(item)
    else:
        if item["title"][1:4] not in excluded:
            excluded.append(item["title"][1:4])
for job in jobs:
    print job["title"][1:].encode('utf8'), job["link"], job["published"]
print "\n"
# print "Excluded countries: %s" % excluded
print "If interested in any of those openings email Pablo.Iranzo@gmail.com for more information"