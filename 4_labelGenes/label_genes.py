# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 08:22:32 2014

@author: Zackery Keith

"""
import json

gfffilename = "Mt4.0v1_genes_20130731_1800.gff3"

GFF = open(gfffilename)

GFF_dict=dict()

for line in GFF:
	if line[0] != "#":
		mSeqid, mSource, mType, mStart, mEnd, mScore, mStrand, mPhase, mAttr \
		= line.split('\t')
		if mType == "gene":
			line_tuple = (int(mStart), int(mEnd), mAttr)
			if mSeqid not in GFF_dict:
				GFF_dict[mSeqid] = list()
			GFF_dict[mSeqid].append(line_tuple)
			
print(len(GFF_dict))
	
for s in ["3", "5", "6", "7", "9", "10", "15", "17", "18"]:
 
	blastfilename = '/mnt/scratch/keithzac/Tf_Analysis/BlastOutput/Tf_' + s + 'blast'
	
	BLAST = open(blastfilename)

	BLAST_list = list()

	for line in BLAST:
		mQuery, mSubject, mIdent, mLen, mMis, mGap, mQStart, mQEnd, mSStart, \
		mSEnd, mE, mBit = line.split('\t')
		mSStart = int(mSStart)
		mSEnd = int(mSEnd)
		if mSEnd < mSStart:
			temp = mSEnd
			mSEnd = mStart
			mStart = temp
		line_tuple = (mSubject, mSStart, mSEnd) ##QStart or SStart?
		BLAST_list.append(line_tuple)
	
	print(len(BLAST_list))

	descriptions = dict()
	
	for match in BLAST_list:
		if match[0] in GFF_dict:
			for gene in GFF_dict[match[0]]:
				if match[1] >= gene[0]:
					if match[2] <= gene[1]:
						descriptions[match] = gene[2]
	
	outfilename = 'Tf_' + s + 'label'
	file = open(outfilename, 'w')

	for key in descriptions:
		file.write(descriptions[key]+'\n')