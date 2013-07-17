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




#****************************** BACK ******************************

dx_back = 10
dy_back_top = 1
dy_back_low = 2
dz_back = 12


c1_fb = BEZIER(S1)([[0,0,0],[dx_back,0,0]])
c2_fb = BEZIER(S1)([[0,0,dz_back/8],[dx_back,0,dz_back/8]])
c3_fb = BEZIER(S1)([[0,0,dz_back/4],[dx_back,0,dz_back/4]])
c4_fb = BEZIER(S1)([[0,0,3*dz_back/8],[dx_back,0,3*dz_back/8]])
c5_fb = BEZIER(S1)([[0,3,2*dz_back/4],[dx_back,3,2*dz_back/4]])
cf_fb = BEZIER(S1)([[0,0,dz_back],[dx_back,0,dz_back]])

front_side_back = COLOR(BLUE)(surface([c1_fb,c2_fb,c3_fb,c4_fb,c5_fb,cf_fb]))


c1_tb = cf_fb
c2_tb = BEZIER(S1)([[0,0-0.1,dz_back+0.2],[dx_back,0-0.1,dz_back+0.2]])
c3_tb = BEZIER(S1)([[0,dy_back_top-0.1,dz_back+0.2],[dx_back,dy_back_top-0.1,dz_back+0.2]])
cf_tb = BEZIER(S1)([[0,dy_back_top,dz_back],[dx_back,dy_back_top,dz_back]])

top_side_back = COLOR(BLUE)(surface([c1_tb,c2_tb,c3_tb,cf_tb]))


c1_bb = cf_tb
c2_bb = BEZIER(S1)([[0,dy_back_top+3,2*dz_back/4],[dx_back,dy_back_top+3,2*dz_back/4]])
cf_bb = BEZIER(S1)([[0,dy_back_low,0],[dx_back,dy_back_low,0]])

back_side_back = COLOR(WHITE)(surface([c1_bb, c2_bb, cf_bb]))


c1_lb = cf_bb
c2_lb = BEZIER(S1)([[0,dy_back_low-0.1,-0.1],[dx_back,dy_back_low-0.1,-0.1]])
c3_lb = BEZIER(S1)([[0,0,-0.1],[dx_back,0,-0.1]])
cf_lb = c1_fb

low_side_back = COLOR(BLUE)(surface([c1_lb,c2_lb,c3_lb,cf_lb]))


c1_leftb = BEZIER(S1)([[0,0,0],[0,0,dz_back/8],[0,0,dz_back/4],[0,0,3*dz_back/8],[0,3,2*dz_back/4],[0,0,dz_back]])
c2_leftb = BEZIER(S1)([[-0.2,0,0],[-0.2,0,dz_back/8],[-0.2,0,dz_back/4],[-0.2,0,3*dz_back/8],[-0.2,3,2*dz_back/4],[-0.2,0,dz_back]])
c3_leftb = BEZIER(S1)([[-0.2,dy_back_low,0],[-0.2,dy_back_top+3,2*dz_back/4],[-0.2,dy_back_top,dz_back]])
cf_leftb = BEZIER(S1)([[0,dy_back_low,0],[0,dy_back_top+3,2*dz_back/4],[0,dy_back_top,dz_back]])

left_side_back = COLOR(WHITE)(surface([c1_leftb,c2_leftb,c3_leftb,cf_leftb]))


c1_lteb = BEZIER(S1)([[0,0,dz_back],[0,0-0.1,dz_back+0.2],[0,dy_back_top-0.1,dz_back+0.2],[0,dy_back_top,dz_back]])
c2_lteb = BEZIER(S1)([[0,0,dz_back],[-0.2,0-0.1,dz_back+0.2],[-0.2,dy_back_top-0.1,dz_back+0.2],[0,dy_back_top,dz_back]])
cf_lteb = BEZIER(S1)([[0,0,dz_back],[-0.2,0,dz_back],[-0.2,dy_back_top,dz_back],[0,dy_back_top,dz_back]])

left_top_edge_back = COLOR(WHITE)(surface([c1_lteb,c2_lteb,cf_lteb]))


c1_rightb = BEZIER(S1)([[dx_back,0,0],[dx_back,0,dz_back/8],[dx_back,0,dz_back/4],
						[dx_back,0,3*dz_back/8],[dx_back,3,2*dz_back/4],[dx_back,0,dz_back]])
