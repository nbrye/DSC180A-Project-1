# etl.py
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import timezone
import pytz
from matplotlib import dates as mdates
import os
# %matplotlib inline

### Data Cleaning
def clean_bedtime(patient, datadir):
    '''
    load and clean the sleep periods data for bedtime plot
    '''
    file_name = "{}/{}_sleep_periods.csv".format(patient, patient)
    file_path = os.path.join(datadir, file_name)
    df = pd.read_csv(file_path)
    date_format='%m/%d/%Y %H:%M:%S %Z'

    bedtimedf = df[["bedtime_start"]]

    bedtimedf["bedtime_start"] = pd.to_datetime(bedtimedf["bedtime_start"], utc="false")
    bedtimedf["bedtime_start"] = bedtimedf["bedtime_start"].apply(lambda x: x.astimezone(timezone('US/Pacific')))

    bedtimedf["start_date"] = bedtimedf["bedtime_start"].dt.date.astype(str)
    bedtimedf["start_time"] = bedtimedf["bedtime_start"].dt.time.astype(str)

    return bedtimedf


def clean_sleep_stages(patient, datadir):
    '''
    load and clean the sleep periods data for the sleep stages plot
    '''
    file_name = "{}/{}_sleep_periods.csv".format(patient, patient)
    file_path = os.path.join(datadir, file_name)
    df = pd.read_csv(file_path)

    sleepstage_df = df[["day", "bedtime_start", "bedtime_end", "awake_time", "deep_sleep_duration", "light_sleep_duration", "rem_sleep_duration"]]
    sleepstage_df["bedtime_start"] = pd.to_datetime(sleepstage_df["bedtime_start"], utc="false")
    sleepstage_df["bedtime_end"] = pd.to_datetime(sleepstage_df["bedtime_end"], utc="false")
    sleepstage_df["bedtime_start"].apply(lambda x: x.astimezone(timezone('US/Pacific')))
    sleepstage_df["bedtime_end"].apply(lambda x: x.astimezone(timezone('US/Pacific')))
    sleepstage_df["start_date"] = sleepstage_df["bedtime_start"].dt.date
    sleepstage_df["end_date"] = sleepstage_df["bedtime_end"].dt.date

    return sleepstage_df

def clean_readiness(patient, datadir):
    '''
    load and clean the readiness data for the readiness plot
    '''

    file_name = "{}/{}_readiness.csv".format(patient, patient)
    file_path = os.path.join(datadir, file_name)
    df = pd.read_csv(file_path)[["summary_date", "score"]]
    return df

def clean_sleep(patient, datadir):
    '''
    load and clean the sleep data for the sleep score plot
    '''
    file_name = "{}/{}_sleep.csv".format(patient, patient)
    file_path = os.path.join(datadir, file_name)
    df = pd.read_csv(file_path)[["summary_date", "score"]]
    return df
