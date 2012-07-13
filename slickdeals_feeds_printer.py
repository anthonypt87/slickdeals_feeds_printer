"""Small script to print out Slickdeals feeds to terminal
Usage:
	python slickdeals_feed_printer.py
"""
import feedparser
from collections import namedtuple


class MultipleFeedsPrinter(object):

	def __init__(self, feeds):
		self.feeds = feeds

	def print_feeds(self):
		for feed in self.feeds:
			feed_printer = FeedPrinter(feed)
			feed_printer.print_feed()
			self._print_feed_delimiter()

	def _print_feed_delimiter(self):
		print "-" * 20
	

class FeedPrinter(object):
	"""`FeedPrinter` objecs are used to print `Feed` objects to the terminal"""

	def __init__(self, feed):
		self.feed = feed

 	def print_feed(self):
		print self.feed.title
		for entry in self.feed.entries:
			print entry.title
			print entry.link
			print


class Feed(object):
	"""A `Feed` is a title and a collection of `Entry` objects"""

	def __init__(self, title, entries):
		self.title = title
		self.entries = entries

	@classmethod
	def get_feed_from_url(cls, title, url):
		feedparser_result = feedparser.parse(url)
		entries = [
			Entry(
				feedparser_entry['title'], 
				feedparser_entry['link']
			) for feedparser_entry in feedparser_result.entries
		]
		return cls(title, entries)
			

Entry = namedtuple('Entry', ['title', 'link'])


if __name__ == '__main__':
	slickdeals_feeds = [
		Feed.get_feed_from_url('Frontpage Deals', 'http://feeds.feedburner.com/SlickdealsnetFP'),
		Feed.get_feed_from_url('Hot Topics', 'http://feeds.feedburner.com/SlickdealsnetHT'),
		Feed.get_feed_from_url('Hot Deals', 'http://feeds.feedburner.com/SlickdealsnetForums-9'),
	]
	MultipleFeedsPrinter(slickdeals_feeds).print_feeds()
