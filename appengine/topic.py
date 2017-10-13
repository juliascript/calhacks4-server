
import uuid

class Topic:

	def __init__(self, topic_id, title, summary, articles):
		self.title = title
		self.summary = summary
		self.articles = articles
		self.id = str(topic_id)
		for article in articles:
			if article.image_url is not None:
				self.image_url = article.image_url
				break

	def small_topic(self):
		return {
			'id': self.id,
			'title': self.title,
			'summary': self.summary,
			'image_url': self.image_url
		}

	def large_topic(self):
		return {
			'id': self.id,
			'title': self.title,
			'summary': self.summary,
			'image_url': self.image_url,
			'articles': list(map(lambda x: x.large_article(), self.articles))
		}
