import numpy

lis = []
ziplis = numpy.random.zipf(1.1, 100000)

with open("zipfian", "w+") as f:

#generate values for the file
	for i in ziplis:
		lis.append(i%256)
		f.write("%d" % int(lis[len(lis)-1]))
