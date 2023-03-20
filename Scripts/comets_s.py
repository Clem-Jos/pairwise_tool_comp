import cometspy as c
import cobra.test
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from medium import *
from copy import *
#os.chdir("C:/Users/u0128864/OneDrive - KU Leuven/Pairwise_comparison/Models/AGORA/")

# load the models and perform the mutation
def spnames(Pmodel1,Pmodel2):
    files=[Pmodel1,Pmodel2]
    id1=Pmodel1.split('/')[-1][:-4]
    id2 = Pmodel2.split('/')[-1][:-4]
    if id1==id2:
        names=id1
    else:
        names=id1+'_'+id2
    return (names)
def comets_function(Pmodel1,Pmodel2, medium,anid):
    names = spnames(Pmodel1, Pmodel2)
    adir='C:/Users/u0128864/Documents/Comets_results/'+names+'_'+anid+'/'
    os.mkdir(adir)
    model1 = c.model(Pmodel1)
    model1.id = 'Sp1'
    model2 = c.model(Pmodel2)
    model2.id = 'Sp2'

# set its initial biomass, 5e-6 gr at coordinate [0,0]
    
    model1.initial_pop = [0, 0, 0.002]
    model2.initial_pop = [0, 0, 0.002]
    # H
    #model1.initial_pop = [0, 0, 1]
    #model2.initial_pop = [0, 0, 1]
# create an empty layout
    test_tube = c.layout()
    test_tube2 = c.layout()
    test_tube.add_model(model1)
    test_tube.add_model(model2)
    test_tube2.add_model(model1)
    test_tube2.add_model(model2)

    md = []
    allmet = model1.get_exchange_metabolites().to_list()+model2.get_exchange_metabolites().to_list()
    for metabolite in allmet:
        if metabolite not in md:
            md.append(metabolite)

    for a in list(medium.keys()):
        if a in md:
            test_tube.set_specific_metabolite(a, medium[a],static=True)
            test_tube2.set_specific_metabolite(a, medium[a],static=True)
    for compound in sink:
        if 'biomass' not in compound:
            test_tube.set_specific_metabolite(compound, 1000)
            test_tube2.set_specific_metabolite(compound, 1000)

    for i in p:
        if i in md:
         test_tube.set_specific_metabolite(i,10)
         test_tube2.set_specific_metabolite(i, 10)

    comp_params = c.params()
    # H
    #comp_params.set_param('timeStep', 1)
    #comp_params.set_param('maxCycles', 10)

    # H/10
    comp_params.set_param('timeStep',0.1)
    comp_params.set_param('maxCycles', 20)

    comp_params.set_param('defaultVmax', 18.5)
    comp_params.set_param('defaultKm', 0.000015)
    comp_params.set_param('spaceWidth', 1)
    comp_params.set_param('maxSpaceBiomass', 100)
    comp_params.set_param('minSpaceBiomass', 1e-11)
    comp_params.set_param('writeMediaLog', True)
    comp_params.set_param('writeTotalBiomassLog', True)
    comp_params.set_param('writeFluxLog', True)
    comp_assay = c.comets(test_tube, comp_params)
    comp_assay.run()

    comp_assay2 = c.comets(test_tube2, comp_params)
    comp_assay2.obj_style = "MAX_OBJECTIVE_MIN_TOTAL"
    comp_assay2.run()

