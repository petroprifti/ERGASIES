from bitarray import bitarray
import hashlib
 
class BloomFilter:
	
	def __init__(self, size, hash_count):
		self.size = size 
		self.hash_count = hash_count
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
	
	def add(self, string):
		for seed in xrange(self.hash_count):
			result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
			self.bit_array[result] = 1
			
	def lookup(self, string):
		for seed in xrange(self.hash_count):
			result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
			if self.bit_array[result] == 0:
				print "--" , leksi, "--" ,
				return ""
				break
	        else:
				return leksi



bf = BloomFilter(500000, 7)

lines = open("american-english.txt").read().splitlines()
for line in lines:
    bf.add(line)

file_name = raw_input("Enter name file: ")
key = False
while key == False:
	try: 
		t = open(file_name,"r")
		lines = t.readlines()
		for line in lines:
			lekseis = line.split()
			for leksi in lekseis:
				print (leksi),
		key = True
		break
	except IOError:
		print "File not found!"
	file_name = raw_input("Enter name file: ")
print ""
print "These are the mistakes: "
for leksi in lekseis:
    print bf.lookup(leksi),