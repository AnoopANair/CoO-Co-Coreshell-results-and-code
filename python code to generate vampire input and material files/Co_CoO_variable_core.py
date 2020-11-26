import os

inner_core_dia = [7,8,9,10,13,18,23]
outer_layer_thickness = 1
foldername = "outputfiles"
folder_input = "inputfiles"
folder_mat = "material_files"

for inner in inner_core_dia :
    diameter = inner + 2*outer_layer_thickness
    ratio = (inner*0.5)/(diameter*0.5)

    f = open("input",'w')
    f.write("# This is the input file\n")
    f.close()

    f = open("input",'a')
    f.write("create:crystal-structure = fcc \n")
    f.write("create:sphere \n")
    f.write("dimensions:unit-cell-size = 3.524 !A \n")
    f.write("dimensions:system-size-x = {} !nm \n".format(diameter))
    f.write("dimensions:system-size-y = {} !nm \n".format(diameter))
    f.write("dimensions:system-size-z = {} !nm \n".format(diameter))
    f.write("dimensions:particle-size = {}.0 !nm \n".format(diameter))
    f.write("material:file = Co.mat \n")
    f.write("sim:temperature = 300.0 \n")
    f.write("sim:minimum-temperature=0 \n")
    f.write("sim:maximum-temperature=2000 \n")
    f.write("sim:temperature-increment=10 \n")
    f.write("sim:time-steps-increment=1 \n")
    f.write("sim:equilibration-time-steps:1000 \n")
    f.write("sim:loop-time-steps=1000 \n")
    f.write("sim:program = curie-temperature \n")
    f.write("sim:integrator =monte-carlo \n")
    f.write("output:real-time \n")
    f.write("output:temperature \n")
    f.write("output:magnetisation \n")
    f.write("output:magnetisation-length \n")
    f.write("output:mean-magnetisation-length \n")
    f.write("screen:temperature \n")
    f.write("screen:mean-magnetisation-length \n")
    f.write("config:atoms \n")
    f.close()

    os.system("cp input ./{}/input_{}nm_{}nm".format(folder_input,diameter,data))
    f1 = open("Co.mat",'w')
    f1.write("# This is the material file   \n")
    f1.close()

    f1 = open("Co.mat",'a')
    f1.write("materials:num-materials=2 \n")
    f1.write('material[1]:material-name = "AFM" \n')
    f1.write('material[1]:material-element = "Co"   \n')
    f1.write("material[1]:exchange-matrix[1] = -4.27e-22    \n")
    f1.write("material[1]:exchange-matrix[2] = 5.75e-21 \n")
    f1.write("material[1]:atomic-spin-moment = 2.55 !muB    \n")
    f1.write("material[1]:damping-constant = 1.0    \n")
    f1.write("material[1]:uniaxial-anisotropy-constant = 6.96e-24   \n")
    f1.write('material[2]:material-name = "FM"  \n')
    f1.write('material[2]:material-element = "O" \n')
    f1.write("material[2]:exchange-matrix[1] = 5.75e-21 \n")
    f1.write("material[2]:exchange-matrix[2] = 5.75e-21 \n")
    f1.write("material[2]:atomic-spin-moment = 1.59 !muB    \n")
    f1.write("material[2]:damping-constant = 1.0    \n")
    f1.write("material[2]:uniaxial-anisotropy-constant = 2.98e-24   \n")
    f1.write("material[1]:core-shell-size = 1.0 \n")
    f1.write("material[2]:core-shell-size = {}  \n".format(round(ratio,5)))

    f1.close()

    os.system("cp Co.mat ./{}/Co_{}nm_{}nm.mat".format(folder_mat,diameter,data))
    os.system("mpirun ./vampire-parallel")
    os.system("cp output ./{}/output_{}nm_{}nm".format(foldername,diameter,data))