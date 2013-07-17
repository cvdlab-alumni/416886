var dom2D = DOMAIN([[0,1],[0,1]])([40,40]);

function surface(curves){
	return MAP(BEZIER(S1)(curves))(dom2D);
}

var blue_persia = [42/255, 82/255, 190/255];
var white = [1.5,1.5,1.5];
var gold = [218/255, 165/255, 32/255];



/****************************** BACK ******************************/

dx_back = 10;
dy_back_top = 1;
dy_back_low = 2;
dz_back = 12;


c1_fb = BEZIER(S0)([[0,0,0],[dx_back,0,0]]);
c2_fb = BEZIER(S0)([[0,0,dz_back/8],[dx_back,0,dz_back/8]]);
c3_fb = BEZIER(S0)([[0,0,dz_back/4],[dx_back,0,dz_back/4]]);
c4_fb = BEZIER(S0)([[0,0,3*dz_back/8],[dx_back,0,3*dz_back/8]]);
c5_fb = BEZIER(S0)([[0,3,2*dz_back/4],[dx_back,3,2*dz_back/4]]);
cf_fb = BEZIER(S0)([[0,0,dz_back],[dx_back,0,dz_back]]);

var front_side_back = COLOR(blue_persia)(surface([c1_fb,c2_fb,c3_fb,c4_fb,c5_fb,cf_fb]));


c1_tb = cf_fb;
c2_tb = BEZIER(S0)([[0,0-0.1,dz_back+0.2],[dx_back,0-0.1,dz_back+0.2]]);
c3_tb = BEZIER(S0)([[0,dy_back_top-0.1,dz_back+0.2],[dx_back,dy_back_top-0.1,dz_back+0.2]]);
cf_tb = BEZIER(S0)([[0,dy_back_top,dz_back],[dx_back,dy_back_top,dz_back]]);

var top_side_back = COLOR(blue_persia)(surface([c1_tb,c2_tb,c3_tb,cf_tb]));


c1_bb = cf_tb;
c2_bb = BEZIER(S0)([[0,dy_back_top+3,2*dz_back/4],[dx_back,dy_back_top+3,2*dz_back/4]]);
cf_bb = BEZIER(S0)([[0,dy_back_low,0],[dx_back,dy_back_low,0]]);

var back_side_back = COLOR(white)(surface([c1_bb, c2_bb, cf_bb]));


c1_lb = cf_bb;
c2_lb = BEZIER(S0)([[0,dy_back_low-0.1,-0.1],[dx_back,dy_back_low-0.1,-0.1]]);
c3_lb = BEZIER(S0)([[0,0,-0.1],[dx_back,0,-0.1]]);
cf_lb = c1_fb;

var low_side_back = COLOR(blue_persia)(surface([c1_lb,c2_lb,c3_lb,cf_lb]));


c1_leftb = BEZIER(S0)([[0,0,0],[0,0,dz_back/8],[0,0,dz_back/4],[0,0,3*dz_back/8],[0,3,2*dz_back/4],[0,0,dz_back]]);
c2_leftb = BEZIER(S0)([[-0.2,0,0],[-0.2,0,dz_back/8],[-0.2,0,dz_back/4],[-0.2,0,3*dz_back/8],[-0.2,3,2*dz_back/4],[-0.2,0,dz_back]]);
c3_leftb = BEZIER(S0)([[-0.2,dy_back_low,0],[-0.2,dy_back_top+3,2*dz_back/4],[-0.2,dy_back_top,dz_back]]);
cf_leftb = BEZIER(S0)([[0,dy_back_low,0],[0,dy_back_top+3,2*dz_back/4],[0,dy_back_top,dz_back]]);

var left_side_back = COLOR(white)(surface([c1_leftb,c2_leftb,c3_leftb,cf_leftb]));


c1_lteb = BEZIER(S0)([[0,0,dz_back],[0,0-0.1,dz_back+0.2],[0,dy_back_top-0.1,dz_back+0.2],[0,dy_back_top,dz_back]]);
c2_lteb = BEZIER(S0)([[0,0,dz_back],[-0.2,0-0.1,dz_back+0.2],[-0.2,dy_back_top-0.1,dz_back+0.2],[0,dy_back_top,dz_back]]);
cf_lteb = BEZIER(S0)([[0,0,dz_back],[-0.2,0,dz_back],[-0.2,dy_back_top,dz_back],[0,dy_back_top,dz_back]]);

var left_top_edge_back = COLOR(white)(surface([c1_lteb,c2_lteb,cf_lteb]));


