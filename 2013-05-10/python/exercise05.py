from pyplasm import *
import scipy
from scipy import *

#---------------------------------------------------------
def VERTEXTRUDE((V,coords)):
    """
        Utility function to generate the output model vertices in a 
        multiple extrusion of a LAR model.
        V is a list of d-vertices (each given as a list of d coordinates).
        coords is a list of absolute translation parameters to be applied to 
        V in order to generate the output vertices.
        
        Return a new list of (d+1)-vertices.
    """
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def cumsum(iterable):
    # cumulative addition: list(cumsum(range(4))) => [0, 1, 3, 6]
    iterable = iter(iterable)
    s = iterable.next()
    yield s
    for c in iterable:
        s = s + c
        yield s

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])
#---------------------------------------------------------

# exercise05
domain1D = GRID([20])

def curve(controlPoints):
    return MAP(BEZIER(S1)(controlPoints))(domain1D)

domain2D = GRID([20,20])

def surface(fnList):
    return MAP(BEZIER(S2)(fnList))(domain2D)

# windshield

cp1 = [[5.38, 3.29, 2.13], [4.99, 3.66, 2.13], [5.02, 4.93, 2.13], [5.44, 5.25, 2.13]]
cp2 = [[6.31, 3.55, 2.46], [6.31, 4.97, 2.46]]

cp3 = [[5.68, 3.29, 2.13], [5.68, 4.25, 2.1], [5.68, 5.25, 2.13]]
cp4 = [[6, 3.55, 2.30], [6, 4.25, 2], [6, 4.97, 2.30]]

b1 = BEZIER(S1)(cp1)
b2 = BEZIER(S1)(cp2)
b3 = BEZIER(S1)(cp3)
b4 = BEZIER(S1)(cp4)

windshield_surface = COLOR(CYAN)(surface([b1,b3,b4,b2]))

#VIEW(STRUCT([windshield_surface, curve(cp1), curve(cp2), curve(cp3), curve(cp4)]))

# roof
cp1 = [[6.4, 5.04, 2.46], [6.4, 3.5, 2.46]]
cp2 = [[7.7, 5.04, 2.46], [7.9, 4.89, 2.46], [7.9, 3.76, 2.46], [7.7, 3.5, 2.46]]

cp3 = [[7.05, 5.04, 2.56],[7.05, 4.27, 2.60],[7.05, 3.5, 2.56]]

b1 = BEZIER(S1)(cp1)
b2 = BEZIER(S1)(cp2)
b3 = BEZIER(S1)(cp3)

roof_surface = COLOR(YELLOW)(surface([b1,b3,b2]))

#VIEW(STRUCT([roof_surface,curve(cp1),curve(cp2), curve(cp3)]))


#---------------------------------------------------------------------------------


# exercise04
def cyl(r,h) :
    return PROD([CIRCUMFERENCE(r)(40), Q(h)])

def circleSez(r1,r2):
    return DIFF([CIRCLE(r1)([40,1]), CIRCLE(r2)([40,1])])

def solidCyl(r,h,r2):
    return STRUCT([cyl(r, h), circleSez(r, r2), cyl(r2, h), T(3)(h)(circleSez(r,r2))])

r1 = 0.5
r2 = 0.4

torus = COLOR(BLACK)(TORUS([r1,r2])([40,40]))

r3 = 0.05
r4 = 0.12
h = 0.04

internal = STRUCT([COLOR(BLACK)(solidCyl(r4,h,r3)), 
    CYLINDER([r3,h])(40)])

verts = [[r3,r3],[-r3,r3],[r3-0.02,r2],[-r3+0.02,r2]]
cells = [[1,2,3],[2,3,4]]
trapeze = COLOR(BLACK)(PROD([MKPOL([verts, cells, None]), Q(h)]))

rot = R([1,2])(PI/2)
trapezes = STRUCT(NN(3)([rot, trapeze]))

steeringWheel = STRUCT([T(3)(h/2)(torus), internal, trapezes])

#VIEW(steeringWheel)


#---------------------------------------------------------------

# exercise03

def cyl(r,h) :
    return PROD([CIRCUMFERENCE(r)(40), Q(h)])

def circleSez(r1,r2):
    return DIFF([CIRCLE(r1)([40,1]), CIRCLE(r2)([40,1])])

def solidCyl(r,h,r2):
    return STRUCT([cyl(r, h), circleSez(r, r2), cyl(r2, h), T(3)(h)(circleSez(r,r2))])

# rubber
r = 0.8
h = 0.6
r2 = 0.6

rubber = COLOR(BLACK)(solidCyl(r,h,r2))

# rim
r3 = 0.55
r4 = 0.1
hrim = 0.1

verts = [[0,0],[-0.1,r3],[0.1,r3]]
cells = [[1,2,3]]
triangle = PROD([MKPOL([verts, cells, None]), Q(hrim)])
triangle = T(3)(h-hrim)(triangle)

