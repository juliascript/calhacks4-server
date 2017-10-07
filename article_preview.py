

class ArticlePreview:

	def __init__(self, article):
		"""Init this article preview with an article and pull out needed data"""
		self.title = article.title
		self.date = article.date
		self.image_url = article.image_url
		self.description = (article.description[:140].strip() + '...') if len(article.description) > 140 else article.description
