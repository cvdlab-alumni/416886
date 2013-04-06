# floor0

verts = [[22,91.5], [45,91.5], [45,47.5], [62,47.5], [62,50.5], [145,50.5], 
	[145,63.5], [150,63.5], [150,75.5], [157,75.5], [157,112.5], [22,112.5]]

cells = [[1,12,2], [2,11,12], [2,3,4], [2,4,5], [2,5,6], [2,6,7], [2,7,8], [2,8,9], [2,9,10], [2,10,11]]

floor_quad = PROD([MKPOL([verts, cells, None]), Q(4)])

# semicircle
dom1 = PROD([INTERVALS(PI)(24), INTERVALS(8.5)(1)])
dom2 = PROD([INTERVALS(PI)(24), INTERVALS(18.5)(1)])

def semicircle(p):
	a,r = p
	return [r*COS(a), r*SIN(a)]

semicircle1 = T([1,2])([53.5,47.5])(R([1,2])(PI)(MAP(semicircle)(dom1)))
semicircle2 = T([1,2])([157,94])(R([1,2])(-PI/2)(MAP(semicircle)(dom2)))


floor0 = STRUCT([floor_quad, PROD([semicircle1,Q(4)]), PROD([semicircle2,Q(4)])])



# floor1

verts = [[22,16.5], [182,16.5], [182,112.5], [88.5,112.5], [88.5,95.5], [38.5,95.5], [38.5,112.5], [22,112.5], [22,110.5], 
	[5.5,110.5], [5.5,95.5], [22,95.5]]

cells = [[1,2,3], [3,4,5], [1,3,5], [1,5,6], [1,6,12], [12,6,7], [8,12,7], [9,11,12], [10,11,9]]

floor1 = T([3])([37])(PROD([MKPOL([verts, cells, None]), Q(4)]))



# floor2

verts = [[104,16.5], [182,16.5], [182,112.5], [88.5,112.5], [88.5,95.5]]

cells = [[1,2,3], [3,4,5], [1,5,3]]

floor2 = T([3])([74])(PROD([MKPOL([verts, cells, None]), Q(4)]))



# floor3

verts = [[22,16.5], [182,16.5], [182,112.5], [138,112.5], [138,95.5], [99.5,95.5], [99.5,112.5], [22,112.5]]

cells = [[1,2,3], [3,4,5], [1,3,5], [1,6,5], [1,6,7], [1,7,8]]

floor3 = T([3])([111])(PROD([MKPOL([verts, cells, None]), Q(4)]))

# floor4

verts = [[99.5,16.5], [182,16.5], [182,112.5], [22,112.5], [22,93.5], [99.5,95.5]]

cells = [[1,2,3], [1,6,3], [3,6,4], [6,5,4]]

floor4 = T([3])([148])(PROD([MKPOL([verts, cells, None]), Q(4)]))




building = STRUCT([floor0, floor1, floor2, floor3, floor4, building])