c2_rightb = BEZIER(S1)([[dx_back+0.2,0,0],[dx_back+0.2,0,dz_back/8],[dx_back+0.2,0,dz_back/4],
						[dx_back+0.2,0,3*dz_back/8],[dx_back+0.2,3,2*dz_back/4],[dx_back+0.2,0,dz_back]])
c3_rightb = BEZIER(S1)([[dx_back+0.2,dy_back_low,0],[dx_back+0.2,dy_back_top+3,2*dz_back/4],[dx_back+0.2,dy_back_top,dz_back]])
cf_rightb = BEZIER(S1)([[dx_back,dy_back_low,0],[dx_back,dy_back_top+3,2*dz_back/4],[dx_back,dy_back_top,dz_back]])

right_side_back = COLOR(WHITE)(surface([c1_rightb, c2_rightb, c3_rightb, cf_rightb]))


c1_rteb = BEZIER(S1)([[dx_back,0,dz_back],[dx_back,0-0.1,dz_back+0.2],
						[dx_back,dy_back_top-0.1,dz_back+0.2],[dx_back,dy_back_top,dz_back]])
c2_rteb = BEZIER(S1)([[dx_back,0,dz_back],[dx_back+0.2,0-0.1,dz_back+0.2],
					[dx_back+0.2,dy_back_top-0.1,dz_back+0.2],[dx_back,dy_back_top,dz_back]])
cf_rteb = BEZIER(S1)([[dx_back,0,dz_back],[dx_back+0.2,0,dz_back],[dx_back+0.2,dy_back_top,dz_back],[dx_back,dy_back_top,dz_back]])

right_top_edge_back = COLOR(WHITE)(surface([c1_rteb, c2_rteb, cf_rteb]))


c1_lleb = BEZIER(S1)([[0,dy_back_low,0],[0,dy_back_low-0.1,-0.1],[0,0,-0.1],[0,0,0]])
c2_lleb = BEZIER(S1)([[0,dy_back_low,0],[-0.2,dy_back_low-0.1,-0.1],[-0.2,0,-0.1],[0,0,0]])
cf_lleb = BEZIER(S1)([[0,dy_back_low,0],[-0.2,dy_back_low,0],[-0.2,0,0],[0,0,0]])

left_low_edge_back = COLOR(WHITE)(surface([c1_lleb,c2_lleb,cf_lleb]))


c1_rleb = BEZIER(S1)([[dx_back,dy_back_low,0],[dx_back,dy_back_low-0.1,-0.1],[dx_back,0,-0.1],[dx_back,0,0]])
c2_rleb = BEZIER(S1)([[dx_back,dy_back_low,0],[dx_back+0.2,dy_back_low-0.1,-0.1],[dx_back+0.2,0,-0.1],[dx_back,0,0]])
cf_rleb = BEZIER(S1)([[dx_back,dy_back_low,0],[dx_back+0.2,dy_back_low,0],[dx_back+0.2,0,0],[dx_back,0,0]])

right_low_edge_back = COLOR(WHITE)(surface([c1_rleb,c2_rleb,cf_rleb]))


back = STRUCT([front_side_back, top_side_back, back_side_back, low_side_back, left_side_back, 
					left_top_edge_back, right_side_back, right_top_edge_back, left_low_edge_back, right_low_edge_back])






#****************************** SEAT ******************************/

dz_seat_back = 2
dz_seat_front = 3
dx_seat = dx_back
dy_seat = 10


c1_bs = cf_bb
cf_bs = BEZIER(S1)([[0,dy_back_low-0.6,-dz_seat_back],[dx_seat,dy_back_low-0.6,-dz_seat_back]])

back_side_seat = COLOR(WHITE)(surface([c1_bs,cf_bs]))


c1_ts = c1_bs
cf_ts = BEZIER(S1)([[0,dy_back_low-dy_seat,-1],[dx_seat,dy_back_low-dy_seat,-1]])

top_side_seat = COLOR(BLUE)(surface([c1_ts,cf_ts]))


c1_fs = cf_ts
c2_fs = BEZIER(S1)([[0,dy_back_low-dy_seat-5,-1.5],[dx_seat,dy_back_low-dy_seat-5,-1.5]])
c3_fs = BEZIER(S1)([[0,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1],[dx_seat,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1]])
cf_fs = BEZIER(S1)([[0,dy_back_low-dy_seat-1,-1-dz_seat_front],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]])

