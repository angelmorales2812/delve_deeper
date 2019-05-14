from django.db import models

class catch_phishing(models.Model):
	assumed_phishing = models.URLField()
	validate = models.BooleanField(null=True)
	validate_user = models.CharField(max_length=100)

class phishing_report():
	url = models.URLField()
	screenshot = models.ImageField(upload_to='screentshot/', blank=True)
	submitted_by = models.CharField(max_length=100)
	whois = models.CharField()

class entities():
	organization = models.CharField(max_length=100)
