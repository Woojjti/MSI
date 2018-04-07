#!/usr/bin/env python
"""
Chunk size influence.
"""
import os, arff, warnings
import numpy as np
import helper as h
import strlearn as sl
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn import neural_network
from scipy.interpolate import spline
warnings.simplefilter('ignore', DeprecationWarning)
warnings.simplefilter('ignore', ImportWarning)

example = 'csi'
dbname = example
resfolder = 'results'
length = 100000
window = 0

chunk_sizes = [10, 100, 1000]
points_on_plot = 100
evaluate_interval = length // points_on_plot

clfname = "MLP100"
clf = neural_network.MLPClassifier(hidden_layer_sizes=(100,))
controller = sl.controllers.Bare()

# Generation of stream from parameters
streams = [
    "generators.RandomRBFGenerator -r 1 -a 20",
    "generators.RandomRBFGenerator -r 2 -a 20",
    "generators.RandomRBFGenerator -r 3 -a 20"
]
h.generate_stream('ds/%s' % dbname, length, window, streams)

# Experimental loop
colors = 'rgbcmyk'
with open('ds/%s.arff' % dbname, 'r') as stream:
    dataset = arff.load(stream)
    data = np.array(dataset['data'])
    X = data[:, :-1].astype(np.float)
    y = data[:, -1]
    fig, ax = plt.subplots(len(chunk_sizes) + 1,
                           figsize=(4,2.5*(len(chunk_sizes)+1)))

    ax[0].set_ylim([.4, 1])
    ax[0].set_xticks([])
    ax[0].set_yticks([])

    i = 1
    for chunk_size in tqdm(chunk_sizes,ascii=True, desc="CHS"):
        filename = '%s/%s_chunk_%i.csv' % (resfolder, example, chunk_size)
        learner = sl.Learner(X, y, clf,
                             evaluate_interval=evaluate_interval,
                             chunk_size=chunk_size,
                             controller=controller)
        learner.run()
        learner.serialize(filename)
        ax[i].plot(learner.score_points,
                 learner.scores, label=chunk_size, c = colors[i-1])
        ax[i].set_title("chunk of %i samples" % chunk_size)
        ax[i].set_ylim([.4, 1])
        ax[i].set_xticks([])
        ax[i].set_yticks([])

        ax[0].plot(learner.score_points,
                   learner.scores, label=chunk_size, c = colors[i-1])
        i += 1
plt.savefig('figures/%s.png' % example)
