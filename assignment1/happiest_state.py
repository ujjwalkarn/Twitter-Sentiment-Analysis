import sys
import json
from pprint import pprint
import operator

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
    
    
                
    d={}     
    new = open(sys.argv[2])
    for line in new:
        data=json.loads(line)
	#pri(data)
        sum=0 
          
        #print sum
        if "place" in data:
            if (sum==0):
	        #l=data["place"]
                #print 5
                if (sum==0):
                    fn=data["place"]
                    #print fn
		    if (fn!=None):
		        
                        #print fn
                        
			cc=fn["country_code"]
			if (cc=="US"):
                            funa=fn["full_name"]
                            #print funa 
            	            ters=funa.split(", ")
                            #print ters[1]
                            t=ters[1]



                            sum=0
        	    	    if "text" in data:
	                        l5=data["text"]
                            	l2=l5.encode('ascii','ignore')
            
                            	ter=l2.split(" ")
              
                            	for a in ter:
                
                                    if a in scores:
                                        sum=sum+scores.get(a)
            	    
            	    
           	            #print sum, t 
                            
			    if t in d:
				#print "yuyiu"
				#print t
			        d[t]=(float(d[t])+sum)/2
                            else:
				
				d.update({t:sum})    
                                #print t  
				#print d           

    #print "f"
    #for t in d.items():
	#print t, sum
        #print "foo"
    print max(d.iteritems(), key=operator.itemgetter(1))[0]

    
	

if __name__ == '__main__':
    main()
	
