import os
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	parsed_data = ""
	def handle_data(self, data):
		self.parsed_data += data
		return self.parsed_data


rootdir = '/home/omkar/Desktop/trec_dataset/trec/'
counter = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
    	f=open(os.path.join(subdir, file),"r")
    	#print(file)
    	s=f.read()
    	parser = MyHTMLParser()
    	parser.feed(s)
    	counter = counter+1
    	fil = open("trec_"+ str(counter),'w')
    	fil.write(parser.parsed_data)
    	fil.write("///////////////////////////////////////////////////////////////////////////////////////////////////////")
    	fil.close()
    	print(os.path.join(subdir, file)) 