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


#****************************** SEAT ******************************/

dx_seat = 6
dy_seat = 8
dz_seat= 0.5
curve_depht = 0.5


c1 = BEZIER(S1)([[0, 0, dz_seat],[dx_seat, 0, dz_seat]])
c2 = BEZIER(S1)([[-curve_depht, -curve_depht, dz_seat/2],[curve_depht+dx_seat, -curve_depht, dz_seat/2]])
c3 = BEZIER(S1)([[0, 0, 0],[dx_seat, 0, 0]])

c4 = BEZIER(S1)([[0, 0, dz_seat],[0, dy_seat, dz_seat]])
c5 = BEZIER(S1)([[-curve_depht, -curve_depht, dz_seat/2],[-curve_depht, curve_depht+dy_seat, dz_seat/2]])
c6 = BEZIER(S1)([[0, 0, 0],[0, dy_seat, 0]])

c7 = BEZIER(S1)([[0, dy_seat, dz_seat],[dx_seat, dy_seat, dz_seat]])
c8 = BEZIER(S1)([[-curve_depht, curve_depht+dy_seat, dz_seat/2],[curve_depht+dx_seat, curve_depht+dy_seat, dz_seat/2]])
c9 = BEZIER(S1)([[0, dy_seat, 0],[dx_seat, dy_seat, 0]])

c10 = BEZIER(S1)([[dx_seat, 0, dz_seat],[dx_seat, dy_seat, dz_seat]])
c11 = BEZIER(S1)([[curve_depht+dx_seat, -curve_depht, dz_seat/2],[curve_depht+dx_seat, curve_depht+dy_seat, dz_seat/2]])
c12 = BEZIER(S1)([[dx_seat, 0, 0],[dx_seat, dy_seat, 0]])


seat = T([1,2])([-dx_seat/2, -dy_seat/2])(COLOR(WHITE)(STRUCT([CUBOID([dx_seat,dy_seat,dz_seat]), surface([c1,c2,c3]), 
                    surface([c4,c5,c6]), surface([c7,c8,c9]), surface([c10,c11,c12])])))



#****************************** FRONT LEGS ******************************/

dz_front_leg = 8

c1 = BEZIER(S1)([[0,0.7,dz_front_leg],[0.5,0.7,dz_front_leg]])
c2 = BEZIER(S1)([[0,0.7,dz_front_leg],[0.25,0,dz_front_leg],[0.5,0.7,dz_front_leg]])

c3 = BEZIER(S1)([[0,0.7,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]])
c4 = BEZIER(S1)([[0,0.7,dz_front_leg/2],[0.25,0,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]])

c5 = BEZIER(S1)([[0,0.4,0],[0.5,0.4,0]])
c6 = BEZIER(S1)([[0,0.4,0],[0.25,0,0],[0.5,0.4,0]])

front_leg = STRUCT([surface([c1,c2]), surface([c3,c4]), surface([c1,c3]), surface([c2,c4]), surface([c5,c6]), 
                        surface([c3,c5]), surface([c4,c6])])

front_legs = STRUCT([T([1,2,3])([-dx_seat/2-0.4,-dy_seat/2-0.7,-dz_front_leg+dz_seat+0.1])(COLOR(BLACK)(front_leg)), 
                        T([1,2,3])([dx_seat/2-0.1,-dy_seat/2-0.7,-dz_front_leg+dz_seat+0.1])(COLOR(WHITE)(front_leg))])



#****************************** BACK LEGS ******************************/

dz_back_leg = 16

c1 = BEZIER(S1)([[0,0.7,3*dz_back_leg/4],[0.5,0.7,3*dz_back_leg/4]])
c2 = BEZIER(S1)([[0,0.7,3*dz_back_leg/4],[0.25,0,3*dz_back_leg/4],[0.5,0.7,3*dz_back_leg/4]])

c3 = BEZIER(S1)([[0,0.7,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]])
c4 = BEZIER(S1)([[0,0.7,dz_front_leg/2],[0.25,0,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]])

c5 = BEZIER(S1)([[0,0.4,0],[0.5,0.4,0]])
c6 = BEZIER(S1)([[0,0.4,0],[0.25,0,0],[0.5,0.4,0]])

c7 = BEZIER(S1)([[0,0.4-0.5,dz_back_leg],[0.5,0.4-0.5,dz_back_leg]])
c8 = BEZIER(S1)([[0,0.4-0.5,dz_back_leg],[0.25,0-0.5,dz_back_leg],[0.5,0.4-0.5,dz_back_leg]])


back_leg = R([1,2])(PI)(STRUCT([surface([c1,c2]), surface([c3,c4]), surface([c1,c3]), surface([c2,c4]), surface([c5,c6]), 
                        surface([c3,c5]), surface([c4,c6]), surface([c7,c8]), surface([c1,c7]), surface([c2,c8])]))

back_legs = STRUCT([T([1,2,3])([-dx_seat/2+0.1,dy_seat/2+0.7,-dz_front_leg+dz_seat+0.1])(COLOR(WHITE)(back_leg)), 
                        T([1,2,3])([dx_seat/2+0.4,dy_seat/2+0.7,-dz_front_leg+dz_seat+0.1])(COLOR(BLACK)(back_leg))])

#****************************** BOARDS ******************************/

horizontal_board = CUBOID([dx_seat, 0.1, 0.4])
vertical_board = CUBOID([0.1, dy_seat, 0.4])


dy_inclination = 0.5

c1 = BEZIER(S1)([[-dx_seat/2,0,0],[0,dy_inclination,0],[dx_seat/2,0,0]])
c2 = BEZIER(S1)([[-dx_seat/2,0,0.6],[0,dy_inclination,0.6],[dx_seat/2,0,0.6]])

c3 = BEZIER(S1)([[-dx_seat/2,0.1,0],[0,dy_inclination+0.1,0],[dx_seat/2,0.1,0]])
c4 = BEZIER(S1)([[-dx_seat/2,0.1,0.6],[0,dy_inclination+0.1,0.6],[dx_seat/2,0.1,0.6]])

back_board = R([2,3])(-PI/20)(STRUCT([surface([c1,c2]), surface([c3,c4]), surface([c1,c3]), surface([c2,c4])]))


boards = STRUCT([T([1,2,3])([-dx_seat/2, -dy_seat/2-0.2, -3*dz_front_leg/8])(COLOR(WHITE)(horizontal_board)), 
                        T([1,2,3])([-dx_seat/2-0.2, -dy_seat/2, -4*dz_front_leg/8])(COLOR(BLACK)(vertical_board)), 
                        T([1,2,3])([-dx_seat/2-0.2, -dy_seat/2, -2*dz_front_leg/8])(COLOR(WHITE)(vertical_board)), 
                        T([1,2,3])([-dx_seat/2, dy_seat/2+0.1, -3*dz_front_leg/8])(COLOR(BLACK)(horizontal_board)), 
                        T([1,2,3])([+dx_seat/2+0.1, -dy_seat/2, -4*dz_front_leg/8])(COLOR(WHITE)(vertical_board)), 
                        T([1,2,3])([+dx_seat/2+0.1, -dy_seat/2, -2*dz_front_leg/8])(COLOR(BLACK)(vertical_board)), 
                        T([2,3])([dy_seat/2+0.2, 5*dz_front_leg/8])(COLOR(WHITE)(back_board)), 
                        T([2,3])([dy_seat/2+0.7, 7*dz_front_leg/8+0.7])(COLOR(BLACK)(back_board))])

#****************************** CHAIR ******************************/

chair = STRUCT([seat, front_legs, back_legs, boards])
VIEW(chair)
