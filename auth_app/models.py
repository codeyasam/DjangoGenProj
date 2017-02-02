from django.db import models
from django.contrib.auth import backends, get_user_model
from django.db.models import Q
# Create your models here.

class EmailOrUsernameModel(backends.ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			UserModel = get_user_model()
			user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
			if user.check_password(password):
				return user
		except UserModel.DoesNotExist:
			return None
