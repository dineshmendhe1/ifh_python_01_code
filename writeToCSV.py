import os
import re
import csv
from textblob import TextBlob

#file variable 
infile = 'data.csv'

#opent the text file for writing 
f= open("sentiment_tweets.csv","w+")

# Read tweet file, apply textblob function, write the results to file also do console output.
with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[0]
        blob = TextBlob(sentence)
	if(blob.sentiment.polarity > 0):
		f.write(str(round(blob.sentiment.polarity,2))+","+"POSITIVE"+","+sentence+"\n\n") 
	elif(blob.sentiment.polarity ==0):
		f.write(str(round(blob.sentiment.polarity,2))+","+"NEUTRAL"+","+sentence+"\n\n") 
	else:
		f.write(str(round(blob.sentiment.polarity,2))+","+"NEGATIVE"+","+sentence+"\n\n") 
        print sentence
        print "Sentiment: "+ str(blob.sentiment.polarity) +"  Subjectivity: " +str(blob.sentiment.subjectivity)
        print "======================================================"
f.close()  