front_side_seat = COLOR(BLUE)(surface([c1_fs,c2_fs,c3_fs,cf_fs]))


c1_ls = cf_fs
c2_ls = BEZIER(S1)([[0,dy_back_low-0.6-0.1,-dz_seat_back-0.4],[dx_seat,dy_back_low-0.6-0.1,-dz_seat_back-0.4]])
cf_ls = cf_bs

low_side_seat = COLOR(WHITE)(surface([c1_ls,c2_ls,cf_ls]))


c1_lefts = BEZIER(S1)([[0,dy_back_low,0],[0,dy_back_low-dy_seat,-1]])
c2_lefts = BEZIER(S1)([[0-0.2,dy_back_low,0],[0-0.2,dy_back_low-dy_seat,-1]])
c3_lefts = BEZIER(S1)([[0-0.2,dy_back_low-0.6,-dz_seat_back],[0-0.2,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[0-0.2,dy_back_low-dy_seat-1,-1-dz_seat_front]])
cf_lefts = BEZIER(S1)([[0,dy_back_low-0.6,-dz_seat_back],[0,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[0,dy_back_low-dy_seat-1,-1-dz_seat_front]])

left_side_seat = COLOR(WHITE)(surface([c1_lefts,c2_lefts,c3_lefts,cf_lefts]))


c1_rights = BEZIER(S1)([[dx_seat,dy_back_low,0],[dx_seat,dy_back_low-dy_seat,-1]])
c2_rights = BEZIER(S1)([[dx_seat+0.2,dy_back_low,0],[dx_seat+0.2,dy_back_low-dy_seat,-1]])
c3_rights = BEZIER(S1)([[dx_seat+0.2,dy_back_low-0.6,-dz_seat_back],[dx_seat+0.2,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[dx_seat+0.2,dy_back_low-dy_seat-1,-1-dz_seat_front]])
cf_rights = BEZIER(S1)([[dx_seat,dy_back_low-0.6,-dz_seat_back],[dx_seat,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]])

right_side_seat = COLOR(WHITE)(surface([c1_rights,c2_rights,c3_rights,cf_rights]))


c1_lfes = BEZIER(S1)([[0,dy_back_low-dy_seat,-1],[0,dy_back_low-dy_seat-5,-1.5],
						[0,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1],[0,dy_back_low-dy_seat-1,-1-dz_seat_front]])
c2_lfes = BEZIER(S1)([[0,dy_back_low-dy_seat,-1],[0-0.2,dy_back_low-dy_seat-2.5,-1.5],
						[0-0.2,dy_back_low-dy_seat-1-0.2,-1-dz_seat_front],[0,dy_back_low-dy_seat-1,-1-dz_seat_front]])
cf_lfes = BEZIER(S1)([[0,dy_back_low-dy_seat,-1],[0-0.2,dy_back_low-dy_seat,-1],
						[0-0.2,dy_back_low-dy_seat-1,-1-dz_seat_front],[0,dy_back_low-dy_seat-1,-1-dz_seat_front]])

left_front_edge_seat = COLOR(WHITE)(surface([c1_lfes,c2_lfes,cf_lfes]))


c1_rfes = BEZIER(S1)([[dx_seat,dy_back_low-dy_seat,-1],[dx_seat,dy_back_low-dy_seat-5,-1.5],
						[dx_seat,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]])
c2_rfes = BEZIER(S1)([[dx_seat,dy_back_low-dy_seat,-1],[dx_seat+0.2,dy_back_low-dy_seat-2.5,-1.5],
						[dx_seat+0.2,dy_back_low-dy_seat-1-0.2,-1-dz_seat_front],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]])
cf_rfes = BEZIER(S1)([[dx_seat,dy_back_low-dy_seat,-1],[dx_seat+0.2,dy_back_low-dy_seat,-1],
						[dx_seat+0.2,dy_back_low-dy_seat-1,-1-dz_seat_front],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]])

right_front_edge_seat = COLOR(WHITE)(surface([c1_rfes,c2_rfes,cf_rfes]))


c1_lbes = BEZIER(S1)([[0,dy_back_low,0],[0,dy_back_low-0.6,-dz_seat_back]])
cf_lbes = BEZIER(S1)([[0,dy_back_low,0],[0-0.2,dy_back_low,0],
						[0-0.2,dy_back_low-0.6,-dz_seat_back],[0,dy_back_low-0.6,-dz_seat_back]])

left_back_edge_seat = COLOR(WHITE)(surface([c1_lbes,cf_lbes]))


c1_rbes = BEZIER(S1)([[dx_seat,dy_back_low,0],[dx_seat,dy_back_low-0.6,-dz_seat_back]])
cf_rbes = BEZIER(S1)([[dx_seat,dy_back_low,0],[dx_seat+0.2,dy_back_low,0],
						[dx_seat+0.2,dy_back_low-0.6,-dz_seat_back],[dx_seat,dy_back_low-0.6,-dz_seat_back]])

right_back_edge_seat = COLOR(WHITE)(surface([c1_rbes,cf_rbes]))



seat = STRUCT([back_side_seat, top_side_seat, front_side_seat, low_side_seat, left_side_seat, right_side_seat, 
					left_front_edge_seat, right_front_edge_seat, left_back_edge_seat, right_back_edge_seat])





#****************************** PILLOW ******************************/


pillows = R([2,3])(-PI/10)(STRUCT([back, seat]))




#****************************** LEGS ******************************/


# support function

def circumference(r,dx,dy,dz):
	def f0(v):
		return [r*COS(v[0])+dx, r*SIN(v[0])+dy, dz]
	return f0
	


domCyl = PROD([INTERVALS(2*PI)(24), INTERVALS(1)(1)])

def cylinder(curves):
	return MAP(BEZIER(S2)(curves))(domCyl)


def torus(R,r):
	def torus0(arg):
		a = arg[0]
		b = arg[1]
		u = (r*COS(a)+R) * COS(b)
		v = (r*COS(a)+R) * SIN(b)
		w = r*SIN(a)
		return [u,v,w]
	return torus0
	


def circle(r, h):
	domain = PROD([INTERVALS(2*PI)(24), INTERVALS(r)(1)])
	def mapping(v):
		a = v[0]
		r = v[1]

		return [r*COS(a), r*SIN(a), h]
	

	model = MAP(mapping)(domain)

	return model


radius = 0.15
distance = dx_back+2
h1 = 8
h2 = 10.1


domain_angle_leg_1 = PROD([INTERVALS(2*PI)(20), INTERVALS(PI/3)(20)])

angle_leg1 = R([2,3])(PI/6)(R([1,2])(PI)(R([1,3])(PI/2)(MAP(torus(radius*2,radius))(domain_angle_leg_1))))


domain_angle_leg_2 = PROD([INTERVALS(2*PI)(20), INTERVALS(PI/2)(20)])

angle_leg2_left = R([1,3])(PI/2)(R([2,3])(PI/2)(MAP(torus(radius*6,radius))(domain_angle_leg_2)))

angle_leg2_right = R([1,3])(PI/2)(R([2,3])(-PI/2)(MAP(torus(radius*6,radius))(domain_angle_leg_2)))



cyl1_left = STRUCT([cylinder([circumference(radius-0.05,0,0,0), circumference(radius,0,0,h1)]), 
				T([2,3])([2*radius,h1])(angle_leg1), 
				T([2,3])([-(radius)/2,5])(CUBOID([1,radius,1.5]))])

cyl1_right = STRUCT([cylinder([circumference(radius-0.05,0,0,0), circumference(radius,0,0,h1)]), 
				T([2,3])([2*radius,h1])(angle_leg1), 
				T([1,2,3])([-1,-(radius)/2,5])(CUBOID([1,radius,1.5]))])


cyl2_left = T([2,3])([radius,h1+(radius*2)-0.04])(R([2,3])(-PI/3)
	(STRUCT([cylinder([circumference(radius,0,0,0), circumference(radius,0,0,dy_seat)]), 
			T([1,3])([radius*6,dy_seat])(angle_leg2_left)])))

cyl2_right = T([2,3])([radius,h1+(radius*2)-0.04])(R([2,3])(-PI/3)
	(STRUCT([cylinder([circumference(radius,0,0,0), circumference(radius,0,0,dy_seat)]), 
			T([1,3])([-radius*6,dy_seat])(angle_leg2_right)])))


cyl3_left = T([2,3])([dy_seat+4,5])(R([2,3])(PI/4)
	(STRUCT([cylinder([circumference(radius-0.05,0,0,0),circumference(radius,0,0,h2)]), 
			T([2,3])([-(radius)/2,6])(CUBOID([1,radius,1.5]))])))

cyl3_right = T([2,3])([dy_seat+4,5])(R([2,3])(PI/4)
	(STRUCT([cylinder([circumference(radius-0.05,0,0,0),circumference(radius,0,0,h2)]), 
			T([1,2,3])([-1,-(radius)/2,6])(CUBOID([1,radius,1.5]))])))


pillars_left = R([2,3])(-PI/10)(STRUCT([cyl1_left, cyl2_left, cyl3_left]))
pillars_right = R([2,3])(-PI/10)(STRUCT([cyl1_right, cyl2_right, cyl3_right]))


r_base = (radius-0.05)*2
h_base = 0.15

base = STRUCT([cylinder([circumference(r_base,0,0,0),circumference(r_base,0,0,h_base)]), 
				circle(r_base,0),circle(r_base,h_base)])


left_leg = STRUCT([pillars_left, T([2,3])([0.02,-0.1])(base), T([2,3])([dy_seat+4.81,0.35])(base)])

right_leg = STRUCT([pillars_right, T([2,3])([0.02,-0.1])(base), T([2,3])([dy_seat+4.81,0.35])(base)])


left_leg = T([1,2,3])([-1,-dy_seat, -(h1-2.5)])(left_leg)

right_leg = T([1,2,3])([-1+distance,-dy_seat, -(h1-2.5)])(right_leg)


legs = COLOR(YELLOW)(STRUCT([left_leg, right_leg]))



#****************************** ARMRESTS ******************************/

dx_arm = 0.8
dy_arm = 10
dz_arm= 0.8
curve_depht = 0.5


c1 = BEZIER(S1)([[0, 0, dz_arm],[dx_arm, 0, dz_arm]])
c2 = BEZIER(S1)([[-curve_depht, -curve_depht, dz_arm],[curve_depht+dx_arm, -curve_depht, dz_arm]])
c3 = BEZIER(S1)([[-curve_depht, -curve_depht, 0],[curve_depht+dx_arm, -curve_depht, 0]])
c4 = BEZIER(S1)([[0, 0, 0],[dx_arm, 0, 0]])

c5 = BEZIER(S1)([[0, 0, dz_arm],[0, dy_arm, dz_arm]])
c6 = BEZIER(S1)([[-curve_depht, -curve_depht, dz_arm],[-curve_depht, curve_depht+dy_arm, dz_arm]])
c7 = BEZIER(S1)([[-curve_depht, -curve_depht, 0],[-curve_depht, curve_depht+dy_arm, 0]])
c8 = BEZIER(S1)([[0, 0, 0],[0, dy_arm, 0]])

c9 = BEZIER(S1)([[0, dy_arm, dz_arm],[dx_arm, dy_arm, dz_arm]])
c10 = BEZIER(S1)([[-curve_depht, curve_depht+dy_arm, dz_arm],[curve_depht+dx_arm, curve_depht+dy_arm, dz_arm]])
c11 = BEZIER(S1)([[-curve_depht, curve_depht+dy_arm, 0],[curve_depht+dx_arm, curve_depht+dy_arm, 0]])
c12 = BEZIER(S1)([[0, dy_arm, 0],[dx_arm, dy_arm, 0]])

c13 = BEZIER(S1)([[dx_arm, 0, dz_arm],[dx_arm, dy_arm, dz_arm]])
c14 = BEZIER(S1)([[curve_depht+dx_arm, -curve_depht, dz_arm],[curve_depht+dx_arm, curve_depht+dy_arm, dz_arm]])
c15 = BEZIER(S1)([[curve_depht+dx_arm, -curve_depht, 0],[curve_depht+dx_arm, curve_depht+dy_arm, 0]])
c16 = BEZIER(S1)([[dx_arm, 0, 0],[dx_arm, dy_arm, 0]])


armrest = R([2,3])((PI/6)-(PI/10))(COLOR(WHITE)(STRUCT([CUBOID([dx_arm,dy_arm,dz_arm]), surface([c1,c2,c3,c4]), 
					surface([c5,c6,c7,c8]), surface([c9,c10,c11,c12]), surface([c13,c14,c15,c16])])))


armrests = STRUCT([T([1,2,3])([-dx_arm-0.6,-8.5,2.2])(armrest), 
						T([1,2,3])([-dx_arm-0.6+distance,-8.5,2.2])(armrest)])



#****************************** ARMCHAIR ******************************/

armchair = STRUCT([pillows, legs, armrests])
VIEW(armchair)
