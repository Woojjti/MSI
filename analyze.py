#!/usr/bin/env python
import pandas as pd
import numpy as np
from scipy import stats

np.set_printoptions(suppress=True)

clfname = "MLP100"
dbs = {
    'RBFGradualRecurring': (.9,.9),
    'RBFNoDrift': (.1,.9),
    'RBFBlips': (.9,.9),
    'SEASuddenFaster': (.3,.7),
    'SEASudden': (.1,.3),
    'LEDNoDrift': (.5,.9),
    'LED': (.5,.9),
    'HyperplaneFaster': (.5,.9),
    'HyperplaneSlow': (.1,.7),
    'elecNormNew': (.1,.9),
    'covtypeNorm': (.9,.9),
    'poker-lsn': (.9,.1)
}
# t, b

for db in dbs:
    t, b = dbs[db]

    # load data
    bare = pd.read_csv("results/%s_%s_bare.csv" % (
        clfname, db
    )).values
    bl = pd.read_csv("results/%s_%s_blalc_b%.2f_t%.2f.csv" % (
        clfname, db, b, t
    )).values

    x = bare[:,0]
    length = np.max(x)
    divider = length / 100

    y_bare = bare[:,1]
    y_bl = bl[:,1]
    y_bl_u = bl[:,4] / divider

    full_mean_accuracy = np.mean(y_bare)
    blalc_mean_accuracy = np.mean(y_bl)
    difference = blalc_mean_accuracy - full_mean_accuracy
    mean_usage = np.mean(y_bl_u)

    stat = stats.wilcoxon(y_bare, y_bl)
    p = stat.pvalue

    print("\\emph{%s} & .%.0f & %.0f & %.3f & %.3f & $%.3f$ & %.1f\\%%\\\\" % (
        db, t*10, b*10, full_mean_accuracy, blalc_mean_accuracy, difference, mean_usage * 100
        ))
