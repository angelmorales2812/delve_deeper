from django.db import models

class catch_phishing(models.Model):
	assumed_phishing = models.URLField()
	validate = models.BooleanField(initial=False)
	validate_user = models.ForeignKey(user)

class phishing_report():
	url = models.URLField()
	screenshot = models.ImageField(upload_to='screentshot/', blank=True)
	submitted_by = models.ForeignKey(user)
	whois = models.CharField()

class entities():
	organization = models.CharField(max_length=100)
