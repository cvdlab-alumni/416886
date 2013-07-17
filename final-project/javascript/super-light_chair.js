var dom2D = DOMAIN([[0,1],[0,1]])([30,30]);

function surface(curves){
	return MAP(BEZIER(S1)(curves))(dom2D);
}

var cream = [1.5,253*1.5/255,208*1.5/255];
var black = [0,0,0];


/****************************** SEAT ******************************/

dx_seat = 6;
dy_seat = 8;
dz_seat= 0.5;
curve_depht = 0.5;


c1 = BEZIER(S0)([[0, 0, dz_seat],[dx_seat, 0, dz_seat]]);
c2 = BEZIER(S0)([[-curve_depht, -curve_depht, dz_seat/2],[curve_depht+dx_seat, -curve_depht, dz_seat/2]]);
c3 = BEZIER(S0)([[0, 0, 0],[dx_seat, 0, 0]]);

c4 = BEZIER(S0)([[0, 0, dz_seat],[0, dy_seat, dz_seat]]);
c5 = BEZIER(S0)([[-curve_depht, -curve_depht, dz_seat/2],[-curve_depht, curve_depht+dy_seat, dz_seat/2]]);
c6 = BEZIER(S0)([[0, 0, 0],[0, dy_seat, 0]]);

c7 = BEZIER(S0)([[0, dy_seat, dz_seat],[dx_seat, dy_seat, dz_seat]]);
c8 = BEZIER(S0)([[-curve_depht, curve_depht+dy_seat, dz_seat/2],[curve_depht+dx_seat, curve_depht+dy_seat, dz_seat/2]]);
c9 = BEZIER(S0)([[0, dy_seat, 0],[dx_seat, dy_seat, 0]]);

c10 = BEZIER(S0)([[dx_seat, 0, dz_seat],[dx_seat, dy_seat, dz_seat]]);
c11 = BEZIER(S0)([[curve_depht+dx_seat, -curve_depht, dz_seat/2],[curve_depht+dx_seat, curve_depht+dy_seat, dz_seat/2]]);
c12 = BEZIER(S0)([[dx_seat, 0, 0],[dx_seat, dy_seat, 0]]);


var seat = T([0,1])([-dx_seat/2, -dy_seat/2])(COLOR(cream)(STRUCT([CUBOID([dx_seat,dy_seat,dz_seat]), surface([c1,c2,c3]), 
					surface([c4,c5,c6]), surface([c7,c8,c9]), surface([c10,c11,c12])])));



/****************************** FRONT LEGS ******************************/

dz_front_leg = 8;

c1 = BEZIER(S0)([[0,0.7,dz_front_leg],[0.5,0.7,dz_front_leg]]);
c2 = BEZIER(S0)([[0,0.7,dz_front_leg],[0.25,0,dz_front_leg],[0.5,0.7,dz_front_leg]]);

c3 = BEZIER(S0)([[0,0.7,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]]);
c4 = BEZIER(S0)([[0,0.7,dz_front_leg/2],[0.25,0,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]]);

c5 = BEZIER(S0)([[0,0.4,0],[0.5,0.4,0]]);
c6 = BEZIER(S0)([[0,0.4,0],[0.25,0,0],[0.5,0.4,0]]);

var front_leg = STRUCT([surface([c1,c2]), surface([c3,c4]), surface([c1,c3]), surface([c2,c4]), surface([c5,c6]), 
						surface([c3,c5]), surface([c4,c6])]);

var front_legs = STRUCT([T([0,1,2])([-dx_seat/2-0.4,-dy_seat/2-0.7,-dz_front_leg+dz_seat+0.1])(COLOR(black)(front_leg)), 
						T([0,1,2])([dx_seat/2-0.1,-dy_seat/2-0.7,-dz_front_leg+dz_seat+0.1])(COLOR(cream)(front_leg))]);



/****************************** BACK LEGS ******************************/

dz_back_leg = 16;

