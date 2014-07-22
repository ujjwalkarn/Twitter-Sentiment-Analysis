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
	
    
    
    
 
    tc=0
    sums={}
    new=open(sys.argv[1])
    for line in new:
        data=json.loads(line)
	
        
        if "text" in data:
	    l=data["text"]
            l2=l.encode('ascii','ignore')
            
            ter=l2.split(" ")
            #print(ter)
            for a in ter:
                tc=tc+1
               
    #print tc
    new2=open(sys.argv[1])
    for line2 in new2:
        data2=json.loads(line2)
	
        
        if "text" in data2:
	    l2=data2["text"]
            l3=l2.encode('ascii','ignore')
            count=1
            te=l3.split(" ")
            #print(te)
            for b in te:
                #print b
                if b in sums:
        	    sums[b] += 1
                else:    
                    sums.update({b:count})
   
    for b,count in sums.items():
        n=float(count)/tc
        k= str(b)+"  "+str(n)
        words=k.split()
        print words[0]+"\t"+words[1]
	   








            
            
                 


    
                
    
    

    
	

if __name__ == '__main__':
    main()
	
