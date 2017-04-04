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

def opText(file):
	try:
		text = open(file,'r')
	except:
		try:
			text = open(file+'.txt','r')
		except:
			try:
				text = open(file+'.doc','r')
			except:
				try:
					text = open(file+'.docx','r')
				except:
					try:
						message = str(input('Message: '))
						return message
					except:
						print('Message to encrypt must be saved with the name "message" and extension of .txt .doc. or .docx.')
						quit(0)
	return text.read()

def binarize(message):
	binary = []
	for i in [bin(int.from_bytes(x.encode(), 'big'))[2:] for x in message]:
		while len(i) < 8:
			i = '0' + i
		binary.append(i)
	return ''.join(binary)

def messageToBinary(message):
	i = 0
	while i < len(message):
		for j in binarize(message[i]):
			yield j
		i += 1

def getPixels(img):
	datas = img.getdata()
	i = 0
	while i < len(datas):
		yield datas[i]
		i += 1

def pixToHex(pix):
	#Pix must be a tuple of integers
	return (['{:02x}'.format(x) for x in pix])

def check(pix,index,num):
	if pix[index][-1] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
		pix[index] = pix[index][0]+num
		return pix, True
	else:
		return pix, False

def hexToDec(pix):
	#Pix must be a tuple of strings
	return tuple([int(x,16) for x in pix])


file = str(input('File to crypt: ')).replace('\\','/')
encFile = str(input('Name for encrypted file: '))

start = clock()
img = op(file)
pixels = list(img.getdata())
size = img.size
img.close

message = opText('message')
delimeter = '"//"'

print('Creating binary generator...\n\n')
binaryMessage = messageToBinary(message+delimeter)

print('Encrypting...\n\n')
binDig = next(binaryMessage)
done = False
pixIndex, numBin = 0, 0
while not done and pixIndex < 3:
	for i, j in enumerate(pixels):
		if numBin < len(message+delimeter)*8:
			hexed = check(pixToHex(j),pixIndex,binDig)
			if hexed[1]:
				pixels[i] = hexToDec(hexed[0])
				numBin += 1
				if numBin < len(message+delimeter)*8:
					binDig = next(binaryMessage)
		else:
			done = True
			break
	pixIndex += 1

if not done:
	print('\n\nFailed to place message.')
elif done:
	print('All binary bits have been placed.\n')

	encImage = Image.new('RGB', size)
	encImage.putdata(pixels)
	#encImage.show()

	try:
		encImage.save(encFile)
	except:
		encImage.save(encFile+'.tiff')

	encImage.close()

	elapse = clock() - start
	print('Finished in', round(elapse,3),' seconds.')