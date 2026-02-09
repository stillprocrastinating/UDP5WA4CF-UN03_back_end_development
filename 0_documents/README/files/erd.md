# Entity Relationship Diagram


## Modules

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
||number|IntegerField()|
||description|TextField()|


## Objectives

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
|ForeignKey|module|Module, related_name="module_objective"|
||number|IntegerField()|
||description|TextField()|


## Questions

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
|ForeignKey|learning_objective|Objective, related_name="objective_question"|
||type|IntegerField(choices)|
||number|IntegerField()|
||question|TextField()|
|TBC|image|CloudinaryField('image')|
||sub_number|IntegerField()|
||sub_answer_number_individual|IntegerField()|
||sub_correct_answer_individual|IntegerField()|
|ForeignKey|author|User, related_name="question_author"|
||difficulty|IntegerField(choices)|
||warning|IntegerField(choices)|


## Tests

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
||date|DateTimeField()|
||type|IntegerField(choices)|
||participant_number|IntegerField()|
|ForeignKey|tester|User, related_name="tester"|
||difficulty|IntegerField(choices)|


## Answers

|Key|Name|Type|
|-|-|-|
|ForeignKey|question_id|Question, related_name="question_answers"|
|ForeignKey|test_id|Test, related_name="test_amswers"|
||option|IntegerField()|
||correct_option_frequency|IntegerField()|
||incorrect_option_frequency|IntegerField()|
|ForeignKey|tester|User, related_name="tester"|

---


## Entity relationship diagram

Master table columns:
- question_type
- answer_options
- correct_answer
- test_date
- test_type
- participant_number
- correct_choice_frequency
- incorrect_choice_frequency
- [calculation] correct_choice_percentage
- [calculation] incorrect_choice_percentage


### Tables

questions
- id
- learning_objective
- type
- answer_number
- correct_answer

tests
- id
- date
- type
- participant_number

~~participants~~ --> GDPR

answers
- id
- [FK] question_id
- [FK] test_id
- option
- correct_option_frequency
- incorrect_option_frequency

[CTE] flagging
- [questions] learning_objective
- [questions] type
- [answers] option
- [answers] correct_option_frequency
- [answers] incorrect_option_frequency
- [tests] participant_number
- [calculation] correct_option_percentage
- [calculation] incorrect_option_percentage
- [calculation] flag


## URL patterns

1. include('modules.urls')
1. include('objectives.urls')
1. include('questions.urls')
1. include('tests.urls')
1. include('answers.urls')
1. admin.site.urls
1. _include('allauth.urls')_


### questions/urls.py

1. views.QuestionList.as_view()
1. views.AnswerList.as_view()     // dependent on structural availability


### tests/urls.py

1. views.TestList.as_view()
1. views.FlagList.as_view()     // dependent on structural availability & CTE functionality