rot = R([1,2])((2*PI)/5)

star = STRUCT(NN(5)([rot, triangle]))

rim = STRUCT([solidCyl(r2,h,r3), T(3)(h-hrim)(CYLINDER([r4, hrim])(40)), star])


wheel = STRUCT([rubber, rim])

#VIEW(wheel)


#--------------------------------------------------------------------------------
# exercise02
domain = GRID([20])

def curve(controlPoints):
    return MAP(BEZIER(S1)(controlPoints))(domain)


# XY view
# round
cp1 = [[3.98, 3.17], [3.58, 3.61], [3.64, 4.87], [3.96, 5.36]]
cp2 = [[3.98, 3.17], [4.28, 3.03], [4.53, 2.96], [4.67, 2.93]]
cp3 = [[7.59, 2.83], [7.43, 2.85], [4.95, 2.91], [4.67, 2.93]]
cp4 = [[7.56, 2.88], [7.6, 2.77], [7.88, 2.78], [7.99, 2.85]]
cp5 = [[9.45, 2.84], [9.32, 2.81], [8.3, 2.85], [7.99, 2.85]]
cp6 = [[5.89, 2.94], [6.23, 2.95], [7.83, 2.91], [7.99, 2.85]]
cp7 = [[9.84, 2.97], [9.81, 2.95], [9.57, 2.87], [9.45, 2.84]]
cp8 = [[9.84, 2.97],[9.87, 3.02]]
cp9 = [[9.87, 3.02], [10.23, 3.07], [10.22, 5.48], [9.86, 5.51]]
cp10 = [[9.86, 5.51], [9.84, 5.55]]
cp11 = [[9.41, 5.69], [9.67, 5.63], [9.55, 5.66], [9.84, 5.55]]
cp12 = [[9.41, 5.69], [8.39, 5.73], [6.59, 5.55], [5.93, 5.57]]
cp13 = [[8.01, 5.67], [7.9, 5.73], [7.64, 5.79], [7.56, 5.64]]
cp14 = [[4.67, 5.62], [5.48, 5.61], [7.28, 5.7], [7.57, 5.68]]
cp15 = [[4.67, 5.62], [4.4, 5.56], [4.13, 5.45], [3.96, 5.36]]

carRound = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6), curve(cp7), curve(cp8), curve(cp9),
    curve(cp10), curve(cp11), curve(cp12), curve(cp13), curve(cp14), curve(cp15)])

# hood
cp1 = [[4.06, 3.22], [3.78, 3.68], [3.81, 4.83], [4.04, 5.33]]
cp2 = [[4.06, 3.22], [4.52, 3.02], [5.45, 3.02], [5.66, 3.04]]
cp3 = [[5.66, 3.04], [5.64, 3.09]]
cp4 = [[5.43, 3.11], [5.64, 3.09]]
cp5 = [[5.43, 3.11], [4.69, 3.66], [4.92, 5.18], [5.43, 5.4]]
cp6 = [[5.66, 5.43], [5.43, 5.4]]
cp7 = [[5.66, 5.43], [5.66, 5.48]]
cp8 = [[4.04, 5.33], [4.51, 5.49], [5.25, 5.56], [5.66, 5.48]]
cp9 = [[3.96, 5.09], [5.02, 4.81]]
cp10 = [[3.96, 3.45], [5.02, 3.72]]
cp11 = [[4.44, 3.56], [4.7, 3.08]]
cp12 = [[4.44, 4.97], [4.7, 5.47]]

hood = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6), curve(cp7), curve(cp8), curve(cp9), 
    curve(cp10), curve(cp11), curve(cp12)])

# windshield
cp1 = [[5.38, 3.29], [4.99, 3.66], [5.02, 4.93], [5.44, 5.25]]
cp2 = [[6.29, 4.97], [5.44, 5.25]]
cp3 = [[6.29, 4.97], [6.31, 3.55]]
cp4 = [[5.38, 3.29], [6.31, 3.55]]

windshield = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4)])

# roof
cp1 = [[9.09, 5.07], [8.05, 5.18], [6.74, 4.67], [5.4, 5.38]]
cp2 = [[9.09, 5.07], [9.18, 4.89], [9.2, 3.76], [9.09, 3.46]]
cp3 = [[5.4, 3.15], [6.28, 3.61], [7.13, 3.6], [9.09, 3.46]]
cp4 = [[6.4, 5.04], [6.4, 3.5]]
cp5 = [[9.12, 4.90], [7.49, 4.90]]
cp6 = [[7.49, 3.65], [7.49, 4.90]]
cp7 = [[7.49, 3.65], [9.12, 3.63]]
cp8 = [[8.42, 3.06], [7.77, 3.65]]
cp9 = [[8.42, 3.06], [9.28, 3.06], [9.02, 3.19], [9.12, 3.63]]
cp10 = [[8.41, 5.47], [7.78, 4.89]]
cp11 = [[8.41, 5.47], [8.84, 5.38], [9.13, 5.67], [9.12, 4.90]]

