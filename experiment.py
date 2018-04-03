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
dbnames = [
    'RBFGradualRecurring',
    'covtypeNorm', 'poker-lsn',
    'RandomTreeRecurringFaster',
    'RandomTreeRecurring', 'elecNormNew', 'SEASuddenFaster',
    'SEASudden', 'LEDNoDrift', 'LED', 'HyperplaneFaster', 'HyperplaneSlow',
    'RBFNoDrift', 'RBFBlips'
]
clfs = {
    "MLP100": neural_network.MLPClassifier(hidden_layer_sizes=(100,)),
    "MLP50": neural_network.MLPClassifier(hidden_layer_sizes=(50,)),
    "MLP101010": neural_network.MLPClassifier(hidden_layer_sizes=(10, 10, 10)),
    "MLP7": neural_network.MLPClassifier(hidden_layer_sizes=(7,))
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
        for controller in tqdm(controllers, ascii=True, desc="CON"):
            for clfname in tqdm(clfs,ascii=True, desc="CLF"):
                clf = clfs[clfname]
                filename = 'results/%s_%s_%s.csv' % (clfname, dbname, controller)
                if os.path.isfile(filename):
                    pass
                else:
                    learner = sl.Learner(X, y, clf,
                                         evaluate_interval=1000, chunk_size=500,
                                         controller=controller)
                    learner.run()
                    learner.serialize(filename)
