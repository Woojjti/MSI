#!/usr/bin/env python
"""
Number of neurons in hidden layer vs sudden drift.
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

example = 'strike'
dbname = example
resfolder = 'results'
length = 400000
window = 0

chunk_size = 100
points_on_plot = 100
evaluate_interval = length // points_on_plot

clfs = {
    #"MLP5": neural_network.MLPClassifier(hidden_layer_sizes=(5,)),
    "MLP20": neural_network.MLPClassifier(hidden_layer_sizes=(20,)),
    "MLP60": neural_network.MLPClassifier(hidden_layer_sizes=(60,)),
    "MLP100": neural_network.MLPClassifier(hidden_layer_sizes=(100,)),
    "MLP500": neural_network.MLPClassifier(hidden_layer_sizes=(500,)),
    "MLP1000": neural_network.MLPClassifier(hidden_layer_sizes=(1000,)),
    "MLP10000": neural_network.MLPClassifier(hidden_layer_sizes=(10000,)),
    #"MLP500": neural_network.MLPClassifier(hidden_layer_sizes=(500,))
}

controller = sl.controllers.Bare()

# Generation of stream from parameters
streams = [
    "generators.RandomRBFGenerator -r 1 -a 20",
    "generators.RandomRBFGenerator -r 3 -a 20"
]
h.generate_stream('ds/%s' % dbname, length, window, streams)

# Experimental loop
colors = 'rgbcmyk'

plt.ylim([0, 1])
# plt.xticks([])
# plt.yticks([])
with open('ds/%s.arff' % dbname, 'r') as stream:
    dataset = arff.load(stream)
    data = np.array(dataset['data'])
    X = data[:, :-1].astype(np.float)
    y = data[:, -1]
    fig, ax = plt.subplots(len(clfs) + 1,
                           figsize=(6,2.5*(len(clfs)+1)))
    ax[0].set_ylim([.4, 1])
    ax[0].set_xticks([])

    i = 1
    for clfname in tqdm(clfs,ascii=True, desc="CLF"):
        clf = clfs[clfname]
        filename = '%s/%s_%s.csv' % (resfolder, example, clfname)
        learner = sl.Learner(X, y, clf,
                             evaluate_interval=evaluate_interval,
                             chunk_size=chunk_size,
                             controller=controller)
        learner.run()
        learner.serialize(filename)
        ax[0].plot(learner.score_points, learner.scores,
                      label=clfname, c = colors[i])

        ax[i].plot(learner.score_points, learner.scores,
                      label=clfname, c = colors[i])
        ax[i].set_title("%s" % clfname)
        ax[i].set_ylim([.4, 1])
        ax[i].set_xticks([])
        #ax[i].set_yticks([])

        i+=1
ax[0].legend()
plt.savefig('figures/%s.png' % example)
