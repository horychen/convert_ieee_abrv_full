#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Abbreviate Journal Names in Bibtex Database.py
#   python2: https://gist.github.com/FilipDominec/9ff081952dbc4aae1df657a56c3db4ea
#   python3: https://gist.github.com/trevismd/e97d85690ca82d65c41447c9f61c8137
# JabRef - abbrv.jabref.org
#   https://github.com/JabRef/abbrv.jabref.org/tree/main/journals

import sys, os, re, csv
with open('./journal_abbreviations_ieee_strings.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    rules = tuple(reader)

def 化繁为简(bibfname_nosuffix):

    with open(bibfname_nosuffix+'.bib', encoding='utf-8') as bibtexfile:
        bibtexdb = bibtexfile.read()

        for rule in rules:
            pattern1, pattern2 = r'{'+rule[0].strip()+r'}', rule[1].strip()[1:-1]
            # print(pattern1, pattern2)

            if pattern1 != pattern1.upper() and (' ' in pattern1):    ## avoid mere abbreviations
                repl = re.compile(re.escape(pattern1), re.IGNORECASE) ## this is more robust, although ca. 10x slower
                (bibtexdb, num_subs) = repl.subn(pattern2, bibtexdb)
                if num_subs > 0:
                    print ("A Replacing '%s' FOR '%s'" % (pattern1, pattern2))

    with open(bibfname_nosuffix+'_abrv.bib', 'w', encoding='utf-8') as outfile:
        outfile.write(bibtexdb)
        print ("Done adding _abrv.bib")

def 由俭入奢(bibfname_nosuffix):

    with open(bibfname_nosuffix+'.bib', encoding='utf-8') as bibtexfile:
        bibtexdb = bibtexfile.read()

        for rule in rules:
            pattern1, pattern2 = r'{'+rule[0].strip()+r'}', rule[1].strip()[1:-1]
            # print(pattern1, pattern2)

            if pattern2 == pattern2.upper() and (' ' not in pattern2): ## avoid mere abbreviations
                repl = re.compile(re.escape(pattern2), re.IGNORECASE)  ## this is more robust, although ca. 10x slower
                (bibtexdb, num_subs) = repl.subn(pattern1, bibtexdb)
                if num_subs > 0:
                    print ("B Replacing '%s' FOR '%s'" % (pattern2, pattern1))

    with open(bibfname_nosuffix+'_full.bib', 'w', encoding='utf-8') as outfile:
        outfile.write(bibtexdb)
        print ("Done adding _full.bib")

if __name__ == '__main__':
    
    化繁为简('pBOOK')

    由俭入奢('pBOOK_abrv')

