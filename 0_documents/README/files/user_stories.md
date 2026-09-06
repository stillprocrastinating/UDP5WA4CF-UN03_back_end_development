# User stories

| # | Description | Goal(s) |
|-|-|-|
| 1 | As an admin, I want edit functionality for test questions. | Build a `Question()` class to model CRUD functions for admins. |
| 2 | As a tester, I want edit functionality for tests I host. | Build a `Test()` class to model CRUD functions.<br>Utilise `django.allauth` to manage login capabilities for `Test()`. |
| 3 | As a tester, I want edit functionality for test answers of my students. | Build an `Answer()` class to model CRUD functions.<br>Utilise `django.allauth` to manage login capabilities for `Answer()`. |
| 4 | As a student, I want to be able to prepare for which questions may occur on the test. | Utilise `django.allauth` to manage login capabilities, disallowed to students, to allow students to see the questions in their entirety, without providing the answers. |
| 5 | As a tester, I want to be able to see which questions are more difficult than others. | Build a `calculateDifficultyQuestion()` function which classifies `Question()` based on the frequency of correct `Answer()`. |
| 6 | As a tester, I want to be able to tell the difference between a question being difficult because it is difficult or because I am teaching it poorly. | Build a `calculateWarningQuestion()` function which classifies `Question()` based on the frequency of specific incorrect `Answer()`. |
| 7 | As a tester, I want to be able to see which tests were more difficult than others. | Build a `calculateDifficultyTest()` function which pulls from `calculateDifficultyQuestion()` per `Test()`. |


## Progress

delete - :white_square_button: -> :ballot_box_with_check:

| Complete | # | Goal |
|-|-|-|
| :ballot_box_with_check: | 1.1 | Build a `Question()` class to model CRUD functions for admins. |
| :ballot_box_with_check: | 2.1 | Build a `Test()` class to model CRUD functions. |
| :ballot_box_with_check: | 2.2 | Utilise `django.allauth` to manage login capabilities for `Test()`. |
| :ballot_box_with_check: | 3.1 | Build an `Answer()` class to model CRUD functions. |
| :ballot_box_with_check: | 3.2 | Utilise `django.allauth` to manage login capabilities for `Answer()`. |
| :ballot_box_with_check: | 4.1 | Utilise `django.allauth` to manage login capabilities, disallowed to students, to allow students to see the questions in their entirety, without providing the answers. |
| :white_square_button: | 5.1 | Build a `calculateDifficultyQuestion()` function which classifies `Question()` based on the frequency of correct `Answer()`. |
| :ballot_box_with_check: | 6.1 | Build a `calculateWarningQuestion()` function which classifies `Question()` based on the frequency of specific incorrect `Answer()`. |
| :white_square_button: | 7.1 | Build a `calculateDifficultyTest()` function which pulls from `calculateDifficultyQuestion()` per `Test()`. |