c1_rightb = BEZIER(S0)([[dx_back,0,0],[dx_back,0,dz_back/8],[dx_back,0,dz_back/4],
						[dx_back,0,3*dz_back/8],[dx_back,3,2*dz_back/4],[dx_back,0,dz_back]]);
c2_rightb = BEZIER(S0)([[dx_back+0.2,0,0],[dx_back+0.2,0,dz_back/8],[dx_back+0.2,0,dz_back/4],
						[dx_back+0.2,0,3*dz_back/8],[dx_back+0.2,3,2*dz_back/4],[dx_back+0.2,0,dz_back]]);
c3_rightb = BEZIER(S0)([[dx_back+0.2,dy_back_low,0],[dx_back+0.2,dy_back_top+3,2*dz_back/4],[dx_back+0.2,dy_back_top,dz_back]]);
cf_rightb = BEZIER(S0)([[dx_back,dy_back_low,0],[dx_back,dy_back_top+3,2*dz_back/4],[dx_back,dy_back_top,dz_back]]);

var right_side_back = COLOR(white)(surface([c1_rightb, c2_rightb, c3_rightb, cf_rightb]));


c1_rteb = BEZIER(S0)([[dx_back,0,dz_back],[dx_back,0-0.1,dz_back+0.2],
						[dx_back,dy_back_top-0.1,dz_back+0.2],[dx_back,dy_back_top,dz_back]]);
c2_rteb = BEZIER(S0)([[dx_back,0,dz_back],[dx_back+0.2,0-0.1,dz_back+0.2],
					[dx_back+0.2,dy_back_top-0.1,dz_back+0.2],[dx_back,dy_back_top,dz_back]]);
cf_rteb = BEZIER(S0)([[dx_back,0,dz_back],[dx_back+0.2,0,dz_back],[dx_back+0.2,dy_back_top,dz_back],[dx_back,dy_back_top,dz_back]]);

var right_top_edge_back = COLOR(white)(surface([c1_rteb, c2_rteb, cf_rteb]));


c1_lleb = BEZIER(S0)([[0,dy_back_low,0],[0,dy_back_low-0.1,-0.1],[0,0,-0.1],[0,0,0]]);
c2_lleb = BEZIER(S0)([[0,dy_back_low,0],[-0.2,dy_back_low-0.1,-0.1],[-0.2,0,-0.1],[0,0,0]]);
cf_lleb = BEZIER(S0)([[0,dy_back_low,0],[-0.2,dy_back_low,0],[-0.2,0,0],[0,0,0]]);

var left_low_edge_back = COLOR(white)(surface([c1_lleb,c2_lleb,cf_lleb]));


c1_rleb = BEZIER(S0)([[dx_back,dy_back_low,0],[dx_back,dy_back_low-0.1,-0.1],[dx_back,0,-0.1],[dx_back,0,0]]);
c2_rleb = BEZIER(S0)([[dx_back,dy_back_low,0],[dx_back+0.2,dy_back_low-0.1,-0.1],[dx_back+0.2,0,-0.1],[dx_back,0,0]]);
cf_rleb = BEZIER(S0)([[dx_back,dy_back_low,0],[dx_back+0.2,dy_back_low,0],[dx_back+0.2,0,0],[dx_back,0,0]]);

var right_low_edge_back = COLOR(white)(surface([c1_rleb,c2_rleb,cf_rleb]));


var back = STRUCT([front_side_back, top_side_back, back_side_back, low_side_back, left_side_back, 
					left_top_edge_back, right_side_back, right_top_edge_back, left_low_edge_back, right_low_edge_back]);






/****************************** SEAT ******************************/

var dz_seat_back = 2;
var dz_seat_front = 3;
var dx_seat = dx_back;
var dy_seat = 10;


c1_bs = cf_bb;
cf_bs = BEZIER(S0)([[0,dy_back_low-0.6,-dz_seat_back],[dx_seat,dy_back_low-0.6,-dz_seat_back]]);

var back_side_seat = COLOR(white)(surface([c1_bs,cf_bs]));


c1_ts = c1_bs;
cf_ts = BEZIER(S0)([[0,dy_back_low-dy_seat,-1],[dx_seat,dy_back_low-dy_seat,-1]]);

var top_side_seat = COLOR(blue_persia)(surface([c1_ts,cf_ts]));


c1_fs = cf_ts;
c2_fs = BEZIER(S0)([[0,dy_back_low-dy_seat-5,-1.5],[dx_seat,dy_back_low-dy_seat-5,-1.5]]);
c3_fs = BEZIER(S0)([[0,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1],[dx_seat,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1]]);
cf_fs = BEZIER(S0)([[0,dy_back_low-dy_seat-1,-1-dz_seat_front],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]]);

