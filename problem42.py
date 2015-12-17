print ord('A')
print ord('a')

sum1=0

def get_value(word):
	sum = 0
	val = 0
	for letter in word:
		val = ord(letter) - 64
		sum += val
	return sum


def checkTriangle(value):
	n = 1
	tri = 1
	while value >= tri:
		if value == tri:
			return True
		n += 1
		tri = tri + n
	return False

f = open('problem042_words.txt', 'r')
tri_count = 0

for words in f:
	#print words
	for word in words.split(","):
		word = word[1:-1]
		print word
		word = word.upper()
		sum1 = get_value(word)
		if checkTriangle(sum1):
			tri_count += 1;


print tri_count
#print checkTriangle("SKY")
val2 = get_value("SKY")
print checkTriangle(val2)
