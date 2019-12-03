# ACCESSIBLITY INDEX

## An application that displays the degree of accessiblity of a geographic location and displays that information on an interactive map. The 'Wikipedia' of accessiblity info.##

## Problem: 
Not all businesses, public buildings, and spaces are accessible to people with phyiscal disablilities. Newer public buildings are often extremely accessble while older buildings are less so. It is often very difficult to tell, without going in person, exactly how accessible a place is. The ADA law is not always followed very strictly and places can often only have minor inconveniences that would qualify them as 'not accessible' when in reality, they are open to many people with minor impairments.

## User Stories

Users will be able to enter the physical address of a place and create a document specific to that place. This document will contain a standard key-value pairs that can be used to determing the degree of accessiblity.

Keys that can be chose might include: 
    Approach: no barrier, ramp, steps, incline, decline
    Main Entrance: No barrier, one step, multiple steps, ramp
    Secondary Entrance: No barrier, one step, multiple steps, ramp
    Main Passages: No barrier, one step, multiple steps, ramp, split-level
    Bathroom: no barrier, steps, big stall, small stalls, door won't shut
    Bedroom: no barrier, can access bed, no access
    Overall rating?
    Additional Notes

Place documents will appear on Google Maps through lat-long provided by Google geotracker API. Also use Google Maps API for map.

Place documents will be viewable by all users and can be edited wiki-style.

Markers on map are clickable and are used to access access info on that site.

Only registered users can create and edit documents, but the information is available without an account.

## Milestones
1. create basic Flask/Python routes and models for users, places, and accessibility
2. Get google maps to render on React
3. Create forms to enter user registration, places, and accessibilbity and get those stored on DB
4. Get markers to populate on map for each place in DB
5. When markers are clicked, accessibility info appears on card
6. Create User profile that shows all places added by user

# Stretch Goals
Get address by phone's location, automatically

Use different criteria based on the type of place: small business, big store, office building, school, restaurant, park, recreational spaces, museums.

Expand to specifically private residences on AirBnB and VRBO
