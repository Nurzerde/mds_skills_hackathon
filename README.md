## Description

**dff-religion-skill** is a dff-based service that allows to provide context-related information based on 
the religious textbooks of Christianity and Islam. 

The DFF scheme is as follows: 
Greetings Node -> [Option 1] Choose source and topic, based on it the algorithm will output phrase for the holy books
-> [Option 2] Algorithm will randomly choose both source and the phrase.

The goal is to show that the texts are conceptually similar. 

Example of the dialogue:

You: hi

hi -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.008s memory = 83.69064331054688)

You: topical

topical -> Name the Holy Book: Bible or Quran to get sample from.
exec time = 0.009s memory = 83.69064331054688)

You: bible

bible -> Name the topic
exec time = 0.009s memory = 83.6639404296875)

You: adam

adam -> [': Yea, they made their hearts as an adamant stone, lest they should hear the law, and the words which the LORD of hosts hath sent in his spirit by the former prophets: therefore came a great wrath from the LORD of hosts.']
exec time = 0.196s memory = 83.6639404296875)

You: adam

adam -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.009s memory = 83.6639404296875)

You: topical

topical -> Name the Holy Book: Bible or Quran to get sample from.
exec time = 0.013s memory = 83.6639404296875)

You: quran

quran -> Name the topic
exec time = 0.008s memory = 83.6639404296875)

You: adam

adam -> No such phrase
exec time = 0.076s memory = 83.6639404296875)

You: f
f -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.007s memory = 83.6639404296875)
You: topical

topical -> Name the Holy Book: Bible or Quran to get sample from.
exec time = 0.009s memory = 83.6639404296875)

You: quran

quran -> Name the topic
exec time = 0.009s memory = 83.6639404296875)

You: angel
angel -> ['He sendeth down the angels with the Spirit of His command unto whom He will of His bondmen, [saying]: Warn mankind that there is no God save Me, so keep your duty unto Me.']
exec time = 0.082s memory = 83.6181640625)

You:  
 -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.009s memory = 83.6181640625)

You: random

random -> ['Bible', ': And it shall be, that the firstborn which she beareth shall succeed in the name of his brother which is dead, that his name be not put out of Israel.']
exec time = 0.007s memory = 83.6181640625)

You:
 -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.008s memory = 83.6181640625)

You: random
random -> ['Bible', ': And Ishmael the son of Nethaniah went forth from Mizpah to meet them, weeping all along as he went: and it came to pass, as he met them, he said unto them, Come to Gedaliah the son of Ahikam.']

exec time = 0.007s memory = 83.6181640625)

You:
 -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.010s memory = 83.6181640625)

You: random

random -> ['Bible', ': When thou goest, thy steps shall not be straitened; and when thou runnest, thou shalt not stumble.']
exec time = 0.007s memory = 83.6181640625)

You:
 -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.009s memory = 83.6181640625)

You: random
random -> ['Bible', ': But when he was strong, his heart was lifted up to his destruction: for he transgressed against the LORD his God, and went into the temple of the LORD to burn incense upon the altar of incense.']
exec time = 0.010s memory = 83.6181640625)

You:
 -> Greetings, do you want TOPICAL PHRASE from specific source or both random source and the phrase?
exec time = 0.008s memory = 83.6181640625)

You: random
random -> ['Bible', ': And Leah said, God hath given me my hire, because I have given my maiden to my husband: and she called his name Issachar.']
exec time = 0.007s memory = 83.6181640625)



## Quickstart

```bash
pip install -r requirements.txt
```
Run interactive mode
```bash
python run_int.py
```
Run tests
```bash
python run_test.py
```
## Resources

* Execution time: 0.08 ms
* Starting time: 0.1 sec
* RAM:  83.69 MB


