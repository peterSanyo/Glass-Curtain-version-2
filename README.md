# Glass-Curtain-version-2
Final Hand-in, Assessment.
Foundations of Web Development 2023, CODE University Berlin
by Péter Sanyó, 26th April 2023

Tech stack
Front end: HTML (Jinja2), CSS, Javascript 
Back end: Python, Flask
Database Framework: SQLAlchemy
Deployed on: render.com
Database hosted separately: POSTGRESQL

OVERALL IDEA:
This application depicts an auction gallery where 4 objects get to be curated over a time period of 2 weeks.
Every two weeks the objects get exchanged and create a new temporary exhibition.
Visitors of the gallery can place bids anonymously on objects which are collected in the database and are accessable by the page admin (api).
The 5 highest bids (including letters from the bidders) are collected and will be then manually forwarded to the offerers.
That is also the point where the rsponsibility of the platform admins ends.
Payment methods and transportations logistics is to be comunicated between offerer and accepted bidder directly.

ADMIN-SIDE:
The idea was to make it easy for the operating person to exchange the objects so that every 2 weeks the gallery is exhibiting a new selection of pieces. 
Users can place bids, and they will be shown in a sorted maner and can be accessed with the api key. 
From there the 3 biggest bids are forwarded to the manufacturer. 
Payment, shipping etc are to be discussed directly once the manufacturer decides which bid to accept. 
Bids are only accepted when all values are entered. 

AESTHETICS / EXPERIENCE:
The App is meant to look engaging and work on laptop-size, bigger screens, bigger TV-Screens as well as on mobilels equally well. 
Touch gestures and mouseclick events are both considered in the JavaScript functionality (although with different sliding sensitivities).  
Since the project is meant to be a digital gallery I tried to make it visually appealing. 
Screens should be watchable and interesting for a longer period of time, therefore I added the slow background animation, to make it breathe. 
Displayed contetn is never 100% but rather displayed with an opacity up to 0.9 to make it blend in with the animation and the colours.
The paralax effect which results from the image position scrolling into the opposite direction to the image container should also add a small twist to the experience. The smaller the screen is the better you see it, since the frames shouldn't exceed the format of the ratio of the pictures.
The HTML Tags are all set to draggable=false to make the drag function work more fluently.

Deployment:
For deployment porpusses I needed to install an older version of python-dotenv and use psycopg2-binary instead of psycopg2 to make it work. 
Also had to use python-dotenv Version 0.21.1 , since render.com didn't seem to support newer versions. 


FUNCTIONALITIES:
Names above the image-slides are clickable linkst to get to the specific product pages. 
The product page urls are rendered dynamically by referring to the piece IDs which are also accessed in the form-picker. 
The Bid-Form needs to be filled out entirely, otherwise the bid is not accepted. 
Same goes for the Objects if wanted to be exchanged, since it is meant to be updated every two weeks only, every value needs to be filled out to make the app dynamically generate the side from the database. NONE-Objects are caught by if-statement in the HTML-Form and not to be displayed to further secure a smooth Exhibition Reset. 

Comments, hints and tips for better solutions and approaches are appreciated and will be considered.


https://user-images.githubusercontent.com/125472114/234611650-92958c70-bbb8-4525-8184-fad185954043.mov



https://user-images.githubusercontent.com/125472114/234611747-0f955294-12fe-4f33-bf0c-535caaa3ca40.mov



https://user-images.githubusercontent.com/125472114/234611772-83967454-a6da-42a9-b41b-80a71aaafa0d.mov

