#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:36:52 2017

"""
import sys;
import nltk;

file = open('./news.txt');
file_content = file.read();
result=[];
sentence_tuple = enumerate(nltk.tokenize.sent_tokenize(file_content));  
                          
print(sentence_tuple)
for sno, sent in sentence_tuple:
    wordlist = nltk.tokenize.word_tokenize(sent)
    posTagList = nltk.pos_tag(wordlist)
    totalN = len([word for word, pos in posTagList if pos in ['NN','NNP']])
    ners=nltk.ne_chunk(posTagList, binary=False)
    nerlist = [chunk for chunk in ners if hasattr(chunk, 'label')]
    totners= len(nerlist)
    score=(totners+totalN)/float(len(wordlist))
    result.append((sno, sent, score))
    
def print_summary(result): 
    sortedByScore = sorted(result, key=lambda item: item[2], reverse=True)
    summary = open("./summary.txt", "w")
    for i in range(5):
        tuple = sortedByScore[i]
        summary.write(tuple[1])

    
print_summary(result)