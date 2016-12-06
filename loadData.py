# -*- coding: utf-8 -*-
"""
This script loads the SNP data from a pair of diseases and estimates the 
genetic correlation per chromosome

Proposed methodology:

For each chromosome:
    Region = Whole Chromosome
    

"""

import pandas as pd
import os

rootdir = '/home/sitara/Documents/6.047-Data/'  # Change this to the path to the data when running on your machine
disease1_SNP = 'pgc.bip.full.2012-04.txt'
disease2_SNP = 'pgc.bip.full.2012-04.txt'

# Load data into a pandas df

disease1 = pd.read_csv(rootdir+disease1_SNP, sep='\t',names=['snpid', 'hg18chr', 'bp', 'a1', 'a2', 'or', 'se', 'pval', 'info', 'ngt', 'CEUaf'],skiprows=[0]) 
disease2 = pd.read_csv(rootdir+disease2_SNP, sep='\t',names=['snpid', 'hg18chr', 'bp', 'a1', 'a2', 'or', 'se', 'pval', 'info', 'ngt', 'CEUaf'],skiprows=[0]) 

# Convert the relevant columns to numeric values
disease1[['bp']] = disease1[['bp']].apply(pd.to_numeric, errors='coerce')
disease2[['bp']] = disease2[['bp']].apply(pd.to_numeric, errors='coerce')


print 'Loaded data'
print '\t Disease 1: \n'
print disease1.head()
print '\t Disease 2: \n'
print disease2.head()

def estimate_corr(chromosome, region_start, region_end):
    '''Given a chromosome and region, creates a SNP data file for each disease,
    computes the genetic correlation between the two diseases in that region, 
    then deletes the created file.
    '''
    d1_file = disease1[disease1.hg18chr==chromosome][disease1.bp>=region_start][disease1.bp<=region_end]    
    d2_file = disease1[disease2.hg18chr==chromosome][disease2.bp>=region_start][disease2.bp<=region_end]

    # Save dataframes to textfile 
    filename = str(chromosome)+'_'+str(region_start)+'_'+str(region_end)
    d1_file.to_csv(rootdir+filename+'1.txt',sep='\t')
    d2_file.to_csv(rootdir+filename+'2.txt',sep='\t')
    
    # Estimate the genetic correlation
    corr = get_genetic_corr(rootdir+filename+'1.txt', rootdir+filename+'2.txt')
    
    # Remove files from folder
    os.remove(rootdir+filename+'1.txt')
    os.remove(rootdir+filename+'2.txt')
    
    return corr
    
def get_genetic_corr(disease1_file, disease2_file):
    '''Runs mungestat and ldsc on two diseases to estimate the genetic correlation'''
    # TODO: Complete this
    pass




    