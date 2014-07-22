import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def pri(y):
    print y

    

def main():
	
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)	
    #data=[]
    
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  
        scores[term] = int(score)  

    #print scores.items() 
    
    new=open(sys.argv[2])
    for line in new:
        data=json.loads(line)
	#pri(data)
        sum=0
        if "text" in data:
	    l=data["text"]
            l2=l.encode('ascii','ignore')
            #l3="hi i am ujjwal"
	    #pri(l2)
            #for word in l3:
		#print(word)
            ter=l2.split(" ")
            #print(ter)
            for a in ter:
                #print a
                if a in scores:
                    sum=sum+scores.get(a)
            for a in ter:
                if a not in scores:
                    #print a
                    print a+" "+str(sum)
            
                 


    
                
    
    #l3="hi i am ujjwal"
    #print (l3)
    #word=l3.split(" ")
    #print word
    

    
	

if __name__ == '__main__':
    main()
	
