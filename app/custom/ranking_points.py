class RankingPoints(object):
    
    def __init__(self, result):
        """Return a new RankingPoints object."""
        self.result = result
        self.record = {}

    
    def athlete(self):
        return self.result.athlete.name

    def tournament(self):
        return self.result.tournament.title

    def category(self):
        return self.result.category

    def date(self):
        return self.result.tournament.date

    def extras(self):
        items = []
        for attr in self.result.attribute_set.all():
            items.append({'tag': attr.tags.names()[0], 'value': attr.value })
        return items

    def score_systems(self):
        return self.result.tournament.score_system.all()

    def calc(self, attribute, reward, score):
        record = {}

        
        if 'victories' == attribute['tag']:                  
            record['victories'] = {
                'victories': attribute['value'],                
                'points': reward.points * attribute['value'] * score.scale
            }

            
            
        if 'place' == attribute['tag']: 
            
            if attribute['value'] == reward.place:

                record['reward'] = {
                    'reward': attribute['value'], 
                    'points': reward.points * attribute['value'] * score.scale
                }


        return record

    def values(self):  
        record = [] 
        record_dict = {}

        for score in self.score_systems():

            if self.category() == score.category:
                for reward in score.score.all():

                    extras = self.extras()

                    for attribute in extras:
                        
                        if attribute['tag'] in reward.tags.names():
                            #print(attribute['tag'], reward.tags.names())
                            #tags = set(attribute.tags.names())
                            record.append(self.calc(attribute, reward, score))


        return record

    def points(self):

        return {

            'attributes': self.values(),            
            #'pointsTotal': points['victories']['total'] + points['reward']['total'],
        }

