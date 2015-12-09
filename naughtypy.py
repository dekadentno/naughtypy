#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import time

bot = False

if bot:
	client = pytumblr.TumblrRestClient(
		'<consumer_key>',
	    '<consumer_secret>',
	    '<oauth_token>',
	    '<oauth_secret>'
	)

def main():

	page = urllib2.urlopen('http://www.pornhub.com/random').read()
	soup = BeautifulSoup(page, "lxml")

	try:
		if len(soup.select("div.commentMessage")) > 0:
			for s in soup.select("div.commentMessage")[0].stripped_strings:
				if len(s) > 18: # I'm so sorry
					print(s)

					if bot:
						client.create_text("porn--quotes", tags=["porn quotes", "porn--quotes", "random pornhub comment" ], state="published", slug="testing-text-posts", body=s)
						print "Posted!"

					time.sleep(5)
					break
				else:
					main()		
	except Exception, e:
		raise e
		main()

if __name__ == "__main__":
    main()