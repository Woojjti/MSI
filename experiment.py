import strlearn as sl
from sklearn import neural_network
import warnings

warnings.filterwarnings("ignore")

clfs = {
    "MLP": neural_network.MLPClassifier()
}

dbnames = [
    'covtypeNorm', 'poker-lsn',  # other real
    'RBFGradualRecurring',
    'RandomTreeRecurringFaster',
    'RandomTreeRecurring', 'elecNormNew', 'SEASuddenFaster',
    'SEASudden', 'LEDNoDrift', 'LED', 'HyperplaneFaster', 'HyperplaneSlow',
    'RBFNoDrift', 'RBFBlips'
]

tresholds = [.1, .3, .5, .7, .9]
budgets = [.1, .3, .5, .7, .9]

controllers = []

controllers.append(sl.controllers.Bare())
for budget in budgets:
    controllers.append(sl.controllers.Budget(budget=budget))

for budget in budgets:
    for treshold in tresholds:
        controllers.append(sl.controllers.BLALC(
            budget=budget, treshold=treshold))

for dbname in dbnames:
    for controller in controllers:
        for clfname in clfs:
            clf = clfs[clfname]
            filename = 'results/%s_%s_%s.csv' % (clfname, dbname, controller)
            print filename

            f = open('datasets/%s.arff' % dbname, 'r')
            learner = sl.Learner(
                f, clf, evaluate_interval=1000, chunk_size=500,
                controller=controller)
            learner.run()
            learner.serialize(filename)
