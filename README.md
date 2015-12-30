# RANKER

RANKER is a ranking list web app for Taekwondo clubs. The club administrator can configure categories and score-systems to calculate athlete points based on his results in any category.

## Categories
The app displays ranking lists for each category that is added. A category can be whatever, sparring, poomsae, training-camp, et.c. You can add whatever you want.

An example of categories for a Taekwondo club might look like this:

**Points given for results in these tournament categories:**

Sparring

Forms - individual

Forms - pair

Forms - groups

Best Player

Training camp

National Team Member

.... whatever.


## Base Score

Base-scores can be set for the system as a whole. An example of a base-scores might look like this:


1st place: 7 points

2st place: 3 points

3st place: 1 point

Participation: 1 point

Best player: 1 point

sparring-matches-won: 1 point

poomsae-opponents-won: 1 point

National team member: 7 points



## Score-systems
Since tournaments can usually be categorized (local tournament, National Cup, National Championships, European Championships, World Championships, et.c) a score-system can be created for each tournament type.

An example of a score-system for the National Championships might look like this:


Category: sparring

Score: 1st, 2nd, 3rd

Scale: 10 


Now we can see why we added base-score before. Scores are selected from available base-scores and then multiplied by 10. So in the National Championships the gold medalist will receive 7 * 10 points since that particular tournament should weigh more than a small local tournament.

## Event
An event can be whatever but typically these are tournaments unless the club admin want´s to reward athletes for participating in other events too.


An example of a tournament might look like this:

Title: National Championships - 2015

Date: 01.01.2015

Score-system: A-Tournament (sparring, forms, forms-individual, forms-pairs, forms-group)

Results: 

    Athlete: Bill Hicks
    
    Category: sparring
    
    attributes
        Place: 1
        Sparring matches won: 6
    ------------------
    
    Athlete: Vandana Shiva
    
    Place: 3
    
    Category: forms-individual
    
    Attributes
        Place: 1
        Poomsae opponents won: 3    

For this tournament the relevant score-systems are selected. These score-systems already have everything set up to calculate the points for each athlete. If you defined custom attributes in the app, you will be able to select them when adding results.

To add results, you select an athlete, add result and category.


## Installation
Install python3
mkdir ~/my-ranking-list && cd my-ranking-list
pyvenv-3.x venv
Clone this repo
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license
