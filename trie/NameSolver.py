#!/usr/bin/env python

import codecs
import itertools

def split_good_bad(filename):
    good_names = set([])
    bad_names = set([])
    with codecs.open(filename, 'r', 'utf-8') as full_file:
        for entry in (name for elem in full_file for name in elem[1:-2].split(' ')):
            if u'\ufffd' in entry:
                bad_names.add(entry)
            else:
                good_names.add(entry)

    with codecs.open('bad_names', 'w+','utf-8') as bad_file:
        for x in bad_names:
            bad_file.write(x+'\n')
    with codecs.open('good_names', 'w+','utf-8') as good_file:
        for x in good_names:
            good_file.write(x+'\n')
        



if __name__ == "__main__":
    split_good_bad('/Users/pcalcao/Dropbox/all_names')
