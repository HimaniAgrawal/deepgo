#!/usr/bin/env python
import numpy as np
import pandas as pd
import click as ck

from utils import (
    get_gene_ontology, get_anchestors, get_go_set,
    EXP_CODES,
    BIOLOGICAL_PROCESS,
    MOLECULAR_FUNCTION,
    CELLULAR_COMPONENT)


DATA_ROOT = 'data/swissexp/'


@ck.command()
def main():
    df = pd.read_pickle(DATA_ROOT + 'test-bp.pkl')
    orgs = set(df['orgs'])
    df = pd.read_pickle(DATA_ROOT + 'test-mf.pkl')
    orgs |= set(df['orgs'])
    df = pd.read_pickle(DATA_ROOT + 'test-cc.pkl')
    orgs |= set(df['orgs'])
    pro = set()
    with open('data/prokaryotes.txt') as f:
        for line in f:
            org = line.strip().split(':')[1]
            if org in orgs:
                pro.add(org)
    eu = set()
    with open('data/eukaryotes.txt') as f:
        for line in f:
            org = line.strip().split(':')[1]
            if org in orgs:
                eu.add(org)
    df = pd.DataFrame({'orgs': list(eu)})
    print(df)
    df.to_pickle('eukaryotes.pkl')
    df = pd.DataFrame({'orgs': list(pro)})
    df.to_pickle('prokaryotes.pkl')



if __name__ == '__main__':
    main()
