from django.db import models
from django.urls import reverse


# Create your models here.
class jobpost(models.Model):
    
    Titel = models. CharField(max_length=100)
    Description = models.TextField(max_length=400)
    company = models.CharField(max_length=100)
    postes_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    type = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    Rulesresponsibilities = models.CharField(max_length=10000)

    def __str__(self):
        return self.Titel

    def get_absolute_url(self):
        return reverse ("detail",kwargs={'pk' : self.pk})
    

class job(models.Model):
    jobtitle = models.ForeignKey(jobpost,related_name="jobposts",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    phone = models.BigIntegerField()   


    def __str__(self):
        return self.first_name 


class post(models.Model):
    author_name = models.CharField(max_length=100)
    post_type = models.CharField(max_length=100)
    post_title = models.CharField(max_length=100,blank=True)
    sub_title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to="userimage/",blank=True)
    post_time = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(blank=True,null=True)

    def __str__(self):
      return self.author_name    


class comment(models.Model):
    content = models.TextField(max_length=100000)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    post = models.CharField(max_length=100)
    author = models.ForeignKey('post',related_name="author",on_delete=models.CASCADE)


    
    def __str__(self):
      return self.post
