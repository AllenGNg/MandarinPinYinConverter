import pinyin
from playsound import playsound
from pathlib import Path
import re
import io
sentance = []

fullStop = re.compile(ur'[\u3002]')
#print("hi")
#print(pinyin.get(","))

with io.open("input1.txt", encoding = 'utf-8') as f:
	content = f.read().splitlines()
	print(f.read())
	#content = splitLine.split(f.read())

#print (len(content))

temp = []
sentances = fullStop.split(content[0])
#print(sentances)
#print(content)


for sentance in sentances:
	print(sentance + ".") 
	for each in sentance:
		if ord(each) == 65292 or ord(each) == 8220 or ord(each) == 8221:
			continue
		else:
			print(pinyin.get(each, delimiter = " "))
			line = pinyin.get(each, format = "numerical", delimiter = " ")
			myfile = Path("audioFiles/" + line + ".mp3")
			if myfile.is_file():
				playsound("audioFiles/" + line + ".mp3")
