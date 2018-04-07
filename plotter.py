#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

clfname = "MLP100"
tresholds = [.1, .3, .5, .7, .9]
budgets = [.1, .3, .5, .7, .9]
dbnames = [
    'RBFGradualRecurring', 'RBFNoDrift', 'RBFBlips', 'SEASuddenFaster',
    'SEASudden', 'LEDNoDrift', 'LED', 'HyperplaneFaster', 'HyperplaneSlow',
    'elecNormNew', 'covtypeNorm', 'poker-lsn'
]
# dbnames = dbnames[:1]

for dbname in dbnames:
    print("# %s" % dbname)
    bare = pd.read_csv("results/%s_%s_bare.csv" % (
        clfname, dbname
    )).values
    x = bare[:,0]
    length = np.max(x)
    divider = length / 100
    y_bare = bare[:,1]
    fig, ax = plt.subplots(5,5, figsize=(12,8), sharex=True,
                           sharey=True)
    fig.subplots_adjust(hspace=0, wspace=0)
    fig.suptitle("Learning curves for %s dataset" % dbname, fontsize=14)
    for i, b in enumerate(budgets):
        ax[i,0].set_ylabel("b = %.1f" % b)
        budget = pd.read_csv("results/%s_%s_bc_b%.2f.csv" % (
            clfname, dbname, b
        )).values
        y_budget = budget[:,1]
        y_budget_u = budget[:,4] / divider
        for j, t in enumerate(tresholds):
            ax[0,j].set_title("t = %.1f" % t)
            bl = pd.read_csv("results/%s_%s_blalc_b%.2f_t%.2f.csv" % (
                clfname, dbname, b, t
            )).values
            y_bl = bl[:,1]
            y_bl_u = bl[:,4] / divider

            # Plotting
            ax[i,j].set_ylim(0,1)

            # Bare
            ax[i,j].plot(x, y_bare, c='black', linewidth=.5)

            # Budget
            ax[i,j].plot(x, y_budget, c='blue', linewidth=.5)
            ax[i,j].plot(x, y_budget_u, c='blue',
                         linewidth=1 , linestyle='dotted')

            # Budget
            ax[i,j].plot(x, y_bl, c='red')
            ax[i,j].plot(x, y_bl_u, c='red',
                         linewidth=1 , linestyle='dotted')
    plt.savefig("figures/%s.png" % dbname)
