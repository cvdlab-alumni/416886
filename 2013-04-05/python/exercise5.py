# ramp1
step2D = MKPOL([[[0,0], [0,3.7], [5,3.7], [5,1.85]], [[1,2,3,4]], None])
step3D = PROD([step2D, Q(17)])

step3D = MAP([S1,S3,S2])(step3D)

ramp = STRUCT(NN(10)([step3D, T([1,3])([5,3.7])]))

ramp1 = T([1,2,3])([38.5, 95.5, 4])(ramp)



# ramp2
step2D = MKPOL([[[0,0], [0,3.7], [5,3.7], [5,1.85]], [[1,2,3,4]], None])
step3D = PROD([step2D, Q(17)])

step3D = MAP([S1,S3,S2])(step3D)

ramp = STRUCT(NN(10)([step3D, T([1,3])([5,3.7])]))

ramp2 = T([1,2,3])([38.5, 95.5, 41])(ramp)


# ramp3
step2D = MKPOL([[[0,0], [0,3.7], [5,3.7], [5,1.85]], [[1,2,3,4]], None])
step3D = PROD([step2D, Q(17)])

step3D = MAP([S1,S3,S2])(step3D)

ramp = STRUCT(NN(10)([step3D, T([1,3])([5,3.7])]))

ramp2 = T([1,2,3])([38.5, 95.5, 41])(ramp)

VIEW(STRUCT([building, ramp1, ramp2]))