roof = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6), curve(cp7), curve(cp8), curve(cp9), 
    curve(cp10), curve(cp11)])

# windows
cp1 = [[5.55, 5.41], [6.79, 4.96], [6.92, 5.06], [7.34, 5.07]]
cp2 = [[7.17, 5.45], [7.14, 5.06]]
cp3 = [[7.36, 5.43], [5.5, 5.42]]
cp4 = [[7.36, 5.43], [7.34, 5.07]]

cp5 = [[5.54, 3.11], [6.8, 3.56], [6.87, 3.46], [7.34, 3.47]]
cp6 = [[7.35, 3.08], [7.34, 3.47]]
cp7 = [[7.35, 3.08], [5.54, 3.11]]
cp8 = [[7.2, 3.08], [7.15, 3.46]]

windows = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6), curve(cp7), curve(cp8)])

# retro
cp1 = [[9.75, 5.39], [9.9, 5.28], [9.97, 3.34], [9.75, 3.16]]
cp2 = [[5.66, 3.04], [8.42, 2.95], [9.67, 3.1], [9.75, 3.16]]
cp3 = [[5.63, 5.48], [8, 5.53], [9.02, 5.51], [9.75, 5.38]]

cp4 = [[9.86, 3.04], [10.11, 3.88], [10.1, 4.8], [9.88, 5.5]]
cp5 = [[9.15, 3.63], [10.09, 3.62]]
cp6 = [[9.14, 4.9], [10.09, 4.91]]

retro = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6)])

XYview = STRUCT([carRound, hood, windshield, roof, windows, retro])
#VIEW(XYview)


# XZ view
# round
cp1 = [[3.74, 1.16], [4.67, 1.16]]
cp2 = [[5.69, 1.16], [5.8, 2.21], [4.55, 2.2], [4.67, 1.16]]
cp3 = [[5.69, 1.16], [8.4, 1.16]]
cp4 = [[9.48, 1.17], [9.55, 2.33], [8.24, 2.07], [8.4, 1.16]]
cp5 = [[9.48, 1.17], [10.18, 1.51]]
cp6 = [[9.93, 2.21], [10.08, 2.09], [10.25, 1.68], [10.18, 1.51]]
cp7 = [[9.93, 2.21], [9.13, 2.31], [7.27, 2.68], [6.39, 2.47]]
cp8 = [[3.71, 1.55], [4.27, 1.98], [6.01, 2.37], [6.39, 2.47]]
cp9 = [[3.71, 1.55], [3.74, 1.16]]

carRound = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6), curve(cp7), curve(cp8), curve(cp9)])

# window
cp1 = [[5.57, 2.07], [6.1, 2.26], [6.55, 2.44], [7.3, 2.43]]
cp2 = [[7.33, 2.12], [7.3, 2.43]]
cp3 = [[7.33, 2.12], [6.87, 2.05], [5.77, 1.98], [5.57, 2.07]]
cp4 = [[7.21, 2.11], [7.17, 2.43]]

window = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4)])

# windshield
cp1 = [[5.41, 2.07], [5.06, 2.11]]
cp2 = [[5.41, 2.07], [6.41, 2.48]]

windshield = STRUCT([curve(cp1), curve(cp2)])


# details
cp1 = [[3.73, 1.19], [4.66, 1.3]]
cp2 = [[3.88, 1.68], [4.75, 1.71]]

cp3 = [[7.33, 2.12], [7.43, 1.86], [7.33, 1.59], [7.32, 1.5]]
cp4 = [[5.41, 2.08], [5.33, 1.87], [5.79, 1.95], [5.78, 1.34]]
cp5 = [[5.53, 1.88], [5.77, 1.71], [7.43, 2], [8.7, 1.92]]
cp6 = [[7.6, 1.51], [7.38, 1.49], [6.44, 1.44], [5.68, 1.34]]
cp7 = [[7.6, 1.51], [7.81, 1.52], [8.09, 1.21], [8.17, 1.16]]
cp8 = [[7.6, 1.49], [7.81, 1.16]]
cp9 = [[7.83, 1.44], [8.4, 1.48]]
cp10 = [[8.08, 1.21], [8.4, 1.24]]

cp11 = [[7.33, 2.12], [8.36, 2.23], [9.28, 2.18], [9.77, 2.15]]
cp12 = [[9.89, 2.23], [9.77, 2.15]]
cp13 = [[9.91, 1.55], [9.95, 1.63], [9.87, 2.09], [9.77, 2.15]]
cp14 = [[9.91, 1.55], [10.17, 1.68]]

