'''Create a compression scheme combining BWT with a suite of list update algorithms...
    The code for reading in the files is based on: https://askubuntu.com/questions/352198/reading-all-files-from-a-directory'''

import sys
import os
import BurrowsWheelerTransform
import time
import MoveToFront
import Timestamp
import BIT
import COMB
import runLengthEncoding
import OtherBWT
import bwtRadix
import glob
import errno

#array of bits 
uniqueBits = []

#initialize array of bits....
for i in range(0, 256):
	uniqueBits.append(i)
	format(uniqueBits[i], 'b')


print("Starting...")


def computeCompression(sequence, origLength, alg):
	per = sequence/origLength

	ret = 100 * per

	print("%1.3f After %s" % (ret, alg))

def computeRatiosAndSpeeds(path):
	files = glob.glob(path)
	for name in files:
		try:
			with open(name, 'rb') as fi:
				bwtString = fi.read()

			print("Testing file: ", name)

			print("starting BWT...")
			origLength = len(bwtString)
			print(origLength)
			if (origLength > 300000):
				bwtString = BurrowsWheelerTransform.bw_custom(bwtString)
			else:
				bwtString = BurrowsWheelerTransform.bwt_me(bwtString)

			print("starting MTF Encode...")
			start = time.time()
			seq = MoveToFront.mtf_encode(bwtString, uniqueBits)
			end = time.time()
			print("total time of mtf encode was")
			print(end-start)
			print("\n\n")

			runLE = runLengthEncoding.rle(seq)
			print(len(runLE))
			print(len(seq))
			print("The compression percentage is ")
			computeCompression(len(runLE), len(seq), "MTF")

			print("starting MTF Decode...")
			start = time.time()
			chars = MoveToFront.mtf_decode(seq, uniqueBits)
			end = time.time()
			print("total time of mtf decode was")
			print(end-start)
			print("\n\n")

			print("starting Timestamp encode...")
			start = time.time()
			seq = Timestamp.timeStamp_encode(bwtString, uniqueBits)
			end = time.time()
			print("total time of Timestamp encode was")
			print(end-start)
	
			runLE = runLengthEncoding.rle(seq)
			print(len(runLE))
			print("The compression percentage is ")
			computeCompression(len(runLE), len(seq), "Timestamp")

			print("starting Timestamp decode...")
			start = time.time()
			Timestamp.timeStamp_decode(seq, uniqueBits)
			end = time.time()
			print("total time of timestamp decode was")
			print(end-start)
			print("\n\n")

			print("starting BIT encode...")
			start = time.time()
			seq = BIT.bitAlg_encode(bwtString, uniqueBits)
			end = time.time()
			print("total time of BIT encode was")
			print(end-start)

			runLE = runLengthEncoding.rle(seq)
			print(len(runLE))
			print("The compression percentage is ")
			computeCompression(len(runLE), len(seq), "BIT")
			
			print("starting BIT decode...")
			start = time.time()
			chars = BIT.bitAlg_decode(seq, uniqueBits)
			end = time.time()
			print("total time of BIT decode was")
			print(end-start)
			print("\n\n")

			print("starting COMB encode...")
			start = time.time()
			seq = COMB.combAlg_encode(bwtString, uniqueBits)
			end = time.time()
			print("total time of COMB encode was")
			print(end-start)
			
			runLE = runLengthEncoding.rle(seq)
			print(len(runLE))
			print("The compression percentage is ")
			computeCompression(len(runLE), len(seq), "COMB")
			
			print("starting COMB decode...")
			start = time.time()
			seq = COMB.combAlg_decode(bwtString, uniqueBits)
			end = time.time()
			print("total time of COMB decode was")
			print(end-start)

			print("\n\n\n\n")
	
		except IOError as exc:
			if exc.errno != errno.EISDIR:
				raise

#Driver code...
path1 = "/home/student/cookea35/Documents/COMP 7720/calgarycorpus/*"
path2 = "/home/student/cookea35/Documents/COMP 7720/cantrbry/*"

computeRatiosAndSpeeds(path1)
computeRatiosAndSpeeds(path2)

