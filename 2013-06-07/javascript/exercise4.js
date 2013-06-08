// es1

var x = 50;
var y = 50;

var h = 5;

var mapping = function(v) {
	var x = v[0];
	var y = v[1];

	var z = Math.random()*h;

	return [x,y,z];
}

var domain = DOMAIN([[0, x], [0, y]])([20,20]);
var mapping_numbers = MAP(mapping)(domain);

var mountains =  COLOR([150/255,75/255,0])(mapping_numbers);


/*******************************************************************/


// es2 
var h_lake = h/8;

var lake = COLOR([0,204/255,204/255])(CUBOID([x,y,h_lake]));


/*******************************************************************/


// es3


var circumference = function (r,h) {
	return function (v) {
		return [r*COS(v[0]), r*SIN(v[0]), h];
	};
};

function surface(curves, discr){
	return MAP(BEZIER(S1)(curves))(DOMAIN([[0,2*PI],[0,1]])([discr,1]));
}

function circle(r, h) {
	var domain = DOMAIN([[0, 2*PI],[0,r]])([50,1]);
	var mapping = function(v) {
		var a = v[0];
		var r = v[1];

		return [r*COS(a), r*SIN(a), h];
	}

	model = MAP(mapping)(domain);

	return model;
} 

var tree = function(h,r,discr) {
	c1 = circumference(r/2,0);
	c2 = circumference(r/2,h/2);
	var trunk = COLOR([101/255, 67/255, 33/255])(STRUCT([circle(r/2,0), CYL_SURFACE([r/2,h/2])([discr,discr])]));

	c3 = circumference(r,h/2);
	c4 = BEZIER(S0)([[0,0,h]]);
	var hair = COLOR([0,1,0])(STRUCT([circle(r,h/2), surface([c3,c4],discr)]));

	return STRUCT([trunk,hair]);
}

// non utilizzata: generare tanti random_tree penalizzava di molto il tempo di esecuzione
var random_tree = function() {
	var random = Math.random();
	return tree(1-random*0.3, 0.1+random*0.5, 50-random*30);
}

var values = function(v) {
	return [v.position.x, v.position.y, v.position.z];
}

var translation_vector = MAP(values)(mapping_numbers.geometry.vertices);

var translation = function(v) {
	return T([0,1,2])(v)(tree(1,0.1,20));
}

var wooded_area = function() {
	var area = [];
	var random = Math.round(Math.random()*350);
	for(var i = random; i<50+random; i++) {
		if(translation_vector[i][2]>h_lake) {
			area.push(translation(translation_vector[i]));
		}
	}
	return STRUCT(area);
}


/*******************************************************************/


// es4
var vx = 2;
var vy = 1.5;
var vz = 1;

var distance = 0.3;

var building = function(vx,vy,vz) {
	var random = Math.random();
	vx_home = random*vx;
	vy_home = random*vy;
	var home = COLOR([1,1,0])(CUBOID([vx_home,vy_home,random*vz]));

	var lawn = COLOR([0,1,0])(CUBOID([vx,vy]));

	return STRUCT([lawn, T([0,1])([vx/2-vx_home/2, vy/2-vy_home/2])(home)]);
}


var village = function(n,m) {
	var buildings = [];
	var translation_x = 0;
	var translation_y = 0;

	for(var i = 0; i<n; i++) {
		for(var j=0; j<m; j++) {
			buildings.push(T([0,1])([translation_x, translation_y])(building(vx,vy,vz)));
			translation_x += distance+vx;
		}
		translation_y += distance+vy;
		translation_x = 0;
	}
	return STRUCT(buildings);
}


var village1 = village(5,5);

var village2 = village(10,6);


model = STRUCT([mountains, lake, wooded_area(), T([0])([x])(village1), T([1])([y])(village2)]);

// DRAW(model);