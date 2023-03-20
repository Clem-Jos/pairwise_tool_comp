import comets_s as c
from medium import *
import micom_s as m
mypath1 = 'C:/Users/u0128864/Documents/MATLAB/AGORA/'
#medium=[YCAG2]
#medium=[AF]
medium=[AF2,ABB2]#YCAG2,YCGMS2,YCFA2,mMCB2,mMCB_A2,YCGD2,
#medium=[YCAG,YCGMS,YCFA,mMCB,mMCB_A,YCGD,AF,ABB]
#med_name=['YCAG']
#med_name=['AF']
med_name=['AF','ABB']#'YCAG','YCGMS','YCFA','mMCB','mMCB_A','YCGD',
#directories=['human2/']# human1/
directories=['mouse1/','human1/']#'human2/','human3/','human4/','human5/','human6/','human7/',
# med = {'EX_MGlcn178_m': 0.7059672031549943, 'EX_MGlcn178_rl_m': 0.6940424881358493, 'EX_ca2_m': 0.003098919079524168,
#        'EX_cl_m': 0.003098919079524168, 'EX_cobalt2_m': 0.003098919079524168, 'EX_cspg_b_m': 0.07418684445717395,
#        'EX_cu2_m': 0.0030990106811733757, 'EX_fe2_m': 0.006193872336463523, 'EX_fe3_m': 0.0030989221327190016,
#        'EX_k_m': 0.003093562058913765, 'EX_mg2_m': 0.0031000461970117107, 'EX_mn2_m': 0.003098919079524168,
#        'EX_pheme_m': 0.0030949531415166106, 'EX_pi_m': 0.8121501610563999, 'EX_pydx_m': 3.965765255687055e-06,
#        'EX_zn2_m': 0.003099320129660056, 'EX_alagln_m': 0.0001482898929251078, 'EX_metala_m': 9.361332507324987e-05}
# medium = {'MGlcn178[e]': 0.7059672031549943, 'MGlcn178_rl[e]': 0.6940424881358493, 'ca2[e]': 0.003098919079524168,
#        'cl[e]': 0.003098919079524168, 'cobalt2[e]': 0.003098919079524168, 'cspg_b[e]': 0.07418684445717395,
#        'cu2[e]': 0.0030990106811733757, 'fe2[e]': 0.006193872336463523, 'fe3[e]': 0.0030989221327190016,
#        'k[e]': 0.003093562058913765, 'mg2[e]': 0.0031000461970117107, 'mn2[e]': 0.003098919079524168,
#        'pheme[e]': 0.0030949531415166106, 'pi[e]': 0.8121501610563999, 'pydx[e]': 3.965765255687055e-06,
#        'zn2[e]': 0.003099320129660056, 'alagln[e]': 0.0001482898929251078, 'metala[e]': 9.361332507324987e-05}

