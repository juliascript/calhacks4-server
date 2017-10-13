
class Article:

	def __init__(self, article_dict):
		self.title = article_dict.get('title', '')
		self.date = article_dict.get('date', '')
		self.desc_text = article_dict.get('desc_text', '')
		self.full_text = article_dict.get('full_text', '')
		self.image_url = article_dict.get('image_url', None)
		self.source = article_dict.get('source', None)
		self.source_url = article_dict.get('source_url', None)
		self.tags = article_dict.get('tags', [])
		self.refs = article_dict.get('refs', [])

	def large_article(self):
		return self.__dict__
