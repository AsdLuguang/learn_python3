#!/usr/bin/python3

data = list(range(10001))
data.pop(0);
data.pop(0);

i = 0;
while i < len(data):
	j = i + 1;
	while j < len(data):
		temp1 = data[j] / data[i];
		temp2 = data[j] // data[i];
		if temp1 == temp2:
			data.pop(j);
			#print(i, j)
			#print(data)
		else:
			j += 1;
	i += 1;

print(data)

