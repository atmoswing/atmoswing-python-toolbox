# -*- coding: utf-8 -*-

import os
import glob
import gzip
import shutil


def pack_file(f):
    with open(f, 'rb') as f_in:
        with gzip.open(f + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(f)
    print(f + ' compressed')


def compress_optimization_outputs(base_path):
    for x in os.listdir(base_path):
        path = os.path.join(base_path, x, 'results')
        final = glob.glob(path + '/*best_individual.txt')
        if len(final) > 0:
            # If optimization ended, compress all files.
            files_generations = glob.glob(path + '/*generations.txt')
            files_operators = glob.glob(path + '/*operators.txt')
            for f in files_generations:
                pack_file(f)
            for f in files_operators:
                pack_file(f)
        else:
            # If not, compress all files but the last.
            files_generations = glob.glob(path + '/*generations.txt')
            files_generations.sort()
            files_operators = glob.glob(path + '/*operators.txt')
            files_operators.sort()
            for f in files_generations[:-1]:
                pack_file(f)
            for f in files_operators[:-1]:
                pack_file(f)
