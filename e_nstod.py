#!/usr/bin/env python
"""
Network structure type of drift
Testujemy wplyw struktury sieci (liczba neuronow) na krzywa uczenia w zaleznosci od rodzaju dryfu (plynny vs nagly).
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

example = 'nstod'
resfolder = 'results'
length = 100000
windows = [0, 11111, 22222, 33333]

chunk_size = 100
points_on_plot = 100
evaluate_interval = length // points_on_plot

clfs = {
    "MLP10": neural_network.MLPClassifier(hidden_layer_sizes=(10,)),
    "MLP50": neural_network.MLPClassifier(hidden_layer_sizes=(50,)),
    "MLP100": neural_network.MLPClassifier(hidden_layer_sizes=(100,)),
    "MLP500": neural_network.MLPClassifier(hidden_layer_sizes=(500,))
}

controller = sl.controllers.Bare()

# Generation of stream from parameters
streams = [
    "generators.RandomRBFGenerator -r 1 -a 20",
    "generators.RandomRBFGenerator -r 2 -a 20",
    "generators.RandomRBFGenerator -r 3 -a 20"
]
for window in windows:
    h.generate_stream("ds/%s_%i" % (example, window), length, window, streams)

# Experimental loop
colors = 'rgbcmyk'
fig, ax = plt.subplots(len(windows) + 1,len(clfs),
                       figsize=(len(clfs)*4,2.5*(len(windows)+1)))
j=0
for window in tqdm(windows, ascii=True, desc="WIN"):
    dbname = "ds/%s_%i" % (example, window)
    ax[0][j].set_ylim([.4, 1])
    ax[0][j].set_xticks([])
    ax[0][j].set_yticks([])
    ax[0][j].set_title(dbname)
    with open('%s.arff' % dbname, 'r') as stream:
        dataset = arff.load(stream)
        data = np.array(dataset['data'])
        X = data[:, :-1].astype(np.float)
        y = data[:, -1]
        i = 1
        for clfname in tqdm(clfs,ascii=True, desc="CLF"):
            clf = clfs[clfname]
            filename = '%s/%s_w_%i_%s.csv' % (resfolder, example, window, clfname)
            learner = sl.Learner(X, y, clf,
                                 evaluate_interval=evaluate_interval,
                                 chunk_size=chunk_size,
                                 controller=controller)
            learner.run()
            learner.serialize(filename)
            ax[i][j].plot(learner.score_points, learner.scores,
                          label=chunk_size, c = colors[i-1])
            ax[i][j].set_title("%s" % clfname)
            ax[i][j].set_ylim([.4, 1])
            ax[i][j].set_xticks([])
            ax[i][j].set_yticks([])

            ax[0][j].plot(learner.score_points, learner.scores,
                          label=chunk_size, c = colors[i-1])
            i += 1
    j += 1
plt.savefig('figures/%s.png' % example)