c1 = BEZIER(S0)([[0,0.7,3*dz_back_leg/4],[0.5,0.7,3*dz_back_leg/4]]);
c2 = BEZIER(S0)([[0,0.7,3*dz_back_leg/4],[0.25,0,3*dz_back_leg/4],[0.5,0.7,3*dz_back_leg/4]]);

c3 = BEZIER(S0)([[0,0.7,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]]);
c4 = BEZIER(S0)([[0,0.7,dz_front_leg/2],[0.25,0,dz_front_leg/2],[0.5,0.7,dz_front_leg/2]]);

c5 = BEZIER(S0)([[0,0.4,0],[0.5,0.4,0]]);
c6 = BEZIER(S0)([[0,0.4,0],[0.25,0,0],[0.5,0.4,0]]);

c7 = BEZIER(S0)([[0,0.4-0.5,dz_back_leg],[0.5,0.4-0.5,dz_back_leg]]);
c8 = BEZIER(S0)([[0,0.4-0.5,dz_back_leg],[0.25,0-0.5,dz_back_leg],[0.5,0.4-0.5,dz_back_leg]]);


var back_leg = R([0,1])([PI])(STRUCT([surface([c1,c2]), surface([c3,c4]), surface([c1,c3]), surface([c2,c4]), surface([c5,c6]), 
						surface([c3,c5]), surface([c4,c6]), surface([c7,c8]), surface([c1,c7]), surface([c2,c8])]));

var back_legs = STRUCT([T([0,1,2])([-dx_seat/2+0.1,dy_seat/2+0.7,-dz_front_leg+dz_seat+0.1])(COLOR(cream)(back_leg)), 
						T([0,1,2])([dx_seat/2+0.4,dy_seat/2+0.7,-dz_front_leg+dz_seat+0.1])(COLOR(black)(back_leg))]);

/****************************** BOARDS ******************************/

var horizontal_board = CUBOID([dx_seat, 0.1, 0.4]);
var vertical_board = CUBOID([0.1, dy_seat, 0.4]);


dy_inclination = 0.5;

c1 = BEZIER(S0)([[-dx_seat/2,0,0],[0,dy_inclination,0],[dx_seat/2,0,0]]);
c2 = BEZIER(S0)([[-dx_seat/2,0,0.6],[0,dy_inclination,0.6],[dx_seat/2,0,0.6]]);

c3 = BEZIER(S0)([[-dx_seat/2,0.1,0],[0,dy_inclination+0.1,0],[dx_seat/2,0.1,0]]);
c4 = BEZIER(S0)([[-dx_seat/2,0.1,0.6],[0,dy_inclination+0.1,0.6],[dx_seat/2,0.1,0.6]]);

var back_board = R([1,2])([-PI/20])(STRUCT([surface([c1,c2]), surface([c3,c4]), surface([c1,c3]), surface([c2,c4])]));


var boards = STRUCT([T([0,1,2])([-dx_seat/2, -dy_seat/2-0.2, -3*dz_front_leg/8])(COLOR(cream)(horizontal_board)), 
						T([0,1,2])([-dx_seat/2-0.2, -dy_seat/2, -4*dz_front_leg/8])(COLOR(black)(vertical_board)), 
						T([0,1,2])([-dx_seat/2-0.2, -dy_seat/2, -2*dz_front_leg/8])(COLOR(cream)(vertical_board)), 
						T([0,1,2])([-dx_seat/2, dy_seat/2+0.1, -3*dz_front_leg/8])(COLOR(black)(horizontal_board)), 
						T([0,1,2])([+dx_seat/2+0.1, -dy_seat/2, -4*dz_front_leg/8])(COLOR(cream)(vertical_board)), 
						T([0,1,2])([+dx_seat/2+0.1, -dy_seat/2, -2*dz_front_leg/8])(COLOR(black)(vertical_board)), 
						T([1,2])([dy_seat/2+0.2, 5*dz_front_leg/8])(COLOR(cream)(back_board)), 
						T([1,2])([dy_seat/2+0.7, 7*dz_front_leg/8+0.7])(COLOR(black)(back_board))]);

/****************************** CHAIR ******************************/

var chair = STRUCT([seat, front_legs, back_legs, boards]);
DRAW(chair);
