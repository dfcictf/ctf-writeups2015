import struct
import base64

def encrypt(data):
	padding = 4 - len(data) % 4
	if padding != 0:
	    data = data + "\x00" * padding

	result = []
	blocks = struct.unpack("I" * (len(data) / 4), data)
	for block in blocks:
	    result += [block ^ block >> 16]
	    print block
	#print blocks
	#print result
	output = ''
	for block in result:
	    output += struct.pack("I", block)

	print base64.b64encode(output)

def decrypt(data):
	result = ""
	decode_b64 = base64.b64decode(data)
	print "Base64 decoded: ", decode_b64
	blocks = struct.unpack("I" * (len(decode_b64) / 4), decode_b64)
	for block in blocks:
		result += struct.pack("I", block ^ block >> 16)
		print result
	print "Found flag: %s" % (result)

def main():
	sample_plain = "AABBCCDDEEFFGG"
 	enc = "CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA="
	
	#encrypt(sample_plain)
	decrypt(enc)

if __name__ == '__main__':
	main()
