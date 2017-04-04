from PIL import Image
from time import clock

def op(file):
	try:
		img = Image.open(file)
	except:
		try:
			img = Image.open(file+'.tiff')
		except:
			try:
				img = Image.open(file+'.tif')
			except:
				try:
					img = Image.open(file+'.jpg')
				except:
					try:
						img = Image.open(file+'.png')
					except:
						print('Unknown file and/or extension, please check directory for image.')
						exit(0)
	return img

def binarize(message):
	binary = []
	for i in [bin(int.from_bytes(x.encode(), 'big'))[2:] for x in message]:
		while len(i) < 8:
			i = '0' + i
		binary.append(i)
	return ''.join(binary)

def pixToHex(pix):
	#Pix must be a tuple of integers
	return ['{:02x}'.format(x) for x in pix]

def decrypt(pix,num):
	if pix[num][-1] in ['0','1']:
		return pix[num][-1], True
	else:
		return None,False

file = str(input('Encrypted Image (path): '))
start = clock()
encImage = op(file)

print('Decrypting...\n\n')
binary = ''
delimeter = binarize('"//"')
z = 0
done = False
while not done and z < 3:
	for i in encImage.getdata():
		hexed = pixToHex(i)
		temp, check = decrypt(hexed,z)
		if binary[-len(delimeter):] == delimeter:
			with open('decryption.txt', 'w') as d:
				[d.write(chr(int(binary[x:x+8],2))) for x in range(0,len(binary)-len(delimeter),8)]
			with open('decryption.txt','r') as dec:
				print(dec.read())
			done = True
			break
		elif check:
			binary += temp
	z += 1

print('\n\n\nFinished: info saved to decryption.txt')
elapse = clock() - start
print('Finished in', round(elapse,3),' seconds.')