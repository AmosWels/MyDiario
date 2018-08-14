## My Diary 
MyDiary is an online journal where users can pen down their thoughts and feelings.

[![Build Status](https://travis-ci.org/AmosWels/My-Diary.svg?branch=database)](https://travis-ci.org/AmosWels/My-Diary)


<a href="https://codeclimate.com/github/AmosWels/My-Diary/maintainability"><img src="https://api.codeclimate.com/v1/badges/911827d24f11c39cdf13/maintainability" /></a>

#### [View coveralls Badge](https://coveralls.io/repos/github/AmosWels/My-Diary/badge.svg?branch=database)


#### [Visit my diario Documentation](https://mydiario.docs.apiary.io/#introduction/mydiario-requests-collection/get-all-users-entries-[get/entries])

#### [Visit my diario at gh-pages](https://amoswels.github.io/My-Diary/UI/)

#### Required Features
1. Create user accounts that can signin/signout from the app. 
2. Get all diary entries for a particular user.
3. Get a specific diary entry for a particular user.
4. Add an entry
5. Modify an entry.

#### Endpoints

POST /auth/signup
Register a user

POST /auth/login
Login a user

GET /entries 
Fetch all the entries for a user.

GET /entries/<entryId>
Fetch the details of an entry for a user

POST /entries
Add an entry

PUT /entries/<entryId>
Modify a diary entry
An entry can only be modified on the same day it was created.


##### Requirements
Requiremets to run this My Diary

1. Flask <framework>
2. git
3. python3
4. pip
