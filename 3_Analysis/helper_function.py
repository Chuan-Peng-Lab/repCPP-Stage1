import mne
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def preprocess_raw_data(subjidx,taskidx):
    # read data
    #- set the number of participant and task
    #- load eeg data
    #- load behavioral data
    ## set the number of participant and task
    # set the number of participant and task
    ## load eeg data
    # load eeg data
    # 'sub-0x_task-xx_run-0x_eeg.xxx'
    folder = '../2_Data/BIDS' # the root directory
    task = os.path.join('sub-'+str(subjidx).zfill(2)+'_task-GTDT_run-'+str(taskidx).zfill(2)+'_eeg.vhdr') # the task name of the experiment 
    filename_eeg = os.path.join(folder,'sub-'+str(subjidx).zfill(2),'eeg',task) # the file name of the eeg data in this experiment
    raw = mne.io.read_raw_brainvision(filename_eeg, preload=True)
    raw.load_data()
    ## load behavioral data

    # preprocess the eeg data
    #In this part, I will describe how we preprocess these data, the steps are listed below, and the details will be described in the following part.

    #- set the channel type
    #- set the electrode location
    #- resample to 512 Hz
    #- filter 1-30 Hz   
    #- rereference
    #- remove ica components
    ## set the channel type
    # set the channel type
    raw.set_channel_types({'EOG':'eog'})   
    # check if the 
    if raw.get_channel_types(['EOG'])[0] == 'eog': # check if the EOG is set as the 'eog'
        pass
    else:
        raise ValueError('Error: Channel type is not EOG.') # if not rasie error
    ## set the electrode location
    # set the electrode location
    raw.set_montage('standard_1020')
    # check if the electrode location is standard 1020 system
    if all(channel in mne.channels.make_standard_montage('standard_1020').ch_names for channel in raw.copy().pick_types(eog=False, eeg=True).info.ch_names):
        pass
    else:
        raise ValueError('Error: montage is not standard 1020') # if not rasie error
    ## resample to 512 Hz
    # resample to 512 Hz
    raw.resample(512, npad="auto")
    # check if the sample rate is 512 Hz
    if raw.info['sfreq'] == 512:
        pass
    else:
        raise ValueError('Error: sample rate is not 512 Hz') # if not rasie error
    ## filter 1-30 Hz   
    # filter 1-30 Hz   
    raw.filter(l_freq=1, h_freq=30, picks=['eog','eeg'])
    # check if the filter is 1-30 Hz   
    if raw.info['highpass']==1 and raw.info['lowpass']==30:
        pass
    else:
        raise ValueError('Error: filter is not 1-30 Hz') # if not rasie error
    ## rereference
    # rereference
    raw.set_eeg_reference('average')
    return raw