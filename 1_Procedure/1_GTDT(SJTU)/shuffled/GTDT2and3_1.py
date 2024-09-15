#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on 八月 17, 2023, at 18:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
from datetime import datetime


# Ensure that relative paths start from the same directory as this script
#root_dir = 'D:/happy_working/repCPP/Stage1/1_Procedure/1_Version_control/make_new/'    # change root #
root_dir = os.path.join(os.getcwd()+"/")
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'GTDT2and3_1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'age':'',
    'gender':'',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=root_dir + 'GTDT2and3_1.py', 
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='cm')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instruction1_1" ---
i1_1 = visual.ImageStim(
    win=win,
    name='i1_1', units='cm', 
    image=root_dir +'instruction1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction1_2" ---
i1_2 = visual.ImageStim(
    win=win,
    name='i1_2', units='cm', 
    image=root_dir +'instruction2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction1_3" ---
i1_3 = visual.ImageStim(
    win=win,
    name='i1_3', units='cm', 
    image=root_dir +'instruction3P2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation1" ---
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bstart = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "GTDT2_1" ---
annular = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=2.8,    #20230816  radius=0.25
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2 = visual.Pie(
    win=win, name='annular2',start=22.5, end=45,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular3 = visual.Pie(
    win=win, name='annular3',start=45, end=67.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular4 = visual.Pie(
    win=win, name='annular4',start=67.5, end=90,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular5 = visual.Pie(
    win=win, name='annular5',start=90,end=112.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular6 = visual.Pie(
    win=win, name='annular6',start=112.5,end=135,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular7 = visual.Pie(
    win=win, name='annular7',start=135,end=157.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular8 = visual.Pie(
    win=win, name='annular8',start=157.5,end=180,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular9 = visual.Pie(
    win=win, name='annular9',start=180,end=202.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular10 = visual.Pie(
    win=win, name='annular10',start=202.5,end=225,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular11 = visual.Pie(
    win=win, name='annular9',start=225,end=247.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular12 = visual.Pie(
    win=win, name='annular12',start=247.5,end=270,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular13 = visual.Pie(
    win=win, name='annular9',start=270,end=292.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular14 = visual.Pie(
    win=win, name='annular14',start=292.5,end=315,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular15 = visual.Pie(
    win=win, name='annular15',start=315,end=337.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular16 = visual.Pie(
    win=win, name='annular16',start=337.5,end=360,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
cover1 = visual.ShapeStim(
    win=win, name='cover1',units='cm', 
    size=(5.6, 5.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
center1 = visual.ShapeStim(
    win=win, name='center1',units='cm', 
    size=(2.8, 2.8), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='grey', fillColor='grey',
    opacity=None, depth=-3.0, interpolate=False)
bg1 = visual.Rect(
    win=win, name='bg1',units='cm', 
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
key_resp_4 = keyboard.Keyboard()
stimulus1 = parallel.ParallelPort(address='0x3EFC')

responses = parallel.ParallelPort(address='0x3EFC')
def responses_marker(value):
    responses.setData(value)
    core.wait(0.05)
    responses.setData(0)
# --- Initialize components for Routine "rest1" ---
rest_1 = visual.ImageStim(
    win=win,
    name='rest_1', units='cm', 
    image=root_dir +'rest1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()
bend1 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "instruction2" ---
i2 = visual.ImageStim(
    win=win,
    name='i2', units='cm', 
    image=root_dir +'instruction3P3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation2" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bstart2 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "GTDT3_1" ---
annular2_1 = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=2.8,    #20230816  radius=0.25
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_2 = visual.Pie(
    win=win, name='annular2',start=22.5, end=45,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_3 = visual.Pie(
    win=win, name='annular3',start=45, end=67.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_4 = visual.Pie(
    win=win, name='annular4',start=67.5, end=90,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_5 = visual.Pie(
    win=win, name='annular5',start=90,end=112.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_6 = visual.Pie(
    win=win, name='annular6',start=112.5,end=135,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_7 = visual.Pie(
    win=win, name='annular7',start=135,end=157.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_8 = visual.Pie(
    win=win, name='annular8',start=157.5,end=180,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_9 = visual.Pie(
    win=win, name='annular9',start=180,end=202.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_10 = visual.Pie(
    win=win, name='annular10',start=202.5,end=225,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_11 = visual.Pie(
    win=win, name='annular9',start=225,end=247.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_12 = visual.Pie(
    win=win, name='annular12',start=247.5,end=270,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_13 = visual.Pie(
    win=win, name='annular9',start=270,end=292.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_14 = visual.Pie(
    win=win, name='annular14',start=292.5,end=315,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_15 = visual.Pie(
    win=win, name='annular15',start=315,end=337.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_16 = visual.Pie(
    win=win, name='annular16',start=337.5,end=360,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
cover2 = visual.ShapeStim(
    win=win, name='cover',
    size=(5.6, 5.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=False)
center2 = visual.ShapeStim(
    win=win, name='center',
    size=(2.8, 2.8), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='grey', fillColor='grey',
    opacity=None, depth=-3.0, interpolate=False)
bg2 = visual.Rect(
    win=win, name='bg',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
stimulus2 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "question" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='请问在这个阶段中，你观察到圆环变暗的次数为？\n填写完成后按空格键提交',
    font='Open Sans',
    units='cm', pos=(-2, 0.15), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bend2 = parallel.ParallelPort(address='0x3EFC')
textbox = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -2.5),units='cm',     letterHeight=1.0,
     size=(10, 10), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     depth=-2, autoLog=True,
)
key_resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "rest2" ---
rest_2 = visual.ImageStim(
    win=win,
    name='rest_2', units='cm', 
    image=root_dir +'rest2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction1_3" ---
i1_3 = visual.ImageStim(
    win=win,
    name='i1_3', units='cm', 
    image=root_dir +'instruction3P2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation1" ---
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bstart = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "GTDT2_1" ---
annular = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=2.8,    #20230816  radius=0.25
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2 = visual.Pie(
    win=win, name='annular2',start=22.5, end=45,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular3 = visual.Pie(
    win=win, name='annular3',start=45, end=67.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular4 = visual.Pie(
    win=win, name='annular4',start=67.5, end=90,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular5 = visual.Pie(
    win=win, name='annular5',start=90,end=112.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular6 = visual.Pie(
    win=win, name='annular6',start=112.5,end=135,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular7 = visual.Pie(
    win=win, name='annular7',start=135,end=157.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular8 = visual.Pie(
    win=win, name='annular8',start=157.5,end=180,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular9 = visual.Pie(
    win=win, name='annular9',start=180,end=202.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular10 = visual.Pie(
    win=win, name='annular10',start=202.5,end=225,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular11 = visual.Pie(
    win=win, name='annular9',start=225,end=247.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular12 = visual.Pie(
    win=win, name='annular12',start=247.5,end=270,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular13 = visual.Pie(
    win=win, name='annular9',start=270,end=292.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular14 = visual.Pie(
    win=win, name='annular14',start=292.5,end=315,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular15 = visual.Pie(
    win=win, name='annular15',start=315,end=337.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular16 = visual.Pie(
    win=win, name='annular16',start=337.5,end=360,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
cover1 = visual.ShapeStim(
    win=win, name='cover1',units='cm', 
    size=(5.6, 5.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
center1 = visual.ShapeStim(
    win=win, name='center1',units='cm', 
    size=(2.8, 2.8), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='grey', fillColor='grey',
    opacity=None, depth=-3.0, interpolate=False)
bg1 = visual.Rect(
    win=win, name='bg1',units='cm', 
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
key_resp_4 = keyboard.Keyboard()
stimulus1 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "rest3" ---
rest_3 = visual.ImageStim(
    win=win,
    name='rest_3', units='cm', 
    image=root_dir + 'rest3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()
bend3 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "instruction1_3" ---
i1_3 = visual.ImageStim(
    win=win,
    name='i1_3', units='cm', 
    image=root_dir + 'instruction3P2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation1" ---
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bstart = parallel.ParallelPort(address='0x0378')

# --- Initialize components for Routine "GTDT2_1" ---
annular = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=2.8,    #20230816  radius=0.25
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2 = visual.Pie(
    win=win, name='annular2',start=22.5, end=45,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular3 = visual.Pie(
    win=win, name='annular3',start=45, end=67.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular4 = visual.Pie(
    win=win, name='annular4',start=67.5, end=90,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular5 = visual.Pie(
    win=win, name='annular5',start=90,end=112.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular6 = visual.Pie(
    win=win, name='annular6',start=112.5,end=135,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular7 = visual.Pie(
    win=win, name='annular7',start=135,end=157.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular8 = visual.Pie(
    win=win, name='annular8',start=157.5,end=180,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular9 = visual.Pie(
    win=win, name='annular9',start=180,end=202.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular10 = visual.Pie(
    win=win, name='annular10',start=202.5,end=225,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular11 = visual.Pie(
    win=win, name='annular9',start=225,end=247.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular12 = visual.Pie(
    win=win, name='annular12',start=247.5,end=270,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular13 = visual.Pie(
    win=win, name='annular9',start=270,end=292.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular14 = visual.Pie(
    win=win, name='annular14',start=292.5,end=315,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular15 = visual.Pie(
    win=win, name='annular15',start=315,end=337.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular16 = visual.Pie(
    win=win, name='annular16',start=337.5,end=360,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
cover1 = visual.ShapeStim(
    win=win, name='cover1',units='cm', 
    size=(5.6, 5.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
center1 = visual.ShapeStim(
    win=win, name='center1',units='cm', 
    size=(2.8, 2.8), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='grey', fillColor='grey',
    opacity=None, depth=-3.0, interpolate=False)
bg1 = visual.Rect(
    win=win, name='bg1',units='cm', 
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
key_resp_4 = keyboard.Keyboard()
stimulus1 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "rest4" ---
rest_4 = visual.ImageStim(
    win=win,
    name='rest_4', units='cm', 
    image=root_dir + 'rest4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_11 = keyboard.Keyboard()
bend4 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "instruction2" ---
i2 = visual.ImageStim(
    win=win,
    name='i2', units='cm', 
    image=root_dir + 'instruction3P3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation1" ---
text_1 = visual.TextStim(win=win, name='text_1',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bstart = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "GTDT3_1" ---
annular2_1 = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=2.8,    #20230816  radius=0.25
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_2 = visual.Pie(
    win=win, name='annular2',start=22.5, end=45,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_3 = visual.Pie(
    win=win, name='annular3',start=45, end=67.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_4 = visual.Pie(
    win=win, name='annular4',start=67.5, end=90,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_5 = visual.Pie(
    win=win, name='annular5',start=90,end=112.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_6 = visual.Pie(
    win=win, name='annular6',start=112.5,end=135,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_7 = visual.Pie(
    win=win, name='annular7',start=135,end=157.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_8 = visual.Pie(
    win=win, name='annular8',start=157.5,end=180,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_9 = visual.Pie(
    win=win, name='annular9',start=180,end=202.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_10 = visual.Pie(
    win=win, name='annular10',start=202.5,end=225,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_11 = visual.Pie(
    win=win, name='annular9',start=225,end=247.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_12 = visual.Pie(
    win=win, name='annular12',start=247.5,end=270,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_13 = visual.Pie(
    win=win, name='annular9',start=270,end=292.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_14 = visual.Pie(
    win=win, name='annular14',start=292.5,end=315,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_15 = visual.Pie(
    win=win, name='annular15',start=315,end=337.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2_16 = visual.Pie(
    win=win, name='annular16',start=337.5,end=360,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
cover2 = visual.ShapeStim(
    win=win, name='cover',
    size=(5.6, 5.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=False)
center2 = visual.ShapeStim(
    win=win, name='center',
    size=(2.8, 2.8), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='grey', fillColor='grey',
    opacity=None, depth=-3.0, interpolate=False)
bg2 = visual.Rect(
    win=win, name='bg',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
stimulus2 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "question" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='请问在这个阶段中，你观察到圆环变暗的次数为？\n填写完成后按空格键提交',
    font='Open Sans',
    units='cm', pos=(-2, 0.15), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bend2 = parallel.ParallelPort(address='0x3EFC')
textbox = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -2.5),units='cm',     letterHeight=1.0,
     size=(10, 10), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     depth=-2, autoLog=True,
)
key_resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "rest5" ---
rest_5 = visual.ImageStim(
    win=win,
    name='rest_5', units='cm', 
    image=root_dir + 'rest5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_12 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction1_3" ---
i1_3 = visual.ImageStim(
    win=win,
    name='i1_3', units='cm', 
    image=root_dir + 'instruction3P2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation1" ---
text_1 = visual.TextStim(win=win, name='text_1',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bstart = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "GTDT2_1" ---
annular = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=2.8,    #20230816  radius=0.25
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2 = visual.Pie(
    win=win, name='annular2',start=22.5, end=45,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular3 = visual.Pie(
    win=win, name='annular3',start=45, end=67.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular4 = visual.Pie(
    win=win, name='annular4',start=67.5, end=90,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular5 = visual.Pie(
    win=win, name='annular5',start=90,end=112.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular6 = visual.Pie(
    win=win, name='annular6',start=112.5,end=135,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular7 = visual.Pie(
    win=win, name='annular7',start=135,end=157.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular8 = visual.Pie(
    win=win, name='annular8',start=157.5,end=180,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular9 = visual.Pie(
    win=win, name='annular9',start=180,end=202.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular10 = visual.Pie(
    win=win, name='annular10',start=202.5,end=225,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular11 = visual.Pie(
    win=win, name='annular9',start=225,end=247.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular12 = visual.Pie(
    win=win, name='annular12',start=247.5,end=270,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular13 = visual.Pie(
    win=win, name='annular9',start=270,end=292.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular14 = visual.Pie(
    win=win, name='annular14',start=292.5,end=315,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular15 = visual.Pie(
    win=win, name='annular15',start=315,end=337.5,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular16 = visual.Pie(
    win=win, name='annular16',start=337.5,end=360,radius=2.8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
cover1 = visual.ShapeStim(
    win=win, name='cover1',units='cm', 
    size=(5.6, 5.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
center1 = visual.ShapeStim(
    win=win, name='center1',units='cm', 
    size=(2.8, 2.8), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='grey', fillColor='grey',
    opacity=None, depth=-3.0, interpolate=False)
bg1 = visual.Rect(
    win=win, name='bg1',units='cm', 
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
key_resp_4 = keyboard.Keyboard()
stimulus1 = parallel.ParallelPort(address='0x3EFC')

# --- Initialize components for Routine "rest6" ---
instruction5 = visual.ImageStim(
    win=win,
    name='instruction5', units='cm', 
    image=root_dir +'instruction5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_13 = keyboard.Keyboard()
bend6 = parallel.ParallelPort(address='0x3EFC')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruction1_1" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instruction1_1Components = [i1_1, key_resp]
for thisComponent in instruction1_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction1_1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i1_1* updates
    
    # if i1_1 is starting this frame...
    if i1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i1_1.frameNStart = frameN  # exact frame index
        i1_1.tStart = t  # local t and not account for scr refresh
        i1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i1_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i1_1.started')
        # update status
        i1_1.status = STARTED
        i1_1.setAutoDraw(True)
    
    # if i1_1 is active this frame...
    if i1_1.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction1_1" ---
for thisComponent in instruction1_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instruction1_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction1_2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instruction1_2Components = [i1_2, key_resp_2]
for thisComponent in instruction1_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction1_2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i1_2* updates
    
    # if i1_2 is starting this frame...
    if i1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i1_2.frameNStart = frameN  # exact frame index
        i1_2.tStart = t  # local t and not account for scr refresh
        i1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i1_2.started')
        # update status
        i1_2.status = STARTED
        i1_2.setAutoDraw(True)
    
    # if i1_2 is active this frame...
    if i1_2.status == STARTED:
        # update params
        pass
    
    # *key_resp_2* updates
    waitOnFlip = False
    
    # if key_resp_2 is starting this frame...
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        # update status
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction1_2" ---
for thisComponent in instruction1_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instruction1_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction1_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction1_3Components = [i1_3, key_resp_3]
for thisComponent in instruction1_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction1_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i1_3* updates
    
    # if i1_3 is starting this frame...
    if i1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i1_3.frameNStart = frameN  # exact frame index
        i1_3.tStart = t  # local t and not account for scr refresh
        i1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i1_3.started')
        # update status
        i1_3.status = STARTED
        i1_3.setAutoDraw(True)
    
    # if i1_3 is active this frame...
    if i1_3.status == STARTED:
        # update params
        pass
    
    # *key_resp_3* updates
    waitOnFlip = False
    
    # if key_resp_3 is starting this frame...
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        # update status
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction1_3" ---
for thisComponent in instruction1_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instruction1_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "fixation1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [text, bstart]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "fixation1" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    # *bstart* updates
    
    # if bstart is starting this frame...
    if bstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bstart.frameNStart = frameN  # exact frame index
        bstart.tStart = t  # local t and not account for scr refresh
        bstart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bstart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bstart.started')
        # update status
        bstart.status = STARTED
        bstart.status = STARTED
        win.callOnFlip(bstart.setData, int(6))
    
    # if bstart is stopping this frame...
    if bstart.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bstart.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bstart.tStop = t  # not accounting for scr refresh
            bstart.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bstart.stopped')
            # update status
            bstart.status = FINISHED
            win.callOnFlip(bstart.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation1" ---
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bstart.status == STARTED:
    win.callOnFlip(bstart.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(root_dir + 'c2.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GTDT2_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    GTDT2_1Components = [annular, annular2, annular3,annular4,
        annular5,annular6,annular7,annular8,annular9,annular10,annular11,annular12,
        annular13,annular14,annular15,annular16, cover1, center1, bg1, key_resp_4, stimulus1]
    for thisComponent in GTDT2_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GTDT2_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *annular1* updates
        # *annular* updates
            
        # if annular is starting this frame...
        if annular.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            #stimulus_marker(1)
            # keep track of start time/frame for later
            annular.frameNStart = frameN  # exact frame index
            annular.tStart = t  # local t and not account for scr refresh
            annular.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular.started')
            # update status
            annular.status = STARTED
            annular.setAutoDraw(True)
        
        # if annular is active this frame...
        if annular.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular.setOpacity(None, log=False)
            annular.setContrast(cont, log=False)
            annular.setLineWidth(1.0, log=False)
        
        # if annular is stopping this frame...
        if annular.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular.tStop = t  # not accounting for scr refresh
                annular.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular.stopped')
                # update status
                annular.status = FINISHED
                annular.setAutoDraw(False)

        # *annular2* updates
        
        # if annular2 is starting this frame...
        if annular2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2.frameNStart = frameN  # exact frame index
            annular2.tStart = t  # local t and not account for scr refresh
            annular2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2.started')
            # update status
            annular2.status = STARTED
            annular2.setAutoDraw(True)
        
        # if annular2 is active this frame...
        if annular2.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2.setOpacity(None, log=False)
            annular2.setContrast(cont, log=False)
            annular2.setLineWidth(1.0, log=False)
        
        # if annular2 is stopping this frame...
        if annular2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2.tStop = t  # not accounting for scr refresh
                annular2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2.stopped')
                # update status
                annular2.status = FINISHED
                annular2.setAutoDraw(False)

        # *annular3* updates
        
        # if annular3 is starting this frame...
        if annular3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular3.frameNStart = frameN  # exact frame index
            annular3.tStart = t  # local t and not account for scr refresh
            annular3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular3.started')
            # update status
            annular3.status = STARTED
            annular3.setAutoDraw(True)
        
        # if annular3 is active this frame...
        if annular3.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular3.setOpacity(None, log=False)
            annular3.setContrast(cont, log=False)
            annular3.setLineWidth(1.0, log=False)
        
        # if annular3 is stopping this frame...
        if annular3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular3.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular3.tStop = t  # not accounting for scr refresh
                annular3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular3.stopped')
                # update status
                annular3.status = FINISHED
                annular3.setAutoDraw(False)


        # *annular4* updates
        
        # if annular4 is starting this frame...
        if annular4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular4.frameNStart = frameN  # exact frame index
            annular4.tStart = t  # local t and not account for scr refresh
            annular4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular4.started')
            # update status
            annular4.status = STARTED
            annular4.setAutoDraw(True)
        
        # if annular4 is active this frame...
        if annular4.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular4.setOpacity(None, log=False)
            annular4.setContrast(cont, log=False)
            annular4.setLineWidth(1.0, log=False)
        
        # if annular4 is stopping this frame...
        if annular4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular4.tStop = t  # not accounting for scr refresh
                annular4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular4.stopped')
                # update status
                annular4.status = FINISHED
                annular4.setAutoDraw(False)

        # *annular5* updates
        
        # if annular5 is starting this frame...
        if annular5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular5.frameNStart = frameN  # exact frame index
            annular5.tStart = t  # local t and not account for scr refresh
            annular5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular5.started')
            # update status
            annular5.status = STARTED
            annular5.setAutoDraw(True)
        
        # if annular5 is active this frame...
        if annular5.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular5.setOpacity(None, log=False)
            annular5.setContrast(cont, log=False)
            annular5.setLineWidth(1.0, log=False)
        
        # if annular5 is stopping this frame...
        if annular5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular5.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular5.tStop = t  # not accounting for scr refresh
                annular5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular5.stopped')
                # update status
                annular5.status = FINISHED
                annular5.setAutoDraw(False)

        # *annular6* updates
        
        # if annular6 is starting this frame...
        if annular6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular6.frameNStart = frameN  # exact frame index
            annular6.tStart = t  # local t and not account for scr refresh
            annular6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular6.started')
            # update status
            annular6.status = STARTED
            annular6.setAutoDraw(True)
        
        # if annular6 is active this frame...
        if annular6.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular6.setOpacity(None, log=False)
            annular6.setContrast(cont, log=False)
            annular6.setLineWidth(1.0, log=False)
        
        # if annular6 is stopping this frame...
        if annular6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular6.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular6.tStop = t  # not accounting for scr refresh
                annular6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular6.stopped')
                # update status
                annular6.status = FINISHED
                annular6.setAutoDraw(False)

        # *annular7* updates
        
        # if annular7 is starting this frame...
        if annular7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular7.frameNStart = frameN  # exact frame index
            annular7.tStart = t  # local t and not account for scr refresh
            annular7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular7.started')
            # update status
            annular7.status = STARTED
            annular7.setAutoDraw(True)
        
        # if annular7 is active this frame...
        if annular7.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular7.setOpacity(None, log=False)
            annular7.setContrast(cont, log=False)
            annular7.setLineWidth(1.0, log=False)
        
        # if annular7 is stopping this frame...
        if annular7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular7.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular7.tStop = t  # not accounting for scr refresh
                annular7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular7.stopped')
                # update status
                annular7.status = FINISHED
                annular7.setAutoDraw(False)

        # *annular8* updates
        
        # if annular8 is starting this frame...
        if annular8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular8.frameNStart = frameN  # exact frame index
            annular8.tStart = t  # local t and not account for scr refresh
            annular8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular8.started')
            # update status
            annular8.status = STARTED
            annular8.setAutoDraw(True)
        
        # if annular8 is active this frame...
        if annular8.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular8.setOpacity(None, log=False)
            annular8.setContrast(cont, log=False)
            annular8.setLineWidth(1.0, log=False)
        
        # if annular8 is stopping this frame...
        if annular8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular8.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular8.tStop = t  # not accounting for scr refresh
                annular8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular8.stopped')
                # update status
                annular8.status = FINISHED
                annular8.setAutoDraw(False)

        # *annular9* updates
        
        # if annular9 is starting this frame...
        if annular9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular9.frameNStart = frameN  # exact frame index
            annular9.tStart = t  # local t and not account for scr refresh
            annular9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular9.started')
            # update status
            annular9.status = STARTED
            annular9.setAutoDraw(True)
        
        # if annular9 is active this frame...
        if annular9.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular9.setOpacity(None, log=False)
            annular9.setContrast(cont, log=False)
            annular9.setLineWidth(1.0, log=False)
        
        # if annular9 is stopping this frame...
        if annular9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular9.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular9.tStop = t  # not accounting for scr refresh
                annular9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular9.stopped')
                # update status
                annular9.status = FINISHED
                annular9.setAutoDraw(False)

        # *annular10* updates
        
        # if annular10 is starting this frame...
        if annular10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular10.frameNStart = frameN  # exact frame index
            annular10.tStart = t  # local t and not account for scr refresh
            annular10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular10.started')
            # update status
            annular10.status = STARTED
            annular10.setAutoDraw(True)
        
        # if annular10 is active this frame...
        if annular10.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular10.setOpacity(None, log=False)
            annular10.setContrast(cont, log=False)
            annular10.setLineWidth(1.0, log=False)
        
        # if annular10 is stopping this frame...
        if annular10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular10.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular10.tStop = t  # not accounting for scr refresh
                annular10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular10.stopped')
                # update status
                annular10.status = FINISHED
                annular10.setAutoDraw(False)

        # *annular11* updates
        
        # if annular11 is starting this frame...
        if annular11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular11.frameNStart = frameN  # exact frame index
            annular11.tStart = t  # local t and not account for scr refresh
            annular11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular11.started')
            # update status
            annular11.status = STARTED
            annular11.setAutoDraw(True)
        
        # if annular11 is active this frame...
        if annular11.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular11.setOpacity(None, log=False)
            annular11.setContrast(cont, log=False)
            annular11.setLineWidth(1.0, log=False)
        
        # if annular11 is stopping this frame...
        if annular11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular11.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular11.tStop = t  # not accounting for scr refresh
                annular11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular11.stopped')
                # update status
                annular11.status = FINISHED
                annular11.setAutoDraw(False)

        # *annular12* updates
        
        # if annular12 is starting this frame...
        if annular12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular12.frameNStart = frameN  # exact frame index
            annular12.tStart = t  # local t and not account for scr refresh
            annular12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular12.started')
            # update status
            annular12.status = STARTED
            annular12.setAutoDraw(True)
        
        # if annular12 is active this frame...
        if annular12.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular12.setOpacity(None, log=False)
            annular12.setContrast(cont, log=False)
            annular12.setLineWidth(1.0, log=False)
        
        # if annular12 is stopping this frame...
        if annular12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular12.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular12.tStop = t  # not accounting for scr refresh
                annular12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular12.stopped')
                # update status
                annular12.status = FINISHED
                annular12.setAutoDraw(False)

        # *annular13* updates
        
        # if annular13 is starting this frame...
        if annular13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular13.frameNStart = frameN  # exact frame index
            annular13.tStart = t  # local t and not account for scr refresh
            annular13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular13.started')
            # update status
            annular13.status = STARTED
            annular13.setAutoDraw(True)
        
        # if annular13 is active this frame...
        if annular13.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular13.setOpacity(None, log=False)
            annular13.setContrast(cont, log=False)
            annular13.setLineWidth(1.0, log=False)
        
        # if annular13 is stopping this frame...
        if annular13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular13.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular13.tStop = t  # not accounting for scr refresh
                annular13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular13.stopped')
                # update status
                annular13.status = FINISHED
                annular13.setAutoDraw(False)

        # *annular14* updates
        
        # if annular14 is starting this frame...
        if annular14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular14.frameNStart = frameN  # exact frame index
            annular14.tStart = t  # local t and not account for scr refresh
            annular14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular14.started')
            # update status
            annular14.status = STARTED
            annular14.setAutoDraw(True)
        
        # if annular14 is active this frame...
        if annular14.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular14.setOpacity(None, log=False)
            annular14.setContrast(cont, log=False)
            annular14.setLineWidth(1.0, log=False)
        
        # if annular14 is stopping this frame...
        if annular14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular14.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular14.tStop = t  # not accounting for scr refresh
                annular14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular14.stopped')
                # update status
                annular14.status = FINISHED
                annular14.setAutoDraw(False)

        # *annular15* updates
        
        # if annular15 is starting this frame...
        if annular15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular15.frameNStart = frameN  # exact frame index
            annular15.tStart = t  # local t and not account for scr refresh
            annular15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular15.started')
            # update status
            annular15.status = STARTED
            annular15.setAutoDraw(True)
        
        # if annular15 is active this frame...
        if annular15.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular15.setOpacity(None, log=False)
            annular15.setContrast(cont, log=False)
            annular15.setLineWidth(1.0, log=False)
        
        # if annular15 is stopping this frame...
        if annular15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular15.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular15.tStop = t  # not accounting for scr refresh
                annular15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular15.stopped')
                # update status
                annular15.status = FINISHED
                annular15.setAutoDraw(False)

        # *annular16* updates
        
        # if annular16 is starting this frame...
        if annular16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular16.frameNStart = frameN  # exact frame index
            annular16.tStart = t  # local t and not account for scr refresh
            annular16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular16.started')
            # update status
            annular16.status = STARTED
            annular16.setAutoDraw(True)
        
        # if annular16 is active this frame...
        if annular16.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular16.setOpacity(None, log=False)
            annular16.setContrast(cont, log=False)
            annular16.setLineWidth(1.0, log=False)
        
        # if annular16 is stopping this frame...
        if annular16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular16.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular16.tStop = t  # not accounting for scr refresh
                annular16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular16.stopped')
                # update status
                annular16.status = FINISHED
                annular16.setAutoDraw(False)
        
        
        # *cover1* updates
        
        # if cover1 is starting this frame...
        if cover1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cover1.frameNStart = frameN  # exact frame index
            cover1.tStart = t  # local t and not account for scr refresh
            cover1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cover1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cover1.started')
            # update status
            cover1.status = STARTED
            cover1.setAutoDraw(True)
        
        # if cover1 is active this frame...
        if cover1.status == STARTED:
            # update params
            opci=0.5+0.5*np.sin(2*np.pi*t*21.25)
            # update params
            cover1.setOpacity(opci, log=False)
            cover1.setContrast(0.0, log=False)
            cover1.setLineWidth(1.0, log=False)
        
        # if cover1 is stopping this frame...
        if cover1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cover1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                cover1.tStop = t  # not accounting for scr refresh
                cover1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover1.stopped')
                # update status
                cover1.status = FINISHED
                cover1.setAutoDraw(False)
        
        # *center1* updates
        
        # if center1 is starting this frame...
        if center1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center1.frameNStart = frameN  # exact frame index
            center1.tStart = t  # local t and not account for scr refresh
            center1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'center1.started')
            # update status
            center1.status = STARTED
            center1.setAutoDraw(True)
        
        # if center1 is active this frame...
        if center1.status == STARTED:
            # update params
            pass
        
        # if center1 is stopping this frame...
        if center1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > center1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                center1.tStop = t  # not accounting for scr refresh
                center1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'center1.stopped')
                # update status
                center1.status = FINISHED
                center1.setAutoDraw(False)
        
        # *bg1* updates
        
        # if bg1 is starting this frame...
        if bg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bg1.frameNStart = frameN  # exact frame index
            bg1.tStart = t  # local t and not account for scr refresh
            bg1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bg1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bg1.started')
            # update status
            bg1.status = STARTED
            bg1.setAutoDraw(True)
        
        # if bg1 is active this frame...
        if bg1.status == STARTED:
            # update params
            #pass
            # update params
            bg1.setOpacity(None, log=False)
            bg1.setContrast(1.0, log=False)
            bg1.setLineWidth(1.0, log=False)
        
        # if bg1 is stopping this frame...
        if bg1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bg1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                bg1.tStop = t  # not accounting for scr refresh
                bg1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg1.stopped')
                # update status
                bg1.status = FINISHED
                bg1.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_4 is stopping this frame...
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                # update status
                key_resp_4.status = FINISHED
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                a= len(key_resp_4.keys)
                key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                b= len(key_resp_4.keys)
                if b-a==1:
                    responses_marker(2)
                key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                # a response ends the routine
                continueRoutine = True
        # *stimulus1* updates
        
        # if stimulus1 is starting this frame...
        if stimulus1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus1.frameNStart = frameN  # exact frame index
            stimulus1.tStart = t  # local t and not account for scr refresh
            stimulus1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimulus1.started')
            # update status
            stimulus1.status = STARTED
            stimulus1.status = STARTED
            win.callOnFlip(stimulus1.setData, int(1))
        
        # if stimulus1 is stopping this frame...
        if stimulus1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus1.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                stimulus1.tStop = t  # not accounting for scr refresh
                stimulus1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus1.stopped')
                # update status
                stimulus1.status = FINISHED
                win.callOnFlip(stimulus1.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GTDT2_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GTDT2_1" ---
    for thisComponent in GTDT2_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    if stimulus1.status == STARTED:
        win.callOnFlip(stimulus1.setData, int(0))
    # the Routine "GTDT2_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "rest1" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
rest1Components = [rest_1, key_resp_5, bend1]
for thisComponent in rest1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "rest1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_1* updates
    
    # if rest_1 is starting this frame...
    if rest_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_1.frameNStart = frameN  # exact frame index
        rest_1.tStart = t  # local t and not account for scr refresh
        rest_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_1.started')
        # update status
        rest_1.status = STARTED
        rest_1.setAutoDraw(True)
    
    # if rest_1 is active this frame...
    if rest_1.status == STARTED:
        # update params
        pass
    
    # *key_resp_5* updates
    waitOnFlip = False
    
    # if key_resp_5 is starting this frame...
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        # update status
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *bend1* updates
    
    # if bend1 is starting this frame...
    if bend1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bend1.frameNStart = frameN  # exact frame index
        bend1.tStart = t  # local t and not account for scr refresh
        bend1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bend1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bend1.started')
        # update status
        bend1.status = STARTED
        bend1.status = STARTED
        win.callOnFlip(bend1.setData, int(6))
    
    # if bend1 is stopping this frame...
    if bend1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bend1.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bend1.tStop = t  # not accounting for scr refresh
            bend1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bend1.stopped')
            # update status
            bend1.status = FINISHED
            win.callOnFlip(bend1.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rest1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rest1" ---
for thisComponent in rest1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
if bend1.status == STARTED:
    win.callOnFlip(bend1.setData, int(0))
# the Routine "rest1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
instruction2Components = [i2, key_resp_6]
for thisComponent in instruction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i2* updates
    
    # if i2 is starting this frame...
    if i2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i2.frameNStart = frameN  # exact frame index
        i2.tStart = t  # local t and not account for scr refresh
        i2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i2.started')
        # update status
        i2.status = STARTED
        i2.setAutoDraw(True)
    
    # if i2 is active this frame...
    if i2.status == STARTED:
        # update params
        pass
    
    # *key_resp_6* updates
    waitOnFlip = False
    
    # if key_resp_6 is starting this frame...
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        # update status
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction2" ---
for thisComponent in instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "fixation2" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
fixation2Components = [text_2, bstart2]
for thisComponent in fixation2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "fixation2" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    
    # if text_2 is starting this frame...
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        # update status
        text_2.status = STARTED
        text_2.setAutoDraw(True)
    
    # if text_2 is active this frame...
    if text_2.status == STARTED:
        # update params
        pass
    
    # if text_2 is stopping this frame...
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            # update status
            text_2.status = FINISHED
            text_2.setAutoDraw(False)
    # *bstart2* updates
    
    # if bstart2 is starting this frame...
    if bstart2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bstart2.frameNStart = frameN  # exact frame index
        bstart2.tStart = t  # local t and not account for scr refresh
        bstart2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bstart2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bstart2.started')
        # update status
        bstart2.status = STARTED
        bstart2.status = STARTED
        win.callOnFlip(bstart2.setData, int(6))
    
    # if bstart2 is stopping this frame...
    if bstart2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bstart2.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bstart2.tStop = t  # not accounting for scr refresh
            bstart2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bstart2.stopped')
            # update status
            bstart2.status = FINISHED
            win.callOnFlip(bstart2.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation2" ---
for thisComponent in fixation2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bstart2.status == STARTED:
    win.callOnFlip(bstart2.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(root_dir + 'c325.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GTDT3_1" ---
    continueRoutine = True
    # keep track of which components have finished
    GTDT3_1Components = [annular2_1, annular2_2, annular2_3,annular2_4,
        annular2_5,annular2_6,annular2_7,annular2_8,annular2_9,annular2_10,annular2_11,annular2_12,
        annular2_13,annular2_14,annular2_15,annular2_16, cover2, center2, bg2, stimulus2]
    for thisComponent in GTDT3_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GTDT3_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *annular* updates
            
        # if annular is starting this frame...
        if annular2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            #stimulus_marker(1)
            # keep track of start time/frame for later
            annular2_1.frameNStart = frameN  # exact frame index
            annular2_1.tStart = t  # local t and not account for scr refresh
            annular2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_1.started')
            # update status
            annular2_1.status = STARTED
            annular2_1.setAutoDraw(True)
        
        # if annular is active this frame...
        if annular2_1.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_1.setOpacity(None, log=False)
            annular2_1.setContrast(cont, log=False)
            annular2_1.setLineWidth(1.0, log=False)
        
        # if annular is stopping this frame...
        if annular2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_1.tStop = t  # not accounting for scr refresh
                annular2_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_1.stopped')
                # update status
                annular2_1.status = FINISHED
                annular2_1.setAutoDraw(False)

        # *annular2_2* updates
        
        # if annular2_2 is starting this frame...
        if annular2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_2.frameNStart = frameN  # exact frame index
            annular2_2.tStart = t  # local t and not account for scr refresh
            annular2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_2.started')
            # update status
            annular2_2.status = STARTED
            annular2_2.setAutoDraw(True)
        
        # if annular2_2 is active this frame...
        if annular2_2.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_2.setOpacity(None, log=False)
            annular2_2.setContrast(cont, log=False)
            annular2_2.setLineWidth(1.0, log=False)
        
        # if annular2_2 is stopping this frame...
        if annular2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_2.tStop = t  # not accounting for scr refresh
                annular2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_2.stopped')
                # update status
                annular2_2.status = FINISHED
                annular2_2.setAutoDraw(False)

        # *annular2_3* updates
        
        # if annular2_3 is starting this frame...
        if annular2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_3.frameNStart = frameN  # exact frame index
            annular2_3.tStart = t  # local t and not account for scr refresh
            annular2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_3.started')
            # update status
            annular2_3.status = STARTED
            annular2_3.setAutoDraw(True)
        
        # if annular2_3 is active this frame...
        if annular2_3.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_3.setOpacity(None, log=False)
            annular2_3.setContrast(cont, log=False)
            annular2_3.setLineWidth(1.0, log=False)
        
        # if annular2_3 is stopping this frame...
        if annular2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_3.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_3.tStop = t  # not accounting for scr refresh
                annular2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_3.stopped')
                # update status
                annular2_3.status = FINISHED
                annular2_3.setAutoDraw(False)


        # *annular2_4* updates
        
        # if annular2_4 is starting this frame...
        if annular2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_4.frameNStart = frameN  # exact frame index
            annular2_4.tStart = t  # local t and not account for scr refresh
            annular2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_4.started')
            # update status
            annular2_4.status = STARTED
            annular2_4.setAutoDraw(True)
        
        # if annular4 is active this frame...
        if annular2_4.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_4.setOpacity(None, log=False)
            annular2_4.setContrast(cont, log=False)
            annular2_4.setLineWidth(1.0, log=False)
        
        # if annular2_4 is stopping this frame...
        if annular2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_4.tStop = t  # not accounting for scr refresh
                annular2_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_4.stopped')
                # update status
                annular2_4.status = FINISHED
                annular2_4.setAutoDraw(False)

        # *annular2_5* updates
        
        # if annular2_5 is starting this frame...
        if annular2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_5.frameNStart = frameN  # exact frame index
            annular2_5.tStart = t  # local t and not account for scr refresh
            annular2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_5.started')
            # update status
            annular2_5.status = STARTED
            annular2_5.setAutoDraw(True)
        
        # if annular5 is active this frame...
        if annular2_5.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_5.setOpacity(None, log=False)
            annular2_5.setContrast(cont, log=False)
            annular2_5.setLineWidth(1.0, log=False)
        
        # if annular5 is stopping this frame...
        if annular2_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_5.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_5.tStop = t  # not accounting for scr refresh
                annular2_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_5.stopped')
                # update status
                annular2_5.status = FINISHED
                annular2_5.setAutoDraw(False)

        # *annular2_6* updates
        
        # if annular2_6 is starting this frame...
        if annular2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_6.frameNStart = frameN  # exact frame index
            annular2_6.tStart = t  # local t and not account for scr refresh
            annular2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_6.started')
            # update status
            annular2_6.status = STARTED
            annular2_6.setAutoDraw(True)
        
        # if annular2_6 is active this frame...
        if annular2_6.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_6.setOpacity(None, log=False)
            annular2_6.setContrast(cont, log=False)
            annular2_6.setLineWidth(1.0, log=False)
        
        # if annular2_6 is stopping this frame...
        if annular2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_6.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_6.tStop = t  # not accounting for scr refresh
                annular2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_6.stopped')
                # update status
                annular2_6.status = FINISHED
                annular2_6.setAutoDraw(False)

        # *annular2_7* updates
        
        # if annular2_7 is starting this frame...
        if annular2_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_7.frameNStart = frameN  # exact frame index
            annular2_7.tStart = t  # local t and not account for scr refresh
            annular2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_7.started')
            # update status
            annular2_7.status = STARTED
            annular2_7.setAutoDraw(True)
        
        # if annular2_7 is active this frame...
        if annular2_7.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_7.setOpacity(None, log=False)
            annular2_7.setContrast(cont, log=False)
            annular2_7.setLineWidth(1.0, log=False)
        
        # if annular2_7 is stopping this frame...
        if annular2_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_7.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_7.tStop = t  # not accounting for scr refresh
                annular2_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_7.stopped')
                # update status
                annular2_7.status = FINISHED
                annular2_7.setAutoDraw(False)

        # *annular2_8* updates
        
        # if annular2_8 is starting this frame...
        if annular2_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_8.frameNStart = frameN  # exact frame index
            annular2_8.tStart = t  # local t and not account for scr refresh
            annular2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_8.started')
            # update status
            annular2_8.status = STARTED
            annular2_8.setAutoDraw(True)
        
        # if annular8 is active this frame...
        if annular2_8.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_8.setOpacity(None, log=False)
            annular2_8.setContrast(cont, log=False)
            annular2_8.setLineWidth(1.0, log=False)
        
        # if annular2_8 is stopping this frame...
        if annular2_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_8.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_8.tStop = t  # not accounting for scr refresh
                annular2_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_8.stopped')
                # update status
                annular2_8.status = FINISHED
                annular2_8.setAutoDraw(False)

        # *annular2_9* updates
        
        # if annular2_9 is starting this frame...
        if annular2_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_9.frameNStart = frameN  # exact frame index
            annular2_9.tStart = t  # local t and not account for scr refresh
            annular2_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_9.started')
            # update status
            annular2_9.status = STARTED
            annular2_9.setAutoDraw(True)
        
        # if annular2_9 is active this frame...
        if annular2_9.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_9.setOpacity(None, log=False)
            annular2_9.setContrast(cont, log=False)
            annular2_9.setLineWidth(1.0, log=False)
        
        # if annular2_9 is stopping this frame...
        if annular2_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_9.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_9.tStop = t  # not accounting for scr refresh
                annular2_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_9.stopped')
                # update status
                annular2_9.status = FINISHED
                annular2_9.setAutoDraw(False)

        # *annular2_10* updates
        
        # if annular2_10 is starting this frame...
        if annular2_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_10.frameNStart = frameN  # exact frame index
            annular2_10.tStart = t  # local t and not account for scr refresh
            annular2_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_10.started')
            # update status
            annular2_10.status = STARTED
            annular2_10.setAutoDraw(True)
        
        # if annular2_10 is active this frame...
        if annular2_10.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_10.setOpacity(None, log=False)
            annular2_10.setContrast(cont, log=False)
            annular2_10.setLineWidth(1.0, log=False)
        
        # if annular2_10 is stopping this frame...
        if annular2_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_10.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_10.tStop = t  # not accounting for scr refresh
                annular2_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_10.stopped')
                # update status
                annular2_10.status = FINISHED
                annular2_10.setAutoDraw(False)

        # *annular2_11* updates
        
        # if annular2_11 is starting this frame...
        if annular2_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_11.frameNStart = frameN  # exact frame index
            annular2_11.tStart = t  # local t and not account for scr refresh
            annular2_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_11.started')
            # update status
            annular2_11.status = STARTED
            annular2_11.setAutoDraw(True)
        
        # if annular2_11 is active this frame...
        if annular2_11.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_11.setOpacity(None, log=False)
            annular2_11.setContrast(cont, log=False)
            annular2_11.setLineWidth(1.0, log=False)
        
        # if annular2_11 is stopping this frame...
        if annular2_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_11.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_11.tStop = t  # not accounting for scr refresh
                annular2_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_11.stopped')
                # update status
                annular2_11.status = FINISHED
                annular2_11.setAutoDraw(False)

        # *annular2_12* updates
        
        # if annular2_12 is starting this frame...
        if annular2_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_12.frameNStart = frameN  # exact frame index
            annular2_12.tStart = t  # local t and not account for scr refresh
            annular2_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_12.started')
            # update status
            annular2_12.status = STARTED
            annular2_12.setAutoDraw(True)
        
        # if annular2_12 is active this frame...
        if annular2_12.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_12.setOpacity(None, log=False)
            annular2_12.setContrast(cont, log=False)
            annular2_12.setLineWidth(1.0, log=False)
        
        # if annular2_12 is stopping this frame...
        if annular2_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_12.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_12.tStop = t  # not accounting for scr refresh
                annular2_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_12.stopped')
                # update status
                annular2_12.status = FINISHED
                annular2_12.setAutoDraw(False)

        # *annular2_13* updates
        
        # if annular2_13 is starting this frame...
        if annular2_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_13.frameNStart = frameN  # exact frame index
            annular2_13.tStart = t  # local t and not account for scr refresh
            annular2_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_13.started')
            # update status
            annular2_13.status = STARTED
            annular2_13.setAutoDraw(True)
        
        # if annular2_13 is active this frame...
        if annular2_13.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_13.setOpacity(None, log=False)
            annular2_13.setContrast(cont, log=False)
            annular2_13.setLineWidth(1.0, log=False)
        
        # if annular2_13 is stopping this frame...
        if annular2_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_13.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_13.tStop = t  # not accounting for scr refresh
                annular2_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_13.stopped')
                # update status
                annular2_13.status = FINISHED
                annular2_13.setAutoDraw(False)

        # *annular2_14* updates
        
        # if annular2_14 is starting this frame...
        if annular2_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_14.frameNStart = frameN  # exact frame index
            annular2_14.tStart = t  # local t and not account for scr refresh
            annular2_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_14.started')
            # update status
            annular2_14.status = STARTED
            annular2_14.setAutoDraw(True)
        
        # if annular2_14 is active this frame...
        if annular2_14.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_14.setOpacity(None, log=False)
            annular2_14.setContrast(cont, log=False)
            annular2_14.setLineWidth(1.0, log=False)
        
        # if annular2_14 is stopping this frame...
        if annular2_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_14.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_14.tStop = t  # not accounting for scr refresh
                annular2_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_14.stopped')
                # update status
                annular2_14.status = FINISHED
                annular2_14.setAutoDraw(False)

        # *annular2_15* updates
        
        # if annular2_15 is starting this frame...
        if annular2_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_15.frameNStart = frameN  # exact frame index
            annular2_15.tStart = t  # local t and not account for scr refresh
            annular2_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_15.started')
            # update status
            annular2_15.status = STARTED
            annular2_15.setAutoDraw(True)
        
        # if annular2_15 is active this frame...
        if annular2_15.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_15.setOpacity(None, log=False)
            annular2_15.setContrast(cont, log=False)
            annular2_15.setLineWidth(1.0, log=False)
        
        # if annular2_15 is stopping this frame...
        if annular2_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_15.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_15.tStop = t  # not accounting for scr refresh
                annular2_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_15.stopped')
                # update status
                annular2_15.status = FINISHED
                annular2_15.setAutoDraw(False)

        # *annular2_16* updates
        
        # if annular2_16 is starting this frame...
        if annular2_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_16.frameNStart = frameN  # exact frame index
            annular2_16.tStart = t  # local t and not account for scr refresh
            annular2_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_16.started')
            # update status
            annular2_16.status = STARTED
            annular2_16.setAutoDraw(True)
        
        # if annular2_16 is active this frame...
        if annular2_16.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_16.setOpacity(None, log=False)
            annular2_16.setContrast(cont, log=False)
            annular2_16.setLineWidth(1.0, log=False)
        
        # if annular2_16 is stopping this frame...
        if annular2_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_16.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_16.tStop = t  # not accounting for scr refresh
                annular2_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_16.stopped')
                # update status
                annular2_16.status = FINISHED
                annular2_16.setAutoDraw(False)
        
        # *cover2* updates
        
        # if cover2 is starting this frame...
        if cover2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cover2.frameNStart = frameN  # exact frame index
            cover2.tStart = t  # local t and not account for scr refresh
            cover2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cover2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cover2.started')
            # update status
            cover2.status = STARTED
            cover2.setAutoDraw(True)
        
        # if cover2 is active this frame...
        if cover2.status == STARTED:
            opci=0.5+0.5*np.sin(2*np.pi*t*21.25)
            # update params
            cover2.setOpacity(opci, log=False)
            cover2.setContrast(0.0, log=False)
            cover2.setLineWidth(1.0, log=False)
        
        # if cover2 is stopping this frame...
        if cover2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cover2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                cover2.tStop = t  # not accounting for scr refresh
                cover2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover2.stopped')
                # update status
                cover2.status = FINISHED
                cover2.setAutoDraw(False)
        
        # *center2* updates
        
        # if center2 is starting this frame...
        if center2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center2.frameNStart = frameN  # exact frame index
            center2.tStart = t  # local t and not account for scr refresh
            center2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'center2.started')
            # update status
            center2.status = STARTED
            center2.setAutoDraw(True)
        
        # if center2 is active this frame...
        if center2.status == STARTED:
            # update params
            pass
        
        # if center2 is stopping this frame...
        if center2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > center2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                center2.tStop = t  # not accounting for scr refresh
                center2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'center2.stopped')
                # update status
                center2.status = FINISHED
                center2.setAutoDraw(False)
        
        # *bg2* updates
        
        # if bg2 is starting this frame...
        if bg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bg2.frameNStart = frameN  # exact frame index
            bg2.tStart = t  # local t and not account for scr refresh
            bg2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bg2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bg2.started')
            # update status
            bg2.status = STARTED
            bg2.setAutoDraw(True)
        
        # if bg2 is active this frame...
        if bg2.status == STARTED:
             # update params
            bg2.setOpacity(None, log=False)
            bg2.setContrast(1.0, log=False)
            bg2.setLineWidth(1.0, log=False)
        
        # if bg2 is stopping this frame...
        if bg2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bg2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                bg2.tStop = t  # not accounting for scr refresh
                bg2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg2.stopped')
                # update status
                bg2.status = FINISHED
                bg2.setAutoDraw(False)
        
        # *stimulus2* updates
        
        # if stimulus2 is starting this frame...
        if stimulus2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus2.frameNStart = frameN  # exact frame index
            stimulus2.tStart = t  # local t and not account for scr refresh
            stimulus2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimulus2.started')
            # update status
            stimulus2.status = STARTED
            stimulus2.status = STARTED
            win.callOnFlip(stimulus2.setData, int(1))
        
        # if stimulus2 is stopping this frame...
        if stimulus2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                stimulus2.tStop = t  # not accounting for scr refresh
                stimulus2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus2.stopped')
                # update status
                stimulus2.status = FINISHED
                win.callOnFlip(stimulus2.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GTDT3_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GTDT3_1" ---
    for thisComponent in GTDT3_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if stimulus2.status == STARTED:
        win.callOnFlip(stimulus2.setData, int(0))
    # the Routine "GTDT3_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "question" ---
continueRoutine = True
# update component parameters for each repeat
textbox.reset()
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
questionComponents = [text_3, bend2, textbox, key_resp_8]
for thisComponent in questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "question" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    
    # if text_3 is starting this frame...
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        # update status
        text_3.status = STARTED
        text_3.setAutoDraw(True)
    
    # if text_3 is active this frame...
    if text_3.status == STARTED:
        # update params
        pass
    # *bend2* updates
    
    # if bend2 is starting this frame...
    if bend2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bend2.frameNStart = frameN  # exact frame index
        bend2.tStart = t  # local t and not account for scr refresh
        bend2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bend2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bend2.started')
        # update status
        bend2.status = STARTED
        bend2.status = STARTED
        win.callOnFlip(bend2.setData, int(6))
    
    # if bend2 is stopping this frame...
    if bend2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bend2.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bend2.tStop = t  # not accounting for scr refresh
            bend2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bend2.stopped')
            # update status
            bend2.status = FINISHED
            win.callOnFlip(bend2.setData, int(0))
    
    # *textbox* updates
    
    # if textbox is starting this frame...
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox.started')
        # update status
        textbox.status = STARTED
        textbox.setAutoDraw(True)
    
    # if textbox is active this frame...
    if textbox.status == STARTED:
        # update params
        pass
    
    # *key_resp_8* updates
    waitOnFlip = False
    
    # if key_resp_8 is starting this frame...
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_8.started')
        # update status
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = [key.name for key in _key_resp_8_allKeys]  # storing all keys
            key_resp_8.rt = [key.rt for key in _key_resp_8_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "question" ---
for thisComponent in questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bend2.status == STARTED:
    win.callOnFlip(bend2.setData, int(0))
thisExp.addData('textbox.text',textbox.text)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "rest2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
rest2Components = [rest_2, key_resp_9]
for thisComponent in rest2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "rest2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_2* updates
    
    # if rest_2 is starting this frame...
    if rest_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_2.frameNStart = frameN  # exact frame index
        rest_2.tStart = t  # local t and not account for scr refresh
        rest_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_2.started')
        # update status
        rest_2.status = STARTED
        rest_2.setAutoDraw(True)
    
    # if rest_2 is active this frame...
    if rest_2.status == STARTED:
        # update params
        pass
    
    # *key_resp_9* updates
    waitOnFlip = False
    
    # if key_resp_9 is starting this frame...
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_9.started')
        # update status
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rest2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rest2" ---
for thisComponent in rest2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "rest2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction1_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction1_3Components = [i1_3, key_resp_3]
for thisComponent in instruction1_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction1_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i1_3* updates
    
    # if i1_3 is starting this frame...
    if i1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i1_3.frameNStart = frameN  # exact frame index
        i1_3.tStart = t  # local t and not account for scr refresh
        i1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i1_3.started')
        # update status
        i1_3.status = STARTED
        i1_3.setAutoDraw(True)
    
    # if i1_3 is active this frame...
    if i1_3.status == STARTED:
        # update params
        pass
    
    # *key_resp_3* updates
    waitOnFlip = False
    
    # if key_resp_3 is starting this frame...
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        # update status
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction1_3" ---
for thisComponent in instruction1_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instruction1_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "fixation1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [text, bstart]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "fixation1" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    # *bstart* updates
    
    # if bstart is starting this frame...
    if bstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bstart.frameNStart = frameN  # exact frame index
        bstart.tStart = t  # local t and not account for scr refresh
        bstart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bstart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bstart.started')
        # update status
        bstart.status = STARTED
        bstart.status = STARTED
        win.callOnFlip(bstart.setData, int(6))
    
    # if bstart is stopping this frame...
    if bstart.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bstart.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bstart.tStop = t  # not accounting for scr refresh
            bstart.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bstart.stopped')
            # update status
            bstart.status = FINISHED
            win.callOnFlip(bstart.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation1" ---
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bstart.status == STARTED:
    win.callOnFlip(bstart.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(root_dir + 'c2.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GTDT2_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    GTDT2_1Components = [annular, annular2, annular3,annular4,
        annular5,annular6,annular7,annular8,annular9,annular10,annular11,annular12,
        annular13,annular14,annular15,annular16, cover1, center1, bg1, key_resp_4, stimulus1]
    for thisComponent in GTDT2_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GTDT2_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *annular1* updates
        # *annular* updates
            
        # if annular is starting this frame...
        if annular.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            #stimulus_marker(1)
            # keep track of start time/frame for later
            annular.frameNStart = frameN  # exact frame index
            annular.tStart = t  # local t and not account for scr refresh
            annular.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular.started')
            # update status
            annular.status = STARTED
            annular.setAutoDraw(True)
        
        # if annular is active this frame...
        if annular.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular.setOpacity(None, log=False)
            annular.setContrast(cont, log=False)
            annular.setLineWidth(1.0, log=False)
        
        # if annular is stopping this frame...
        if annular.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular.tStop = t  # not accounting for scr refresh
                annular.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular.stopped')
                # update status
                annular.status = FINISHED
                annular.setAutoDraw(False)

        # *annular2* updates
        
        # if annular2 is starting this frame...
        if annular2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2.frameNStart = frameN  # exact frame index
            annular2.tStart = t  # local t and not account for scr refresh
            annular2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2.started')
            # update status
            annular2.status = STARTED
            annular2.setAutoDraw(True)
        
        # if annular2 is active this frame...
        if annular2.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2.setOpacity(None, log=False)
            annular2.setContrast(cont, log=False)
            annular2.setLineWidth(1.0, log=False)
        
        # if annular2 is stopping this frame...
        if annular2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2.tStop = t  # not accounting for scr refresh
                annular2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2.stopped')
                # update status
                annular2.status = FINISHED
                annular2.setAutoDraw(False)

        # *annular3* updates
        
        # if annular3 is starting this frame...
        if annular3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular3.frameNStart = frameN  # exact frame index
            annular3.tStart = t  # local t and not account for scr refresh
            annular3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular3.started')
            # update status
            annular3.status = STARTED
            annular3.setAutoDraw(True)
        
        # if annular3 is active this frame...
        if annular3.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular3.setOpacity(None, log=False)
            annular3.setContrast(cont, log=False)
            annular3.setLineWidth(1.0, log=False)
        
        # if annular3 is stopping this frame...
        if annular3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular3.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular3.tStop = t  # not accounting for scr refresh
                annular3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular3.stopped')
                # update status
                annular3.status = FINISHED
                annular3.setAutoDraw(False)


        # *annular4* updates
        
        # if annular4 is starting this frame...
        if annular4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular4.frameNStart = frameN  # exact frame index
            annular4.tStart = t  # local t and not account for scr refresh
            annular4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular4.started')
            # update status
            annular4.status = STARTED
            annular4.setAutoDraw(True)
        
        # if annular4 is active this frame...
        if annular4.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular4.setOpacity(None, log=False)
            annular4.setContrast(cont, log=False)
            annular4.setLineWidth(1.0, log=False)
        
        # if annular4 is stopping this frame...
        if annular4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular4.tStop = t  # not accounting for scr refresh
                annular4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular4.stopped')
                # update status
                annular4.status = FINISHED
                annular4.setAutoDraw(False)

        # *annular5* updates
        
        # if annular5 is starting this frame...
        if annular5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular5.frameNStart = frameN  # exact frame index
            annular5.tStart = t  # local t and not account for scr refresh
            annular5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular5.started')
            # update status
            annular5.status = STARTED
            annular5.setAutoDraw(True)
        
        # if annular5 is active this frame...
        if annular5.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular5.setOpacity(None, log=False)
            annular5.setContrast(cont, log=False)
            annular5.setLineWidth(1.0, log=False)
        
        # if annular5 is stopping this frame...
        if annular5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular5.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular5.tStop = t  # not accounting for scr refresh
                annular5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular5.stopped')
                # update status
                annular5.status = FINISHED
                annular5.setAutoDraw(False)

        # *annular6* updates
        
        # if annular6 is starting this frame...
        if annular6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular6.frameNStart = frameN  # exact frame index
            annular6.tStart = t  # local t and not account for scr refresh
            annular6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular6.started')
            # update status
            annular6.status = STARTED
            annular6.setAutoDraw(True)
        
        # if annular6 is active this frame...
        if annular6.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular6.setOpacity(None, log=False)
            annular6.setContrast(cont, log=False)
            annular6.setLineWidth(1.0, log=False)
        
        # if annular6 is stopping this frame...
        if annular6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular6.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular6.tStop = t  # not accounting for scr refresh
                annular6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular6.stopped')
                # update status
                annular6.status = FINISHED
                annular6.setAutoDraw(False)

        # *annular7* updates
        
        # if annular7 is starting this frame...
        if annular7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular7.frameNStart = frameN  # exact frame index
            annular7.tStart = t  # local t and not account for scr refresh
            annular7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular7.started')
            # update status
            annular7.status = STARTED
            annular7.setAutoDraw(True)
        
        # if annular7 is active this frame...
        if annular7.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular7.setOpacity(None, log=False)
            annular7.setContrast(cont, log=False)
            annular7.setLineWidth(1.0, log=False)
        
        # if annular7 is stopping this frame...
        if annular7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular7.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular7.tStop = t  # not accounting for scr refresh
                annular7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular7.stopped')
                # update status
                annular7.status = FINISHED
                annular7.setAutoDraw(False)

        # *annular8* updates
        
        # if annular8 is starting this frame...
        if annular8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular8.frameNStart = frameN  # exact frame index
            annular8.tStart = t  # local t and not account for scr refresh
            annular8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular8.started')
            # update status
            annular8.status = STARTED
            annular8.setAutoDraw(True)
        
        # if annular8 is active this frame...
        if annular8.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular8.setOpacity(None, log=False)
            annular8.setContrast(cont, log=False)
            annular8.setLineWidth(1.0, log=False)
        
        # if annular8 is stopping this frame...
        if annular8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular8.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular8.tStop = t  # not accounting for scr refresh
                annular8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular8.stopped')
                # update status
                annular8.status = FINISHED
                annular8.setAutoDraw(False)

        # *annular9* updates
        
        # if annular9 is starting this frame...
        if annular9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular9.frameNStart = frameN  # exact frame index
            annular9.tStart = t  # local t and not account for scr refresh
            annular9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular9.started')
            # update status
            annular9.status = STARTED
            annular9.setAutoDraw(True)
        
        # if annular9 is active this frame...
        if annular9.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular9.setOpacity(None, log=False)
            annular9.setContrast(cont, log=False)
            annular9.setLineWidth(1.0, log=False)
        
        # if annular9 is stopping this frame...
        if annular9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular9.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular9.tStop = t  # not accounting for scr refresh
                annular9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular9.stopped')
                # update status
                annular9.status = FINISHED
                annular9.setAutoDraw(False)

        # *annular10* updates
        
        # if annular10 is starting this frame...
        if annular10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular10.frameNStart = frameN  # exact frame index
            annular10.tStart = t  # local t and not account for scr refresh
            annular10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular10.started')
            # update status
            annular10.status = STARTED
            annular10.setAutoDraw(True)
        
        # if annular10 is active this frame...
        if annular10.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular10.setOpacity(None, log=False)
            annular10.setContrast(cont, log=False)
            annular10.setLineWidth(1.0, log=False)
        
        # if annular10 is stopping this frame...
        if annular10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular10.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular10.tStop = t  # not accounting for scr refresh
                annular10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular10.stopped')
                # update status
                annular10.status = FINISHED
                annular10.setAutoDraw(False)

        # *annular11* updates
        
        # if annular11 is starting this frame...
        if annular11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular11.frameNStart = frameN  # exact frame index
            annular11.tStart = t  # local t and not account for scr refresh
            annular11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular11.started')
            # update status
            annular11.status = STARTED
            annular11.setAutoDraw(True)
        
        # if annular11 is active this frame...
        if annular11.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular11.setOpacity(None, log=False)
            annular11.setContrast(cont, log=False)
            annular11.setLineWidth(1.0, log=False)
        
        # if annular11 is stopping this frame...
        if annular11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular11.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular11.tStop = t  # not accounting for scr refresh
                annular11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular11.stopped')
                # update status
                annular11.status = FINISHED
                annular11.setAutoDraw(False)

        # *annular12* updates
        
        # if annular12 is starting this frame...
        if annular12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular12.frameNStart = frameN  # exact frame index
            annular12.tStart = t  # local t and not account for scr refresh
            annular12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular12.started')
            # update status
            annular12.status = STARTED
            annular12.setAutoDraw(True)
        
        # if annular12 is active this frame...
        if annular12.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular12.setOpacity(None, log=False)
            annular12.setContrast(cont, log=False)
            annular12.setLineWidth(1.0, log=False)
        
        # if annular12 is stopping this frame...
        if annular12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular12.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular12.tStop = t  # not accounting for scr refresh
                annular12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular12.stopped')
                # update status
                annular12.status = FINISHED
                annular12.setAutoDraw(False)

        # *annular13* updates
        
        # if annular13 is starting this frame...
        if annular13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular13.frameNStart = frameN  # exact frame index
            annular13.tStart = t  # local t and not account for scr refresh
            annular13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular13.started')
            # update status
            annular13.status = STARTED
            annular13.setAutoDraw(True)
        
        # if annular13 is active this frame...
        if annular13.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular13.setOpacity(None, log=False)
            annular13.setContrast(cont, log=False)
            annular13.setLineWidth(1.0, log=False)
        
        # if annular13 is stopping this frame...
        if annular13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular13.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular13.tStop = t  # not accounting for scr refresh
                annular13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular13.stopped')
                # update status
                annular13.status = FINISHED
                annular13.setAutoDraw(False)

        # *annular14* updates
        
        # if annular14 is starting this frame...
        if annular14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular14.frameNStart = frameN  # exact frame index
            annular14.tStart = t  # local t and not account for scr refresh
            annular14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular14.started')
            # update status
            annular14.status = STARTED
            annular14.setAutoDraw(True)
        
        # if annular14 is active this frame...
        if annular14.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular14.setOpacity(None, log=False)
            annular14.setContrast(cont, log=False)
            annular14.setLineWidth(1.0, log=False)
        
        # if annular14 is stopping this frame...
        if annular14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular14.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular14.tStop = t  # not accounting for scr refresh
                annular14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular14.stopped')
                # update status
                annular14.status = FINISHED
                annular14.setAutoDraw(False)

        # *annular15* updates
        
        # if annular15 is starting this frame...
        if annular15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular15.frameNStart = frameN  # exact frame index
            annular15.tStart = t  # local t and not account for scr refresh
            annular15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular15.started')
            # update status
            annular15.status = STARTED
            annular15.setAutoDraw(True)
        
        # if annular15 is active this frame...
        if annular15.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular15.setOpacity(None, log=False)
            annular15.setContrast(cont, log=False)
            annular15.setLineWidth(1.0, log=False)
        
        # if annular15 is stopping this frame...
        if annular15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular15.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular15.tStop = t  # not accounting for scr refresh
                annular15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular15.stopped')
                # update status
                annular15.status = FINISHED
                annular15.setAutoDraw(False)

        # *annular16* updates
        
        # if annular16 is starting this frame...
        if annular16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular16.frameNStart = frameN  # exact frame index
            annular16.tStart = t  # local t and not account for scr refresh
            annular16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular16.started')
            # update status
            annular16.status = STARTED
            annular16.setAutoDraw(True)
        
        # if annular16 is active this frame...
        if annular16.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular16.setOpacity(None, log=False)
            annular16.setContrast(cont, log=False)
            annular16.setLineWidth(1.0, log=False)
        
        # if annular16 is stopping this frame...
        if annular16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular16.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular16.tStop = t  # not accounting for scr refresh
                annular16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular16.stopped')
                # update status
                annular16.status = FINISHED
                annular16.setAutoDraw(False)
        
        
        # *cover1* updates
        
        # if cover1 is starting this frame...
        if cover1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cover1.frameNStart = frameN  # exact frame index
            cover1.tStart = t  # local t and not account for scr refresh
            cover1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cover1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cover1.started')
            # update status
            cover1.status = STARTED
            cover1.setAutoDraw(True)
        
        # if cover1 is active this frame...
        if cover1.status == STARTED:
            # update params
            opci=0.5+0.5*np.sin(2*np.pi*t*21.25)
            # update params
            cover1.setOpacity(opci, log=False)
            cover1.setContrast(0.0, log=False)
            cover1.setLineWidth(1.0, log=False)
        
        # if cover1 is stopping this frame...
        if cover1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cover1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                cover1.tStop = t  # not accounting for scr refresh
                cover1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover1.stopped')
                # update status
                cover1.status = FINISHED
                cover1.setAutoDraw(False)
        
        # *center1* updates
        
        # if center1 is starting this frame...
        if center1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center1.frameNStart = frameN  # exact frame index
            center1.tStart = t  # local t and not account for scr refresh
            center1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'center1.started')
            # update status
            center1.status = STARTED
            center1.setAutoDraw(True)
        
        # if center1 is active this frame...
        if center1.status == STARTED:
            # update params
            pass
        
        # if center1 is stopping this frame...
        if center1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > center1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                center1.tStop = t  # not accounting for scr refresh
                center1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'center1.stopped')
                # update status
                center1.status = FINISHED
                center1.setAutoDraw(False)
        
        # *bg1* updates
        
        # if bg1 is starting this frame...
        if bg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bg1.frameNStart = frameN  # exact frame index
            bg1.tStart = t  # local t and not account for scr refresh
            bg1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bg1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bg1.started')
            # update status
            bg1.status = STARTED
            bg1.setAutoDraw(True)
        
        # if bg1 is active this frame...
        if bg1.status == STARTED:
            # update params
            #pass
            # update params
            bg1.setOpacity(None, log=False)
            bg1.setContrast(1.0, log=False)
            bg1.setLineWidth(1.0, log=False)
        
        # if bg1 is stopping this frame...
        if bg1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bg1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                bg1.tStop = t  # not accounting for scr refresh
                bg1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg1.stopped')
                # update status
                bg1.status = FINISHED
                bg1.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_4 is stopping this frame...
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                # update status
                key_resp_4.status = FINISHED
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                a= len(key_resp_4.keys)
                key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                b= len(key_resp_4.keys)
                if b-a==1:
                    responses_marker(2)
                key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                # a response ends the routine
                continueRoutine = True
        # *stimulus1* updates
        
        # if stimulus1 is starting this frame...
        if stimulus1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus1.frameNStart = frameN  # exact frame index
            stimulus1.tStart = t  # local t and not account for scr refresh
            stimulus1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimulus1.started')
            # update status
            stimulus1.status = STARTED
            stimulus1.status = STARTED
            win.callOnFlip(stimulus1.setData, int(1))
        
        # if stimulus1 is stopping this frame...
        if stimulus1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus1.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                stimulus1.tStop = t  # not accounting for scr refresh
                stimulus1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus1.stopped')
                # update status
                stimulus1.status = FINISHED
                win.callOnFlip(stimulus1.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GTDT2_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GTDT2_1" ---
    for thisComponent in GTDT2_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials_3.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_3.addData('key_resp_4.rt', key_resp_4.rt)
    if stimulus1.status == STARTED:
        win.callOnFlip(stimulus1.setData, int(0))
    # the Routine "GTDT2_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# --- Prepare to start Routine "rest3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
rest3Components = [rest_3, key_resp_10, bend3]
for thisComponent in rest3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "rest3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_3* updates
    
    # if rest_3 is starting this frame...
    if rest_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_3.frameNStart = frameN  # exact frame index
        rest_3.tStart = t  # local t and not account for scr refresh
        rest_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_3.started')
        # update status
        rest_3.status = STARTED
        rest_3.setAutoDraw(True)
    
    # if rest_3 is active this frame...
    if rest_3.status == STARTED:
        # update params
        pass
    
    # *key_resp_10* updates
    waitOnFlip = False
    
    # if key_resp_10 is starting this frame...
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_10.started')
        # update status
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *bend3* updates
    
    # if bend3 is starting this frame...
    if bend3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bend3.frameNStart = frameN  # exact frame index
        bend3.tStart = t  # local t and not account for scr refresh
        bend3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bend3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bend3.started')
        # update status
        bend3.status = STARTED
        bend3.status = STARTED
        win.callOnFlip(bend3.setData, int(6))
    
    # if bend3 is stopping this frame...
    if bend3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bend3.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bend3.tStop = t  # not accounting for scr refresh
            bend3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bend3.stopped')
            # update status
            bend3.status = FINISHED
            win.callOnFlip(bend3.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rest3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rest3" ---
for thisComponent in rest3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
if bend3.status == STARTED:
    win.callOnFlip(bend3.setData, int(0))
# the Routine "rest3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction1_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction1_3Components = [i1_3, key_resp_3]
for thisComponent in instruction1_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction1_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i1_3* updates
    
    # if i1_3 is starting this frame...
    if i1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i1_3.frameNStart = frameN  # exact frame index
        i1_3.tStart = t  # local t and not account for scr refresh
        i1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i1_3.started')
        # update status
        i1_3.status = STARTED
        i1_3.setAutoDraw(True)
    
    # if i1_3 is active this frame...
    if i1_3.status == STARTED:
        # update params
        pass
    
    # *key_resp_3* updates
    waitOnFlip = False
    
    # if key_resp_3 is starting this frame...
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        # update status
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction1_3" ---
for thisComponent in instruction1_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instruction1_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "fixation1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [text, bstart]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "fixation1" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    # *bstart* updates
    
    # if bstart is starting this frame...
    if bstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bstart.frameNStart = frameN  # exact frame index
        bstart.tStart = t  # local t and not account for scr refresh
        bstart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bstart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bstart.started')
        # update status
        bstart.status = STARTED
        bstart.status = STARTED
        win.callOnFlip(bstart.setData, int(6))
    
    # if bstart is stopping this frame...
    if bstart.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bstart.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bstart.tStop = t  # not accounting for scr refresh
            bstart.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bstart.stopped')
            # update status
            bstart.status = FINISHED
            win.callOnFlip(bstart.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation1" ---
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bstart.status == STARTED:
    win.callOnFlip(bstart.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(root_dir + 'c2.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GTDT2_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    GTDT2_1Components = [annular, annular2, annular3,annular4,
        annular5,annular6,annular7,annular8,annular9,annular10,annular11,annular12,
        annular13,annular14,annular15,annular16, cover1, center1, bg1, key_resp_4, stimulus1]
    for thisComponent in GTDT2_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GTDT2_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *annular1* updates
        # *annular* updates
            
        # if annular is starting this frame...
        if annular.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            #stimulus_marker(1)
            # keep track of start time/frame for later
            annular.frameNStart = frameN  # exact frame index
            annular.tStart = t  # local t and not account for scr refresh
            annular.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular.started')
            # update status
            annular.status = STARTED
            annular.setAutoDraw(True)
        
        # if annular is active this frame...
        if annular.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular.setOpacity(None, log=False)
            annular.setContrast(cont, log=False)
            annular.setLineWidth(1.0, log=False)
        
        # if annular is stopping this frame...
        if annular.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular.tStop = t  # not accounting for scr refresh
                annular.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular.stopped')
                # update status
                annular.status = FINISHED
                annular.setAutoDraw(False)

        # *annular2* updates
        
        # if annular2 is starting this frame...
        if annular2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2.frameNStart = frameN  # exact frame index
            annular2.tStart = t  # local t and not account for scr refresh
            annular2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2.started')
            # update status
            annular2.status = STARTED
            annular2.setAutoDraw(True)
        
        # if annular2 is active this frame...
        if annular2.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2.setOpacity(None, log=False)
            annular2.setContrast(cont, log=False)
            annular2.setLineWidth(1.0, log=False)
        
        # if annular2 is stopping this frame...
        if annular2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2.tStop = t  # not accounting for scr refresh
                annular2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2.stopped')
                # update status
                annular2.status = FINISHED
                annular2.setAutoDraw(False)

        # *annular3* updates
        
        # if annular3 is starting this frame...
        if annular3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular3.frameNStart = frameN  # exact frame index
            annular3.tStart = t  # local t and not account for scr refresh
            annular3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular3.started')
            # update status
            annular3.status = STARTED
            annular3.setAutoDraw(True)
        
        # if annular3 is active this frame...
        if annular3.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular3.setOpacity(None, log=False)
            annular3.setContrast(cont, log=False)
            annular3.setLineWidth(1.0, log=False)
        
        # if annular3 is stopping this frame...
        if annular3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular3.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular3.tStop = t  # not accounting for scr refresh
                annular3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular3.stopped')
                # update status
                annular3.status = FINISHED
                annular3.setAutoDraw(False)


        # *annular4* updates
        
        # if annular4 is starting this frame...
        if annular4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular4.frameNStart = frameN  # exact frame index
            annular4.tStart = t  # local t and not account for scr refresh
            annular4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular4.started')
            # update status
            annular4.status = STARTED
            annular4.setAutoDraw(True)
        
        # if annular4 is active this frame...
        if annular4.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular4.setOpacity(None, log=False)
            annular4.setContrast(cont, log=False)
            annular4.setLineWidth(1.0, log=False)
        
        # if annular4 is stopping this frame...
        if annular4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular4.tStop = t  # not accounting for scr refresh
                annular4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular4.stopped')
                # update status
                annular4.status = FINISHED
                annular4.setAutoDraw(False)

        # *annular5* updates
        
        # if annular5 is starting this frame...
        if annular5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular5.frameNStart = frameN  # exact frame index
            annular5.tStart = t  # local t and not account for scr refresh
            annular5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular5.started')
            # update status
            annular5.status = STARTED
            annular5.setAutoDraw(True)
        
        # if annular5 is active this frame...
        if annular5.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular5.setOpacity(None, log=False)
            annular5.setContrast(cont, log=False)
            annular5.setLineWidth(1.0, log=False)
        
        # if annular5 is stopping this frame...
        if annular5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular5.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular5.tStop = t  # not accounting for scr refresh
                annular5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular5.stopped')
                # update status
                annular5.status = FINISHED
                annular5.setAutoDraw(False)

        # *annular6* updates
        
        # if annular6 is starting this frame...
        if annular6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular6.frameNStart = frameN  # exact frame index
            annular6.tStart = t  # local t and not account for scr refresh
            annular6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular6.started')
            # update status
            annular6.status = STARTED
            annular6.setAutoDraw(True)
        
        # if annular6 is active this frame...
        if annular6.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular6.setOpacity(None, log=False)
            annular6.setContrast(cont, log=False)
            annular6.setLineWidth(1.0, log=False)
        
        # if annular6 is stopping this frame...
        if annular6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular6.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular6.tStop = t  # not accounting for scr refresh
                annular6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular6.stopped')
                # update status
                annular6.status = FINISHED
                annular6.setAutoDraw(False)

        # *annular7* updates
        
        # if annular7 is starting this frame...
        if annular7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular7.frameNStart = frameN  # exact frame index
            annular7.tStart = t  # local t and not account for scr refresh
            annular7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular7.started')
            # update status
            annular7.status = STARTED
            annular7.setAutoDraw(True)
        
        # if annular7 is active this frame...
        if annular7.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular7.setOpacity(None, log=False)
            annular7.setContrast(cont, log=False)
            annular7.setLineWidth(1.0, log=False)
        
        # if annular7 is stopping this frame...
        if annular7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular7.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular7.tStop = t  # not accounting for scr refresh
                annular7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular7.stopped')
                # update status
                annular7.status = FINISHED
                annular7.setAutoDraw(False)

        # *annular8* updates
        
        # if annular8 is starting this frame...
        if annular8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular8.frameNStart = frameN  # exact frame index
            annular8.tStart = t  # local t and not account for scr refresh
            annular8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular8.started')
            # update status
            annular8.status = STARTED
            annular8.setAutoDraw(True)
        
        # if annular8 is active this frame...
        if annular8.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular8.setOpacity(None, log=False)
            annular8.setContrast(cont, log=False)
            annular8.setLineWidth(1.0, log=False)
        
        # if annular8 is stopping this frame...
        if annular8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular8.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular8.tStop = t  # not accounting for scr refresh
                annular8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular8.stopped')
                # update status
                annular8.status = FINISHED
                annular8.setAutoDraw(False)

        # *annular9* updates
        
        # if annular9 is starting this frame...
        if annular9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular9.frameNStart = frameN  # exact frame index
            annular9.tStart = t  # local t and not account for scr refresh
            annular9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular9.started')
            # update status
            annular9.status = STARTED
            annular9.setAutoDraw(True)
        
        # if annular9 is active this frame...
        if annular9.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular9.setOpacity(None, log=False)
            annular9.setContrast(cont, log=False)
            annular9.setLineWidth(1.0, log=False)
        
        # if annular9 is stopping this frame...
        if annular9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular9.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular9.tStop = t  # not accounting for scr refresh
                annular9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular9.stopped')
                # update status
                annular9.status = FINISHED
                annular9.setAutoDraw(False)

        # *annular10* updates
        
        # if annular10 is starting this frame...
        if annular10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular10.frameNStart = frameN  # exact frame index
            annular10.tStart = t  # local t and not account for scr refresh
            annular10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular10.started')
            # update status
            annular10.status = STARTED
            annular10.setAutoDraw(True)
        
        # if annular10 is active this frame...
        if annular10.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular10.setOpacity(None, log=False)
            annular10.setContrast(cont, log=False)
            annular10.setLineWidth(1.0, log=False)
        
        # if annular10 is stopping this frame...
        if annular10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular10.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular10.tStop = t  # not accounting for scr refresh
                annular10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular10.stopped')
                # update status
                annular10.status = FINISHED
                annular10.setAutoDraw(False)

        # *annular11* updates
        
        # if annular11 is starting this frame...
        if annular11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular11.frameNStart = frameN  # exact frame index
            annular11.tStart = t  # local t and not account for scr refresh
            annular11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular11.started')
            # update status
            annular11.status = STARTED
            annular11.setAutoDraw(True)
        
        # if annular11 is active this frame...
        if annular11.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular11.setOpacity(None, log=False)
            annular11.setContrast(cont, log=False)
            annular11.setLineWidth(1.0, log=False)
        
        # if annular11 is stopping this frame...
        if annular11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular11.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular11.tStop = t  # not accounting for scr refresh
                annular11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular11.stopped')
                # update status
                annular11.status = FINISHED
                annular11.setAutoDraw(False)

        # *annular12* updates
        
        # if annular12 is starting this frame...
        if annular12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular12.frameNStart = frameN  # exact frame index
            annular12.tStart = t  # local t and not account for scr refresh
            annular12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular12.started')
            # update status
            annular12.status = STARTED
            annular12.setAutoDraw(True)
        
        # if annular12 is active this frame...
        if annular12.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular12.setOpacity(None, log=False)
            annular12.setContrast(cont, log=False)
            annular12.setLineWidth(1.0, log=False)
        
        # if annular12 is stopping this frame...
        if annular12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular12.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular12.tStop = t  # not accounting for scr refresh
                annular12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular12.stopped')
                # update status
                annular12.status = FINISHED
                annular12.setAutoDraw(False)

        # *annular13* updates
        
        # if annular13 is starting this frame...
        if annular13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular13.frameNStart = frameN  # exact frame index
            annular13.tStart = t  # local t and not account for scr refresh
            annular13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular13.started')
            # update status
            annular13.status = STARTED
            annular13.setAutoDraw(True)
        
        # if annular13 is active this frame...
        if annular13.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular13.setOpacity(None, log=False)
            annular13.setContrast(cont, log=False)
            annular13.setLineWidth(1.0, log=False)
        
        # if annular13 is stopping this frame...
        if annular13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular13.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular13.tStop = t  # not accounting for scr refresh
                annular13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular13.stopped')
                # update status
                annular13.status = FINISHED
                annular13.setAutoDraw(False)

        # *annular14* updates
        
        # if annular14 is starting this frame...
        if annular14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular14.frameNStart = frameN  # exact frame index
            annular14.tStart = t  # local t and not account for scr refresh
            annular14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular14.started')
            # update status
            annular14.status = STARTED
            annular14.setAutoDraw(True)
        
        # if annular14 is active this frame...
        if annular14.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular14.setOpacity(None, log=False)
            annular14.setContrast(cont, log=False)
            annular14.setLineWidth(1.0, log=False)
        
        # if annular14 is stopping this frame...
        if annular14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular14.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular14.tStop = t  # not accounting for scr refresh
                annular14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular14.stopped')
                # update status
                annular14.status = FINISHED
                annular14.setAutoDraw(False)

        # *annular15* updates
        
        # if annular15 is starting this frame...
        if annular15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular15.frameNStart = frameN  # exact frame index
            annular15.tStart = t  # local t and not account for scr refresh
            annular15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular15.started')
            # update status
            annular15.status = STARTED
            annular15.setAutoDraw(True)
        
        # if annular15 is active this frame...
        if annular15.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular15.setOpacity(None, log=False)
            annular15.setContrast(cont, log=False)
            annular15.setLineWidth(1.0, log=False)
        
        # if annular15 is stopping this frame...
        if annular15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular15.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular15.tStop = t  # not accounting for scr refresh
                annular15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular15.stopped')
                # update status
                annular15.status = FINISHED
                annular15.setAutoDraw(False)

        # *annular16* updates
        
        # if annular16 is starting this frame...
        if annular16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular16.frameNStart = frameN  # exact frame index
            annular16.tStart = t  # local t and not account for scr refresh
            annular16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular16.started')
            # update status
            annular16.status = STARTED
            annular16.setAutoDraw(True)
        
        # if annular16 is active this frame...
        if annular16.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular16.setOpacity(None, log=False)
            annular16.setContrast(cont, log=False)
            annular16.setLineWidth(1.0, log=False)
        
        # if annular16 is stopping this frame...
        if annular16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular16.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular16.tStop = t  # not accounting for scr refresh
                annular16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular16.stopped')
                # update status
                annular16.status = FINISHED
                annular16.setAutoDraw(False)
        
        
        # *cover1* updates
        
        # if cover1 is starting this frame...
        if cover1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cover1.frameNStart = frameN  # exact frame index
            cover1.tStart = t  # local t and not account for scr refresh
            cover1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cover1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cover1.started')
            # update status
            cover1.status = STARTED
            cover1.setAutoDraw(True)
        
        # if cover1 is active this frame...
        if cover1.status == STARTED:
            # update params
            opci=0.5+0.5*np.sin(2*np.pi*t*21.25)
            # update params
            cover1.setOpacity(opci, log=False)
            cover1.setContrast(0.0, log=False)
            cover1.setLineWidth(1.0, log=False)
        
        # if cover1 is stopping this frame...
        if cover1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cover1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                cover1.tStop = t  # not accounting for scr refresh
                cover1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover1.stopped')
                # update status
                cover1.status = FINISHED
                cover1.setAutoDraw(False)
        
        # *center1* updates
        
        # if center1 is starting this frame...
        if center1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center1.frameNStart = frameN  # exact frame index
            center1.tStart = t  # local t and not account for scr refresh
            center1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'center1.started')
            # update status
            center1.status = STARTED
            center1.setAutoDraw(True)
        
        # if center1 is active this frame...
        if center1.status == STARTED:
            # update params
            pass
        
        # if center1 is stopping this frame...
        if center1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > center1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                center1.tStop = t  # not accounting for scr refresh
                center1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'center1.stopped')
                # update status
                center1.status = FINISHED
                center1.setAutoDraw(False)
        
        # *bg1* updates
        
        # if bg1 is starting this frame...
        if bg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bg1.frameNStart = frameN  # exact frame index
            bg1.tStart = t  # local t and not account for scr refresh
            bg1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bg1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bg1.started')
            # update status
            bg1.status = STARTED
            bg1.setAutoDraw(True)
        
        # if bg1 is active this frame...
        if bg1.status == STARTED:
            # update params
            #pass
            # update params
            bg1.setOpacity(None, log=False)
            bg1.setContrast(1.0, log=False)
            bg1.setLineWidth(1.0, log=False)
        
        # if bg1 is stopping this frame...
        if bg1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bg1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                bg1.tStop = t  # not accounting for scr refresh
                bg1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg1.stopped')
                # update status
                bg1.status = FINISHED
                bg1.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_4 is stopping this frame...
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                # update status
                key_resp_4.status = FINISHED
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                a= len(key_resp_4.keys)
                key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                b= len(key_resp_4.keys)
                if b-a==1:
                    responses_marker(2)
                key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                # a response ends the routine
                continueRoutine = True
        # *stimulus1* updates
        
        # if stimulus1 is starting this frame...
        if stimulus1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus1.frameNStart = frameN  # exact frame index
            stimulus1.tStart = t  # local t and not account for scr refresh
            stimulus1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimulus1.started')
            # update status
            stimulus1.status = STARTED
            stimulus1.status = STARTED
            win.callOnFlip(stimulus1.setData, int(1))
        
        # if stimulus1 is stopping this frame...
        if stimulus1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus1.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                stimulus1.tStop = t  # not accounting for scr refresh
                stimulus1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus1.stopped')
                # update status
                stimulus1.status = FINISHED
                win.callOnFlip(stimulus1.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GTDT2_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GTDT2_1" ---
    for thisComponent in GTDT2_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials_4.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_4.addData('key_resp_4.rt', key_resp_4.rt)
    if stimulus1.status == STARTED:
        win.callOnFlip(stimulus1.setData, int(0))
    # the Routine "GTDT2_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# --- Prepare to start Routine "rest4" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
rest4Components = [rest_4, key_resp_11, bend4]
for thisComponent in rest4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "rest4" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_4* updates
    
    # if rest_4 is starting this frame...
    if rest_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_4.frameNStart = frameN  # exact frame index
        rest_4.tStart = t  # local t and not account for scr refresh
        rest_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_4.started')
        # update status
        rest_4.status = STARTED
        rest_4.setAutoDraw(True)
    
    # if rest_4 is active this frame...
    if rest_4.status == STARTED:
        # update params
        pass
    
    # *key_resp_11* updates
    waitOnFlip = False
    
    # if key_resp_11 is starting this frame...
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_11.started')
        # update status
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *bend4* updates
    
    # if bend4 is starting this frame...
    if bend4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bend4.frameNStart = frameN  # exact frame index
        bend4.tStart = t  # local t and not account for scr refresh
        bend4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bend4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bend4.started')
        # update status
        bend4.status = STARTED
        bend4.status = STARTED
        win.callOnFlip(bend4.setData, int(6))
    
    # if bend4 is stopping this frame...
    if bend4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bend4.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bend4.tStop = t  # not accounting for scr refresh
            bend4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bend4.stopped')
            # update status
            bend4.status = FINISHED
            win.callOnFlip(bend4.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rest4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rest4" ---
for thisComponent in rest4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
if bend4.status == STARTED:
    win.callOnFlip(bend4.setData, int(0))
# the Routine "rest4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
instruction2Components = [i2, key_resp_6]
for thisComponent in instruction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i2* updates
    
    # if i2 is starting this frame...
    if i2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i2.frameNStart = frameN  # exact frame index
        i2.tStart = t  # local t and not account for scr refresh
        i2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i2.started')
        # update status
        i2.status = STARTED
        i2.setAutoDraw(True)
    
    # if i2 is active this frame...
    if i2.status == STARTED:
        # update params
        pass
    
    # *key_resp_6* updates
    waitOnFlip = False
    
    # if key_resp_6 is starting this frame...
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        # update status
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction2" ---
for thisComponent in instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "fixation1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [text, bstart]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "fixation1" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    # *bstart* updates
    
    # if bstart is starting this frame...
    if bstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bstart.frameNStart = frameN  # exact frame index
        bstart.tStart = t  # local t and not account for scr refresh
        bstart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bstart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bstart.started')
        # update status
        bstart.status = STARTED
        bstart.status = STARTED
        win.callOnFlip(bstart.setData, int(6))
    
    # if bstart is stopping this frame...
    if bstart.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bstart.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bstart.tStop = t  # not accounting for scr refresh
            bstart.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bstart.stopped')
            # update status
            bstart.status = FINISHED
            win.callOnFlip(bstart.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation1" ---
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bstart.status == STARTED:
    win.callOnFlip(bstart.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)
    
# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(root_dir + 'c326.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GTDT3_1" ---
    continueRoutine = True
    # keep track of which components have finished
    GTDT3_1Components = [annular2_1, annular2_2, annular2_3,annular2_4,
        annular2_5,annular2_6,annular2_7,annular2_8,annular2_9,annular2_10,annular2_11,annular2_12,
        annular2_13,annular2_14,annular2_15,annular2_16, cover2, center2, bg2, stimulus2]
    for thisComponent in GTDT3_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GTDT3_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *annular* updates
            
        # if annular is starting this frame...
        if annular2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            #stimulus_marker(1)
            # keep track of start time/frame for later
            annular2_1.frameNStart = frameN  # exact frame index
            annular2_1.tStart = t  # local t and not account for scr refresh
            annular2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_1.started')
            # update status
            annular2_1.status = STARTED
            annular2_1.setAutoDraw(True)
        
        # if annular is active this frame...
        if annular2_1.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_1.setOpacity(None, log=False)
            annular2_1.setContrast(cont, log=False)
            annular2_1.setLineWidth(1.0, log=False)
        
        # if annular is stopping this frame...
        if annular2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_1.tStop = t  # not accounting for scr refresh
                annular2_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_1.stopped')
                # update status
                annular2_1.status = FINISHED
                annular2_1.setAutoDraw(False)

        # *annular2_2* updates
        
        # if annular2_2 is starting this frame...
        if annular2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_2.frameNStart = frameN  # exact frame index
            annular2_2.tStart = t  # local t and not account for scr refresh
            annular2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_2.started')
            # update status
            annular2_2.status = STARTED
            annular2_2.setAutoDraw(True)
        
        # if annular2_2 is active this frame...
        if annular2_2.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_2.setOpacity(None, log=False)
            annular2_2.setContrast(cont, log=False)
            annular2_2.setLineWidth(1.0, log=False)
        
        # if annular2_2 is stopping this frame...
        if annular2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_2.tStop = t  # not accounting for scr refresh
                annular2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_2.stopped')
                # update status
                annular2_2.status = FINISHED
                annular2_2.setAutoDraw(False)

        # *annular2_3* updates
        
        # if annular2_3 is starting this frame...
        if annular2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_3.frameNStart = frameN  # exact frame index
            annular2_3.tStart = t  # local t and not account for scr refresh
            annular2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_3.started')
            # update status
            annular2_3.status = STARTED
            annular2_3.setAutoDraw(True)
        
        # if annular2_3 is active this frame...
        if annular2_3.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_3.setOpacity(None, log=False)
            annular2_3.setContrast(cont, log=False)
            annular2_3.setLineWidth(1.0, log=False)
        
        # if annular2_3 is stopping this frame...
        if annular2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_3.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_3.tStop = t  # not accounting for scr refresh
                annular2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_3.stopped')
                # update status
                annular2_3.status = FINISHED
                annular2_3.setAutoDraw(False)


        # *annular2_4* updates
        
        # if annular2_4 is starting this frame...
        if annular2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_4.frameNStart = frameN  # exact frame index
            annular2_4.tStart = t  # local t and not account for scr refresh
            annular2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_4.started')
            # update status
            annular2_4.status = STARTED
            annular2_4.setAutoDraw(True)
        
        # if annular4 is active this frame...
        if annular2_4.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_4.setOpacity(None, log=False)
            annular2_4.setContrast(cont, log=False)
            annular2_4.setLineWidth(1.0, log=False)
        
        # if annular2_4 is stopping this frame...
        if annular2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_4.tStop = t  # not accounting for scr refresh
                annular2_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_4.stopped')
                # update status
                annular2_4.status = FINISHED
                annular2_4.setAutoDraw(False)

        # *annular2_5* updates
        
        # if annular2_5 is starting this frame...
        if annular2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_5.frameNStart = frameN  # exact frame index
            annular2_5.tStart = t  # local t and not account for scr refresh
            annular2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_5.started')
            # update status
            annular2_5.status = STARTED
            annular2_5.setAutoDraw(True)
        
        # if annular5 is active this frame...
        if annular2_5.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_5.setOpacity(None, log=False)
            annular2_5.setContrast(cont, log=False)
            annular2_5.setLineWidth(1.0, log=False)
        
        # if annular5 is stopping this frame...
        if annular2_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_5.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_5.tStop = t  # not accounting for scr refresh
                annular2_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_5.stopped')
                # update status
                annular2_5.status = FINISHED
                annular2_5.setAutoDraw(False)

        # *annular2_6* updates
        
        # if annular2_6 is starting this frame...
        if annular2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_6.frameNStart = frameN  # exact frame index
            annular2_6.tStart = t  # local t and not account for scr refresh
            annular2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_6.started')
            # update status
            annular2_6.status = STARTED
            annular2_6.setAutoDraw(True)
        
        # if annular2_6 is active this frame...
        if annular2_6.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_6.setOpacity(None, log=False)
            annular2_6.setContrast(cont, log=False)
            annular2_6.setLineWidth(1.0, log=False)
        
        # if annular2_6 is stopping this frame...
        if annular2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_6.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_6.tStop = t  # not accounting for scr refresh
                annular2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_6.stopped')
                # update status
                annular2_6.status = FINISHED
                annular2_6.setAutoDraw(False)

        # *annular2_7* updates
        
        # if annular2_7 is starting this frame...
        if annular2_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_7.frameNStart = frameN  # exact frame index
            annular2_7.tStart = t  # local t and not account for scr refresh
            annular2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_7.started')
            # update status
            annular2_7.status = STARTED
            annular2_7.setAutoDraw(True)
        
        # if annular2_7 is active this frame...
        if annular2_7.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_7.setOpacity(None, log=False)
            annular2_7.setContrast(cont, log=False)
            annular2_7.setLineWidth(1.0, log=False)
        
        # if annular2_7 is stopping this frame...
        if annular2_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_7.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_7.tStop = t  # not accounting for scr refresh
                annular2_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_7.stopped')
                # update status
                annular2_7.status = FINISHED
                annular2_7.setAutoDraw(False)

        # *annular2_8* updates
        
        # if annular2_8 is starting this frame...
        if annular2_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_8.frameNStart = frameN  # exact frame index
            annular2_8.tStart = t  # local t and not account for scr refresh
            annular2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_8.started')
            # update status
            annular2_8.status = STARTED
            annular2_8.setAutoDraw(True)
        
        # if annular8 is active this frame...
        if annular2_8.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_8.setOpacity(None, log=False)
            annular2_8.setContrast(cont, log=False)
            annular2_8.setLineWidth(1.0, log=False)
        
        # if annular2_8 is stopping this frame...
        if annular2_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_8.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_8.tStop = t  # not accounting for scr refresh
                annular2_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_8.stopped')
                # update status
                annular2_8.status = FINISHED
                annular2_8.setAutoDraw(False)

        # *annular2_9* updates
        
        # if annular2_9 is starting this frame...
        if annular2_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_9.frameNStart = frameN  # exact frame index
            annular2_9.tStart = t  # local t and not account for scr refresh
            annular2_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_9.started')
            # update status
            annular2_9.status = STARTED
            annular2_9.setAutoDraw(True)
        
        # if annular2_9 is active this frame...
        if annular2_9.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_9.setOpacity(None, log=False)
            annular2_9.setContrast(cont, log=False)
            annular2_9.setLineWidth(1.0, log=False)
        
        # if annular2_9 is stopping this frame...
        if annular2_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_9.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_9.tStop = t  # not accounting for scr refresh
                annular2_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_9.stopped')
                # update status
                annular2_9.status = FINISHED
                annular2_9.setAutoDraw(False)

        # *annular2_10* updates
        
        # if annular2_10 is starting this frame...
        if annular2_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_10.frameNStart = frameN  # exact frame index
            annular2_10.tStart = t  # local t and not account for scr refresh
            annular2_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_10.started')
            # update status
            annular2_10.status = STARTED
            annular2_10.setAutoDraw(True)
        
        # if annular2_10 is active this frame...
        if annular2_10.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_10.setOpacity(None, log=False)
            annular2_10.setContrast(cont, log=False)
            annular2_10.setLineWidth(1.0, log=False)
        
        # if annular2_10 is stopping this frame...
        if annular2_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_10.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_10.tStop = t  # not accounting for scr refresh
                annular2_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_10.stopped')
                # update status
                annular2_10.status = FINISHED
                annular2_10.setAutoDraw(False)

        # *annular2_11* updates
        
        # if annular2_11 is starting this frame...
        if annular2_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_11.frameNStart = frameN  # exact frame index
            annular2_11.tStart = t  # local t and not account for scr refresh
            annular2_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_11.started')
            # update status
            annular2_11.status = STARTED
            annular2_11.setAutoDraw(True)
        
        # if annular2_11 is active this frame...
        if annular2_11.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_11.setOpacity(None, log=False)
            annular2_11.setContrast(cont, log=False)
            annular2_11.setLineWidth(1.0, log=False)
        
        # if annular2_11 is stopping this frame...
        if annular2_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_11.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_11.tStop = t  # not accounting for scr refresh
                annular2_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_11.stopped')
                # update status
                annular2_11.status = FINISHED
                annular2_11.setAutoDraw(False)

        # *annular2_12* updates
        
        # if annular2_12 is starting this frame...
        if annular2_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_12.frameNStart = frameN  # exact frame index
            annular2_12.tStart = t  # local t and not account for scr refresh
            annular2_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_12.started')
            # update status
            annular2_12.status = STARTED
            annular2_12.setAutoDraw(True)
        
        # if annular2_12 is active this frame...
        if annular2_12.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_12.setOpacity(None, log=False)
            annular2_12.setContrast(cont, log=False)
            annular2_12.setLineWidth(1.0, log=False)
        
        # if annular2_12 is stopping this frame...
        if annular2_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_12.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_12.tStop = t  # not accounting for scr refresh
                annular2_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_12.stopped')
                # update status
                annular2_12.status = FINISHED
                annular2_12.setAutoDraw(False)

        # *annular2_13* updates
        
        # if annular2_13 is starting this frame...
        if annular2_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_13.frameNStart = frameN  # exact frame index
            annular2_13.tStart = t  # local t and not account for scr refresh
            annular2_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_13.started')
            # update status
            annular2_13.status = STARTED
            annular2_13.setAutoDraw(True)
        
        # if annular2_13 is active this frame...
        if annular2_13.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_13.setOpacity(None, log=False)
            annular2_13.setContrast(cont, log=False)
            annular2_13.setLineWidth(1.0, log=False)
        
        # if annular2_13 is stopping this frame...
        if annular2_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_13.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_13.tStop = t  # not accounting for scr refresh
                annular2_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_13.stopped')
                # update status
                annular2_13.status = FINISHED
                annular2_13.setAutoDraw(False)

        # *annular2_14* updates
        
        # if annular2_14 is starting this frame...
        if annular2_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_14.frameNStart = frameN  # exact frame index
            annular2_14.tStart = t  # local t and not account for scr refresh
            annular2_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_14.started')
            # update status
            annular2_14.status = STARTED
            annular2_14.setAutoDraw(True)
        
        # if annular2_14 is active this frame...
        if annular2_14.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_14.setOpacity(None, log=False)
            annular2_14.setContrast(cont, log=False)
            annular2_14.setLineWidth(1.0, log=False)
        
        # if annular2_14 is stopping this frame...
        if annular2_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_14.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_14.tStop = t  # not accounting for scr refresh
                annular2_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_14.stopped')
                # update status
                annular2_14.status = FINISHED
                annular2_14.setAutoDraw(False)

        # *annular2_15* updates
        
        # if annular2_15 is starting this frame...
        if annular2_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_15.frameNStart = frameN  # exact frame index
            annular2_15.tStart = t  # local t and not account for scr refresh
            annular2_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_15.started')
            # update status
            annular2_15.status = STARTED
            annular2_15.setAutoDraw(True)
        
        # if annular2_15 is active this frame...
        if annular2_15.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_15.setOpacity(None, log=False)
            annular2_15.setContrast(cont, log=False)
            annular2_15.setLineWidth(1.0, log=False)
        
        # if annular2_15 is stopping this frame...
        if annular2_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_15.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_15.tStop = t  # not accounting for scr refresh
                annular2_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_15.stopped')
                # update status
                annular2_15.status = FINISHED
                annular2_15.setAutoDraw(False)

        # *annular2_16* updates
        
        # if annular2_16 is starting this frame...
        if annular2_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2_16.frameNStart = frameN  # exact frame index
            annular2_16.tStart = t  # local t and not account for scr refresh
            annular2_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2_16.started')
            # update status
            annular2_16.status = STARTED
            annular2_16.setAutoDraw(True)
        
        # if annular2_16 is active this frame...
        if annular2_16.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2_16.setOpacity(None, log=False)
            annular2_16.setContrast(cont, log=False)
            annular2_16.setLineWidth(1.0, log=False)
        
        # if annular2_16 is stopping this frame...
        if annular2_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2_16.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2_16.tStop = t  # not accounting for scr refresh
                annular2_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2_16.stopped')
                # update status
                annular2_16.status = FINISHED
                annular2_16.setAutoDraw(False)
        
        # *cover2* updates
        
        # if cover2 is starting this frame...
        if cover2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cover2.frameNStart = frameN  # exact frame index
            cover2.tStart = t  # local t and not account for scr refresh
            cover2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cover2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cover2.started')
            # update status
            cover2.status = STARTED
            cover2.setAutoDraw(True)
        
        # if cover2 is active this frame...
        if cover2.status == STARTED:
            opci=0.5+0.5*np.sin(2*np.pi*t*21.25)
            # update params
            cover2.setOpacity(opci, log=False)
            cover2.setContrast(0.0, log=False)
            cover2.setLineWidth(1.0, log=False)
        
        # if cover2 is stopping this frame...
        if cover2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cover2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                cover2.tStop = t  # not accounting for scr refresh
                cover2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover2.stopped')
                # update status
                cover2.status = FINISHED
                cover2.setAutoDraw(False)
        
        # *center2* updates
        
        # if center2 is starting this frame...
        if center2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center2.frameNStart = frameN  # exact frame index
            center2.tStart = t  # local t and not account for scr refresh
            center2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'center2.started')
            # update status
            center2.status = STARTED
            center2.setAutoDraw(True)
        
        # if center2 is active this frame...
        if center2.status == STARTED:
            # update params
            pass
        
        # if center2 is stopping this frame...
        if center2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > center2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                center2.tStop = t  # not accounting for scr refresh
                center2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'center2.stopped')
                # update status
                center2.status = FINISHED
                center2.setAutoDraw(False)
        
        # *bg2* updates
        
        # if bg2 is starting this frame...
        if bg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bg2.frameNStart = frameN  # exact frame index
            bg2.tStart = t  # local t and not account for scr refresh
            bg2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bg2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bg2.started')
            # update status
            bg2.status = STARTED
            bg2.setAutoDraw(True)
        
        # if bg2 is active this frame...
        if bg2.status == STARTED:
             # update params
            bg2.setOpacity(None, log=False)
            bg2.setContrast(1.0, log=False)
            bg2.setLineWidth(1.0, log=False)
        
        # if bg2 is stopping this frame...
        if bg2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bg2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                bg2.tStop = t  # not accounting for scr refresh
                bg2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg2.stopped')
                # update status
                bg2.status = FINISHED
                bg2.setAutoDraw(False)
        
        # *stimulus2* updates
        
        # if stimulus2 is starting this frame...
        if stimulus2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus2.frameNStart = frameN  # exact frame index
            stimulus2.tStart = t  # local t and not account for scr refresh
            stimulus2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimulus2.started')
            # update status
            stimulus2.status = STARTED
            stimulus2.status = STARTED
            win.callOnFlip(stimulus2.setData, int(1))
        
        # if stimulus2 is stopping this frame...
        if stimulus2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus2.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                stimulus2.tStop = t  # not accounting for scr refresh
                stimulus2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus2.stopped')
                # update status
                stimulus2.status = FINISHED
                win.callOnFlip(stimulus2.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GTDT3_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GTDT3_1" ---
    for thisComponent in GTDT3_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if stimulus2.status == STARTED:
        win.callOnFlip(stimulus2.setData, int(0))
    # the Routine "GTDT3_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_5'


# --- Prepare to start Routine "question" ---
continueRoutine = True
# update component parameters for each repeat
textbox.reset()
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
questionComponents = [text_3, bend2, textbox, key_resp_8]
for thisComponent in questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "question" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    
    # if text_3 is starting this frame...
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        # update status
        text_3.status = STARTED
        text_3.setAutoDraw(True)
    
    # if text_3 is active this frame...
    if text_3.status == STARTED:
        # update params
        pass
    # *bend2* updates
    
    # if bend2 is starting this frame...
    if bend2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bend2.frameNStart = frameN  # exact frame index
        bend2.tStart = t  # local t and not account for scr refresh
        bend2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bend2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bend2.started')
        # update status
        bend2.status = STARTED
        bend2.status = STARTED
        win.callOnFlip(bend2.setData, int(6))
    
    # if bend2 is stopping this frame...
    if bend2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bend2.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bend2.tStop = t  # not accounting for scr refresh
            bend2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bend2.stopped')
            # update status
            bend2.status = FINISHED
            win.callOnFlip(bend2.setData, int(0))
    
    # *textbox* updates
    
    # if textbox is starting this frame...
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox.started')
        # update status
        textbox.status = STARTED
        textbox.setAutoDraw(True)
    
    # if textbox is active this frame...
    if textbox.status == STARTED:
        # update params
        pass
    
    # *key_resp_8* updates
    waitOnFlip = False
    
    # if key_resp_8 is starting this frame...
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_8.started')
        # update status
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = [key.name for key in _key_resp_8_allKeys]  # storing all keys
            key_resp_8.rt = [key.rt for key in _key_resp_8_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "question" ---
for thisComponent in questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bend2.status == STARTED:
    win.callOnFlip(bend2.setData, int(0))
thisExp.addData('textbox.text',textbox.text)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "rest5" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
rest5Components = [rest_5, key_resp_12]
for thisComponent in rest5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "rest5" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_5* updates
    
    # if rest_5 is starting this frame...
    if rest_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_5.frameNStart = frameN  # exact frame index
        rest_5.tStart = t  # local t and not account for scr refresh
        rest_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_5.started')
        # update status
        rest_5.status = STARTED
        rest_5.setAutoDraw(True)
    
    # if rest_5 is active this frame...
    if rest_5.status == STARTED:
        # update params
        pass
    
    # *key_resp_12* updates
    waitOnFlip = False
    
    # if key_resp_12 is starting this frame...
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_12.started')
        # update status
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rest5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rest5" ---
for thisComponent in rest5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "rest5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction1_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction1_3Components = [i1_3, key_resp_3]
for thisComponent in instruction1_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction1_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i1_3* updates
    
    # if i1_3 is starting this frame...
    if i1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i1_3.frameNStart = frameN  # exact frame index
        i1_3.tStart = t  # local t and not account for scr refresh
        i1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i1_3.started')
        # update status
        i1_3.status = STARTED
        i1_3.setAutoDraw(True)
    
    # if i1_3 is active this frame...
    if i1_3.status == STARTED:
        # update params
        pass
    
    # *key_resp_3* updates
    waitOnFlip = False
    
    # if key_resp_3 is starting this frame...
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        # update status
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction1_3" ---
for thisComponent in instruction1_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instruction1_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "fixation1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [text, bstart]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "fixation1" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    # *bstart* updates
    
    # if bstart is starting this frame...
    if bstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bstart.frameNStart = frameN  # exact frame index
        bstart.tStart = t  # local t and not account for scr refresh
        bstart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bstart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bstart.started')
        # update status
        bstart.status = STARTED
        bstart.status = STARTED
        win.callOnFlip(bstart.setData, int(6))
    
    # if bstart is stopping this frame...
    if bstart.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bstart.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bstart.tStop = t  # not accounting for scr refresh
            bstart.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bstart.stopped')
            # update status
            bstart.status = FINISHED
            win.callOnFlip(bstart.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation1" ---
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if bstart.status == STARTED:
    win.callOnFlip(bstart.setData, int(0))
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)
    
# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(root_dir + 'c2.xlsx'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GTDT2_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    GTDT2_1Components = [annular, annular2, annular3,annular4,
        annular5,annular6,annular7,annular8,annular9,annular10,annular11,annular12,
        annular13,annular14,annular15,annular16, cover1, center1, bg1, key_resp_4, stimulus1]
    for thisComponent in GTDT2_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GTDT2_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *annular1* updates
        # *annular* updates
            
        # if annular is starting this frame...
        if annular.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            #stimulus_marker(1)
            # keep track of start time/frame for later
            annular.frameNStart = frameN  # exact frame index
            annular.tStart = t  # local t and not account for scr refresh
            annular.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular.started')
            # update status
            annular.status = STARTED
            annular.setAutoDraw(True)
        
        # if annular is active this frame...
        if annular.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular.setOpacity(None, log=False)
            annular.setContrast(cont, log=False)
            annular.setLineWidth(1.0, log=False)
        
        # if annular is stopping this frame...
        if annular.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular.tStop = t  # not accounting for scr refresh
                annular.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular.stopped')
                # update status
                annular.status = FINISHED
                annular.setAutoDraw(False)

        # *annular2* updates
        
        # if annular2 is starting this frame...
        if annular2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular2.frameNStart = frameN  # exact frame index
            annular2.tStart = t  # local t and not account for scr refresh
            annular2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular2.started')
            # update status
            annular2.status = STARTED
            annular2.setAutoDraw(True)
        
        # if annular2 is active this frame...
        if annular2.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular2.setOpacity(None, log=False)
            annular2.setContrast(cont, log=False)
            annular2.setLineWidth(1.0, log=False)
        
        # if annular2 is stopping this frame...
        if annular2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular2.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular2.tStop = t  # not accounting for scr refresh
                annular2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular2.stopped')
                # update status
                annular2.status = FINISHED
                annular2.setAutoDraw(False)

        # *annular3* updates
        
        # if annular3 is starting this frame...
        if annular3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular3.frameNStart = frameN  # exact frame index
            annular3.tStart = t  # local t and not account for scr refresh
            annular3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular3.started')
            # update status
            annular3.status = STARTED
            annular3.setAutoDraw(True)
        
        # if annular3 is active this frame...
        if annular3.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular3.setOpacity(None, log=False)
            annular3.setContrast(cont, log=False)
            annular3.setLineWidth(1.0, log=False)
        
        # if annular3 is stopping this frame...
        if annular3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular3.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular3.tStop = t  # not accounting for scr refresh
                annular3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular3.stopped')
                # update status
                annular3.status = FINISHED
                annular3.setAutoDraw(False)


        # *annular4* updates
        
        # if annular4 is starting this frame...
        if annular4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular4.frameNStart = frameN  # exact frame index
            annular4.tStart = t  # local t and not account for scr refresh
            annular4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular4.started')
            # update status
            annular4.status = STARTED
            annular4.setAutoDraw(True)
        
        # if annular4 is active this frame...
        if annular4.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular4.setOpacity(None, log=False)
            annular4.setContrast(cont, log=False)
            annular4.setLineWidth(1.0, log=False)
        
        # if annular4 is stopping this frame...
        if annular4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular4.tStop = t  # not accounting for scr refresh
                annular4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular4.stopped')
                # update status
                annular4.status = FINISHED
                annular4.setAutoDraw(False)

        # *annular5* updates
        
        # if annular5 is starting this frame...
        if annular5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular5.frameNStart = frameN  # exact frame index
            annular5.tStart = t  # local t and not account for scr refresh
            annular5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular5.started')
            # update status
            annular5.status = STARTED
            annular5.setAutoDraw(True)
        
        # if annular5 is active this frame...
        if annular5.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular5.setOpacity(None, log=False)
            annular5.setContrast(cont, log=False)
            annular5.setLineWidth(1.0, log=False)
        
        # if annular5 is stopping this frame...
        if annular5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular5.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular5.tStop = t  # not accounting for scr refresh
                annular5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular5.stopped')
                # update status
                annular5.status = FINISHED
                annular5.setAutoDraw(False)

        # *annular6* updates
        
        # if annular6 is starting this frame...
        if annular6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular6.frameNStart = frameN  # exact frame index
            annular6.tStart = t  # local t and not account for scr refresh
            annular6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular6.started')
            # update status
            annular6.status = STARTED
            annular6.setAutoDraw(True)
        
        # if annular6 is active this frame...
        if annular6.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular6.setOpacity(None, log=False)
            annular6.setContrast(cont, log=False)
            annular6.setLineWidth(1.0, log=False)
        
        # if annular6 is stopping this frame...
        if annular6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular6.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular6.tStop = t  # not accounting for scr refresh
                annular6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular6.stopped')
                # update status
                annular6.status = FINISHED
                annular6.setAutoDraw(False)

        # *annular7* updates
        
        # if annular7 is starting this frame...
        if annular7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular7.frameNStart = frameN  # exact frame index
            annular7.tStart = t  # local t and not account for scr refresh
            annular7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular7.started')
            # update status
            annular7.status = STARTED
            annular7.setAutoDraw(True)
        
        # if annular7 is active this frame...
        if annular7.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular7.setOpacity(None, log=False)
            annular7.setContrast(cont, log=False)
            annular7.setLineWidth(1.0, log=False)
        
        # if annular7 is stopping this frame...
        if annular7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular7.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular7.tStop = t  # not accounting for scr refresh
                annular7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular7.stopped')
                # update status
                annular7.status = FINISHED
                annular7.setAutoDraw(False)

        # *annular8* updates
        
        # if annular8 is starting this frame...
        if annular8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular8.frameNStart = frameN  # exact frame index
            annular8.tStart = t  # local t and not account for scr refresh
            annular8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular8.started')
            # update status
            annular8.status = STARTED
            annular8.setAutoDraw(True)
        
        # if annular8 is active this frame...
        if annular8.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular8.setOpacity(None, log=False)
            annular8.setContrast(cont, log=False)
            annular8.setLineWidth(1.0, log=False)
        
        # if annular8 is stopping this frame...
        if annular8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular8.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular8.tStop = t  # not accounting for scr refresh
                annular8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular8.stopped')
                # update status
                annular8.status = FINISHED
                annular8.setAutoDraw(False)

        # *annular9* updates
        
        # if annular9 is starting this frame...
        if annular9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular9.frameNStart = frameN  # exact frame index
            annular9.tStart = t  # local t and not account for scr refresh
            annular9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular9.started')
            # update status
            annular9.status = STARTED
            annular9.setAutoDraw(True)
        
        # if annular9 is active this frame...
        if annular9.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular9.setOpacity(None, log=False)
            annular9.setContrast(cont, log=False)
            annular9.setLineWidth(1.0, log=False)
        
        # if annular9 is stopping this frame...
        if annular9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular9.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular9.tStop = t  # not accounting for scr refresh
                annular9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular9.stopped')
                # update status
                annular9.status = FINISHED
                annular9.setAutoDraw(False)

        # *annular10* updates
        
        # if annular10 is starting this frame...
        if annular10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular10.frameNStart = frameN  # exact frame index
            annular10.tStart = t  # local t and not account for scr refresh
            annular10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular10.started')
            # update status
            annular10.status = STARTED
            annular10.setAutoDraw(True)
        
        # if annular10 is active this frame...
        if annular10.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular10.setOpacity(None, log=False)
            annular10.setContrast(cont, log=False)
            annular10.setLineWidth(1.0, log=False)
        
        # if annular10 is stopping this frame...
        if annular10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular10.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular10.tStop = t  # not accounting for scr refresh
                annular10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular10.stopped')
                # update status
                annular10.status = FINISHED
                annular10.setAutoDraw(False)

        # *annular11* updates
        
        # if annular11 is starting this frame...
        if annular11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular11.frameNStart = frameN  # exact frame index
            annular11.tStart = t  # local t and not account for scr refresh
            annular11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular11.started')
            # update status
            annular11.status = STARTED
            annular11.setAutoDraw(True)
        
        # if annular11 is active this frame...
        if annular11.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular11.setOpacity(None, log=False)
            annular11.setContrast(cont, log=False)
            annular11.setLineWidth(1.0, log=False)
        
        # if annular11 is stopping this frame...
        if annular11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular11.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular11.tStop = t  # not accounting for scr refresh
                annular11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular11.stopped')
                # update status
                annular11.status = FINISHED
                annular11.setAutoDraw(False)

        # *annular12* updates
        
        # if annular12 is starting this frame...
        if annular12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular12.frameNStart = frameN  # exact frame index
            annular12.tStart = t  # local t and not account for scr refresh
            annular12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular12.started')
            # update status
            annular12.status = STARTED
            annular12.setAutoDraw(True)
        
        # if annular12 is active this frame...
        if annular12.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular12.setOpacity(None, log=False)
            annular12.setContrast(cont, log=False)
            annular12.setLineWidth(1.0, log=False)
        
        # if annular12 is stopping this frame...
        if annular12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular12.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular12.tStop = t  # not accounting for scr refresh
                annular12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular12.stopped')
                # update status
                annular12.status = FINISHED
                annular12.setAutoDraw(False)

        # *annular13* updates
        
        # if annular13 is starting this frame...
        if annular13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular13.frameNStart = frameN  # exact frame index
            annular13.tStart = t  # local t and not account for scr refresh
            annular13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular13.started')
            # update status
            annular13.status = STARTED
            annular13.setAutoDraw(True)
        
        # if annular13 is active this frame...
        if annular13.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular13.setOpacity(None, log=False)
            annular13.setContrast(cont, log=False)
            annular13.setLineWidth(1.0, log=False)
        
        # if annular13 is stopping this frame...
        if annular13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular13.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular13.tStop = t  # not accounting for scr refresh
                annular13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular13.stopped')
                # update status
                annular13.status = FINISHED
                annular13.setAutoDraw(False)

        # *annular14* updates
        
        # if annular14 is starting this frame...
        if annular14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular14.frameNStart = frameN  # exact frame index
            annular14.tStart = t  # local t and not account for scr refresh
            annular14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular14.started')
            # update status
            annular14.status = STARTED
            annular14.setAutoDraw(True)
        
        # if annular14 is active this frame...
        if annular14.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular14.setOpacity(None, log=False)
            annular14.setContrast(cont, log=False)
            annular14.setLineWidth(1.0, log=False)
        
        # if annular14 is stopping this frame...
        if annular14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular14.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular14.tStop = t  # not accounting for scr refresh
                annular14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular14.stopped')
                # update status
                annular14.status = FINISHED
                annular14.setAutoDraw(False)

        # *annular15* updates
        
        # if annular15 is starting this frame...
        if annular15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular15.frameNStart = frameN  # exact frame index
            annular15.tStart = t  # local t and not account for scr refresh
            annular15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular15.started')
            # update status
            annular15.status = STARTED
            annular15.setAutoDraw(True)
        
        # if annular15 is active this frame...
        if annular15.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular15.setOpacity(None, log=False)
            annular15.setContrast(cont, log=False)
            annular15.setLineWidth(1.0, log=False)
        
        # if annular15 is stopping this frame...
        if annular15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular15.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular15.tStop = t  # not accounting for scr refresh
                annular15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular15.stopped')
                # update status
                annular15.status = FINISHED
                annular15.setAutoDraw(False)

        # *annular16* updates
        
        # if annular16 is starting this frame...
        if annular16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annular16.frameNStart = frameN  # exact frame index
            annular16.tStart = t  # local t and not account for scr refresh
            annular16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annular16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'annular16.started')
            # update status
            annular16.status = STARTED
            annular16.setAutoDraw(True)
        
        # if annular16 is active this frame...
        if annular16.status == STARTED:
            if 0<t<=1.6:
                cont=(-0.1875)*t+0.65
            elif 1.6<t<=2.4:
                cont=0.375*t-0.25
            else:
                cont=0.65
            # update params
            annular16.setOpacity(None, log=False)
            annular16.setContrast(cont, log=False)
            annular16.setLineWidth(1.0, log=False)
        
        # if annular16 is stopping this frame...
        if annular16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > annular16.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                annular16.tStop = t  # not accounting for scr refresh
                annular16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'annular16.stopped')
                # update status
                annular16.status = FINISHED
                annular16.setAutoDraw(False)
        
        
        # *cover1* updates
        
        # if cover1 is starting this frame...
        if cover1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cover1.frameNStart = frameN  # exact frame index
            cover1.tStart = t  # local t and not account for scr refresh
            cover1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cover1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cover1.started')
            # update status
            cover1.status = STARTED
            cover1.setAutoDraw(True)
        
        # if cover1 is active this frame...
        if cover1.status == STARTED:
            # update params
            opci=0.5+0.5*np.sin(2*np.pi*t*21.25)
            # update params
            cover1.setOpacity(opci, log=False)
            cover1.setContrast(0.0, log=False)
            cover1.setLineWidth(1.0, log=False)
        
        # if cover1 is stopping this frame...
        if cover1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cover1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                cover1.tStop = t  # not accounting for scr refresh
                cover1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover1.stopped')
                # update status
                cover1.status = FINISHED
                cover1.setAutoDraw(False)
        
        # *center1* updates
        
        # if center1 is starting this frame...
        if center1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            center1.frameNStart = frameN  # exact frame index
            center1.tStart = t  # local t and not account for scr refresh
            center1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(center1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'center1.started')
            # update status
            center1.status = STARTED
            center1.setAutoDraw(True)
        
        # if center1 is active this frame...
        if center1.status == STARTED:
            # update params
            pass
        
        # if center1 is stopping this frame...
        if center1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > center1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                center1.tStop = t  # not accounting for scr refresh
                center1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'center1.stopped')
                # update status
                center1.status = FINISHED
                center1.setAutoDraw(False)
        
        # *bg1* updates
        
        # if bg1 is starting this frame...
        if bg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bg1.frameNStart = frameN  # exact frame index
            bg1.tStart = t  # local t and not account for scr refresh
            bg1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bg1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bg1.started')
            # update status
            bg1.status = STARTED
            bg1.setAutoDraw(True)
        
        # if bg1 is active this frame...
        if bg1.status == STARTED:
            # update params
            #pass
            # update params
            bg1.setOpacity(None, log=False)
            bg1.setContrast(1.0, log=False)
            bg1.setLineWidth(1.0, log=False)
        
        # if bg1 is stopping this frame...
        if bg1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bg1.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                bg1.tStop = t  # not accounting for scr refresh
                bg1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg1.stopped')
                # update status
                bg1.status = FINISHED
                bg1.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_4 is stopping this frame...
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + asec-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                # update status
                key_resp_4.status = FINISHED
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                a= len(key_resp_4.keys)
                key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                b= len(key_resp_4.keys)
                if b-a==1:
                    responses_marker(2)
                key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                # a response ends the routine
                continueRoutine = True
        # *stimulus1* updates
        
        # if stimulus1 is starting this frame...
        if stimulus1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus1.frameNStart = frameN  # exact frame index
            stimulus1.tStart = t  # local t and not account for scr refresh
            stimulus1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimulus1.started')
            # update status
            stimulus1.status = STARTED
            stimulus1.status = STARTED
            win.callOnFlip(stimulus1.setData, int(1))
        
        # if stimulus1 is stopping this frame...
        if stimulus1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus1.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                stimulus1.tStop = t  # not accounting for scr refresh
                stimulus1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus1.stopped')
                # update status
                stimulus1.status = FINISHED
                win.callOnFlip(stimulus1.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GTDT2_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GTDT2_1" ---
    for thisComponent in GTDT2_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials_6.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_6.addData('key_resp_4.rt', key_resp_4.rt)
    if stimulus1.status == STARTED:
        win.callOnFlip(stimulus1.setData, int(0))
    # the Routine "GTDT2_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_6'


# --- Prepare to start Routine "rest6" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
rest6Components = [instruction5, key_resp_13, bend6]
for thisComponent in rest6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "rest6" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction5* updates
    
    # if instruction5 is starting this frame...
    if instruction5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction5.frameNStart = frameN  # exact frame index
        instruction5.tStart = t  # local t and not account for scr refresh
        instruction5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction5.started')
        # update status
        instruction5.status = STARTED
        instruction5.setAutoDraw(True)
    
    # if instruction5 is active this frame...
    if instruction5.status == STARTED:
        # update params
        pass
    
    # *key_resp_13* updates
    waitOnFlip = False
    
    # if key_resp_13 is starting this frame...
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_13.started')
        # update status
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *bend6* updates
    
    # if bend6 is starting this frame...
    if bend6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bend6.frameNStart = frameN  # exact frame index
        bend6.tStart = t  # local t and not account for scr refresh
        bend6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bend6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bend6.started')
        # update status
        bend6.status = STARTED
        bend6.status = STARTED
        win.callOnFlip(bend6.setData, int(6))
    
    # if bend6 is stopping this frame...
    if bend6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bend6.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            bend6.tStop = t  # not accounting for scr refresh
            bend6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bend6.stopped')
            # update status
            bend6.status = FINISHED
            win.callOnFlip(bend6.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rest6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rest6" ---
for thisComponent in rest6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
if bend6.status == STARTED:
    win.callOnFlip(bend6.setData, int(0))
# the Routine "rest6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