cp15 = [[9.84, 1.97], [9.96, 1.86], [9.11, 1.94], [9.1, 1.95]]
cp16 = [[9.86, 1.84], [9.4, 1.71]]

details = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6), curve(cp7), curve(cp8), curve(cp9), 
    curve(cp10), curve(cp11), curve(cp12), curve(cp13), curve(cp14), curve(cp15), curve(cp16)])

XZview = STRUCT([carRound, window, windshield, details])
#VIEW(XZview)


# YZ view
# round 
cp1 = [[3.14, 1.16], [0.38, 1.16]]
cp2 = [[3.14, 1.16], [3.24, 1.27], [3.27, 2], [3.17, 2.1]]
cp3 = [[2.57, 2.5], [3.17, 2.1]]
cp4 = [[2.57, 2.5], [2.26, 2.58], [1.33, 2.6], [0.92, 2.5]]
cp5 = [[0.34, 2.1], [0.92, 2.5]]
cp6 = [[0.34, 2.09], [0.24, 1.93], [0.29, 1.36], [0.38, 1.16]]

roundCar = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6)])

# windshield
cp1 = [[0.66, 2.13], [2.87, 2.13]]
cp2 = [[2.58, 2.46], [2.87, 2.13]]
cp3 = [[2.58, 2.46], [2.33, 2.48], [1.24, 2.5], [0.93, 2.46]]
cp4 = [[0.93, 2.46], [0.66, 2.13]]

windshield = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4)])

# hood
cp1 = [[0.41, 1.16], [0.37, 1.88], [0.24, 2.08], [0.66, 2.13]]
cp2 = [[3.1, 1.16], [3.14, 1.95], [3.27, 2.05], [2.87, 2.13]]

cp3 = [[3.15, 1.73], [2.42, 1.64], [0.8, 1.67], [0.36, 1.73]]
cp4 = [[0.93, 1.69], [0.99, 1.82], [1.06, 1.97], [1.19, 2.13]]
cp5 = [[2.58, 1.69], [2.58, 1.81], [2.38, 2.06], [2.32, 2.13]]
cp6 = [[2.82, 1.7], [2.98, 1.97]]
cp7 = [[2.47, 1.94], [2.98, 1.97]]
cp8 = [[1.04, 1.94], [0.52, 1.97]]
cp9 = [[0.68, 1.7], [0.52, 1.97]]

cp10 = [[3.11, 1.31], [2.89, 1.19], [0.78, 1.15], [0.41, 1.31]]
cp11 = [[0.77, 1.53], [0.69, 1.26]]
cp12 = [[0.77, 1.53], [2.73, 1.53]]
cp13 = [[2.82, 1.26], [2.73, 1.53]]


hood = STRUCT([curve(cp1), curve(cp2), curve(cp3), curve(cp4), curve(cp5), curve(cp6), curve(cp7), curve(cp8), curve(cp9), 
    curve(cp10), curve(cp11), curve(cp12), curve(cp13)])

YZview = STRUCT([roundCar, windshield, hood])
# VIEW(YZview)

XYviewMoved = T([1,2,3])([-6.5,-4.5,1.6])(XYview)
XZviewMoved = T([1,2,3])([-6.5,1.3,-1])(R([2,3])(PI/2)(XZview))
YZviewMoved = T([1,2,3])([-2.8,-2,-1])(R([1,2])(PI/2)(R([2,3])(PI/2)(YZview)))

profileCurvesCar = R([1,2])(PI)(STRUCT([XYviewMoved, XZviewMoved, YZviewMoved]))


# insert 4 wheel

wheelRestructDx = T(3)(0.3)(R([2,3])(PI/2)(S([1,2,3])([0.5, 0.5, 0.5])(wheel)))
wheelRestructSx = R([1,2])(PI)(wheelRestructDx)

wheels = STRUCT([T([1,2])([1.3,-1])(wheelRestructDx), 
    T([1,2])([-2.5,-1])(wheelRestructDx), 
    T([1,2])([1.3,1.5])(wheelRestructSx), 
    T([1,2])([-2.5,1.5])(wheelRestructSx)])


# insert steering wheel
steeringWheelMoved = S([1,2,3])([0.7,0.7,0.7])(T([1,2,3])([0.5,0.8,1])(R([2,3])(PI/2)(R([1,3])(PI/2)(steeringWheel))))


# insert surfaces
windshield_surface_moved = T([1,2,3])([6.8,-4,0.35])(R([1,3])(PI-PI/6)(windshield_surface))
roof_surface_moved = T([1,2,3])([6.5,4.52,-1.08])(R([1,2])(PI)(roof_surface))

VIEW(STRUCT([profileCurvesCar, wheels, steeringWheelMoved, windshield_surface_moved, roof_surface_moved]))