# graph monocultures
    biomass = comp_assay.total_biomass
    biomass.to_csv(adir+'Biomass1.csv')
    biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']
    bm=biomass.copy()
    bm["Sp2"] = np.log(bm["Sp2"])
    bm["Sp1"] = np.log(bm["Sp1"])

    biomass2 = comp_assay2.total_biomass
    biomass2['t'] = biomass2['cycle'] * comp_assay2.parameters.all_params['timeStep']
    bm2 = biomass2.copy()
    bm2["Sp2"] = np.log(bm2["Sp2"])
    bm2["Sp1"] = np.log(bm2["Sp1"])
    biomass2.to_csv(adir + 'Biomass2.csv')

    myplot = biomass.drop(columns=['cycle']).plot(x = 't')
    myplot.set_ylabel("Biomass (gr.)")
    plt.savefig(adir+'Biomass_normal')
    plt.close()

    myplot = bm.drop(columns=['cycle']).plot(x = 't')
    myplot.set_ylabel("Ln Biomass (gr.)")
    plt.savefig(adir+'LN_Biomass_normal')
    plt.close()

    myplot = biomass2.drop(columns=['cycle']).plot(x='t')
    myplot.set_ylabel("Biomass  pars(gr.)")
    plt.savefig(adir+'Biomass_pars')
    plt.close()

    myplot = bm2.drop(columns=['cycle']).plot(x='t')
    myplot.set_ylabel("Ln Biomass pars (gr.)")
    ids=spnames(Pmodel1,Pmodel2)
    names = ids[0] + '_' + ids[1]
    plt.savefig(adir+'LN_Biomass_pars')
    plt.close()
    return (comp_assay,comp_assay2)

def monoculture_only(model,medium,out):
    model1 = c.model(model)
    model1.id = 'Sp1'
    model1.open_exchanges()
    names = spnames(model,model)
    print(names)
    adir = 'C:/Users/u0128864/Documents/Comets_results/monos/' + out +names

    # H/10
    #model1.initial_pop = [0, 0, 0.002]
    # H 
    model1.initial_pop = [0, 0, 1]

    # create an empty layout
    test_tube = c.layout()

    md = []
    test_tube.add_model(model1)
    for metabolite in model1.get_exchange_metabolites():
        md.append(metabolite)


    sink=[f for f in md if '[c]' in f]


    for a in list(medium.keys()):
        if a in md:
            test_tube.set_specific_metabolite(a, medium[a],static=True)# don't reduce
    for compound in sink:
        test_tube.set_specific_metabolite(compound, 1000)
    #p=['26dap_M[e]','h2s[e]','ribflv[e]','thymd[e]','fol[e]','12dgr180[e]','hxan[e]',
    #  'pheme[e]', 'q8[e]','arab_D[e]','cgly[e]','cit[e]','no2[e]','no3[e]','ocdca[e]','orn[e]','pheme[e]','ptrc[e]','q8[e]','sheme[e]','spmd[e]','mqn7[e]']
    #p=p+q

    #comp_params.set_param('defaultKm', 0.000015)
    comp_params = c.params()
    # H
    #comp_params.set_param('timeStep',0.1)
    #comp_params.set_param('maxCycles', 100)
    # H/10
    comp_params.set_param('timeStep', 1)
    comp_params.set_param('maxCycles', 66)


    comp_params.set_param('defaultVmax', 18.5)
    comp_params.set_param('defaultKm', 0.000015)
    comp_params.set_param('spaceWidth', 1)
    comp_params.set_param('maxSpaceBiomass', 100)
    comp_params.set_param('minSpaceBiomass', 1e-11)
    comp_params.set_param('writeMediaLog', True)
    comp_params.set_param('writeTotalBiomassLog', True)
    comp_params.set_param('writeFluxLog', True)
    comp_assay = c.comets(test_tube, comp_params)
    comp_assay.obj_style = "MAX_OBJECTIVE_MIN_TOTAL"
    #print(test_tube.media)
    comp_assay.run()
    biomass = comp_assay.total_biomass
    biomass['t'] = biomass['cycle'] * comp_assay.parameters.all_params['timeStep']
    bm = biomass.copy()
    bm["Sp1"] = np.log(bm["Sp1"])
    biomass.to_csv(adir+'Biomass.csv')
    myplot = biomass.drop(columns=['cycle']).plot(x = 't')
    #plt.show()
    plt.savefig(adir + 'Biomass_normal')
    plt.close()

    myplot = bm.drop(columns=['cycle']).plot(x = 't')
    myplot.set_ylabel("Ln Biomass (gr.)")
    #plt.show()
    plt.savefig(adir+"biomass_LN")
    plt.close()

    return (test_tube, comp_assay,biomass)


