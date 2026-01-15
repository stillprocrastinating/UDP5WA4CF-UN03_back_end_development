# Entity Relationship Diagram


## Questions

|Key|Name|Type|
|-|-|-|
||id|CharField(20)|
||learning_objective|IntegerField(choices)|
||type|IntegerField(choices)|
||number|IntegerField()|
||answer_number|IntegerField()|
||correct_answer|IntegerField()|
||warning|IntegerField(choices)|


## Tests

|Key|Name|Type|
|-|-|-|
||id|CharField(20)|
||date|DateTimeField()|
||type|IntegerField(choices)|
||participant_number|IntegerField()|
|ForeignKey|tester|User, related_name="tester"|


## Answers

|Key|Name|Type|
|-|-|-|
|ForeignKey|question_id|Question, related_name="question_answers"|
|ForeignKey|test_id|Test, related_name="test_amswers"|
||option|IntegerField()|
||correct_option_frequency|IntegerField()|
||incorrect_option_frequency|IntegerField()|
|ForeignKey|tester|User, related_name="tester"|
