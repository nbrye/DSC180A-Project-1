#!/usr/bin/env python

#run.py

import sys
import os
import json
import numpy as np

sys.path.insert(0, 'src')

from etl import clean_bedtime, clean_sleep_stages, clean_readiness, clean_sleep, clean_resting_hr, clean_longitudinal_data

from plots import readiness_score_plot, sleep_score_plot, bedtimes_plot, sleep_stages_plot, resting_hr_plot, longitudinal_hr_sleep_burn


def main(targets):
    targets = targets[1:]
   

    for p in targets:
        if p == 'test':
            p = 'testdata'
            ddir = 'test'
        else:
            ddir = 'data'
            
        readiness_score_plot(p, clean_readiness(p, ddir))
        sleep_score_plot(p, clean_sleep(p, ddir))
        bedtimes_plot(p, clean_bedtime(p, ddir))
        resting_hr_plot(p, clean_resting_hr(p, ddir))
        
        # Test data is too small for the sleep stages plot and longitudinal plot
        try:
            sleep_stages_plot(p, clean_sleep_stages(p, ddir))
        except:
            pass
        
        if p!= 'testdata':
            longitudinal_hr_sleep_burn(p, clean_longitudinal_data(p, ddir))
            
    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv
    main(targets)

    print("Predictions were made and saved to plots folder")
