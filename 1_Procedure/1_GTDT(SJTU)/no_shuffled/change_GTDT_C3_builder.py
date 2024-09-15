#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on 七月 25, 2023, at 19:14
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
#root_dir = 'D:/happy_working/repCPP/Stage1/1_Procedure/1_Version_control/make_new/'    # change root #
root_dir = os.path.join(os.getcwd()+"/")
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'GTDT3'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 9999):06.0f}",
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
    originPath=root_dir + 'change_GTDT_C3_builder.py',
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

#hz = 59
#win = visual.Window(fullscr=True, winType='glfw', refreshHz=hz, waitBlanking=True, swapInterval=1)
# if using the latest 'master' branch
# win = Window(fullscr=True, winType='glfw', refreshHz=hz, waitBlanking=True)

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

# --- Initialize components for Routine "instruction1" ---
i1 = visual.ImageStim(
    win=win,
    name='i1', 
    image=root_dir + 'instruction1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(48, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction2" ---
i2 = visual.ImageStim(
    win=win,
    name='i2', 
    image=root_dir + 'instruction2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(48, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction3" ---
i3 = visual.ImageStim(
    win=win,
    name='i3', 
    image=root_dir + 'instruction3C3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(48, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation" ---
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bstart = parallel.ParallelPort(address='0x3EFC')   # diff

# --- Initialize components for Routine "GTDT_2" ---

annular = visual.Pie(
    win=win, name='annular',start=0, end=22.5,radius=2.8,
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
cover = visual.ShapeStim(
    win=win, name='cover',
    size=(5.6, 5.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=False)
center = visual.ShapeStim(
    win=win, name='center',
    size=(2.8, 2.8), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='grey', fillColor='grey',
    opacity=None, depth=-3.0, interpolate=False)
bg = visual.Rect(
    win=win, name='bg',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
stimulus = parallel.ParallelPort(address='0x3EFC')

    #def stimulus_marker(value):
    #    stimulus.setData(value)
    #    core.wait(0.05)
    #    stimulus.setData(0)
    #stimulus_marker(1)
    #stimulus_marker('bseq')
    #bstart = parallel.ParallelPort(address='0x5FB8')
    #def bstart_marker(value):
    #    bstart.setData(value)
    #    core.wait(0.05)
    #    bstart.setData(0)
    #bstart_marker('bseq')
    #bend = parallel.ParallelPort(address='0x5FB8')
    #def bend_marker(value):
    #    bend.setData(value)
    #    core.wait(0.05)
    #    bend.setData(0)
#bend_marker('bseq')
# --- Initialize components for Routine "question" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='请问在这个阶段中，你观察到圆环变暗的次数为？\n填写完成后按空格键提交',
    font='Open Sans',
    pos=(0, 0.15), height=1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bend = parallel.ParallelPort(address='0x3EFC')
textbox = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Arial',
     pos=(0, -2.5),     letterHeight=1,
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
     depth=-1, autoLog=True,
)
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "rest" ---
i4 = visual.ImageStim(
    win=win,
    name='i4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(48, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "condition" ---
i5 = visual.ImageStim(
    win=win,
    name='i5', 
    image=root_dir + 'instruction5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(48, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruction1" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instruction1Components = [i1, key_resp]
for thisComponent in instruction1Components:
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

# --- Run Routine "instruction1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i1* updates
    
    # if i1 is starting this frame...
    if i1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i1.frameNStart = frameN  # exact frame index
        i1.tStart = t  # local t and not account for scr refresh
        i1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i1.started')
        # update status
        i1.status = STARTED
        i1.setAutoDraw(True)
    
    # if i1 is active this frame...
    if i1.status == STARTED:
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
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction1" ---
for thisComponent in instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instruction2Components = [i2, key_resp_2]
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
instruction3Components = [i3, key_resp_3]
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
    
    # *i3* updates
    
    # if i3 is starting this frame...
    if i3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i3.frameNStart = frameN  # exact frame index
        i3.tStart = t  # local t and not account for scr refresh
        i3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i3.started')
        # update status
        i3.status = STARTED
        i3.setAutoDraw(True)
    
    # if i3 is active this frame...
    if i3.status == STARTED:
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
block = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(root_dir + 'blist_c3.xlsx'),
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [text,bstart]
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
            #bstart_marker(9)
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
        
        # if bstart is starting this frame...    # dell
        if bstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance: # dell
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
            win.callOnFlip(bstart.setData, int(bseq))   # dell
            
        
        
        # if bstart is stopping this frame...
        if bstart.status == STARTED:     # dell
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bstart.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                bstart.tStop = t  # not accounting for scr refresh
                bstart.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bstart.stopped')
                # update status
                bstart.status = FINISHED
                win.callOnFlip(bstart.setData, int(0))   # dell
        
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
    if bstart.status == STARTED:   # dell
        win.callOnFlip(bstart.setData, int(0)) # dell
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(btrials),
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
        
        # --- Prepare to start Routine "GTDT_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        GTDTComponents = [bg, annular, annular2, annular3,annular4,
        annular5,annular6,annular7,annular8,annular9,annular10,annular11,annular12,
        annular13,annular14,annular15,annular16, cover, center, stimulus]
        for thisComponent in GTDTComponents:
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
        
        # --- Run Routine "GTDT" ---
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
                opci=0.5+0.5*np.sin(2*np.pi*t*21.25)
                # update params
                cover.setOpacity(opci, log=False)
                cover.setContrast(0.0, log=False)
                cover.setLineWidth(1.0, log=False)
            
            # if cover is stopping this frame...
            if cover.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cover.tStartRefresh + asec-frameTolerance:
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
                if tThisFlipGlobal > center.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    center.tStop = t  # not accounting for scr refresh
                    center.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'center.stopped')
                    # update status
                    center.status = FINISHED
                    center.setAutoDraw(False)
            
            # *bg* updates
            
            # if bg is starting this frame...
            if bg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bg.frameNStart = frameN  # exact frame index
                bg.tStart = t  # local t and not account for scr refresh
                bg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg.started')
                # update status
                bg.status = STARTED
                bg.setAutoDraw(True)
            
            # if bg is active this frame...
            if bg.status == STARTED:
                # update params
                bg.setOpacity(None, log=False)
                bg.setContrast(1.0, log=False)
                bg.setLineWidth(1.0, log=False)
            
            # if bg is stopping this frame...
            if bg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > bg.tStartRefresh + asec-frameTolerance:
                    # keep track of stop time/frame for later
                    bg.tStop = t  # not accounting for scr refresh
                    bg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bg.stopped')
                    # update status
                    bg.status = FINISHED
                    bg.setAutoDraw(False)
            
            # if stimulus is starting this frame...
            if stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:     # dell
                # keep track of start time/frame for later
                stimulus.frameNStart = frameN  # exact frame index      dell
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus.started')
                # update status
                stimulus.status = STARTED
                stimulus.status = STARTED
                win.callOnFlip(stimulus.setData, int(1))      # dell
            
            
            
            # if stimulus is stopping this frame...    dell
            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulus.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    stimulus.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus.stopped')
                    # update status
                    stimulus.status = FINISHED
                    win.callOnFlip(stimulus.setData, int(0)) # dell
                    
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GTDTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "GTDT" ---
        for thisComponent in GTDTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if stimulus.status == STARTED:    ##dell
            win.callOnFlip(stimulus.setData, int(0))   ##dell
        # the Routine "GTDT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "question" ---
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    questionComponents = [text_2, textbox, key_resp_6, bend]
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
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = [key.name for key in _key_resp_6_allKeys]  # storing all keys
                key_resp_6.rt = [key.rt for key in _key_resp_6_allKeys]
                # a response ends the routine
                continueRoutine = False
        # *bend* updates
        
        # if bend is starting this frame...
        if bend.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bend.frameNStart = frameN  # exact frame index
            bend.tStart = t  # local t and not account for scr refresh
            bend.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bend, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('bend.started', t)
            # update status
            bend.status = STARTED
            bend.status = STARTED
            win.callOnFlip(bend.setData, int(bseq))
        
        # if bend is stopping this frame...
        if bend.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bend.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                bend.tStop = t  # not accounting for scr refresh
                bend.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('bend.stopped', t)
                # update status
                bend.status = FINISHED
                win.callOnFlip(bend.setData, int(0))
                
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
    if bend.status == STARTED:
        win.callOnFlip(bend.setData, int(0))
    block.addData('textbox.text',textbox.text)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    block.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        block.addData('key_resp_6.rt', key_resp_6.rt)
    if bend.status == STARTED:
        win.callOnFlip(bend.setData, int(0))
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    restComponents = [i4, key_resp_4]
    for thisComponent in restComponents:
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
    
    # --- Run Routine "rest" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *i4* updates
        
        # if i4 is starting this frame...
        if i4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            #bend_marker(9)
            i4.frameNStart = frameN  # exact frame index
            i4.tStart = t  # local t and not account for scr refresh
            i4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'i4.started')
            # update status
            i4.status = STARTED
            i4.setAutoDraw(True)
        
        # if i4 is active this frame...
        if i4.status == STARTED:
            # update params
            #pass
            i4.setImage(brest, log=False)
        
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
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['p'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
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
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    block.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        block.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block'


# --- Prepare to start Routine "condition" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
conditionComponents = [i5, key_resp_5]
for thisComponent in conditionComponents:
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

# --- Run Routine "condition" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i5* updates
    
    # if i5 is starting this frame...
    if i5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        i5.frameNStart = frameN  # exact frame index
        i5.tStart = t  # local t and not account for scr refresh
        i5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(i5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'i5.started')
        # update status
        i5.status = STARTED
        i5.setAutoDraw(True)
    
    # if i5 is active this frame...
    if i5.status == STARTED:
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in conditionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "condition" ---
for thisComponent in conditionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "condition" was not non-slip safe, so reset the non-slip timer
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
