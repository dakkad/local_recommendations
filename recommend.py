from __future__ import print_function
n = input() #get place count
#places = [[0, 0, 0, 7, 10], [1, 0, 7, 0, 5], [2, 1, 10, 5, 0]] #test case for places
places = []
for i in range(n):
	places.append(list(map(int, raw_input().strip().split()))) #parse and store place

p = input() #get route count
#routes = [[0, 1, 2], [2, 1, 0], [2, 1], [0, 2], [0, 2, 1]] #test case for routes already travelled
routes = []
for i in range(p):
	routes.append(list(map(int, raw_input().strip().split()))) #parse and store route

#cur_route = [1,2] # test case for current route
cur_route = map(int, raw_input().strip().split()) # get our current route
cur_place = cur_route[len(cur_route) - 1] # get our current place on this route
recommendations = []

for x in routes:	
	if x[0] == cur_place: #someone previously started at our current position
		i = 1
		while i < len(x):
			if recommendations.count(x[i]) < 1: #ensure our recomendation isn't duplicated
				recommendations.append(x[i]) 
			i += 1
			if len(recommendations) == 5:
				break


	if len(recommendations) == 5:
		break

for x in recommendations:
	print(x, end=' ')

#TODO: Order 'recommendations' by distance using 'cur_place' against 'places'



