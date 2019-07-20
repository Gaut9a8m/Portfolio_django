from django.db import models
 #it is inheriting model class and object is created as models
class Blog(models.Model):
    title = models.CharField(max_length = 30)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
    
    def __str__(self):
        return self.title
