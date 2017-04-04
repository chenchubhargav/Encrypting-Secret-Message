Setup:

1. Drop files into it's own directory.

2. If you have not installed the Python Image Library (PIL), open command prompt and 'pip install pillow'

3. Open command prompt, change directory to file directory in step one.



To encrypt (through command prompt):

1. Drag an image you like into file directory.

2. Type your message and save it as 'message' with extension .txt .doc or .docx. If message.'ext' isn't found you can manually enter it in command prompt.

3. Type 'python encrypt.pyc'
	-Enter image name with or without extension
		Extension .tiff .tif .jpg or .png
	-Type the name you want for encrypted image

4. Wait, depending on image size and message length it can be done in less than a second more than an hour.



To decrypt (through command prompt):

1. Drop encrypted image into directory.

2. Type 'python decrypt.pyc'
	-Enter encrypted image name
	-When finished you will have a 'decryption.txt' in directory

Note: Depending on length of message decryption can take less than a second or more than an hour.