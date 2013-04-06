T = function (dims) {
	dims = dims.map(function (v) {
		return v-1; 
	});
	return function(values){
		return function(object) {
			return object.clone().translate(dims, values);
		};
	};
}


R = function (dims) {
	dims = dims.map(function (v) {
		return v-1; 
	});
	return function(angle){
		return function(object) {
			return object.clone().rotate(dims, angle);
		};
	};
}


S = function (dims) {
	dims = dims.map(function (v) {
		return v-1; 
	});
	return function(values){
		return function(object) {
			return object.clone().scale(dims, values);
		};
	};
}


S3 = S2;
S2 = S1;
S1 = S0;

GRID = SIMPLEX_GRID;

VIEW = DRAW;

// floor0

verts = [[22,91.5], [45,91.5], [45,47.5], [62,47.5], [62,50.5], [145,50.5], 
	[145,63.5], [150,63.5], [150,75.5], [157,75.5], [157,112.5], [22,112.5]];

cells = [[0,11,1], [1,10,11], [1,2,3], [1,3,4], [1,4,5], [1,5,6], [1,6,7], [1,7,8], [1,8,9], [1,9,10]];

floor_quad = EXTRUDE([4])(SIMPLICIAL_COMPLEX(verts)(cells));

// semicircle

function arc(alpha, r, R) {
	var domain = DOMAIN([[0, alpha],[r,R]])([36,1]);

	var mapping = function(v) {
		var a = v[0];
		var r = v[1];

		return [r*COS(a), r*SIN(a)];
	}

	model = MAP(mapping)(domain);

	return model;
} 

semicircle1 = T([1,2])([53.5,47.5])(R([1,2])(PI)(arc(PI, 0, 8.5)));
semicircle2 = T([1,2])([157,94])(R([1,2])(-PI/2)(arc(PI, 0, 18.5)));


floor0 = STRUCT([floor_quad, EXTRUDE([4])(semicircle1), EXTRUDE([4])(semicircle2)]);


// floor1

verts = [[22,16.5], [182,16.5], [182,112.5], [88.5,112.5], [88.5,95.5], [38.5,95.5], [38.5,112.5], [22,112.5], [22,110.5], 
	[5.5,110.5], [5.5,95.5], [22,95.5]];

cells = [[0,1,2], [2,3,4], [0,2,4], [0,4,5], [0,5,11], [11,5,6], [7,11,6], [8,10,11], [9,10,8]];

floor1 = T([3])([37])(EXTRUDE([4])(SIMPLICIAL_COMPLEX(verts)(cells)));



// floor2

verts = [[104,16.5], [182,16.5], [182,112.5], [88.5,112.5], [88.5,95.5]];

cells = [[0,1,2], [2,3,4], [0,4,2]];

floor2 = T([3])([74])(EXTRUDE([4])(SIMPLICIAL_COMPLEX(verts)(cells)));



// floor3

verts = [[22,16.5], [182,16.5], [182,112.5], [138,112.5], [138,95.5], [99.5,95.5], [99.5,112.5], [22,112.5]];

cells = [[0,1,2], [2,3,4], [0,2,4], [0,5,4], [0,5,6], [0,6,7]];

floor3 = T([3])([111])(EXTRUDE([4])(SIMPLICIAL_COMPLEX(verts)(cells)));


// floor4

verts = [[99.5,16.5], [182,16.5], [182,112.5], [22,112.5], [22,93.5], [99.5,95.5]]

cells = [[0,1,2], [0,5,2], [2,5,3], [5,4,3]]

floor4 = T([3])([148])(EXTRUDE([4])(SIMPLICIAL_COMPLEX(verts)(cells)))




building = STRUCT([floor0, floor1, floor2, floor3, floor4, building])