
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import timezone
import pytz
from matplotlib import dates as mdates
import os
import ast
import calendar
# %matplotlib inline
# plots.py
def readiness_score_plot(patient, readiness_df):
#     input_file = "{}/{}_readiness.csv".format(patient, patient)
#     df = pd.read_csv(input_file)[["summary_date", "score"]]
    rdf = readiness_df.tail(20)
    av_score = np.mean(rdf["score"])

    x = mdates.datestr2num(rdf['summary_date'])
    y = rdf["score"]

    fig, ax = plt.subplots(figsize=(15,8))
    ax.clear() # Clear the axes
    ax.plot(x, y, 'bo-', color = 'pink') #Plot the data
    ##Below draws horizontal line for the average readiness score
    plt.axhline(y = (av_score), color = 'red', linestyle = '--', linewidth = 0.75)

    plt.xticks(x,rotation = '75')

    ax.xaxis_date()
    xfmt = mdates.DateFormatter('%d-%b-%y')
    ax.xaxis.set_major_formatter(xfmt)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))   # Every 1 Day

    plt.style.use('bmh')
    plt.xlabel('Dates\n')
    plt.ylabel('Readiness Score\n')
    plot_title = "Daily Readiness Scores - {}".format(patient)
    plt.title(plot_title + "\n")
    plt.rcParams["font.size"] = "12"
    plt.tick_params(left = False, bottom = False, labelsize = 10)
    plt.box(False)

    # os.path.join(datadir, file_name)
    output_file = "{}/{}_readiness.png".format(patient, patient)
    output_path = os.path.join('plots/'+output_file)
    plt.savefig(output_path)


def sleep_score_plot(patient, sleep_df):
#     input_file = "{}/{}_sleep.csv".format(patient, patient)

#     df = pd.read_csv(input_file)[["summary_date", "score"]]
    ssdf = sleep_df.tail(20)
    av_score = np.mean(ssdf["score"])

    x = mdates.datestr2num(ssdf['summary_date'])
    y = ssdf["score"]

    fig, ax = plt.subplots(figsize=(15,8))
    ax.clear() # Clear the axes
    ax.plot(x, y, 'bo-', color = 'skyblue') #Plot the data
    ##Below draws horizontal line for the average sleep score
    plt.axhline(y = (av_score), color = 'red', linestyle = '--', linewidth = 0.75)

    plt.xticks(x,rotation = '75')
    ax.xaxis_date()
    xfmt = mdates.DateFormatter('%d-%b-%y')
    ax.xaxis.set_major_formatter(xfmt)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

    plt.style.use('bmh')
    plt.xlabel('Dates\n')
    plt.ylabel('Sleep Score\n')
    plot_title = "Daily Sleep Scores - {}".format(patient)
    plt.title(plot_title + "\n")
    plt.rcParams["font.size"] = "12"
    plt.tick_params(left = False, bottom = False, labelsize = 10)
    plt.box(False)

    output_file = "{}/{}_sleep.png".format(patient, patient)
    output_path = os.path.join('plots/'+output_file)
    
    os.makedirs(os.path.join("plots", patient), exist_ok=True)
    
    plt.savefig(output_path)


def bedtimes_plot(patient, bedtimedf):

#     input_file = "{}/{}_sleep_periods.csv".format(patient, patient)
#     df = pd.read_csv(input_file)
#     date_format='%m/%d/%Y %H:%M:%S %Z'

#     bedtimedf = df[["bedtime_start"]]
#     bedtimedf["bedtime_start"] = pd.to_datetime(bedtimedf["bedtime_start"], utc="false")
#     bedtimedf["bedtime_start"] = bedtimedf["bedtime_start"].apply(lambda x: x.astimezone(timezone('US/Pacific')))

#     bedtimedf["start_date"] = bedtimedf["bedtime_start"].dt.date.astype(str)
#     bedtimedf["start_time"] = bedtimedf["bedtime_start"].dt.time.astype(str)

    col = pd.to_timedelta(bedtimedf["start_time"].astype(str))
    time = col.mean()
    t = (datetime.min + time).time()
    av_bedtime = pd.to_datetime(t.strftime("%H:%M:%S"))

    bedtime_plot = bedtimedf.tail(20)
    x = mdates.datestr2num(bedtime_plot['start_date'])
    y = mdates.datestr2num(bedtime_plot['start_time'])

    fig, ax = plt.subplots(figsize=(15,8))
    ax.clear() # Clear the axes
    ax.plot(x, y, 'bo-', color = 'dodgerblue')
    ##Below lines are to draw a horizontal line average bedtime
    plt.axhline(y = mdates.date2num (pd.to_datetime(av_bedtime)), color = 'red', linestyle = '--', linewidth = 0.75)

    plt.xticks(x,rotation = '75')
    ax.yaxis_date()
    ax.xaxis_date()

    yfmt = mdates.DateFormatter('%H:%M')
    xfmt = mdates.DateFormatter('%d-%b-%y')
    ax.yaxis.set_major_formatter(yfmt)
    ax.xaxis.set_major_formatter(xfmt)
    ax.yaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

    plt.style.use('bmh')
    plt.xlabel('Dates\n')
    plt.ylabel('Bedtime\n')
    plot_title = "Daily Bedtimes - {}".format(patient)
    plt.title(plot_title + "\n")
    plt.rcParams["font.size"] = "12"

    plt.tick_params(left = False, bottom = False, labelsize = 10) #Remove ticks, make tick labelsize 10
    plt.box(False)

    output_file = "{}/{}_bedtimes.png".format(patient, patient)
    output_path = os.path.join('plots/'+output_file)
    
    os.makedirs(os.path.join("plots", patient), exist_ok=True)
    
    plt.savefig(output_path)


