
import comets_s as c
from medium import *
import micom_s as m
import os

mypath = 'C:/Users/u0128864/Documents/MATLAB/AGORA/'

#mypath = 'C:/Users/u0128864/Documents/MATLAB/AGORA/refined/good/'
# AGORA PAIRS
#directories=['human1/','human2/','human3/','human4/','human5/','human6/','human7/', 'mouse1/']
#mediumi=[ABB,YCAG,YCGMS,YCFA,mMCB,mMCB_A,YCGD,AF] #media for COMETS
#mediumi=[ABB2,YCAG2,YCGMS2,YCFA2,mMCB2,mMCB_A2,YCGD2,AF2] # media for MICOM
#med_namei=['ABB','YCAG','YCGMS','YCFA','mMCB','mMCB_A','YCGD','AF']


#REFINED MODLES PAIRS
directories=['human1/','human3/','human4/','human6/','human7/', 'mouse1/']
mediumi=[ABB,YCGMS,YCFA,mMCB,YCGD,AF] #media for COMETS
#mediumi=[ABB2,YCGMS2,YCFA2,mMCB2,YCGD2,AF2] # media for MICOM
med_namei=['ABB','YCGMS','YCFA','mMCB','YCGD','AF']

# Western Diet
medium=[dietConstraints1]
med_name=['DietCs1/']

for i in  range(len(directories)):
    onlyfiles = [mypath+directories[i] + f for f in m.listdir(mypath+directories[i]) if m.isfile(m.join(mypath,directories[i], f))]
    ids = [c.spnames(f, f) for f in onlyfiles]
    #COMETS IVm
    if not os.path.exists('C:/Users/u0128864/Documents/Comets_results/monos/'+directories[i]):
        os.mkdir('C:/Users/u0128864/Documents/Comets_results/monos/'+directories[i])
    for j in range(len(onlyfiles)):
        print(med_namei[i])
        test_tube, comm_rest, biomass = c.monoculture_only(onlyfiles[j], mediumi[i],directories[i]+ med_namei[i])
    #COMETS WD
    if not os.path.exists('C:/Users/u0128864/Documents/Comets_results/monos/'+med_name[0]):
        os.mkdir('C:/Users/u0128864/Documents/Comets_results/monos/'+med_name[0])
    for j in range(len(onlyfiles)):
        test_tube, comm_rest, biomass = c.monoculture_only(onlyfiles[j], medium[0], med_name[0])#
    #MICOM IVm and WD
    for j in range(len(onlyfiles)):
        single=Micom_loop.micom_mono(ids[j],onlyfiles[j],mediumi[i])
        f = open(micomdir + 'micom_ref_mono2.csv', 'a')
        f.write(directories[i][:-1]+','+ids[j]+','+ str(single[0]) +','+med_namei[i]+"\n")
        f.close()
        single = Micom_loop.micom_mono(ids[j], onlyfiles[j], medium[0])
        f = open(micomdir + 'micom_ref_mono2.csv', 'a')
        f.write(directories[i][:-1] + ',' + ids[j] + ',' + str(single[0]) + ',' + med_name[0] + "\n")
        print(single)
        f.close()

