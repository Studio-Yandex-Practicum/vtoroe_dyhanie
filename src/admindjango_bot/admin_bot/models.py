from django.db import models


class AboutFundKeyboards(models.Model):
    keyboard_name = models.CharField(unique=False, max_length=100)
    keyboard_text = models.CharField(max_length=100)

    class Meta:
        db_table = "about_fund_keyboards"
