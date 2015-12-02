from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

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

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', always_update=True, blank=True)

    def __str__(self):
        return self.title

class ScoreItem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', always_update=True, blank=True)    
    place = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    #category = models.ForeignKey(Category, blank=True, null=True) 

    def title_rendered(self):
        return self.title + ' ('+str(self.points)+')' if not self.place else str(self.place)+'. place ('+str(self.points)+' points)' 

    def __str__(self):
        return self.title_rendered()

    class Meta:
        verbose_name = "Score Item"
        verbose_name_plural = "Score Items"
        ordering = ['place'] 
        

class ScoreSystem(models.Model):
    title = models.CharField(max_length=255)
    score = models.ManyToManyField(ScoreItem, blank=True)
    scale = models.FloatField(default=1)
    category = models.ForeignKey(Category, blank=True, null=True) 
    #tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

class Tournament(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=False)
    #score_system = models.ForeignKey(ScoreSystem, blank=True, null=True)
    score_system = models.ManyToManyField(ScoreSystem, blank=True)

    def rank_system(self):
        rank = [s.title + ' - '+str(s.scale) for s in self.score_system.all()]
        if rank:
            return ' (' + ", ".join(rank) +')'
        else:
            return ''

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-date'] 

class Results(models.Model):
    tournament = models.ForeignKey(Tournament)
    athlete = models.ForeignKey(Athlete)
    category = models.ForeignKey(Category)
    score    = models.IntegerField(default=0)

    def __str__(self):
        return self.athlete.name + ' - ' + str(self.score)+'. place' + ' - ' + self.category.title + ' - ' + self.tournament.title

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        ordering = ['athlete']        