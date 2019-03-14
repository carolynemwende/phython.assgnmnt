Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[0,1,2,3,4,5,6,7,8,9]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.append(10)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x.extend([11,12,13])
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> x.pop()
13
>>> x.remove(12)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> x.sort()
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> x.pop()
11
>>> 
>>> 
>>> y=[y*10 for y in x]
>>> y
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> 
>>> 
>>> for y in x:
	print(y*10)

	
0
10
20
30
40
50
60
70
80
90
100
>>> 
>>> 
>>> 
>>> k=x[5: ]
>>> k
[5, 6, 7, 8, 9, 10]
>>> v=x[ :5]
>>> v
[0, 1, 2, 3, 4]
>>> 
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>> n
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> 
>>> flatlist=[]
>>>  m=[]
SyntaxError: unexpected indent
>>> m=[]
>>> for subist in n:
	for item in sublist:
		m.append(item)

		
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    for item in sublist:
NameError: name 'sublist' is not defined
>>> print(m)
[]
>>> for sublist in n:
	for item in sublist:
		m.append(item)

		
>>> print(m)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
