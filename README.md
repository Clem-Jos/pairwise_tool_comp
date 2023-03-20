# pairwise_tool_comp
Data used for the comparison of Genome Scale Metaboli model tool on bacterial species pairwise interactions
In this repository can be found the scripts,used to produce monoculture and coculture data, the produced results and the model that have been modified for this analysis.

## Content
We describe here the content of the four following directories:
### Extra figures
This directory contain the roc curves for every species or methods for each conditions. 

### Models
This directory contains the model modfified to be compatible with the AGORA models.

### Results
This directory contains excel file for :
- cocultures: the predicted coculture growth rate of maximal biomass and the ratio associated with each condition. Experimenta l ratio are added to tha table for comparison.
- experimental-ratio: contains the experimental ratio calculated or obtained from original articles.
- monocultures: predicted monocultures for each conditions with the experimental growth rates.

### Scripts
The 'Scripts' directory contains the scripts used to produce MICOM, MMT and COMETS results.
- micom_s: is the script containing the function to run MICOM on cocultures and monocultures.
- comets_s: is the script containing the function to run COMETS on cocultures and monocultures.
- mono_comets_micom: is the scriped executed for the production of monocultures results for MICOM and COMETS in function of the condition (cf file).
- co_comets_micom: is the scriped executed for the production of cocultures results for MICOM and COMETS in function of the condition (cf file).
- medium : is the file containing the desctiptio of each medium for MICOM and MMT.
- mmt_interaction : is the file to run mmt on pairs. The file contains the description of the media.
