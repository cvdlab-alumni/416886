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


model = STRUCT([mountains, lake]);

// DRAW(model);