for a in  range(len(medium)):
    mypath = mypath1+directories[a]#-master/CurrentVersion/AGORA_1_03/AGORA_1_03_sbml/tt/'
    files_cuts=m.listdir(mypath)
    onlyfiles = [mypath+f for f in m.listdir(mypath) if m.isfile(m.join(mypath, f))]
    ids, files = m.c_combination(files_cuts, mypath)
    print(len(ids))
    print(onlyfiles)
    # ids =['B_thetaiotaomicron','F_prausnitzii']
    #doc='C:/Users/u0128864/Documents/MATLAB/AGORA/'
    #files =[doc+"Bacteroides_uniformis_ATCC_8492.xml",doc+"Collinsella_aerofaciens_ATCC_25986.xml"]
    #files=[doc+'Prevotella_copri_CB7_DSM_18205.xml',doc+'Flavonifractor_plautii_ATCC_29863.xml']
    #test_tube,test_tube2,comp_assay,comp_assay2 =c.comets_function(files[0],files[1],dietCs1,"il_etait8")
    #mono1,mono2,comm1,com_pars =c.comets_function(files[0],files[1],dietCs3,"il_etait8")

    #for i in range(len(onlyfiles)):
    #    test_tube, comm_rest, biomass = c.monoculture_only(onlyfiles[i], dietCs1, 'DC1')
    #    test_tube, comm_rest , biomass = c.monoculture_only(onlyfiles[i],dietCs3, 'DC3')
    #    test_tube, comm_rest, biomass = c.monoculture_only(onlyfiles[i], ABB, 'ABB')

    micomdir ='C:/Users/u0128864/Documents/Micom_results/'

    for i in range(24,len(ids)): #
        print(i)
        print(ids[i])
        #c.comets_function(files[i][0], files[i][1], dietCs1, "DC1")
        #c.comets_function(files[i][0], files[i][1], dietCs3, "DC3")
        #c.comets_function(files[i][0], files[i][1], medium[a], med_name[a])
        # print(i)

        print(ids[i])
        single, solution1, solution2, solution3,solution4 = m.run_pairwise(ids[i], files[i],dietConstraints1 )
        f=open(micomdir+directories[a][:-1]+'_micom_results_c1_to.csv','a')
        f.write("Single:\n")
        f.write(ids[i][0]+","+ids[i][1]+"\n")
        print(single)
        f.write(str(single[0])+','+str(single[1])+'\n')
        f.close()
        #solution1.to_csv(micomdir+directories[a][:-1]+'_micom_results_c1.csv', mode='a', index=True, header=True)
        #solution2.to_csv(micomdir+directories[a][:-1]+'_micom_results_c1.csv', mode='a', index=True, header=True)
        #solution3.to_csv(micomdir+directories[a][:-1]+'_micom_results_c1.csv', mode='a', index=True, header=True)
        solution4.to_csv(micomdir+directories[a][:-1]+'_micom_results_c1_to.csv', mode='a', index=True, header=True)

        single, solution1, solution2, solution3 ,solution4 = m.run_pairwise(ids[i], files[i], dietConstraints3)
        single = m.run_pairwise(ids[i], files[i], dietConstraints3)
        f=open(micomdir+directories[a][:-1]+'_micom_results_c3_to.csv','a')
        f.write("Single:\n")
        f.write(ids[i][0]+","+ids[i][1]+"\n")
        f.write(str(single[0])+','+str(single[1])+'\n')
        f.close()
        #solution1.to_csv(micomdir+directories[a][:-1]+'_micom_results_c3.csv', mode='a', index=True, header=True)
        #solution2.to_csv(micomdir+directories[a][:-1]+'_micom_results_c3.csv', mode='a', index=True, header=True)
        #solution3.to_csv(micomdir+directories[a][:-1]+'_micom_results_c3.csv', mode='a', index=True, header=True)
        solution4.to_csv(micomdir+directories[a][:-1]+'_micom_results_c3_to.csv', mode='a', index=True, header=True)
        
        single, solution1, solution2, solution3, solution4 = m.run_pairwise(ids[i], files[i], medium[a])
        f = open(micomdir+directories[a][:-1]+'_micom_results_VITAMINES_to_'+med_name[a]+'.csv', 'a')
        f.write("Single:\n")
        f.write(ids[i][0] + "," + ids[i][1] + "\n")
        f.write(str(single[0])+','+str(single[1])+'\n')
        f.close()
        print('done',a,i)
        #solution1.to_csv(micomdir+directories[a][:-1]+'_micom_results_VITAMINES_'+med_name[a]+'.csv', mode='a', index=True, header=True)
        #solution2.to_csv(micomdir+directories[a][:-1]+'_micom_results_VITAMINES_'+med_name[a]+'.csv', mode='a', index=True, header=True)
        #solution3.to_csv(micomdir+directories[a][:-1]+'_micom_results_VITAMINES_'+med_name[a]+'.csv', mode='a', index=True, header=True)
        solution4.to_csv(micomdir+directories[a][:-1]+'_micom_results_VITAMINES_to_'+med_name[a]+'.csv', mode='a', index=True, header=True)
        print('saved')


"""results = workflow(run_pairwise,[ids,files,med],threads=1)
media = comm1.media.copy()
media = media[media.conc_mmol<900]
fig, ax = c.plt.subplots()
compoundofinterest = ['glc_D[e]','ac[e]','h2o[e]']
media = media[media.metabolite.isin(compoundofinterest)]
media.groupby('metabolite').plot(x='cycle', ax =ax, y='conc_mmol')
ax.legend(('ac[e]','glc_D[e]','h2o[e]'))
ax.set_ylabel("Concentration (mmol)")"""

#Micom_loop.run_pairwise(['BO','CA'], ['C:/Users/u0128864/Documents/MATLAB/AGORA/human1/Bacteroides_ovatus_ATCC_8483.xml','C:/Users/u0128864/Documents/MATLAB/AGORA/human1/Collinsella_aerofaciens_ATCC_25986.xml'], dietConstraints1)