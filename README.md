# Morse-Code

## Morse Code is a method of transmitting natural langauge text originally developed for telegraph communication.

## Valid Morse Code Criteria:

### 1) The Morse Code sequences can be of any length but with the minimum length of 1.

### 2) The Morse Code sequence can only contain '0', '1' or '*' - as the delimeter.

### 3) The Morse Code can contain as many sentences, provided:
###   - Every sentence MUST end with either ',' , '.' or a '?' else should be deemed Invalid.
###   - Each sentence is delimited with ','.
###   - a letter is delimited with ' * ' and a word with '***'.

## Implementation:

## 1.1: Building Morse code decoder class:

### Here, decoder class is created to accept the morse code encoded sequence and decodes sentences, words and full sentence. I have implemented the code into 3-levels.
###   Level-1: decodes individual sentences.
###   Level-2 decodes individual words 
###   Level-3 decodes individual characters.

## 1.2: Building character analyzer class:

### Here, character analyzer will give the count of each character in the decoded sentence. A method is used to remove punctuation from the sequence. Finally, the decoded characters are stored in dictionary and presented in ‘for’ loop.

## 1.3: Building word analyzer class:

### Here, word analyzer will give the count of each word in the decoded sentence. A method is used to remove punctuation from the sequence. Finally, the decoded words are stored in dictionary and presented in ‘for’ loop.

## 1.4: Building sentence analyzer class:
### Here, sentence analyzer will give the count of each sentence punctuation in the decoded sentence. A method is used to remove word from the sequence to identify the punctuations. Finally, the output is stored in dictionary and presented in ‘for’ loop.

## 1.5: Main method:
### Here, objects for each classes is created and called appropriately. A method (valid_seq) is used to validate the input sequence.  A menu option is given to user to select which analysis is required. Finally, exception is implemented to catch if any.

## OutPut:

### 1) The Morse Code sequences can be of any length but with the minimum length of 1.

![1](https://user-images.githubusercontent.com/42957613/97344142-60a90d80-18ae-11eb-9ba7-0ba0cb662f31.PNG)


###  2) The Morse Code sequence can only contain '0', '1' or '*' - as the delimeter.

![2](https://user-images.githubusercontent.com/42957613/97344317-9817ba00-18ae-11eb-96cf-b6cd83f0f378.PNG)


### 3) Every sentence MUST end with either ',' , '.' or a '?' else should be deemed Invalid.

![3](https://user-images.githubusercontent.com/42957613/97344426-c0071d80-18ae-11eb-9fee-b41977965f1d.PNG)

### Once all the above criterias are met, below is the screenshot of using all the classes created:

![final](https://user-images.githubusercontent.com/42957613/97344486-d2815700-18ae-11eb-8ebc-528ab50fa8bf.PNG)



