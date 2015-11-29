from django.db import models
from autoslug import AutoSlugField

class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    
    def filename(self):
        return os.path.basename(self.photo.name)

    def __str__(self):
        return self.filename()
    
class Athlete(models.Model):
    name = models.CharField(max_length=255)    
    ssn = models.CharField(max_length=255, blank=True, null=True)
    #slug = AutoSlugField(populate_from='title')
    avatar = models.ForeignKey(Image, blank=True, null=True)
  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Athlete"
        verbose_name_plural = "Athletes"
        ordering = ['name']

class ScoreItem(models.Model):
    place = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.place)+'. sæti ('+str(self.points)+' stig)'

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', always_update=True, blank=True)

    def __str__(self):
        return self.title

class ScoreSystem(models.Model):
    title = models.CharField(max_length=255)
    score = models.ManyToManyField(ScoreItem, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True) 

    def __str__(self):
        return self.title

class Tournament(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=False)
    #score_system = models.ForeignKey(ScoreSystem, blank=True, null=True)
    score_system = models.ManyToManyField(ScoreSystem, blank=True)


    def __str__(self):
        return self.title

class Results(models.Model):
    tournament = models.ForeignKey(Tournament)
    athlete = models.ForeignKey(Athlete)
    category = models.ForeignKey(Category)
    score    = models.IntegerField(default=0)

    def __str__(self):
        return self.athlete.name + ' - ' + str(self.score)+'. sæti' + ' - ' + self.category.title + ' - ' + self.tournament.title

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        ordering = ['athlete']        