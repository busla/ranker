from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

class Club(models.Model):
    title = models.CharField(max_length=255)
    site = models.ForeignKey(Site)

    def __str__(self):
        return self.title

class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    
    def filename(self):
        return os.path.basename(self.photo.name)

    def __str__(self):
        return self.filename()

class AttributeItem(models.Model):
    title = models.CharField(max_length=255)
    participation = models.BooleanField(default=False)
    #value = models.FloatField(default=0)

    def __str__(self):
        return self.title
    
class Athlete(models.Model):
    name = models.CharField(max_length=255)    
    ssn = models.CharField(max_length=255, blank=True, null=True)
    club = models.ForeignKey(Club, blank=True, null=True)
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
    #points = models.IntegerField(blank=True, null=True)
    value = models.FloatField(default=0)
    attribute_item = models.ForeignKey('AttributeItem', blank=True, null=True)
    #tags = TaggableManager(blank=True)
    #category = models.ForeignKey(Category, blank=True, null=True) 

        
    def title_rendered(self):
        return self.title + ' ('+str(self.value)+')' if not self.place else str(self.place)+'. place ('+str(self.value)+' points)' 

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

    class Meta:
        verbose_name = "Score System"
        verbose_name_plural = "Score Systems"
        ordering = ['title']        

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
    athlete_club = models.ForeignKey(Club, blank=True, null=True)
    category = models.ForeignKey(Category)
    victories = models.IntegerField(default=0)
    score    = models.IntegerField(default=0)
    #site = models.ForeignKey(Site)

    def save(self, *args, **kwargs):
        #participation_attr = AttributeItem.objects.filter(participation=True)
        
        if self.athlete.club:
            self.athlete_club = self.athlete.club

        super(Results, self).save(*args, **kwargs)
        
        for score in self.tournament.score_system.all():
            if score.category == self.category:
                for reward in score.score.all():            
                    if reward.attribute_item.participation:                    
                        if not self.attribute_set.filter(attribute_item=reward.attribute_item):
                            participation_obj = Attribute.objects.create(result=self, attribute_item=reward.attribute_item, value=1)                            
 
    def attribute_points(self):
        points = {}
        record = []
        for score in self.tournament.score_system.all():
            if self.category == score.category:
                attributes = self.attribute_set.all()
                
                if attributes:                
                    for attribute in attributes:  
                        for reward in score.score.all():
                            #print(reward)
                            if reward.attribute_item.pk == attribute.attribute_item.pk:
                                if reward.place:
                                    if reward.place == attribute.value:

                                        #print('Reward place: %s - Attribute place: %s' % (reward.place, attribute.value))
                                        record.append({
                                            'title': attribute.attribute_item.title,
                                            'id': attribute.attribute_item.id,
                                            'value': attribute.value,
                                            'points': reward.value * attribute.value * score.scale,
                                        })                                
                                
                                else:
                                    record.append({
                                        'title': attribute.attribute_item.title,
                                        'id': attribute.attribute_item.id,
                                        'value': attribute.value,
                                        'points': reward.value * attribute.value * score.scale,
                                    })                

                                #record.update(points)                                
        return record

    def category_points(self):
        points = {}
        reward_list = []

        attributes = self.attribute_set.all()
        if not attributes:
            for score in self.tournament.score_system.all():
                if self.category == score.category:
                    for reward in score.score.all():

                        reward_list.append({
                            'title': reward.title,
                            'id': self.category.id,
                            'value': reward.value,
                            'points': reward.value * score.scale,
                        })

                        #points.update(reward_dict)            
        return reward_list

    def __str__(self):
        return self.athlete.name + ' - ' + str(self.score)+'. place' + ' - ' + self.category.title + ' - ' + self.tournament.title

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        ordering = ['athlete']

class Attribute(models.Model):
    #results = models.ForeignKey('Results', blank=True, null=True)
    #tags = TaggableManager(blank=True)
    
    result = models.ForeignKey('Results', blank=True, null=True)
    attribute_item = models.ForeignKey('AttributeItem', blank=True, null=True)
    #score_item = models.ForeignKey('ScoreItem', blank=True, null=True)
    value = models.FloatField(default=0)

    def __str__(self):
        return self.attribute_item.title                

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    club = models.ManyToManyField(Club, blank=True, related_name='clubs')
