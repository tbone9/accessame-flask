# Accessame

## Live App
[Accessame](https://accessame-react.herokuapp.com/)

## An application that displays the degree of accessiblity of a geographic location and displays that information on an interactive map. The 'Wikipedia' of accessiblity info.

## Problem: 
Not all businesses, public buildings, and spaces are accessible to people with phyiscal disablilities. Newer public buildings are often extremely accessble while older buildings are less so. It is often very difficult to tell, without going in person, exactly how accessible a place is. The ADA law is not always followed very strictly and places can often only have minor inconveniences that would qualify them as 'not accessible' when in reality, they are open to many people with minor impairments. This app allows a user to search for places just like they would using google maps. Once the desired place is found, a user can add that place to the map as well as add a rating for how accessible the place is. Other users and visitors to the site can see all places and ratings ever added from all users. 

## User Stories

Users will be able to enter the physical address of a place and create a document specific to that place. This document will contain a standard key-value pairs that can be used to determing the degree of accessiblity.

Ratings might include: 
1. Main Entrance: 1 = no access, 2 = limited access with skill, 3 = no barrier to access
2. Bathroom: 1 = no access, 2 = limited access with skill, 3 = no barrier to access
3. Hallways: 1 = no access, 2 = limited access with skill, 3 = no barrier to access
4. Additional Notes

Place documents will appear on Google Maps through lat-long provided by Google geotracker API. Also use Google Maps API for map.

Place documents will be viewable by all users and can be edited wiki-style.

Markers on map are clickable and are used to access access info on that site.

Only registered users can create and edit documents, but the information is available without an account.

## Technology Used
### Front-End
React

### Back-end
Server: Python/Flask
Database: PostgreSQL

### Third-party API
Google Maps and Places

## Installation Steps to Run React App Locally
1. clone repo: [accessame-react](https://github.com/tbone9/accessame-react)
2. run 'npm install' in terminal
3. run 'npm start' in terminal 

## Installation Steps to Run Server and Database Locally
1. clone repo: [accessame-flask](https://github.com/tbone9/accessame-flask)
2. run 'pip install -r requirements.txt' in terminal
3. run 'source .env/bin/activate' in terminal to start virtual environment
3. run 'python app.py' from virtual environment in terminal 

## Wireframes and Entity Relationships (note: these diagrams were from the app planning stage)

### CRUD Routes
![crud routes](https://i.imgur.com/T6REWGt.png)

### Database Structure
![database structure](https://i.imgur.com/zGwkxiN.png)

### Database Models
![database models](https://i.imgur.com/elxxjco.png)

### React Layout
![React layout](https://i.imgur.com/W31fTOX.png)

## Milestones
1. create basic Flask/Python routes and models for users, places, and accessibility
2. Get google maps to render on React
3. Create forms to enter user registration, places, and accessibilbity and get those stored on DB
4. Get markers to populate on map for each place in DB
5. When markers are clicked, accessibility info appears on card
6. Create User profile that shows all places added by user

## Unresolved Problems
1. Modals and info windows on map don't close when just clicking outside of modals. 
2. Can't add place or rating from within map component. Currently performed from outside component.
3. Deleting user deletes all ratings added by user. I would prefer their ratings persisted.

## Future Features
1. Have an average of all ratings appear on infowindow on map.
2. Add more categories to rate with more options and tailor to specific disabilities.
3. Restyle infowindows on map.
4. Intial center of map is set by current location of user.
5. Organize places added by users in a less cluttered way. 
6. Add date to each rating. 
