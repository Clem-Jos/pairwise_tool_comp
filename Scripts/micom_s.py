import pandas as pd
from micom import Community
import shutil
from micom.workflows import tradeoff
from micom.data import test_db
from micom.workflows import build
import tempfile
from micom.media import minimal_medium
# from micom.workflows import workflow
from medium import *


from os import listdir
from os.path import isfile, join


def createCombination(init_condition, nbComb):
    """
    Function creating a ist of species combination function used to run species pairwise
    Can be use alone
    :param init_condition: List compound to use in combination
    :param nbComb:
    :return:
    """
    combination = []
    for i in range(len(init_condition)):
        combination.append([init_condition[i]])
    while len(combination[-1]) < nbComb:
        comb2 = []
        for a in combination:
            for b in init_condition:
                comb2.append(a + [b])
        combination = deleteBis(comb2)
    return combination


def deleteBis(valbis):
    """
    Function linked to create combination, delete the dubbed data.
    :param valbis:
    :return:
    """
    toDel = []
    for i in range(len(valbis)):
        valbis[i].sort()
        for j in range(len(valbis[i])):
            if valbis[i][j] in valbis[i][j + 1:]:
                toDel.append(i)
    if toDel:
        toDel.sort(reverse=True)
    for i in toDel:
        del (valbis[i])
    toDel = []
    for i in range(len(valbis)):
        if valbis[i] in valbis[i + 1:]:
            toDel.append(i)
    if toDel:
        toDel.sort(reverse=True)
    for i in toDel:
        del (valbis[i])
    return valbis


def c_combination(files, path):
    id = [f[:-4] for f in files]
    files = [path + f for f in files]
    cmb = [i for i in range(len(files))]
    combinations = createCombination(cmb, 2)
    IDS_all = []
    FILES_all = []
    for a, b in combinations:
        IDS_all.append([id[a], id[b]])
        FILES_all.append([files[a], files[b]])
    return IDS_all, FILES_all


def run_pairwise(ids, files, med):
    d = {'id': ids, 'file': files}
    df = pd.DataFrame(data=d)
    com = Community(df, solver='gurobi')#change for gurobi here only for AKK , solver="cplex"
    # print("Build a community with a total of {} reactions.".format(len(com.reactions)))
    #print(com.taxonomy)
    """DEFINE MEDIUM
    Med is a dictionary with the reaction name_m  and the value of the flux."""
    com.medium = med
    single = [com.optimize_single(ids[0]), com.optimize_single(ids[1])]

    #The medium is not ideal, which is half of a problem since the model will be the same for the different environment
    solution1 = com.optcom('moma', 0, False, True)  # marche
    solution2 = com.optcom('lmoma', 0, False, True)  # marche
    solution3 = com.optcom('original', 0, False, True)  # marche
    #define tradeoff for each twice species : tradeoff ==

    medium = pd.DataFrame.from_dict(med, orient='index', columns=['flux'])
    medium=medium.rename_axis('reaction').reset_index()

    tempdir = tempfile.mkdtemp()
    sample_id=['sample_1','sample_1']


    data= pd.DataFrame(list(zip(ids, files, sample_id)), columns =['id', 'file','sample_id'])
    manifest = build(data,model_db=None, out_folder=tempdir, cutoff=0.0001,threads=1,solver='gurobi')  # create a temp  with the two models,solver='gurobi'

    tradeoff_rates = tradeoff(manifest, model_folder=tempdir, medium=medium, threads=1)
    res=tradeoff_rates.groupby("tradeoff").apply(lambda df: (df.growth_rate > 1e-6).sum()).reset_index()

    maxsp = res[0].min()
    shutil.rmtree(tempdir)
    trdoff = res['tradeoff'].loc[res[0] == maxsp].min()
    test=tradeoff_rates['growth_rate'].loc[tradeoff_rates['tradeoff']==trdoff]
    solution4 = com.cooperative_tradeoff(fraction=trdoff,fluxes=False, pfba=True,min_growth=0)
    return single,solution1.members, solution2.members, solution3.members, solution4.members
   

def micom_mono(id,file,med):
    d = {'id': [id], 'file': [file]}
    df = pd.DataFrame(data=d)
    com = Community(df,solver='gurobi')
    med2 = minimal_medium(com, 0.8, min_growth=0.8)

    """DEFINE MEDIUM
    Med is a dictionary with the reaction name_m  and the value of the flux."""
    com.medium = med
    single = [com.optimize_single(id)]

    return single
