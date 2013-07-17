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


dom2D = GRID([20,20])

def surface(curves):
    return MAP(BEZIER(S2)(curves))(dom2D)


#****************************** OUTSIDE ******************************/

dx = 14
dy = 4
dz = 6

bottom_side = CUBOID([dx,dy])
upper_side = T([3])([dz])(CUBOID([dx,dy]))
left_side = R([1,3])(PI/2)(CUBOID([dz,dy]))
right_side = T([1])([dx])(left_side)
back_side = T([2])([dy])(R([2,3])(PI/2)(CUBOID([dx,dz])))

exterior = COLOR(WHITE)(STRUCT([bottom_side, upper_side, left_side, right_side, back_side]))

dx_recess = 0.2
dy_recess = 0.1
dz_recess = 0.2

p1 = [0,0,0]
p2 = [dx,0,0]
p3 = [dx,0,dz]
p4 = [0,0,dz]

p5 = [dx_recess,dy_recess,dz_recess]
p6 = [dx-dx_recess,dy_recess,dz_recess]
p7 = [dx-dx_recess,dy_recess,dz-dz_recess]
p8 = [dx_recess,dy_recess,dz-dz_recess]

c1 = BEZIER(S1)([p4,p3])
c2 = BEZIER(S1)([p8,p7])

c3 = BEZIER(S1)([p1,p4])
c4 = BEZIER(S1)([p5,p8])

c5 = BEZIER(S1)([p1,p2])
c6 = BEZIER(S1)([p5,p6])

c7 = BEZIER(S1)([p2,p3])
c8 = BEZIER(S1)([p6,p7])

p9 = [dx_recess,dy-0.01,dz_recess]
p10 = [dx-dx_recess,dy-0.01,dz_recess]
p11 = [dx-dx_recess,dy-0.01,dz-dz_recess]
p12 = [dx_recess,dy-0.01,dz-dz_recess]

c9 = BEZIER(S1)([p12,p11])
c10 = BEZIER(S1)([p9,p12])
c11 = BEZIER(S1)([p9,p10])
c12 = BEZIER(S1)([p10,p11])


interior = COLOR(BROWN)(
                STRUCT([surface([c1,c2]), surface([c3,c4]), surface([c5,c6]), surface([c7,c8]), 
                        surface([c2,c9]), surface([c4,c10]), surface([c6,c11]), surface([c8,c12])]))


outside = STRUCT([exterior, interior])



#****************************** DRAWERS ******************************/

distance = 0.02

dx_drs = dx-(dx_recess*2)-(distance*2)
dy_drs = dy-dy_recess-(distance)
dz_drs = dz-(dz_recess*2)-(distance*2)

dx_dr123 = (2*(dx_drs-distance))/3
dy_dr123 = dy_drs
dz_dr123 = (dz_drs-distance-distance)/3

dx_dr4 = dx_dr123/2
dy_dr4 = dy_drs
dz_dr4 = dz_drs

case123 = COLOR(BROWN)(STRUCT([CUBOID([dx_dr123, dy_dr123, 0.1]), 
                                        CUBOID([dx_dr123, 0.1, dz_dr123]), 
                                        CUBOID([0.1, dy_dr123, dz_dr123]), 
                                        T([1])([dx_dr123-0.1])(CUBOID([0.1, dy_dr123, dz_dr123])), 
                                        T([2])([dy_dr123-0.1])(CUBOID([dx_dr123, 0.1, dz_dr123]))]))


case4 = COLOR(BROWN)(STRUCT([CUBOID([dx_dr4, dy_dr4, 0.1]), 
                                        CUBOID([dx_dr4, 0.1, dz_dr4]), 
                                        CUBOID([0.1, dy_dr4, dz_dr4]), 
                                        T([1])([dx_dr4-0.1])(CUBOID([0.1, dy_dr4, dz_dr4])), 
                                        T([2])([dy_dr4-0.1])(CUBOID([dx_dr4, 0.1, dz_dr4]))]))

