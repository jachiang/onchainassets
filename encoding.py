#PILLOW installed via "brew install homebrew/python/pillow"
#HOW to open image in python "https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python"
from PIL import Image
from huffman import encode
import binascii

#Open Image "test.bmp"
im = Image.open("test.bmp")
width,height = im.size
pixel_values = list(im.getdata()) #all pixel values in series (255,255,255), etc.
print "size of image:", width, height





#COLOR PALETTE CAPTURES ALL POSSIBLE PIXEL VALUES IN DICT
color_palette = {}
total_pix = len(pixel_values) #num of total pixels of image
for i in range(total_pix):
	pixvalstr= str(pixel_values[i]) 
	palette = color_palette.keys()
	# if new value, add to dictionary
	if pixvalstr not in palette:
		color_palette[pixvalstr] = 1
	else:
		color_palette[pixvalstr] += 1	
#add huffman marker to color_palette
color_palette['end'] = 1

#Huffman tree creation
huff = encode(color_palette) #array of tuples
huff_dict = {}  #convert array to huff_dictionary
for p in huff:
    huff_dict[p[0]] = p[1]

#Generate binary string of image
img_bin_str = ''
for i in pixel_values:
    j = str(i) #convert RGB value into string for key dict usage
    img_bin_str = img_bin_str + huff_dict[j]

#Generate ENCODETABLEHEADER
#255,255,255,freq1,255,255,255,freq2,BASE128
encodertableheader = str(len(huff_dict) - 1) #start with number of keys, minus the 'end' marker
keys = huff_dict.keys()
for i in range(len(keys)): #iterating through keys, ignoring end
  if keys[i] is not 'end':
    #Iterating through key entries, shorten to eg  _255,12,1,freq_
    #encodertableheader = encodertableheader + keys[i][1:len(keys[i])-1]
print encodertableheader
#problems
  #commas
  #spacing



#End of string with huffman marker, add filler to round to multiple of 8
bits = 7 #SET TO 7 for 128 Base, SET TO 8 FOR 256 Base
img_bin_str = img_bin_str + huff_dict['end']
remainder = len(img_bin_str) % bits
if remainder is not 0:
    number_ones = bits - remainder
    img_bin_str = img_bin_str + number_ones * '1'

#Convert to ASCII - marker has been added, and filler 1 bits
#img_char: use chr(0-255) to convert to ASCII
i = 0 #iterate +8 per loop #or +7 for BASE128
counter = 0
img_char = ''
while i < len(img_bin_str):
	current_bin = img_bin_str[i:i + bits]
	current_ascii_num = int(current_bin,2)
	current_char = chr(current_ascii_num)
	#store current_bin in array
	img_char = img_char + current_char
	#iterate i, assume 8 bit signal
	i = i + bits

#ADD ENCODETABLEHEADER

print img_char





####### CREATE TOKEN WITH STRING INVOLVED
import json
import requests
from requests.auth import HTTPBasicAuth
import sys

#TESTNET PORT 14000
url = 'http://ec2-54-93-227-47.eu-central-1.compute.amazonaws.com:14000/api/'
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('rpc','rpc')

#CREATE TOKEN
payload = {
           "method": "create_issuance",
           "params": {
                      "source": "n4a9WAw1scE8WVTtyjckcKx5sL8o5upxvW", #need to create address at bitcoind?
                      "asset": "A11945611906419650003",
                      "quantity": 10,
                      "divisible": False,
                      "description": img_char,
                      "transfer_destination": None
                     },
           "jsonrpc": "2.0",
           "id": 0
          }

resp = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
data = resp.json()
#u before the keys are handled automatically (unicode)
print data





####### DECODE img_char #######
img_bin_str_2 = ''
for i in range(len(img_char)):
	#character to binary
  bits_format = '{0:0'+str(bits)+'b}'
  img_bin_str_2 += bits_format.format( ord(img_char[i]) )
if img_bin_str == img_bin_str_2:
	print 'ok'

#Huffman decoding 
#include decoding table
#Decoding table not included yet
#Parse and recreate 11 x 11 image





















#This website works http://www.rapidtables.com/convert/number/ascii-to-binary.htm
#https://cryptii.com/text/select
#text_file = open("Output_char.txt", "w")
#text_file.write(img_char)
#text_file.close()


















#dict length = total events
#build dict probability event:0-1




#build color probabilities






#build color palette
#build huffman code based on color probabilities
#translate pixel values into huffman binary
#translate into characters