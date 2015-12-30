# RANKER

RANKER is a ranking list web app for Taekwondo clubs. It displays ranking-lists for each category added and a link to the athlete profile. It´s a custom project for one club but most of the custom stuff has been abstracted away to make it as general as possible. The project is rough around the edges and I don´t plan on continuing the development. Unless someone hires me to do so :-)

Demo: http://styrkleikalisti.armanntkd.com

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
1. Install python3
2. mkdir ~/my-ranking-list && cd my-ranking-list
3. pyvenv-3.x venv
4. Clone this repo
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver


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

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to http://unlicense.org
