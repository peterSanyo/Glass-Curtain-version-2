# Glass-Curtain-version-2
Hand-in 4/5 , Deployment of an application.
Foundations 2023, CODE University Berlin
by Péter Sanyó, 14th April 2023

Tech stack
Front end:HTML, CSS(responsive), Javascript 
Back end: Python, Flask, Jinja2
Deployed on: render.com
Database hosted separately.

This is the second iteration of my foundations project. 
Project has been redone from scratch since I ran into issues over and over. 
Second version seems more solid and clean to work with until now. 

The idea of this application is of an Auction Gallery where 4 objects get to be curated over a time-period of a week.
The idea was to make it easy for the operating person to exchange the objects so that every 2 weeks the gallery is exhibiting a new selection of pieces. 
Users can place bids, and they will be shown in a sorted maner and can be accessed with the api key. 
From there the 3 biggest bids are forwarded to the manufacturer. 
Payment, shipping etc are to be discussed directly once the manufacturer decides which bid to accept. 
Bids are only accepted when all values are entered. 

The App is meant to look engaging and work on laptop-size, bigger screens, bigger TV-Screens as on mobile as well. Touch gestures and mouseclick events are both considered in this case. 
Mobile differs from browser to browser but works best on chrome and firefox. 
Since it should be some kind of digital gallery I tried to make it visually appealing. For that reason i added the slow background animation so that the page stays interesting for a longer period of time. 
The paralax effect which results from the image position scrolling into the complientary direction to the image container should also add a small twist to the experience. 
The HTML Tags are all set to draggable=false to make the drag fucntion work. 

For deployment porpusses i needed to install an older version of python-dotenv and use psycopg2-binary instead of psycopg2 to make it work. 

This project is a work in progress. 
Work ist still to be done.

Will work further on following topics:
- Accessibility: alternative design-concept, maybe animation-stop toggle, audio description read by manufacturer (?) 
- Fine-tuned mobile version.
- Fine-Tuned Api interface 
- What ways exist to make the application more performant? It seems to be very performance heavy on my laptop, advice is appreciated. 



