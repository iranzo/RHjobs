#!/usr/bin/env python
# coding: utf-8
# Author: Pablo Iranzo Gomez (Pablo.Iranzo@gmail.com)
# Description: RSS Feed parser from RH Jobs portal

import feedparser
url = "http://redhat.jobs/feed/rss"
feed = feedparser.parse(url)

# Countries to consider in our interest region
# countries=["GBR","ESP","CZE","RUS","BEL", "CHE", "DEU", "IRL", "FRA", "FIN", "ITA", "NLD", "SWE"]
excluded = []

for item in feed["items"]:
    if item["title"][1:4] not in excluded:
        # For each job in our interest list, print title and job link
        title = item["title"][1:]
        print title.encode('utf8'), item["link"]
    else:
        if item["title"][1:4] not in excluded:
            excluded.append(item["title"][1:4])

print excluded
