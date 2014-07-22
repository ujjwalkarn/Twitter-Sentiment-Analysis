import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
	
def lin(yo):
	for line in yo:
		data = json.load(line)
		pprint(data)
		json_data.close()
		l=data["text"]
		lines(l)

def main():
	
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
	
    lines(sent_file)
    lines(tweet_file)
	lin(tweet_file)
	
	
	

if __name__ == '__main__':
    main()
	
