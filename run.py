#!/usr/bin/env python

#run.py

import sys
import os
import json
import numpy as np

sys.path.insert(0, 'src')

from etl import clean_bedtime, clean_sleep_stages, clean_readiness, clean_sleep

from plots import readiness_score_plot, sleep_score_plot, bedtimes_plot, sleep_stages_plot


def main(targets):
    inputs = ['patient_1', 'patient_2', 'patient_3']

    for p in inputs:
        readiness_score_plot(p, clean_readiness(p, "data"))
        sleep_score_plot(p, clean_sleep(p, "data"))
        bedtimes_plot(p, clean_bedtime(p, "data"))
        sleep_stages_plot(p, clean_sleep_stages(p, "data"))
    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv
    main(targets)

    print("Predictions were made and saved to plots folder")
