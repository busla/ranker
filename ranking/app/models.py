from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    
    def filename(self):
        return os.path.basename(self.photo.name)

    def __str__(self):
        return self.filename()

class ResultsManager(models.Manager):
    def points(self):        
        total = 0
        results = Results.objects.all()
        for result in results:               
            for score in result.tournament.score_system.all():
                if result.category == score.category:
                    for point in score.score.all():                        
                        if result.score == point.place:
                            total += point.points

        return total
    
class Athlete(models.Model):
    name = models.CharField(max_length=255)    
    ssn = models.CharField(max_length=255, blank=True, null=True)
    #slug = AutoSlugField(populate_from='title')
    avatar = models.ForeignKey(Image, blank=True, null=True)
    """
    def _points(self):        
        total = 0
        for result in self.results_set.prefetch_related('tournament__score_system'):               
            for score in result.tournament.score_system.all():
                if result.category == score.category:
                    for point in score.score.all():                        
                        if result.score == point.place:
                            total += point.points

        return total
    points = property(_points)
    """
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

    #total = ResultsManager()

    def __str__(self):
        return self.athlete.name + ' - ' + str(self.score)+'. sæti' + ' - ' + self.category.title + ' - ' + self.tournament.title

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        ordering = ['athlete']        