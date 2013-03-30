// muri
// davanti
var points = [[0,0],[2,0],[2,5],[4,5],[4,0],[6,0],[6,8],[0,8]];
var cells = [[0,1,2,7],[2,3,6,7],[3,4,5,6]]
var davanti = SIMPLICIAL_COMPLEX(points)(cells);

// laterali
var points = [[0,0],[10,0],[10,8],[0,8],[4,3],[6,3],[6,5],[4,5]];
var cells = [[0,1,4,5],[2,3,6,7],[0,3,4,7],[1,2,5,6]]
var laterale = SIMPLICIAL_COMPLEX(points)(cells);

var laterale_sx = R([0,2])(PI/2)(laterale);
var laterale_dx = T([0])([6])(laterale_sx);

// dietro
var points = [[0,0],[6,0],[6,8],[0,8]];
var cells = [[0,1,2,3]]
var dietro = T([2])([-10])(SIMPLICIAL_COMPLEX(points)(cells));

var muri = COLOR([1,0,0])(STRUCT([davanti, laterale_sx, laterale_dx, dietro]));

// tetto
var points = [[0,0],[6,0],[3,3]];
var cells = [[0,1,2]]
var tetto2D = SIMPLICIAL_COMPLEX(points)(cells);
var tetto = EXTRUDE([10])(tetto2D);
tetto = COLOR([0.7,0.4,0])(T([1,2])([8,-10])(tetto));

var casa_template = STRUCT([muri, tetto]);

// porta
var points = [[2,5],[4,5],[2,0],[4,0]];
var cells = [[0,1,2,3]]
var porta = COLOR([1,1,1])(SIMPLICIAL_COMPLEX(points)(cells));

// finestra
var points = [[4,3],[6,3],[6,5],[4,5]];
var cells = [[0,1,2,3]]
var finestra = COLOR([0,0.7,1])(SIMPLICIAL_COMPLEX(points)(cells));

var finestra_sx = R([0,2])(PI/2)(finestra);
var finestra_dx = T([0])([6])(finestra_sx);

var casa = STRUCT([casa_template, porta, finestra_sx, finestra_dx]);

// prato
var prato = COLOR([0,1,0])(CUBOID([40,0,40]));
prato = T([0,2])([-16,-25])(prato)

DRAW(STRUCT([casa, prato]));