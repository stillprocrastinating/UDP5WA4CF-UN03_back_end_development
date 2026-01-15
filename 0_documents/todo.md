# Features
1. Logins for all examiners.
1. Ability to compare stats.
1. Graphs?
1. Traffic light (?) highlighting system for questions which score lower than difficulty --> could indicate teaching issues.
1. Form (each question type) --> update database.
1. Question mark icons which deliver instructions.


# TODO
1. Whenever a package is installed, use `pip freeze > requirements.txt`.
1. Use CSS classes for each "traffic light" difficulty & understanding and utilise django conditioning to activate them (text colours for stated calculated numbers).
1. Use different CSS classes for each "traffic light" validity... django conditioning... (text-decoration: underline; text-transform: uppercase OR icons of coloured flags OR border-color).


## To ask KD
1. What, if any, logo(s)/colour schemes to use?
    - Zebrafish - as in on Moodle.
    - UCL - I assume not, but thought I should check.
    - Home Office - regarding ASPeL PiL process.
    - Royal Society of Biology - regarding accreditation.
    - Colours - use https://webaim.org/resources/contrastchecker/.  
1. Which features are essential at presentation (as opposed to "would be nice", which can be implemented later on)?
    - Logins.
    - [ADMIN only] Form to create database of test questions (aka, the question pool).
    - Form to create database of test dates (aka, the questions selected for each test participants took).
    - Form to create database of participant answers.
    - Display of test questions (preferably with "traffic light" indication of question difficulty/validity).
    - Display of test dates (preferably with "traffic light" indication of test difficulty/validity).
    - Display of participant answers (preferably with "traffic light" indication of learning objectives understanding & question difficulty). Unsure if wise to go this deep regarding data protection - could stop at specific test question level with percentage success, still with LO understanding & Q difficulty.
1. Check parameters for "traffic light" systems.
    - Difficulty & understanding: "Green" = >75% succeed, "Amber" = >50% succeed, "Red" = <50% succeed.
    - Validity: "Green"/default text = no concern... Tried to identify difference from difficulty but not sure.
1. Which layout is preferred?  
    - Logo top left.
    - Navigation bar across top.
    - Footer contains links to examiners? accreditors? ASPeL?
    - Login page includes "sign-up" button (once implemented).
    - [Non-essential, implement later] Login sign-up page requires examiner ID of some description.
    - [Non-essential, implement later] Examiners list page contains contacts and links to course sign-up.
    - Test details are always a list until only a specific test question has been selected.
    - Specific test question pages show percentage data over time.