var front_side_seat = COLOR(blue_persia)(surface([c1_fs,c2_fs,c3_fs,cf_fs]));


c1_ls = cf_fs;
c2_ls = BEZIER(S0)([[0,dy_back_low-0.6-0.1,-dz_seat_back-0.4],[dx_seat,dy_back_low-0.6-0.1,-dz_seat_back-0.4]]);
cf_ls = cf_bs;

var low_side_seat = COLOR(white)(surface([c1_ls,c2_ls,cf_ls]));


c1_lefts = BEZIER(S0)([[0,dy_back_low,0],[0,dy_back_low-dy_seat,-1]]);
c2_lefts = BEZIER(S0)([[0-0.2,dy_back_low,0],[0-0.2,dy_back_low-dy_seat,-1]]);
c3_lefts = BEZIER(S0)([[0-0.2,dy_back_low-0.6,-dz_seat_back],[0-0.2,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[0-0.2,dy_back_low-dy_seat-1,-1-dz_seat_front]]);
cf_lefts = BEZIER(S0)([[0,dy_back_low-0.6,-dz_seat_back],[0,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[0,dy_back_low-dy_seat-1,-1-dz_seat_front]]);

var left_side_seat = COLOR(white)(surface([c1_lefts,c2_lefts,c3_lefts,cf_lefts]));


c1_rights = BEZIER(S0)([[dx_seat,dy_back_low,0],[dx_seat,dy_back_low-dy_seat,-1]]);
c2_rights = BEZIER(S0)([[dx_seat+0.2,dy_back_low,0],[dx_seat+0.2,dy_back_low-dy_seat,-1]]);
c3_rights = BEZIER(S0)([[dx_seat+0.2,dy_back_low-0.6,-dz_seat_back],[dx_seat+0.2,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[dx_seat+0.2,dy_back_low-dy_seat-1,-1-dz_seat_front]]);
cf_rights = BEZIER(S0)([[dx_seat,dy_back_low-0.6,-dz_seat_back],[dx_seat,dy_back_low-0.6-0.1,-dz_seat_back-0.4],
						[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]]);

var right_side_seat = COLOR(white)(surface([c1_rights,c2_rights,c3_rights,cf_rights]));


c1_lfes = BEZIER(S0)([[0,dy_back_low-dy_seat,-1],[0,dy_back_low-dy_seat-5,-1.5],
						[0,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1],[0,dy_back_low-dy_seat-1,-1-dz_seat_front]]);
c2_lfes = BEZIER(S0)([[0,dy_back_low-dy_seat,-1],[0-0.2,dy_back_low-dy_seat-2.5,-1.5],
						[0-0.2,dy_back_low-dy_seat-1-0.2,-1-dz_seat_front],[0,dy_back_low-dy_seat-1,-1-dz_seat_front]]);
cf_lfes = BEZIER(S0)([[0,dy_back_low-dy_seat,-1],[0-0.2,dy_back_low-dy_seat,-1],
						[0-0.2,dy_back_low-dy_seat-1,-1-dz_seat_front],[0,dy_back_low-dy_seat-1,-1-dz_seat_front]]);

var left_front_edge_seat = COLOR(white)(surface([c1_lfes,c2_lfes,cf_lfes]));


c1_rfes = BEZIER(S0)([[dx_seat,dy_back_low-dy_seat,-1],[dx_seat,dy_back_low-dy_seat-5,-1.5],
						[dx_seat,dy_back_low-dy_seat-1-0.4,-1-dz_seat_front+0.1],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]]);
c2_rfes = BEZIER(S0)([[dx_seat,dy_back_low-dy_seat,-1],[dx_seat+0.2,dy_back_low-dy_seat-2.5,-1.5],
						[dx_seat+0.2,dy_back_low-dy_seat-1-0.2,-1-dz_seat_front],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]]);
cf_rfes = BEZIER(S0)([[dx_seat,dy_back_low-dy_seat,-1],[dx_seat+0.2,dy_back_low-dy_seat,-1],
						[dx_seat+0.2,dy_back_low-dy_seat-1,-1-dz_seat_front],[dx_seat,dy_back_low-dy_seat-1,-1-dz_seat_front]]);

var right_front_edge_seat = COLOR(white)(surface([c1_rfes,c2_rfes,cf_rfes]));


c1_lbes = BEZIER(S0)([[0,dy_back_low,0],[0,dy_back_low-0.6,-dz_seat_back]]);
cf_lbes = BEZIER(S0)([[0,dy_back_low,0],[0-0.2,dy_back_low,0],
						[0-0.2,dy_back_low-0.6,-dz_seat_back],[0,dy_back_low-0.6,-dz_seat_back]])

var left_back_edge_seat = COLOR(white)(surface([c1_lbes,cf_lbes]));


c1_rbes = BEZIER(S0)([[dx_seat,dy_back_low,0],[dx_seat,dy_back_low-0.6,-dz_seat_back]]);
cf_rbes = BEZIER(S0)([[dx_seat,dy_back_low,0],[dx_seat+0.2,dy_back_low,0],
						[dx_seat+0.2,dy_back_low-0.6,-dz_seat_back],[dx_seat,dy_back_low-0.6,-dz_seat_back]])

var right_back_edge_seat = COLOR(white)(surface([c1_rbes,cf_rbes]));



var seat = STRUCT([back_side_seat, top_side_seat, front_side_seat, low_side_seat, left_side_seat, right_side_seat, 
					left_front_edge_seat, right_front_edge_seat, left_back_edge_seat, right_back_edge_seat]);





/****************************** PILLOW ******************************/


var pillows = R([1,2])([-PI/10])(STRUCT([back, seat]));




/****************************** LEGS ******************************/


// support function

var circumference = function (r,dx,dy,dz) {
	return function (v) {
		return [r*COS(v[0])+dx, r*SIN(v[0])+dy, dz];
	};
};


var domCyl = DOMAIN([[0,2*PI],[0,1]])([20,20]);

function cylinder(curves){
	return MAP(BEZIER(S1)(curves))(domCyl);
}

var torus = function (R,r){
	return function (arg){
		var a = arg[0];
		var b = arg[1];
		var u = (r*COS(a)+R) * COS(b);
		var v = (r*COS(a)+R) * SIN(b);
		var w = r*SIN(a);
		return [u,v,w];
	};
};

function circle(r, h) {
	var domain = DOMAIN([[0, 2*PI],[0,r]])([30,30]);
	var mapping = function(v) {
		var a = v[0];
		var r = v[1];

		return [r*COS(a), r*SIN(a), h];
	}

	model = MAP(mapping)(domain);

	return model;
} 

var radius = 0.15;
var distance = dx_back+2;
var h1 = 8;
var h2 = 10.1;


domain_angle_leg_1 = DOMAIN([[0, 2*PI],[0,PI/3]])([20,20]);

var angle_leg1 = R([1,2])([PI/6])(R([0,1])([PI])(R([0,2])([-PI/2])(MAP(torus(radius*2,radius))(domain_angle_leg_1))));


domain_angle_leg_2 = DOMAIN([[0, 2*PI],[0,PI/2]])([20,20]);

var angle_leg2_left = R([0,2])([-PI/2])(R([1,2])([PI/2])(MAP(torus(radius*6,radius))(domain_angle_leg_2)));

var angle_leg2_right = R([0,2])([-PI/2])(R([1,2])([-PI/2])(MAP(torus(radius*6,radius))(domain_angle_leg_2)));



cyl1_left = STRUCT([cylinder([circumference(radius-0.05,0,0,0), circumference(radius,0,0,h1)]), 
				T([1,2])([2*radius,h1])(angle_leg1), 
				T([1,2])([-(radius)/2,5])(CUBOID([1,radius,1.5]))]);

cyl1_right = STRUCT([cylinder([circumference(radius-0.05,0,0,0), circumference(radius,0,0,h1)]), 
				T([1,2])([2*radius,h1])(angle_leg1), 
				T([0,1,2])([-1,-(radius)/2,5])(CUBOID([1,radius,1.5]))]);


cyl2_left = T([1,2])([radius,h1+(radius*2)-0.04])(R([1,2])([-PI/3])
	(STRUCT([cylinder([circumference(radius,0,0,0), circumference(radius,0,0,dy_seat)]), 
			T([0,2])([radius*6,dy_seat])(angle_leg2_left)])));

cyl2_right = T([1,2])([radius,h1+(radius*2)-0.04])(R([1,2])([-PI/3])
	(STRUCT([cylinder([circumference(radius,0,0,0), circumference(radius,0,0,dy_seat)]), 
			T([0,2])([-radius*6,dy_seat])(angle_leg2_right)])));


cyl3_left = T([1,2])([dy_seat+4,5])(R([1,2])([PI/4])
	(STRUCT([cylinder([circumference(radius-0.05,0,0,0),circumference(radius,0,0,h2)]), 
			T([1,2])([-(radius)/2,6])(CUBOID([1,radius,1.5]))])));

cyl3_right = T([1,2])([dy_seat+4,5])(R([1,2])([PI/4])
	(STRUCT([cylinder([circumference(radius-0.05,0,0,0),circumference(radius,0,0,h2)]), 
			T([0,1,2])([-1,-(radius)/2,6])(CUBOID([1,radius,1.5]))])));


var pillars_left = R([1,2])([-PI/10])(STRUCT([cyl1_left, cyl2_left, cyl3_left]));
var pillars_right = R([1,2])([-PI/10])(STRUCT([cyl1_right, cyl2_right, cyl3_right]));


r_base = (radius-0.05)*2;
h_base = 0.15;

var base = STRUCT([cylinder([circumference(r_base,0,0,0),circumference(r_base,0,0,h_base)]), 
				circle(r_base,0),circle(r_base,h_base)]);


var left_leg = STRUCT([pillars_left, T([1,2])([0.02,-0.1])(base), T([1,2])([dy_seat+4.81,0.35])(base)]);

var right_leg = STRUCT([pillars_right, T([1,2])([0.02,-0.1])(base), T([1,2])([dy_seat+4.81,0.35])(base)]);


left_leg = T([0,1,2])([-1,-dy_seat, -(h1-2.5)])(left_leg);

right_leg = T([0,1,2])([-1+distance,-dy_seat, -(h1-2.5)])(right_leg);


var legs = COLOR(gold)(STRUCT([left_leg, right_leg]));



/****************************** ARMRESTS ******************************/

dx_arm = 0.8;
dy_arm = 10;
dz_arm= 0.8;
curve_depht = 0.5;


c1 = BEZIER(S0)([[0, 0, dz_arm],[dx_arm, 0, dz_arm]]);
c2 = BEZIER(S0)([[-curve_depht, -curve_depht, dz_arm],[curve_depht+dx_arm, -curve_depht, dz_arm]]);
c3 = BEZIER(S0)([[-curve_depht, -curve_depht, 0],[curve_depht+dx_arm, -curve_depht, 0]]);
c4 = BEZIER(S0)([[0, 0, 0],[dx_arm, 0, 0]]);

c5 = BEZIER(S0)([[0, 0, dz_arm],[0, dy_arm, dz_arm]]);
c6 = BEZIER(S0)([[-curve_depht, -curve_depht, dz_arm],[-curve_depht, curve_depht+dy_arm, dz_arm]]);
c7 = BEZIER(S0)([[-curve_depht, -curve_depht, 0],[-curve_depht, curve_depht+dy_arm, 0]]);
c8 = BEZIER(S0)([[0, 0, 0],[0, dy_arm, 0]]);

c9 = BEZIER(S0)([[0, dy_arm, dz_arm],[dx_arm, dy_arm, dz_arm]]);
c10 = BEZIER(S0)([[-curve_depht, curve_depht+dy_arm, dz_arm],[curve_depht+dx_arm, curve_depht+dy_arm, dz_arm]]);
c11 = BEZIER(S0)([[-curve_depht, curve_depht+dy_arm, 0],[curve_depht+dx_arm, curve_depht+dy_arm, 0]]);
c12 = BEZIER(S0)([[0, dy_arm, 0],[dx_arm, dy_arm, 0]]);

c13 = BEZIER(S0)([[dx_arm, 0, dz_arm],[dx_arm, dy_arm, dz_arm]]);
c14 = BEZIER(S0)([[curve_depht+dx_arm, -curve_depht, dz_arm],[curve_depht+dx_arm, curve_depht+dy_arm, dz_arm]]);
c15 = BEZIER(S0)([[curve_depht+dx_arm, -curve_depht, 0],[curve_depht+dx_arm, curve_depht+dy_arm, 0]]);
c16 = BEZIER(S0)([[dx_arm, 0, 0],[dx_arm, dy_arm, 0]]);


var armrest = R([1,2])([(PI/6)-(PI/10)])(COLOR(white)(STRUCT([CUBOID([dx_arm,dy_arm,dz_arm]), surface([c1,c2,c3,c4]), 
					surface([c5,c6,c7,c8]), surface([c9,c10,c11,c12]), surface([c13,c14,c15,c16])])));


var armrests = STRUCT([T([0,1,2])([-dx_arm-0.6,-8.5,2.2])(armrest), 
						T([0,1,2])([-dx_arm-0.6+distance,-8.5,2.2])(armrest)]);



/****************************** ARMCHAIR ******************************/

var armchair = STRUCT([pillows, legs, armrests]);
DRAW(armchair);
