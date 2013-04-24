# This file is to be used as a helper for amazon's S3 service 

from storages.backends.s3boto import S3BotoStorage

class StaticRootS3BotoStorage(S3BotoStorage):
	def __init__(self, *args, **kwargs):
		super(StaticRootS3BotoStorage, self).__init__(*args, **kwargs)
		self.location = 'static'

class MediaRootS3BotoStorage(S3BotoStorage):
	def __init__(self, *args, **kwargs):
		super(MediaRootS3BotoStorage, self).__init__(*args, **kwargs)
		self.location = 'media'