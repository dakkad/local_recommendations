from __future__ import print_function
n = input() #get place count
places = []
for i in range(n):
	places.append(list(map(int, raw_input().strip().split()))) #parse and store place

p = input() #get route count
routes = []
for i in range(p):
	routes.append(list(map(int, raw_input().strip().split()))) #parse and store route
	
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