space = 0.2
dz_figure123 = dz_dr123-(space)
dz_figure4 = dz_dr4-(space)
depht = 0.1

# drawer1

verts11 = [[space,space],[space,dz_figure123],[3.3,dz_figure123],[4.5,1.1],[5,dz_figure123],[5.3,dz_figure123],[5.7,space]]
cells11 = [[7,1,2],[7,3,2],[7,3,4],[7,4,5],[7,5,6]]
figure11 = STRUCT([T([3])([depht])(PROD([MKPOL([verts11,cells11,None]),Q(depht)])), 
                    T([1,2])([2.1,0.5])(CUBOID([1,1,depht]))])

verts21 = [[5.9,space],[5.5,dz_figure123],[dx_dr123-space,dz_figure123],[dx_dr123-space,space]]
cells21 = [[1,2,4],[2,3,4]]
figure21 = STRUCT([T([3])([depht])(PROD([MKPOL([verts21,cells21,None]), Q(depht)])), 
                    T([1,2])([6.8,0.5])(CUBOID([1,1,depht]))])

figures1 = COLOR(WHITE)(STRUCT([figure11, figure21]))

drawer1 = STRUCT([case123, R([2,3])(PI/2)(figures1)])


# drawer2

verts12 = [[space,space],[space,dz_figure123],[4.7,dz_figure123],[5,1.1],[4,space]]
cells12 = [[1,2,3],[1,3,4],[4,2,1],[4,5,1]]
figure12 = STRUCT([T([3])([depht])(PROD([MKPOL([verts12,cells12,None]), Q(depht)])),
                    T([1,2])([2.1,0.5])(CUBOID([1,1,depht]))])

verts22 = [[5.4,space],[5.8,dz_figure123],[dx_dr123-space,dz_figure123],[dx_dr123-space,space]]
cells22 = [[1,2,4],[2,3,4]]
figure22 = STRUCT([T([3])([depht])(PROD([MKPOL([verts22,cells22,None]), Q(depht)])),
                    T([1,2])([6.8,0.5])(CUBOID([1,1,depht]))])

figures2 = COLOR(WHITE)(STRUCT([figure12, figure22]))

drawer2 = STRUCT([case123, R([2,3])(PI/2)(figures2)])


# drawer3

verts13 = [[space,space],[space,dz_figure123],[2.8,dz_figure123],[2.3,space]]
cells13 = [[1,2,4],[2,3,4]]
figure13 = STRUCT([T([3])([depht])(PROD([MKPOL([verts13,cells13,None]), Q(depht)])),
                    T([1,2])([0.6,0.5])(CUBOID([1,1,depht]))])

verts23 = [[3,space],[2.7,dz_figure123/2],[3,dz_figure123],[5.6,dz_figure123],[5.6,space]]
cells23 = [[2,3,4],[2,4,5],[2,5,1]]
figure23 = STRUCT([T([3])([depht])(PROD([MKPOL([verts23,cells23,None]), Q(depht)])),
                    T([1,2])([3.8,0.5])(CUBOID([1,1,depht]))])

verts33 = [[5.8,space],[5.8,dz_figure123],[dx_dr123-space,dz_figure123],[dx_dr123-space,space]]
cells33 = [[1,2,4],[2,3,4]]
figure33 = STRUCT([T([3])([depht])(PROD([MKPOL([verts33,cells33,None]), Q(depht)])),
                    T([1,2])([6.8,0.5])(CUBOID([1,1,depht]))])

figures3 = COLOR(WHITE)(STRUCT([figure13, figure23, figure33]))

drawer3 = STRUCT([case123, R([2,3])(PI/2)(figures3)])


# drawer4

