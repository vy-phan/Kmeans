import math

points = [[11,12],[22,44],[88,44]]
clusers = [[33,22],[22,55]]

def distance(p1, p2):
	return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))


for p in points:
	for c in clusers:
		print(f'{p},{c}')

lables = []
for p in points:
	distance_to_cluster = []
	for c in clusers:
		dis = distance(p,c)
		print(dis)	
		distance_to_cluster.append(dis)
		print(distance_to_cluster)	
	print(distance_to_cluster)	
	min_distance = min(distance_to_cluster)
	print(min_distance)
	lable = distance_to_cluster.index(min_distance)
	print(lable)
	lables.append(lable)	
	print(lables)	