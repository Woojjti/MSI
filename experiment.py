#!/usr/bin/env python
from __future__ import absolute_import
from sklearn import neural_network
import strlearn as sl
import arff
import warnings
import numpy as np
import os.path
from tqdm import tqdm
warnings.simplefilter('ignore', DeprecationWarning)
warnings.simplefilter('ignore', ImportWarning)

# Set of parameters
points_on_plot = 100
dbnames = [
    'RBFGradualRecurring', 'RBFNoDrift', 'RBFBlips',
    # 'RandomTreeRecurringFaster', 'RandomTreeRecurring',
    'SEASuddenFaster', 'SEASudden',
    'LEDNoDrift', 'LED',
    'HyperplaneFaster', 'HyperplaneSlow',
    'elecNormNew', 'covtypeNorm', 'poker-lsn'
]
clfs = {
    "MLP100": neural_network.MLPClassifier(hidden_layer_sizes=(100,))
}
tresholds = [.1, .3, .5, .7, .9]
budgets = [.1, .3, .5, .7, .9]


# Set of controllers
controllers = []
controllers.append(sl.controllers.Bare())
for budget in budgets:
    controllers.append(sl.controllers.Budget(budget=budget))
for budget in budgets:
    for treshold in tresholds:
        controllers.append(sl.controllers.BLALC(
            budget=budget, treshold=treshold))

# Experimental loop
for dbname in tqdm(dbnames, ascii=True, desc="DBS"):
    with open('datasets/%s.arff' % dbname, 'r') as stream:
        dataset = arff.load(stream)
        data = np.array(dataset['data'])
        X = data[:, :-1].astype(np.float)
        y = data[:, -1]
        length = len(y)
        evaluate_interval = length // points_on_plot
        for controller in tqdm(controllers, ascii=True, desc="CON"):
            for clfname in clfs:
                clf = clfs[clfname]
                filename = 'results/%s_%s_%s.csv' % (clfname, dbname, controller)
                if os.path.isfile(filename):
                    pass
                else:
                    learner = sl.Learner(X, y, clf,
                                         evaluate_interval=evaluate_interval, chunk_size=500,
                                         controller=controller)
                    learner.run()
                    learner.serialize(filename)