def sleep_stages_plot(patient, sleepstage_df):
#     input_file = "{}/{}_sleep_periods.csv".format(patient, patient)
#     df = pd.read_csv(input_file)#, parse_dates = ["bedtime_start", "bedtime_end)#"])

#     sleepstage_df = df[["day", "bedtime_start", "bedtime_end", "awake_time", "deep_sleep_duration", "light_sleep_duration", "rem_sleep_duration"]]
#     sleepstage_df["bedtime_start"] = pd.to_datetime(sleepstage_df["bedtime_start"], utc="false")
#     sleepstage_df["bedtime_end"] = pd.to_datetime(sleepstage_df["bedtime_end"], utc="false")
#     sleepstage_df["bedtime_start"].apply(lambda x: x.astimezone(timezone('US/Pacific')))
#     sleepstage_df["bedtime_end"].apply(lambda x: x.astimezone(timezone('US/Pacific')))
#     sleepstage_df["start_date"] = sleepstage_df["bedtime_start"].dt.date
#     sleepstage_df["end_date"] = sleepstage_df["bedtime_end"].dt.date

    td = '2019-02-15'
    test_date = sleepstage_df.sort_values(by="start_date")[sleepstage_df["day"] == td].head(1)
    plot_point_ss = test_date[['awake_time', 'deep_sleep_duration', 'light_sleep_duration', 'rem_sleep_duration']]
    plot_point_ss = plot_point_ss/60/60

    # sns.set(style="darkgrid")
    # plt.figure(figsize = (14, 14))
    plot_point_ss.plot(kind='bar', stacked=True, color=['pink', 'red', 'blue', 'skyblue'])
    plot_title = "Sleep Stages for {} - {}".format(td, patient)
    plt.title(plot_title + "\n")
    plt.xlabel(td)
    plt.ylabel('Hours')

    output_file = "{}/{}_sleep_stages.png".format(patient, patient)
    output_path = os.path.join('plots/'+output_file)
    
    os.makedirs(os.path.join("plots", patient), exist_ok=True)
    
    plt.savefig(output_path)

def resting_hr_plot(patient, df, day=""):
    """
    Creates a resting heart rate plot for the specified date or the latest night.
    """
    if len(day) == 0:
        selection = df.iloc[-1]
        hr = selection["heart_rate"]
        bedtime = selection["bedtime_start"]
    else:
        selection = df[df["day"] == day]
        hr = selection["heart_rate"].iloc[0]
        bedtime = selection["bedtime_start"].iloc[0]

    times = []
    x = 300
    for i in hr["items"]:
        times.append((bedtime) + pd.Timedelta("{} seconds".format(x)))
        x += 300

    fig, ax = plt.subplots(figsize=(15,8))
    ax.clear() # Clear the axes
    ax.plot(times, hr["items"], color = 'skyblue')
    plt.title("Resting Heart Rate", fontsize=15)
    plt.axhline(pd.Series(hr["items"]).mean(), color='black', ls="--")

    plt.xlabel('Time\n')
    plt.ylabel('Heart Rate\n')
    plt.rcParams["font.size"] = "12"
    plt.tick_params(left = False, bottom = False, labelsize = 10)
    plt.box(False)

    output_file = "{}/{}_resting_hr.png".format(patient, patient)
    output_path = os.path.join('plots/'+output_file)
    
    os.makedirs(os.path.join("plots", patient), exist_ok=True)
    
    plt.savefig(output_path)

def longitudinal_hr_sleep_burn(patient, df, month="", year=""):
    """
    Creates graph that shows longitudinal data including calories burnt, sleep hours, and lowest heart rate.
    If no month or year given, returns the graph for the last fully complete month. (second to last).
    """
    if len(month) == 0:
        year = df.iloc[-1].Year
        month = df.iloc[-1].Month - 1

    df = df[(df["Year"] == year) & (df["Month"] == month)]

    fig, ax = plt.subplots(3, figsize=(15,15))
    fig.suptitle('{} {} Recap'.format(calendar.month_name[month], year))
    ax[0].plot(df["Day"], df["hr_lowest"], color = 'darkblue')
    ax[0].set_xlabel("Day")
    ax[0].set_ylabel("Lowest Heart Rate")

    ax[1].plot(df["Day"], df["Sleep"], color = 'skyblue')
    ax[1].set_xlabel("Day")
    ax[1].set_ylabel("Total Sleep Hours")

    ax[2].plot(df["Day"], df["cal_active"], color = 'orange')
    ax[2].set_xlabel("Day")
    ax[2].set_ylabel("Calories Burned")

    output_file = "{}/{}_longitudinal_recap_{}_{}.png".format(patient, patient, month, year)
    output_path = os.path.join('plots/'+output_file)
    
    os.makedirs(os.path.join("plots", patient), exist_ok=True)
    
    plt.savefig(output_path)
