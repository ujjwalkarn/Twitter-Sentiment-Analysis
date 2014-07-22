import sys
import json
import operator
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))



    

def main():
	
   
    
    
    dic={}
    count=1
    new=open(sys.argv[1])
    for line in new:
        data=json.loads(line)
	
        sum=0
        if "entities" in data:
	    l=data["entities"]
            #l2=l.encode('ascii','ignore')

	    ht=l["hashtags"]
            
            #ter=l2.split(" ")
            #print(ter)
            
            #print ht 
	        
            for d in ht:
		
                ht3=d["text"] 
            	#print ht2 
     	        ht2=ht3.encode('ascii','ignore')
	        if ht2 in dic:
	            dic[ht2]+=1
                else:
		    dic.update({ht2:count})

    #for ht2,count in dic.items():
        
     #   print str(ht2)+"\t"+str(count)
    #del dic["_"]
    #del dic["__"]
    #del dic["___"]
    #del dic[""]
    sorts = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)
    #s=sorts
    #print sorts
    i=0
    for k in sorts:
        i=i+1
        if (i<=10):
	    #print str(k)+"\t"+str(dic[k])
            print k[0]+"\t"+str(k[1])		

    #print max(dic.iteritems(), key=operator.itemgetter(1))[0]    
                
                
    
  
    

    
	

if __name__ == '__main__':
    main()
	
