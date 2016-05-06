
twitment: Twitter Sentiment Analysis
====================================

Twitment is a console application programmed in python and it's used as twitter sentient analysis tool.
This document gives you a quick overview of:

 * General structure of the program
 * Features of the application 
 * How to install and use it.

###1.Project Structure:



###2. Features of the application:

* Use the Twitter API to fetch tweets

* Perform a word-frequency analysis

* Perform sentiment analysis using the Alchemy API

* Send SMS to mobile number



###3. Installing

To install the required packages use the following command: 

``` 
		$ pip install -r /path/to/requirements.txt
```	

In particular, this program requires you to have the following libraries:


* Africa is Talking API
* Alchemy Sentiment Analysis API


###4. Running the Program

The program can be run in the following way:
Use the following test cases

* Ma3Route
* masaku

* Command Line method:
	
	```python manage.py -i ``` 

	```(manage) search <twitter name> ```
    
    ```(manage) send <mobile number> ```


###5. Using the program

The correct way to use this program is as follows:

* Install all requirements from requirements.txt file

* cd to the project folder and run ``` manage.py``` file

* Make sure SMS and sentiment analysis API are in the folders.

If you get a ```key error``` it might be API registration issues

* First register with Alchemy 
* API, get the key,
* Navigate to where Alchemyapi.py is and run

```  Alchemyapi.py <name of your key> ```


======================================================================================
