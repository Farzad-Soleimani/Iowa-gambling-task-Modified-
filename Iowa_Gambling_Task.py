#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.3),
    on November 06, 2024, at 13:42
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.3'
expName = 'Iowa_Gambling_Task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 960]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\SAM-Tech\\Desktop\\IGT test 3\\Iowa_Gambling_Task.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0.0196, 0.2549, 0.0196], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.0196, 0.2549, 0.0196]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('response_key') is None:
        # initialise response_key
        response_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response_key',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instruction" ---
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    # Run 'Begin Experiment' code from Initialization
    import random
    
    # Begin Experiment
    net_worth = 0
    feedback_text = ""
    final_message_text = ""
    
    def simulateOutcome(chosen_deck, conditions):
        deck_data = conditions[chosen_deck]  # Access reward and penalty from conditions
        reward, penalty = deck_data['Reward'], deck_data['Penalty']
    
        if random.random() < 0.5:  # Assuming 50% chance to win/lose for demonstration
            return reward
        else:
            return penalty
    
    deck_positions = [(-0.5, 0), (-0.17, 0), (0.17, 0), (0.5, 0)]
    arrow_offset_y = 0.2  # Adjust this value to move the arrow higher
    current_position = random.randint(0, len(deck_positions) - 1)
    instruction_image = visual.ImageStim(
        win=win,
        name='instruction_image', 
        image='Instruction_slide.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.645, 1.029),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "Main_Task" ---
    deck_a_image = visual.ImageStim(
        win=win,
        name='deck_a_image', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    deck_b_image = visual.ImageStim(
        win=win,
        name='deck_b_image', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.17, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    deck_c_image = visual.ImageStim(
        win=win,
        name='deck_c_image', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.17, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    deck_d_image = visual.ImageStim(
        win=win,
        name='deck_d_image', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    arrow_image = visual.ImageStim(
        win=win,
        name='arrow_image', 
        image='arrow.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 1), draggable=False, size=(0.2,0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    # Run 'Begin Experiment' code from arrow_movement
    deck_positions = [(-0.5, 0), (-0.17, 0), (0.17, 0), (0.5, 0)]
    current_position = 0
    arrow_offset_y = 0.3  # Adjust this value to move the arrow higher
    arrow_image.pos = (deck_positions[current_position][0], deck_positions[current_position][1] + arrow_offset_y)
    
    
    response_key = keyboard.Keyboard(deviceName='response_key')
    
    # --- Initialize components for Routine "Feedback" ---
    feedback_display = visual.TextStim(win=win, name='feedback_display',
        text='',
        font='B koodak ',
        pos=(0, 0), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    
    # --- Initialize components for Routine "End" ---
    final_message = visual.TextStim(win=win, name='final_message',
        text=final_message_text
    ,
        font='B Koodak',
        pos=(0, 0), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Instruction" ---
    # create an object to store info about Routine Instruction
    Instruction = data.Routine(
        name='Instruction',
        components=[key_resp, instruction_image],
    )
    Instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for Instruction
    Instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instruction.tStart = globalClock.getTime(format='float')
    Instruction.status = STARTED
    thisExp.addData('Instruction.started', Instruction.tStart)
    Instruction.maxDuration = None
    # keep track of which components have finished
    InstructionComponents = Instruction.components
    for thisComponent in Instruction.components:
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
    
    # --- Run Routine "Instruction" ---
    Instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *instruction_image* updates
        
        # if instruction_image is starting this frame...
        if instruction_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_image.frameNStart = frameN  # exact frame index
            instruction_image.tStart = t  # local t and not account for scr refresh
            instruction_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_image.started')
            # update status
            instruction_image.status = STARTED
            instruction_image.setAutoDraw(True)
        
        # if instruction_image is active this frame...
        if instruction_image.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction" ---
    for thisComponent in Instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instruction
    Instruction.tStop = globalClock.getTime(format='float')
    Instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instruction.stopped', Instruction.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop = data.TrialHandler2(
        name='loop',
        nReps=2.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(loop)  # add the loop to the experiment
    thisLoop = loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            globals()[paramName] = thisLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop in loop:
        currentLoop = loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
        if thisLoop != None:
            for paramName in thisLoop:
                globals()[paramName] = thisLoop[paramName]
        
        # --- Prepare to start Routine "Main_Task" ---
        # create an object to store info about Routine Main_Task
        Main_Task = data.Routine(
            name='Main_Task',
            components=[deck_a_image, deck_b_image, deck_c_image, deck_d_image, arrow_image, response_key],
        )
        Main_Task.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from arrow_movement
        # Set arrow position at the start of each trial
        arrow_image.pos = (deck_positions[current_position][0], deck_positions[current_position][1] + arrow_offset_y)
        
        # create starting attributes for response_key
        response_key.keys = []
        response_key.rt = []
        _response_key_allKeys = []
        # store start times for Main_Task
        Main_Task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Task.tStart = globalClock.getTime(format='float')
        Main_Task.status = STARTED
        thisExp.addData('Main_Task.started', Main_Task.tStart)
        Main_Task.maxDuration = None
        # keep track of which components have finished
        Main_TaskComponents = Main_Task.components
        for thisComponent in Main_Task.components:
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
        
        # --- Run Routine "Main_Task" ---
        # if trial has changed, end Routine now
        if isinstance(loop, data.TrialHandler2) and thisLoop.thisN != loop.thisTrial.thisN:
            continueRoutine = False
        Main_Task.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *deck_a_image* updates
            
            # if deck_a_image is starting this frame...
            if deck_a_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_a_image.frameNStart = frameN  # exact frame index
                deck_a_image.tStart = t  # local t and not account for scr refresh
                deck_a_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_a_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_a_image.started')
                # update status
                deck_a_image.status = STARTED
                deck_a_image.setAutoDraw(True)
            
            # if deck_a_image is active this frame...
            if deck_a_image.status == STARTED:
                # update params
                pass
            
            # *deck_b_image* updates
            
            # if deck_b_image is starting this frame...
            if deck_b_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_b_image.frameNStart = frameN  # exact frame index
                deck_b_image.tStart = t  # local t and not account for scr refresh
                deck_b_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_b_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_b_image.started')
                # update status
                deck_b_image.status = STARTED
                deck_b_image.setAutoDraw(True)
            
            # if deck_b_image is active this frame...
            if deck_b_image.status == STARTED:
                # update params
                pass
            
            # *deck_c_image* updates
            
            # if deck_c_image is starting this frame...
            if deck_c_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_c_image.frameNStart = frameN  # exact frame index
                deck_c_image.tStart = t  # local t and not account for scr refresh
                deck_c_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_c_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_c_image.started')
                # update status
                deck_c_image.status = STARTED
                deck_c_image.setAutoDraw(True)
            
            # if deck_c_image is active this frame...
            if deck_c_image.status == STARTED:
                # update params
                pass
            
            # *deck_d_image* updates
            
            # if deck_d_image is starting this frame...
            if deck_d_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_d_image.frameNStart = frameN  # exact frame index
                deck_d_image.tStart = t  # local t and not account for scr refresh
                deck_d_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_d_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_d_image.started')
                # update status
                deck_d_image.status = STARTED
                deck_d_image.setAutoDraw(True)
            
            # if deck_d_image is active this frame...
            if deck_d_image.status == STARTED:
                # update params
                pass
            
            # *arrow_image* updates
            
            # if arrow_image is starting this frame...
            if arrow_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_image.frameNStart = frameN  # exact frame index
                arrow_image.tStart = t  # local t and not account for scr refresh
                arrow_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow_image.started')
                # update status
                arrow_image.status = STARTED
                arrow_image.setAutoDraw(True)
            
            # if arrow_image is active this frame...
            if arrow_image.status == STARTED:
                # update params
                pass
            
            # *response_key* updates
            waitOnFlip = False
            
            # if response_key is starting this frame...
            if response_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_key.frameNStart = frameN  # exact frame index
                response_key.tStart = t  # local t and not account for scr refresh
                response_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_key.started')
                # update status
                response_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response_key.status == STARTED and not waitOnFlip:
                theseKeys = response_key.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _response_key_allKeys.extend(theseKeys)
                if len(_response_key_allKeys):
                    response_key.keys = _response_key_allKeys[-1].name  # just the last key pressed
                    response_key.rt = _response_key_allKeys[-1].rt
                    response_key.duration = _response_key_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Task.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Task.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Task" ---
        for thisComponent in Main_Task.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Task
        Main_Task.tStop = globalClock.getTime(format='float')
        Main_Task.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Task.stopped', Main_Task.tStop)
        # check responses
        if response_key.keys in ['', [], None]:  # No response was made
            response_key.keys = None
        loop.addData('response_key.keys',response_key.keys)
        if response_key.keys != None:  # we had a response
            loop.addData('response_key.rt', response_key.rt)
            loop.addData('response_key.duration', response_key.duration)
        # Run 'End Routine' code from code_2
        conditions = {
            'deck_a': {'Reward': 100, 'Penalty': -250},
            'deck_b': {'Reward': 100, 'Penalty': -1150},
            'deck_c': {'Reward': 50, 'Penalty': -25},
            'deck_d': {'Reward': 50, 'Penalty': -200},
        }
        
        #if response_key.keys:
        #    if 'f' in response_key.keys:
        #        chosen_action = 'deck_' + chr(97 + current_position)  # Dynamically select the deck based on arrow position
        #outcome = simulateOutcome(chosen_action, conditions)
        #        net_worth += outcome
        #        feedback_text = f"شما بازی کردید\n نتیجه: {outcome}\n  جمع پول شما اکنون: {net_worth}"
        #    elif 'j' in response_key.keys:
        #        chosen_action = 'pass'
        #        feedback_text = f"You passed. Your total remains: {net_worth}"
        def to_persian_number(number):
            english_to_persian = {
                '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
                '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
            }
            
            number_str = str(abs(number))  # Convert number to string and ignore the sign for now
            persian_number = ''.join(english_to_persian.get(char, char) for char in number_str)
            
            # Add negative sign to the right side if the number is negative
            if number < 0:
                persian_number += '−'
            
            return persian_number
        
        if response_key.keys:
            if 'f' in response_key.keys:
                chosen_action = 'deck_' + chr(97 + current_position)  # Dynamically select the deck based on arrow position
                outcome = simulateOutcome(chosen_action, conditions)
                net_worth += outcome
                feedback_text = f"شما بازی کردید\n\n نتیجه:  ${to_persian_number(outcome)}\n\n  جمع پول شما اکنون:  ${to_persian_number(net_worth)}"
            elif 'j' in response_key.keys:
                chosen_action = 'pass'
                feedback_text = f"شما گذشتید\n\n  جمع پول شما اکنون:  ${to_persian_number(net_worth)}"
        
            feedback_display.setText(feedback_text)  # Update the text component with feedback_text
        
        
            
            feedback_display.setText(feedback_text)  # Update the text component with feedback_text
            
            # Randomly move the arrow to a new position for the next trial
            current_position = random.randint(0, len(deck_positions) - 1)
            
            continueRoutine = False  # End the routine after making a choice
        
        # the Routine "Main_Task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        # create an object to store info about Routine Feedback
        Feedback = data.Routine(
            name='Feedback',
            components=[feedback_display],
        )
        Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        feedback_display.setText(feedback_text)
        # store start times for Feedback
        Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Feedback.tStart = globalClock.getTime(format='float')
        Feedback.status = STARTED
        thisExp.addData('Feedback.started', Feedback.tStart)
        Feedback.maxDuration = None
        # keep track of which components have finished
        FeedbackComponents = Feedback.components
        for thisComponent in Feedback.components:
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
        
        # --- Run Routine "Feedback" ---
        # if trial has changed, end Routine now
        if isinstance(loop, data.TrialHandler2) and thisLoop.thisN != loop.thisTrial.thisN:
            continueRoutine = False
        Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_display* updates
            
            # if feedback_display is starting this frame...
            if feedback_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_display.frameNStart = frameN  # exact frame index
                feedback_display.tStart = t  # local t and not account for scr refresh
                feedback_display.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_display, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_display.started')
                # update status
                feedback_display.status = STARTED
                feedback_display.setAutoDraw(True)
            
            # if feedback_display is active this frame...
            if feedback_display.status == STARTED:
                # update params
                pass
            
            # if feedback_display is stopping this frame...
            if feedback_display.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_display.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_display.tStop = t  # not accounting for scr refresh
                    feedback_display.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_display.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_display.stopped')
                    # update status
                    feedback_display.status = FINISHED
                    feedback_display.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Feedback
        Feedback.tStop = globalClock.getTime(format='float')
        Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Feedback.stopped', Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Feedback.maxDurationReached:
            routineTimer.addTime(-Feedback.maxDuration)
        elif Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'loop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if loop.trialList in ([], [None], None):
        params = []
    else:
        params = loop.trialList[0].keys()
    # save data for this loop
    loop.saveAsExcel(filename + '.xlsx', sheetName='loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "End" ---
    # create an object to store info about Routine End
    End = data.Routine(
        name='End',
        components=[final_message],
    )
    End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for End
    End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End.tStart = globalClock.getTime(format='float')
    End.status = STARTED
    thisExp.addData('End.started', End.tStart)
    End.maxDuration = None
    # keep track of which components have finished
    EndComponents = End.components
    for thisComponent in End.components:
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
    
    # --- Run Routine "End" ---
    End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *final_message* updates
        
        # if final_message is starting this frame...
        if final_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            final_message.frameNStart = frameN  # exact frame index
            final_message.tStart = t  # local t and not account for scr refresh
            final_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(final_message, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'final_message.started')
            # update status
            final_message.status = STARTED
            final_message.setAutoDraw(True)
        
        # if final_message is active this frame...
        if final_message.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End
    End.tStop = globalClock.getTime(format='float')
    End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End.stopped', End.tStop)
    # Run 'End Routine' code from code
    final_message_text =f"پایان بازی\n\n لغ نهایی شما:{to_persian_number(net_worth)}"
    thisExp.nextEntry()
    # the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
