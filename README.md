# RANKER

Ranker is a ranking list web app, originally written for Taekwondo clubs, to manage ranking lists for any type of sport. The club administrator can configure categories and score-systems to calculate athlete points based on his results in any category.

## Categories
The app displays ranking lists for each category that is added. If the club also wants to give points for something else e.g. for participating in a tournament, then a participation category is also added.

An example of categories for a Taekwondo club might look like this:


**Points given for results in these tournament categories:**

Sparring

Forms - individual

Forms - pair

Forms - groups


**Points given for other categories:**

Participation

Tournament best player

Training camp

National Team member (forms)

National Team member (sparring)



For each category a base-score can be set. An example of a base-score for the Sparring category might look like this:

Category: sparring

1st place: 6 points

2st place: 4 points

3st place: 2 points


Category: participation

1 point

The reason for this abstraction is to be able to scale these points later when we create a score-system for a particular tournament.

## Score-systems
Score-systems are added for each category and each type of tournament. Since tournaments can usually be categorized (local tournament, National Cup, National Championships, European Championships, World Championships, et.c) a score-system will be created for each tournament type (not to be confused with categories above).

An example of a score-system for the National Championships might look like this:


Category: sparring

Score: 1st, 2nd, 3rd

Scale: 10 


Now we can see why we added base-score before. Scores are selected from available base-scores and then multiplied by 10. So in the National Championships the gold medalist will receive 6 * 10 points since that particular tournament should weigh more than a small local tournament.

## Event
An event can be whatever but typically these are tournaments unless the club admin want´s to reward athletes for participating in other events too.


An example of a tournament might look like this:

Title: National Championships - 2015

Date: 01.01.2015

Score-system: national-tournament (sparring, forms, forms-individual, forms-pairs, forms-group)

Results: 

    Athlete: Bill Hicks
    
    Place: 1
    
    Category: sparring
    
    ------------------
    
    Athlete: Vandana Shiva
    
    Place: 3
    
    Category: forms-individual
    

For this tournament the relevant score-systems are selected. These score-systems already have everything set up to calculate the points for each athlete.

To add results, you select an athlete, add result and category.


## Installation

todo

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