verts14 = [[space,dz_recess+(distance*3)+(dz_dr123*2)],[space,dz_figure4],[2.3,dz_figure4],[2,dz_recess+(distance*3)+(dz_dr123*2)]]
cells14 = [[1,2,4],[2,3,4]]
figure14 = STRUCT([T([3])([depht])(PROD([MKPOL([verts14,cells14,None]), Q(depht)])),
                    T([1,2])([0.6,dz_figure4-1.2])(CUBOID([1,1,depht]))])

verts24 = [[space,space],[space,-dz_recess+(distance)+(dz_dr123*2)],[2.3,-dz_recess+(distance)+(dz_dr123*2)],[2.7,dz_figure4],
            [dx_dr4-space,dz_figure4],[dx_dr4-space,dz_recess+(distance*2)+(dz_dr123)], 
            [dx_dr4-2.5,dz_recess+(distance*2)+(dz_dr123)],[1.4,space]]
cells24 = [[1,7,8],[1,7,2],[2,7,3],[3,7,6],[3,6,5],[3,4,5]]
figure24 = STRUCT([T([3])([depht])(PROD([MKPOL([verts24,cells24,None]), Q(depht)])),
                    T([1,2])([2.8,3.5])(CUBOID([1,1,depht])), T([1,2])([0.8,2])(CUBOID([1,1,depht]))])

verts34 = [[dx_dr4-2,space],[dx_dr4-2.3,dz_figure123],[dx_dr4-space,dz_figure123],[dx_dr4-space,space]]
cells34 = [[1,2,4],[2,3,4]]
figure34 = STRUCT([T([3])([depht])(PROD([MKPOL([verts34,cells34,None]), Q(depht)])),
                    T([1,2])([2.8,0.5])(CUBOID([1,1,depht]))])

figures4 = COLOR(WHITE)(STRUCT([figure14, figure24, figure34]))

drawer4 = STRUCT([case4, R([2,3])(PI/2)(figures4)])


drawers = STRUCT([T([1,2,3])([dx_recess+distance, dy_recess, dz_recess+distance])(drawer1), 
                    T([1,2,3])([dx_recess+distance, dy_recess, dz_recess+(distance*2)+dz_dr123])(drawer2), 
                    T([1,2,3])([dx_recess+distance, dy_recess, dz_recess+(distance*3)+(dz_dr123*2)])(drawer3), 
                    T([1,2,3])([dx_recess+(distance*2)+dx_dr123, dy_recess, dz_recess+distance])(drawer4)])


#****************************** FEET ******************************/

base = CUBOID([0.3,0.3,0.01])

side_left = T([1,2])([0.05,0.05])(R([1,3])(PI/45)(CUBOID([0.01,0.2,1.8])))
side_right = T([1,2])([0.24,0.05])(R([1,3])(-PI/45)(CUBOID([0.01,0.2,1.8])))

verts = [[0,0],[-0.028,0.5],[0.2+0.028,0.5],[0.2,0]]
cells = [[1,2,3],[1,3,4]]
trapeze = R([2,3])(PI/2)(PROD([MKPOL([verts,cells,None]), Q(0.01)]))

front = T([1,2])([0.051,0.06])(trapeze)
back = T([1,2])([0.051,0.25])(trapeze)


top_side = T([1,2,3])([0.15,0.15,1.77])(CYLINDER([0.5,0.1])(30))

foot = COLOR(YELLOW)(STRUCT([base, side_left, side_right, front, back, top_side]))

feet = STRUCT([T([1,2,3])([-0.15+2,-0.15+0.8, -1.87])(foot), T([1,2,3])([-0.15-2+dx,-0.15+0.8, -1.87])(foot), 
                    T([1,2,3])([-0.15-2+dx,-0.15-0.8+dy, -1.87])(foot), T([1,2,3])([-0.15+2,-0.15-0.8+dy, -1.87])(foot)])


#****************************** COMMODE ******************************/

commode = STRUCT([outside, drawers, feet])
VIEW(commode)