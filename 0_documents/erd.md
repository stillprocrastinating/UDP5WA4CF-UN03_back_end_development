# Entity Relationship Diagram


## Questions

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
||learning_objective|IntegerField(choices)|
||type|IntegerField(choices)|
||number|IntegerField()|
|TBC|question|TextField()|
|TBC|image|CloudinaryField('image')|
||sub_number|IntegerField()|
||sub_answer_number_individual|IntegerField()|
||sub_correct_answer_individual|IntegerField()|
|ForeignKey|author|User, related_name="question_author"|
||warning|IntegerField(choices)|


## Tests

|Key|Name|Type|
|-|-|-|
|PrimaryKey|id|CharField(20)|
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
