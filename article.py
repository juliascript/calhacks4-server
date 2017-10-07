

#  subclass dict instead and change instantiation
class Article(object):

	def __init__(	self, 
					title, 
					date, 
					full_text, 
					short_description, 
					source_title, 
					source_url, 
					tags, 
					image_url, 
					videos,
					reference_urls):
		self.title = title
		self.date = date
		self.full_text = full_text
		self.short_description = short_description
		self.source_title = source_title
		self.source_url = source_url
		self.tags = tags
		self.image_url = image_url
		self.videos = videos 
		self.reference_urls = reference_urls

