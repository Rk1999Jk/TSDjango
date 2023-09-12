from django.db import models

# Create your models here.




class DataTable(models.Model):
    user_id = models.IntegerField()
    news_article_id = models.IntegerField()
    s1_cnn_original=models.FloatField()
    s1_adam=models.FloatField()
    s1_xsum=models.FloatField()
    s2_cnn_original=models.FloatField()
    s2_adam=models.FloatField()
    s2_xsum=models.FloatField()
    s3_cnn_original=models.FloatField()
    s3_adam=models.FloatField()
    s3_xsum=models.FloatField()
    s4_cnn_original=models.FloatField()
    s4_adam=models.FloatField()
    s4_xsum=models.FloatField()
    cnn_original_rank=models.IntegerField()
    xsum_rank=models.IntegerField()
    adam_rank=models.IntegerField()


