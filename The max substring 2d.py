# codeing=utf-8
'''
2013-9-17  XTH
'''
n1 = raw_input("please input the row number of array")           #the row number of array
n2 = raw_input("please input the line number of array")     #the line number of array
f = open(n1 + "," + n2 + ".txt","r")
num=[[]]*int(n1)
for i in range(0,int(n1)):
	line = f.readline()
	line = line.strip('\n')
	num[i] = line.split(",")
num=[[int(x) for x in inner] for inner in num]

# read in data from a txt file which is created by anohter python program
# recording to this problem, I tryed to traverse the rows of the matrix, and transform the problem into a 1d problem.

def max_2d(num,n1,n2):
	line = [0]*n2
	max_sum = 0     #the max num
	fore_sum = 0    #
	now_sum = 0     #the num now
	x = [0]*2
	y = [0]*2
	for i in range(0,n1):
		for j in range(i,n1):
			x[0] = i
			y[0] = 0
			for k in range(0,n2):
				line[k] += num[j][k]
				if fore_sum <0:
					now_sum = 0
					y[0]=k
				now_sum += line[k]
				if now_sum > max_sum:
					max_sum = now_sum
					y[1]=k
					x[1]=j
					x2=x[0]
					y2=y[0]
			now_sum = 0
		now_sum=0
		line = [0]*n2
	return "the max num is " + str(max_sum) + "\n"+ "the area is " + str(x2) + "," + str(y2) + " to " + str(x[1]) + "," + str(y[1])
print(max_2d(num,int(n1),int(n2)))