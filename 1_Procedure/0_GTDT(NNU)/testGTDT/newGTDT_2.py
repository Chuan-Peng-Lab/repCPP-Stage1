#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on 六月 07, 2023, at 15:31
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'newGTDT'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
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
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Desktop\\NewGTDT\\newGTDT.py',
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
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
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

# --- Initialize components for Routine "instruction" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='D:/Desktop/GT/instruction1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction2" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='instruction2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction3" ---
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='instruction3C1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation" ---
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
p_port = parallel.ParallelPort(address='0x5FB8')

# --- Initialize components for Routine "trial" ---
background = visual.Rect(
    win=win, name='background',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=False)
annular = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular2 = visual.Pie(
    win=win, name='annular2',start=22.5, end=45,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular3 = visual.Pie(
    win=win, name='annular3',start=45, end=67.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular4 = visual.Pie(
    win=win, name='annular4',start=67.5, end=90,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular5 = visual.Pie(
    win=win, name='annular5',start=90,end=112.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular6 = visual.Pie(
    win=win, name='annular6',start=112.5,end=135,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular7 = visual.Pie(
    win=win, name='annular7',start=135,end=157.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular8 = visual.Pie(
    win=win, name='annular8',start=157.5,end=180,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular9 = visual.Pie(
    win=win, name='annular9',start=180,end=202.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular10 = visual.Pie(
    win=win, name='annular10',start=202.5,end=225,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular11 = visual.Pie(
    win=win, name='annular9',start=225,end=247.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular12 = visual.Pie(
    win=win, name='annular12',start=247.5,end=270,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular13 = visual.Pie(
    win=win, name='annular9',start=270,end=292.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular14 = visual.Pie(
    win=win, name='annular14',start=292.5,end=315,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular15 = visual.Pie(
    win=win, name='annular15',start=315,end=337.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
annular16 = visual.Pie(
    win=win, name='annular16',start=337.5,end=360,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
cover = visual.ShapeStim(
    win=win, name='cover',
    size=(0.5, 0.5), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=False)
center = visual.ShapeStim(
    win=win, name='center',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=False)
press = keyboard.Keyboard()
stimulus = parallel.ParallelPort(address='0x5FB8')
response = parallel.ParallelPort(address='0x5FB8')
wrong1 = keyboard.Keyboard()

# --- Initialize components for Routine "duration" ---
dbackground = visual.Rect(
    win=win, name='dbackground',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=False)
dannular = visual.Pie(
    win=win, name='dannular',start=0, end=22.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular2 = visual.Pie(
    win=win, name='dannular2',start=22.5, end=45,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular3 = visual.Pie(
    win=win, name='dannular3',start=45, end=67.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular4 = visual.Pie(
    win=win, name='dannular4',start=67.5, end=90,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular5 = visual.Pie(
    win=win, name='dannular5',start=90,end=112.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular6 = visual.Pie(
    win=win, name='dannular6',start=112.5,end=135,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular7 = visual.Pie(
    win=win, name='dannular7',start=135,end=157.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular8 = visual.Pie(
    win=win, name='dannular8',start=157.5,end=180,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular9 = visual.Pie(
    win=win, name='dannular9',start=180,end=202.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular10 = visual.Pie(
    win=win, name='dannular10',start=202.5,end=225,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular11 = visual.Pie(
    win=win, name='dannular9',start=225,end=247.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular12 = visual.Pie(
    win=win, name='dannular12',start=247.5,end=270,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular13 = visual.Pie(
    win=win, name='dannular9',start=270,end=292.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular14 = visual.Pie(
    win=win, name='dannular14',start=292.5,end=315,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular15 = visual.Pie(
    win=win, name='dannular15',start=315,end=337.5,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgrey', fillColor='lightgrey',
    opacity=None, depth=-1.0, interpolate=False)
dannular16 = visual.Pie(
    win=win, name='dannular16',start=337.5,end=360,radius=0.25,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='darkgrey', fillColor='darkgrey',
    opacity=None, depth=-1.0, interpolate=False)
dcover = visual.ShapeStim(
    win=win, name='dcover',
    size=(0.5, 0.5), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=False)
dcenter = visual.ShapeStim(
    win=win, name='dcenter',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=False)
wrong2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruction" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionComponents = [image, key_resp]
for thisComponent in instructionComponents:
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

# --- Run Routine "instruction" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    
    # if image is starting this frame...
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image.started')
        # update status
        image.status = STARTED
        image.setAutoDraw(True)
    
    # if image is active this frame...
    if image.status == STARTED:
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
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction" ---
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instruction2Components = [image_2, key_resp_2]
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
    
    # *image_2* updates
    
    # if image_2 is starting this frame...
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_2.started')
        # update status
        image_2.status = STARTED
        image_2.setAutoDraw(True)
    
    # if image_2 is active this frame...
    if image_2.status == STARTED:
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
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction3Components = [image_3, key_resp_3]
for thisComponent in instruction3Components:
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

# --- Run Routine "instruction3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    
    # if image_3 is starting this frame...
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3.started')
        # update status
        image_3.status = STARTED
        image_3.setAutoDraw(True)
    
    # if image_3 is active this frame...
    if image_3.status == STARTED:
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
    for thisComponent in instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction3" ---
for thisComponent in instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blockList.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [text, p_port]
    for thisComponent in fixationComponents:
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
    
    # --- Run Routine "fixation" ---
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
        # *p_port* updates
        
        # if p_port is starting this frame...
        if p_port.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port.frameNStart = frameN  # exact frame index
            p_port.tStart = t  # local t and not account for scr refresh
            p_port.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port.started', t)
            # update status
            p_port.status = STARTED
            p_port.status = STARTED
            win.callOnFlip(p_port.setData, int(bmarker))
        
        # if p_port is stopping this frame...
        if p_port.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port.tStop = t  # not accounting for scr refresh
                p_port.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port.stopped', t)
                # update status
                p_port.status = FINISHED
                win.callOnFlip(p_port.setData, int())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port.status == STARTED:
        win.callOnFlip(p_port.setData, int())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialList.xlsx'),
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
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        press.keys = []
        press.rt = []
        _press_allKeys = []
        wrong1.keys = []
        wrong1.rt = []
        _wrong1_allKeys = []
        # keep track of which components have finished
        trialComponents = [background, annular, annular2, annular3,annular4,
        annular5,annular6,annular7,annular8,annular9,annular10,annular11,annular12,
        annular13,annular14,annular15,annular16, cover, center, press, stimulus, response, wrong1]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.4000000000000004:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background* updates
            
            # if background is starting this frame...
            if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background.frameNStart = frameN  # exact frame index
                background.tStart = t  # local t and not account for scr refresh
                background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background.started')
                # update status
                background.status = STARTED
                background.setAutoDraw(True)
            
            # if background is active this frame...
            if background.status == STARTED:
                # update params
                background.setOpacity(None, log=False)
                background.setContrast(1.0, log=False)
                background.setLineWidth(1.0, log=False)
            
            # if background is stopping this frame...
            if background.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > background.tStartRefresh + 2.4-frameTolerance:
                    # keep track of stop time/frame for later
                    background.tStop = t  # not accounting for scr refresh
                    background.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'background.stopped')
                    # update status
                    background.status = FINISHED
                    background.setAutoDraw(False)
            
            # *annular* updates
            
            # if annular is starting this frame...
            if annular.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular.setOpacity(None, log=False)
                annular.setContrast(cont, log=False)
                annular.setLineWidth(1.0, log=False)
            
            # if annular is stopping this frame...
            if annular.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular2.setOpacity(None, log=False)
                annular2.setContrast(cont, log=False)
                annular2.setLineWidth(1.0, log=False)
            
            # if annular2 is stopping this frame...
            if annular2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular2.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular3.setOpacity(None, log=False)
                annular3.setContrast(cont, log=False)
                annular3.setLineWidth(1.0, log=False)
            
            # if annular3 is stopping this frame...
            if annular3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular3.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular4.setOpacity(None, log=False)
                annular4.setContrast(cont, log=False)
                annular4.setLineWidth(1.0, log=False)
            
            # if annular4 is stopping this frame...
            if annular4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular4.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular5.setOpacity(None, log=False)
                annular5.setContrast(cont, log=False)
                annular5.setLineWidth(1.0, log=False)
            
            # if annular5 is stopping this frame...
            if annular5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular5.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular6.setOpacity(None, log=False)
                annular6.setContrast(cont, log=False)
                annular6.setLineWidth(1.0, log=False)
            
            # if annular6 is stopping this frame...
            if annular6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular6.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular7.setOpacity(None, log=False)
                annular7.setContrast(cont, log=False)
                annular7.setLineWidth(1.0, log=False)
            
            # if annular7 is stopping this frame...
            if annular7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular7.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular8.setOpacity(None, log=False)
                annular8.setContrast(cont, log=False)
                annular8.setLineWidth(1.0, log=False)
            
            # if annular8 is stopping this frame...
            if annular8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular8.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular9.setOpacity(None, log=False)
                annular9.setContrast(cont, log=False)
                annular9.setLineWidth(1.0, log=False)
            
            # if annular9 is stopping this frame...
            if annular9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular9.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular10.setOpacity(None, log=False)
                annular10.setContrast(cont, log=False)
                annular10.setLineWidth(1.0, log=False)
            
            # if annular10 is stopping this frame...
            if annular10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular10.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular11.setOpacity(None, log=False)
                annular11.setContrast(cont, log=False)
                annular11.setLineWidth(1.0, log=False)
            
            # if annular11 is stopping this frame...
            if annular11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular11.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular12.setOpacity(None, log=False)
                annular12.setContrast(cont, log=False)
                annular12.setLineWidth(1.0, log=False)
            
            # if annular12 is stopping this frame...
            if annular12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular12.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular13.setOpacity(None, log=False)
                annular13.setContrast(cont, log=False)
                annular13.setLineWidth(1.0, log=False)
            
            # if annular13 is stopping this frame...
            if annular13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular13.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular14.setOpacity(None, log=False)
                annular14.setContrast(cont, log=False)
                annular14.setLineWidth(1.0, log=False)
            
            # if annular14 is stopping this frame...
            if annular14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular14.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular15.setOpacity(None, log=False)
                annular15.setContrast(cont, log=False)
                annular15.setLineWidth(1.0, log=False)
            
            # if annular15 is stopping this frame...
            if annular15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular15.tStartRefresh + 2.4-frameTolerance:
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
                else:
                    cont=0.375*t-0.25
                # update params
                annular16.setOpacity(None, log=False)
                annular16.setContrast(cont, log=False)
                annular16.setLineWidth(1.0, log=False)
            
            # if annular16 is stopping this frame...
            if annular16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > annular16.tStartRefresh + 2.4-frameTolerance:
                    # keep track of stop time/frame for later
                    annular16.tStop = t  # not accounting for scr refresh
                    annular16.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'annular16.stopped')
                    # update status
                    annular16.status = FINISHED
                    annular16.setAutoDraw(False)

            # *cover* updates
            
            # if cover is starting this frame...
            if cover.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cover.frameNStart = frameN  # exact frame index
                cover.tStart = t  # local t and not account for scr refresh
                cover.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cover, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cover.started')
                # update status
                cover.status = STARTED
                cover.setAutoDraw(True)
            
            # if cover is active this frame...
            if cover.status == STARTED:
                opci=0.5+0.5*np.sin(2*np.pi*t*22)
                # update params
                cover.setOpacity(opci, log=False)
                cover.setContrast(0.0, log=False)
                cover.setLineWidth(1.0, log=False)
            
            # if cover is stopping this frame...
            if cover.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cover.tStartRefresh + 2.4-frameTolerance:
                    # keep track of stop time/frame for later
                    cover.tStop = t  # not accounting for scr refresh
                    cover.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cover.stopped')
                    # update status
                    cover.status = FINISHED
                    cover.setAutoDraw(False)
            
            # *center* updates
            
            # if center is starting this frame...
            if center.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                center.frameNStart = frameN  # exact frame index
                center.tStart = t  # local t and not account for scr refresh
                center.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(center, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'center.started')
                # update status
                center.status = STARTED
                center.setAutoDraw(True)
            
            # if center is active this frame...
            if center.status == STARTED:
                # update params
                pass
            
            # if center is stopping this frame...
            if center.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > center.tStartRefresh + 2.4-frameTolerance:
                    # keep track of stop time/frame for later
                    center.tStop = t  # not accounting for scr refresh
                    center.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'center.stopped')
                    # update status
                    center.status = FINISHED
                    center.setAutoDraw(False)
            
            # *press* updates
            waitOnFlip = False
            
            # if press is starting this frame...
            if press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press.frameNStart = frameN  # exact frame index
                press.tStart = t  # local t and not account for scr refresh
                press.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'press.started')
                # update status
                press.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(press.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(press.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if press is stopping this frame...
            if press.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > press.tStartRefresh + 1.6-frameTolerance:
                    # keep track of stop time/frame for later
                    press.tStop = t  # not accounting for scr refresh
                    press.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'press.stopped')
                    # update status
                    press.status = FINISHED
                    press.status = FINISHED
            if press.status == STARTED and not waitOnFlip:
                theseKeys = press.getKeys(keyList=['space'], waitRelease=False)
                _press_allKeys.extend(theseKeys)
                if len(_press_allKeys):
                    press.keys = _press_allKeys[0].name  # just the first key pressed
                    press.rt = _press_allKeys[0].rt
                                # *response* updates
            # if response is starting this frame...
                    if response.status == NOT_STARTED and t >= press.rt-frameTolerance:
                # keep track of start time/frame for later
                        response.frameNStart = frameN  # exact frame index
                        response.tStart = t  # local t and not account for scr refresh
                        response.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                        thisExp.addData('response.started', t)
                # update status
                        response.status = STARTED
                        response.status = STARTED
                        win.callOnFlip(response.setData, int(2))
            # if response is stopping this frame...
                    if response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > response.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                            response.tStop = t  # not accounting for scr refresh
                            response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                            thisExp.addData('response.stopped', t)
                    # update status
                            response.status = FINISHED
                            win.callOnFlip(response.setData, int())
                    # a response ends the routine
                    continueRoutine = True#False
            # *stimulus* updates
            
            # if stimulus is starting this frame...
            if stimulus.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('stimulus.started', t)
                # update status
                stimulus.status = STARTED
                stimulus.status = STARTED
                win.callOnFlip(stimulus.setData, int(1))
            
            # if stimulus is stopping this frame...
            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulus.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    stimulus.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('stimulus.stopped', t)
                    # update status
                    stimulus.status = FINISHED
                    win.callOnFlip(stimulus.setData, int())
            
            # *wrong1* updates
            waitOnFlip = False
            
            # if wrong1 is starting this frame...
            if wrong1.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                wrong1.frameNStart = frameN  # exact frame index
                wrong1.tStart = t  # local t and not account for scr refresh
                wrong1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wrong1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wrong1.started')
                # update status
                wrong1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wrong1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wrong1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if wrong1 is stopping this frame...
            if wrong1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wrong1.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    wrong1.tStop = t  # not accounting for scr refresh
                    wrong1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wrong1.stopped')
                    # update status
                    wrong1.status = FINISHED
                    wrong1.status = FINISHED
            if wrong1.status == STARTED and not waitOnFlip:
                theseKeys = wrong1.getKeys(keyList=['space'], waitRelease=False)
                _wrong1_allKeys.extend(theseKeys)
                if len(_wrong1_allKeys):
                    wrong1.keys = [key.name for key in _wrong1_allKeys]  # storing all keys
                    wrong1.rt = [key.rt for key in _wrong1_allKeys]
                    # a response ends the routine
                    continueRoutine = True#False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if press.keys in ['', [], None]:  # No response was made
            press.keys = None
        trials.addData('press.keys',press.keys)
        if press.keys != None:  # we had a response
            trials.addData('press.rt', press.rt)
        if stimulus.status == STARTED:
            win.callOnFlip(stimulus.setData, int())
        if response.status == STARTED:
            win.callOnFlip(response.setData, int())
        # check responses
        if wrong1.keys in ['', [], None]:  # No response was made
            wrong1.keys = None
        trials.addData('wrong1.keys',wrong1.keys)
        if wrong1.keys != None:  # we had a response
            trials.addData('wrong1.rt', wrong1.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.400000)
        
        # --- Prepare to start Routine "duration" ---
        continueRoutine = True
        # update component parameters for each repeat
        wrong2.keys = []
        wrong2.rt = []
        _wrong2_allKeys = []
        # keep track of which components have finished
        durationComponents = [dbackground, dannular, dannular2, dannular3,dannular4,
        dannular5,dannular6,dannular7,dannular8,dannular9,dannular10,dannular11,dannular12,
        dannular13,dannular14,dannular15,dannular16,dcover, dcenter, wrong2]
        for thisComponent in durationComponents:
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
        
        # --- Run Routine "duration" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *dbackground* updates
            
            # if dbackground is starting this frame...
            if dbackground.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dbackground.frameNStart = frameN  # exact frame index
                dbackground.tStart = t  # local t and not account for scr refresh
                dbackground.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dbackground, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dbackground.started')
                # update status
                dbackground.status = STARTED
                dbackground.setAutoDraw(True)
            
            # if dbackground is active this frame...
            if dbackground.status == STARTED:
                # update params
                dbackground.setOpacity(None, log=False)
                dbackground.setContrast(1.0, log=False)
                dbackground.setLineWidth(1.0, log=False)
            
            # if dbackground is stopping this frame...
            if dbackground.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dbackground.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dbackground.tStop = t  # not accounting for scr refresh
                    dbackground.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dbackground.stopped')
                    # update status
                    dbackground.status = FINISHED
                    dbackground.setAutoDraw(False)
            
            # *dannular* updates
            
            # if dannular is starting this frame...
            if dannular.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular.frameNStart = frameN  # exact frame index
                dannular.tStart = t  # local t and not account for scr refresh
                dannular.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular.started')
                # update status
                dannular.status = STARTED
                dannular.setAutoDraw(True)
            
            # if dannular is active this frame...
            if dannular.status == STARTED:
                # update params
                dannular.setOpacity(None, log=False)
                dannular.setContrast(0.65, log=False)
                dannular.setLineWidth(1.0, log=False)
            
            # if dannular is stopping this frame...
            if dannular.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular.tStop = t  # not accounting for scr refresh
                    dannular.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular.stopped')
                    # update status
                    dannular.status = FINISHED
                    dannular.setAutoDraw(False)

            # *dannular2* updates
            
            # if dannular2 is starting this frame...
            if dannular2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular2.frameNStart = frameN  # exact frame index
                dannular2.tStart = t  # local t and not account for scr refresh
                dannular2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular2.started')
                # update status
                dannular2.status = STARTED
                dannular2.setAutoDraw(True)
            
            # if dannular2 is active this frame...
            if dannular2.status == STARTED:
                # update params
                dannular2.setOpacity(None, log=False)
                dannular2.setContrast(0.65, log=False)
                dannular2.setLineWidth(1.0, log=False)
            
            # if dannular2 is stopping this frame...
            if dannular2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular2.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular2.tStop = t  # not accounting for scr refresh
                    dannular2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular2.stopped')
                    # update status
                    dannular2.status = FINISHED
                    dannular2.setAutoDraw(False)

            # *dannular3* updates
            
            # if dannular3 is starting this frame...
            if dannular3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular3.frameNStart = frameN  # exact frame index
                dannular3.tStart = t  # local t and not account for scr refresh
                dannular3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular3.started')
                # update status
                dannular3.status = STARTED
                dannular3.setAutoDraw(True)
            
            # if dannular3 is active this frame...
            if dannular3.status == STARTED:
                # update params
                dannular3.setOpacity(None, log=False)
                dannular3.setContrast(0.65, log=False)
                dannular3.setLineWidth(1.0, log=False)
            
            # if dannular3 is stopping this frame...
            if dannular3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular3.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular3.tStop = t  # not accounting for scr refresh
                    dannular3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular3.stopped')
                    # update status
                    dannular3.status = FINISHED
                    dannular3.setAutoDraw(False)

            # *dannular4* updates
            
            # if dannular4 is starting this frame...
            if dannular4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular4.frameNStart = frameN  # exact frame index
                dannular4.tStart = t  # local t and not account for scr refresh
                dannular4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular4.started')
                # update status
                dannular4.status = STARTED
                dannular4.setAutoDraw(True)
            
            # if dannular4 is active this frame...
            if dannular4.status == STARTED:
                # update params
                dannular4.setOpacity(None, log=False)
                dannular4.setContrast(0.65, log=False)
                dannular4.setLineWidth(1.0, log=False)
            
            # if dannular4 is stopping this frame...
            if dannular4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular4.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular4.tStop = t  # not accounting for scr refresh
                    dannular4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular4.stopped')
                    # update status
                    dannular4.status = FINISHED
                    dannular4.setAutoDraw(False)

            # *dannular5* updates
            
            # if dannular5 is starting this frame...
            if dannular5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular5.frameNStart = frameN  # exact frame index
                dannular5.tStart = t  # local t and not account for scr refresh
                dannular5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular5.started')
                # update status
                dannular5.status = STARTED
                dannular5.setAutoDraw(True)
            
            # if dannular5 is active this frame...
            if dannular5.status == STARTED:
                # update params
                dannular5.setOpacity(None, log=False)
                dannular5.setContrast(0.65, log=False)
                dannular5.setLineWidth(1.0, log=False)
            
            # if dannular5 is stopping this frame...
            if dannular5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular5.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular5.tStop = t  # not accounting for scr refresh
                    dannular5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular5.stopped')
                    # update status
                    dannular5.status = FINISHED
                    dannular5.setAutoDraw(False)

            # *dannular6* updates
            
            # if dannular6 is starting this frame...
            if dannular6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular6.frameNStart = frameN  # exact frame index
                dannular6.tStart = t  # local t and not account for scr refresh
                dannular6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular6.started')
                # update status
                dannular6.status = STARTED
                dannular6.setAutoDraw(True)
            
            # if dannular6 is active this frame...
            if dannular6.status == STARTED:
                # update params
                dannular6.setOpacity(None, log=False)
                dannular6.setContrast(0.65, log=False)
                dannular6.setLineWidth(1.0, log=False)
            
            # if dannular6 is stopping this frame...
            if dannular6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular6.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular6.tStop = t  # not accounting for scr refresh
                    dannular6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular6.stopped')
                    # update status
                    dannular6.status = FINISHED
                    dannular6.setAutoDraw(False)

            # *dannular7* updates
            
            # if dannular7 is starting this frame...
            if dannular7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular7.frameNStart = frameN  # exact frame index
                dannular7.tStart = t  # local t and not account for scr refresh
                dannular7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular7.started')
                # update status
                dannular7.status = STARTED
                dannular7.setAutoDraw(True)
            
            # if dannular7 is active this frame...
            if dannular7.status == STARTED:
                # update params
                dannular7.setOpacity(None, log=False)
                dannular7.setContrast(0.65, log=False)
                dannular7.setLineWidth(1.0, log=False)
            
            # if dannular7 is stopping this frame...
            if dannular7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular7.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular7.tStop = t  # not accounting for scr refresh
                    dannular7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular7.stopped')
                    # update status
                    dannular7.status = FINISHED
                    dannular7.setAutoDraw(False)

            # *dannular8* updates
            
            # if dannular8 is starting this frame...
            if dannular8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular8.frameNStart = frameN  # exact frame index
                dannular8.tStart = t  # local t and not account for scr refresh
                dannular8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular8.started')
                # update status
                dannular8.status = STARTED
                dannular8.setAutoDraw(True)
            
            # if dannular8 is active this frame...
            if dannular8.status == STARTED:
                # update params
                dannular8.setOpacity(None, log=False)
                dannular8.setContrast(0.65, log=False)
                dannular8.setLineWidth(1.0, log=False)
            
            # if dannular8 is stopping this frame...
            if dannular8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular8.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular8.tStop = t  # not accounting for scr refresh
                    dannular8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular8.stopped')
                    # update status
                    dannular8.status = FINISHED
                    dannular8.setAutoDraw(False)

            # *dannular9* updates
            
            # if dannular9 is starting this frame...
            if dannular9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular9.frameNStart = frameN  # exact frame index
                dannular9.tStart = t  # local t and not account for scr refresh
                dannular9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular9.started')
                # update status
                dannular9.status = STARTED
                dannular9.setAutoDraw(True)
            
            # if dannular9 is active this frame...
            if dannular9.status == STARTED:
                # update params
                dannular9.setOpacity(None, log=False)
                dannular9.setContrast(0.65, log=False)
                dannular9.setLineWidth(1.0, log=False)
            
            # if dannular9 is stopping this frame...
            if dannular9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular9.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular9.tStop = t  # not accounting for scr refresh
                    dannular9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular9.stopped')
                    # update status
                    dannular9.status = FINISHED
                    dannular9.setAutoDraw(False)

            # *dannular10* updates
            
            # if dannular10 is starting this frame...
            if dannular10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular10.frameNStart = frameN  # exact frame index
                dannular10.tStart = t  # local t and not account for scr refresh
                dannular10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular10.started')
                # update status
                dannular10.status = STARTED
                dannular10.setAutoDraw(True)
            
            # if dannular10 is active this frame...
            if dannular10.status == STARTED:
                # update params
                dannular10.setOpacity(None, log=False)
                dannular10.setContrast(0.65, log=False)
                dannular10.setLineWidth(1.0, log=False)
            
            # if dannular10 is stopping this frame...
            if dannular10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular10.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular10.tStop = t  # not accounting for scr refresh
                    dannular10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular10.stopped')
                    # update status
                    dannular10.status = FINISHED
                    dannular10.setAutoDraw(False)

            # *dannular11* updates
            
            # if dannular11 is starting this frame...
            if dannular11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular11.frameNStart = frameN  # exact frame index
                dannular11.tStart = t  # local t and not account for scr refresh
                dannular11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular11.started')
                # update status
                dannular11.status = STARTED
                dannular11.setAutoDraw(True)
            
            # if dannular11 is active this frame...
            if dannular11.status == STARTED:
                # update params
                dannular11.setOpacity(None, log=False)
                dannular11.setContrast(0.65, log=False)
                dannular11.setLineWidth(1.0, log=False)
            
            # if dannular11 is stopping this frame...
            if dannular11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular11.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular11.tStop = t  # not accounting for scr refresh
                    dannular11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular11.stopped')
                    # update status
                    dannular11.status = FINISHED
                    dannular11.setAutoDraw(False)

            # *dannular12* updates
            
            # if dannular12 is starting this frame...
            if dannular12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular12.frameNStart = frameN  # exact frame index
                dannular12.tStart = t  # local t and not account for scr refresh
                dannular12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular12.started')
                # update status
                dannular12.status = STARTED
                dannular12.setAutoDraw(True)
            
            # if dannular12 is active this frame...
            if dannular12.status == STARTED:
                # update params
                dannular12.setOpacity(None, log=False)
                dannular12.setContrast(0.65, log=False)
                dannular12.setLineWidth(1.0, log=False)
            
            # if dannular12 is stopping this frame...
            if dannular12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular12.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular12.tStop = t  # not accounting for scr refresh
                    dannular12.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular12.stopped')
                    # update status
                    dannular12.status = FINISHED
                    dannular12.setAutoDraw(False)

            # *dannular13* updates
            
            # if dannular13 is starting this frame...
            if dannular13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular13.frameNStart = frameN  # exact frame index
                dannular13.tStart = t  # local t and not account for scr refresh
                dannular13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular13.started')
                # update status
                dannular13.status = STARTED
                dannular13.setAutoDraw(True)
            
            # if dannular13 is active this frame...
            if dannular13.status == STARTED:
                # update params
                dannular13.setOpacity(None, log=False)
                dannular13.setContrast(0.65, log=False)
                dannular13.setLineWidth(1.0, log=False)
            
            # if dannular13 is stopping this frame...
            if dannular13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular13.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular13.tStop = t  # not accounting for scr refresh
                    dannular13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular13.stopped')
                    # update status
                    dannular13.status = FINISHED
                    dannular13.setAutoDraw(False)

            # *dannular14* updates
            
            # if dannular14 is starting this frame...
            if dannular14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular14.frameNStart = frameN  # exact frame index
                dannular14.tStart = t  # local t and not account for scr refresh
                dannular14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular14.started')
                # update status
                dannular14.status = STARTED
                dannular14.setAutoDraw(True)
            
            # if dannular14 is active this frame...
            if dannular14.status == STARTED:
                # update params
                dannular14.setOpacity(None, log=False)
                dannular14.setContrast(0.65, log=False)
                dannular14.setLineWidth(1.0, log=False)
            
            # if dannular14 is stopping this frame...
            if dannular14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular14.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular14.tStop = t  # not accounting for scr refresh
                    dannular14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular14.stopped')
                    # update status
                    dannular14.status = FINISHED
                    dannular14.setAutoDraw(False)

            # *dannular15* updates
            
            # if dannular15 is starting this frame...
            if dannular15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular15.frameNStart = frameN  # exact frame index
                dannular15.tStart = t  # local t and not account for scr refresh
                dannular15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular15.started')
                # update status
                dannular15.status = STARTED
                dannular15.setAutoDraw(True)
            
            # if dannular15 is active this frame...
            if dannular15.status == STARTED:
                # update params
                dannular15.setOpacity(None, log=False)
                dannular15.setContrast(0.65, log=False)
                dannular15.setLineWidth(1.0, log=False)
            
            # if dannular15 is stopping this frame...
            if dannular15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular15.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular15.tStop = t  # not accounting for scr refresh
                    dannular15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular15.stopped')
                    # update status
                    dannular15.status = FINISHED
                    dannular15.setAutoDraw(False)

            # *dannular16* updates
            
            # if dannular16 is starting this frame...
            if dannular16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dannular16.frameNStart = frameN  # exact frame index
                dannular16.tStart = t  # local t and not account for scr refresh
                dannular16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dannular16, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dannular16.started')
                # update status
                dannular16.status = STARTED
                dannular16.setAutoDraw(True)
            
            # if dannular16 is active this frame...
            if dannular16.status == STARTED:
                # update params
                dannular16.setOpacity(None, log=False)
                dannular16.setContrast(0.65, log=False)
                dannular16.setLineWidth(1.0, log=False)
            
            # if dannular16 is stopping this frame...
            if dannular16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dannular16.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dannular16.tStop = t  # not accounting for scr refresh
                    dannular16.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dannular16.stopped')
                    # update status
                    dannular16.status = FINISHED
                    dannular16.setAutoDraw(False)

            # *dcover* updates
            
            # if dcover is starting this frame...
            if dcover.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dcover.frameNStart = frameN  # exact frame index
                dcover.tStart = t  # local t and not account for scr refresh
                dcover.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dcover, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dcover.started')
                # update status
                dcover.status = STARTED
                dcover.setAutoDraw(True)
            
            # if dcover is active this frame...
            if dcover.status == STARTED:
                opci=0.5+0.5*np.sin(2*np.pi*t*22)
                # update params
                dcover.setOpacity(opci, log=False)
                dcover.setContrast(0.0, log=False)
                dcover.setLineWidth(1.0, log=False)
            
            # if dcover is stopping this frame...
            if dcover.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dcover.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dcover.tStop = t  # not accounting for scr refresh
                    dcover.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dcover.stopped')
                    # update status
                    dcover.status = FINISHED
                    dcover.setAutoDraw(False)
            
            # *dcenter* updates
            
            # if dcenter is starting this frame...
            if dcenter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dcenter.frameNStart = frameN  # exact frame index
                dcenter.tStart = t  # local t and not account for scr refresh
                dcenter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dcenter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dcenter.started')
                # update status
                dcenter.status = STARTED
                dcenter.setAutoDraw(True)
            
            # if dcenter is active this frame...
            if dcenter.status == STARTED:
                # update params
                dcenter.setOpacity(None, log=False)
                dcenter.setContrast(1.0, log=False)
                dcenter.setLineWidth(1.0, log=False)
            
            # if dcenter is stopping this frame...
            if dcenter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dcenter.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    dcenter.tStop = t  # not accounting for scr refresh
                    dcenter.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dcenter.stopped')
                    # update status
                    dcenter.status = FINISHED
                    dcenter.setAutoDraw(False)
            
            # *wrong2* updates
            waitOnFlip = False
            
            # if wrong2 is starting this frame...
            if wrong2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wrong2.frameNStart = frameN  # exact frame index
                wrong2.tStart = t  # local t and not account for scr refresh
                wrong2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wrong2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wrong2.started')
                # update status
                wrong2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wrong2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wrong2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if wrong2 is stopping this frame...
            if wrong2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wrong2.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    wrong2.tStop = t  # not accounting for scr refresh
                    wrong2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wrong2.stopped')
                    # update status
                    wrong2.status = FINISHED
                    wrong2.status = FINISHED
            if wrong2.status == STARTED and not waitOnFlip:
                theseKeys = wrong2.getKeys(keyList=['space'], waitRelease=False)
                _wrong2_allKeys.extend(theseKeys)
                if len(_wrong2_allKeys):
                    wrong2.keys = [key.name for key in _wrong2_allKeys]  # storing all keys
                    wrong2.rt = [key.rt for key in _wrong2_allKeys]
                    # a response ends the routine
                    continueRoutine = True#False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in durationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "duration" ---
        for thisComponent in durationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if wrong2.keys in ['', [], None]:  # No response was made
            wrong2.keys = None
        trials.addData('wrong2.keys',wrong2.keys)
        if wrong2.keys != None:  # we had a response
            trials.addData('wrong2.rt', wrong2.rt)
        # the Routine "duration" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


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
