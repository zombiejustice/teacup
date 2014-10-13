###################################
#                                 #
# Teacup Genetics/Critters module #
#                                 #
###################################

import random

def make_genemap(cn = 8, sl = [['off', 3], ['def', 3], ['ddg', 3], ['sed', 2]]):
#[planned] called at world creation
#[planned] reads from plaintext skill/stat list
#used to look up locations of genes
#takes a number of chromosomes, cn; and
#   a list of [stat, weight] tuples, sl
#returns the genemap in the form
#   [{stat locations}, [chromosomes]]

    #populate chromosome list with blanks
    chromos = [[] for i in range(cn)]
    #populat stat dic with blanks
    stats = {}
    for s in sl:
        stats[s[0]] = []
    #slots stats into chromosome list
    while sl:
        i = random.randint(0, cn-1)
        s = sl.pop()
        #put the stat in the chromosome
        chromos[i].append(s[0])
        #put the chromo and gene indices into stat dict
        stats[s[0]].append((i, len(chromos[i])-1))
        #put important stats back in the queue
        if s[1] > 1:
            s[1] -= 1
            sl.append(s)
    #end while
    return [stats, chromos]

            
bear_sl = {'off': [0, 6], 'def': [1, 6], 'ddg': [-1, 2], 'sed': [1, 1]}
rabbit_sl = {'off': [0, 2], 'def': [-1, 1], 'ddg': [1, 6], 'sed': [1, 6]}

            
class Genetics:
#a class to hold genetic information
#and perform genetic manipulations

    def __init__(self, gm, sl):
    #[placeholder] this is for kings and other critters made by fiat
        return
        
        