#!/bin/env python3

import sys
import os
from sentence_transformers import SentenceTransformer
import scipy.spatial
import numpy

print(len(sys.argv))
embedder = SentenceTransformer('bert-base-nli-mean-tokens')



def help():
    print(f"""
Monty Python Flying Muppet

Usage:

 * {sys.argv[0]} train shakespeare_script.txt
   Generate S-BERT embeddings for each line of the file
   "shakespeare_script.txt" into a file called "shakespeare_script.dat"

 * {sys.argv[0]} predict shakespeare_script.txt shakespeare_script.dat
                 holy_grail.txt <dont_like_the_film.txt>
   Generate S-BERT embeddings for each line of the file "holy_grail.txt" and
   use them to predict a line in holy_grail.txt. It prints to stdout unless
   the optional parameter "dont_like_the_film.txt" is given.

Copyright (C) Enrico Trombetta 2020, released under WTFPL. Can't think of
anything more appropriate.
   """)
    sys.exit(1)


def train(filename):
    dump_filename = os.path.splitext(filename)[0] + ".dat"

    with open(filename, "r") as f:
        lines = [s.strip() for s in f.readlines()]

    print("Training. This may take some time...")
    embeddings = embedder.encode(lines)

    print(f"Performed training; saving embeddings to {dump_filename}")

    with open(dump_filename, "wb") as f:
        numpy.save(f, embeddings)

def predict(original_script_filename, original_embedding_filename, test_script, *args):
    with open(original_embedding_filename, "rb") as dump_file:
        corpus_embedding = numpy.load(dump_file)

    with open(test_script, "r") as test_script_file:
        test_script_lines = [s.strip() for s in test_script_file.readlines()]

    test_script_embeddings = embedder.encode(test_script_lines)

    # Here's the albeit slow O(n*m) part.
    with open(original_script_filename, "r") as original_script_file:
        corpus = original_script_file.readlines()

    for line, line_embedding in zip(test_script_lines, test_script_embeddings):
        distances = scipy.spatial.distance.cdist([line_embedding],
                                                 corpus_embedding, "cosine")[0]

        results = zip(range(len(distances)), distances)
        picked_sentence_idx = min(results, key=lambda x: x[1])[0]
        print(corpus[picked_sentence_idx].strip() + " (original: " + line + ")" )


def main():
    args = sys.argv
    if len(args) < 2:
        help()

    command = args[1]
    print(command)
    if command == 'train':
        if len(args) == 3:
            train(args[2])
        else:
            help()
    elif command == 'predict':
        if 5 <= len(args) <= 6:
            predict(*args[2:])
        else:
            help()
    else:
        help()


if __name__ == '__main__':
    main()
