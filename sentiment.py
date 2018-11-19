import csv
from textblob import TextBlob

infile = 'data.csv'

with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[0]
        blob = TextBlob(sentence)
        print sentence
        print "Sentiment: "+ str(blob.sentiment.polarity) +"  Subjectivity: " +str(blob.sentiment.subjectivity)
        print "======================================================"
