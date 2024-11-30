#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.3),
    on November 30, 2024, at 16:29
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
        originPath='C:\\Users\\SAM-Tech\\Desktop\\Iowa_Gambling_Task_Modified\\Iowa_Gambling_Task_lastrun.py',
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
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('practice_response') is None:
        # initialise practice_response
        practice_response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='practice_response',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
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
    net_worth = 2000
    net_worth_practice = 2000
    feedback_text = ""
    final_message_text = ""
    feedback_text_2 = ""
    info_text = ""
    practice_info_text = ""
    
    
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
        image='Instruction_1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.645, 1.029),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "practice_instruction" ---
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    practice_instruction_image = visual.ImageStim(
        win=win,
        name='practice_instruction_image', 
        image='practice_instruction.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.645, 1.029),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "Instruction_2" ---
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    instruction_2_image = visual.ImageStim(
        win=win,
        name='instruction_2_image', 
        image='Instruction_2.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.645, 1.029),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "practice_task" ---
    deck_a_image_2 = visual.ImageStim(
        win=win,
        name='deck_a_image_2', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    deck_b_image_2 = visual.ImageStim(
        win=win,
        name='deck_b_image_2', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.17, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    deck_c_image_2 = visual.ImageStim(
        win=win,
        name='deck_c_image_2', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.17, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    deck_d_image_2 = visual.ImageStim(
        win=win,
        name='deck_d_image_2', 
        image='Card.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), draggable=False, size=(0.25, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    arrow_image_2 = visual.ImageStim(
        win=win,
        name='arrow_image_2', 
        image='arrow.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 1), draggable=False, size=(0.2,0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    practice_response = keyboard.Keyboard(deviceName='practice_response')
    # Run 'Begin Experiment' code from arrow_movement_2
    deck_positions = [(-0.5, 0), (-0.17, 0), (0.17, 0), (0.5, 0)]
    current_position = 0
    arrow_offset_y = 0.3  # Adjust this value to move the arrow higher
    arrow_image_2.pos = (deck_positions[current_position][0], deck_positions[current_position][1] + arrow_offset_y)
    
    
    # Run 'Begin Experiment' code from code_3
    net_worth_practice = 2000  # Initialize net worth for practice
    practice_completed = False  # Flag to check if practice is completed
    previous_outcome_practice = 0
    practice_info_display = visual.TextStim(win=win, name='practice_info_display',
        text=practice_info_text,
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-8.0);
    
    # --- Initialize components for Routine "Feedback_2" ---
    feedback_display_2 = visual.TextStim(win=win, name='feedback_display_2',
        text=feedback_text_2
    
    ,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    
    # --- Initialize components for Routine "after_practice" ---
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    after_practice_image = visual.ImageStim(
        win=win,
        name='after_practice_image', 
        image='after_practice.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.645, 1.029),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
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
    # Run 'Begin Experiment' code from code_2
    net_worth = 2000
    previous_choice = 'None'
    previous_outcome = 0
    
    # Prepare to store data
    choices = []
    outcomes = []
    net_worths = []
    
    def log_data(trial_type, choice, outcome, net_worth):
        choices.append(choice)
        outcomes.append(outcome)
        net_worths.append(net_worth)
        thisExp.addData('trialType', trial_type)
        thisExp.addData('choice', choice)
        thisExp.addData('outcome', outcome)
        thisExp.addData('net_worth', net_worth)
        thisExp.nextEntry()  # Ensure data is logged correctly
    
    info_display = visual.TextStim(win=win, name='info_display',
        text=info_text,
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-8.0);
    
    # --- Initialize components for Routine "Feedback" ---
    feedback_display = visual.TextStim(win=win, name='feedback_display',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    
    # --- Initialize components for Routine "End" ---
    final_message = visual.TextStim(win=win, name='final_message',
        text=final_message_text
    ,
        font='B koodak ',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
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
    
    # --- Prepare to start Routine "practice_instruction" ---
    # create an object to store info about Routine practice_instruction
    practice_instruction = data.Routine(
        name='practice_instruction',
        components=[key_resp_3, practice_instruction_image],
    )
    practice_instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for practice_instruction
    practice_instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice_instruction.tStart = globalClock.getTime(format='float')
    practice_instruction.status = STARTED
    thisExp.addData('practice_instruction.started', practice_instruction.tStart)
    practice_instruction.maxDuration = None
    # keep track of which components have finished
    practice_instructionComponents = practice_instruction.components
    for thisComponent in practice_instruction.components:
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
    
    # --- Run Routine "practice_instruction" ---
    practice_instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *practice_instruction_image* updates
        
        # if practice_instruction_image is starting this frame...
        if practice_instruction_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_instruction_image.frameNStart = frameN  # exact frame index
            practice_instruction_image.tStart = t  # local t and not account for scr refresh
            practice_instruction_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_instruction_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_instruction_image.started')
            # update status
            practice_instruction_image.status = STARTED
            practice_instruction_image.setAutoDraw(True)
        
        # if practice_instruction_image is active this frame...
        if practice_instruction_image.status == STARTED:
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
            practice_instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_instruction" ---
    for thisComponent in practice_instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice_instruction
    practice_instruction.tStop = globalClock.getTime(format='float')
    practice_instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice_instruction.stopped', practice_instruction.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "practice_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction_2" ---
    # create an object to store info about Routine Instruction_2
    Instruction_2 = data.Routine(
        name='Instruction_2',
        components=[key_resp_2, instruction_2_image],
    )
    Instruction_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for Instruction_2
    Instruction_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instruction_2.tStart = globalClock.getTime(format='float')
    Instruction_2.status = STARTED
    thisExp.addData('Instruction_2.started', Instruction_2.tStart)
    Instruction_2.maxDuration = None
    # keep track of which components have finished
    Instruction_2Components = Instruction_2.components
    for thisComponent in Instruction_2.components:
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
    
    # --- Run Routine "Instruction_2" ---
    Instruction_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *instruction_2_image* updates
        
        # if instruction_2_image is starting this frame...
        if instruction_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_2_image.frameNStart = frameN  # exact frame index
            instruction_2_image.tStart = t  # local t and not account for scr refresh
            instruction_2_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_2_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_2_image.started')
            # update status
            instruction_2_image.status = STARTED
            instruction_2_image.setAutoDraw(True)
        
        # if instruction_2_image is active this frame...
        if instruction_2_image.status == STARTED:
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
            Instruction_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction_2" ---
    for thisComponent in Instruction_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instruction_2
    Instruction_2.tStop = globalClock.getTime(format='float')
    Instruction_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instruction_2.stopped', Instruction_2.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "Instruction_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_loop = data.TrialHandler2(
        name='practice_loop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practice_loop)  # add the loop to the experiment
    thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            globals()[paramName] = thisPractice_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_loop in practice_loop:
        currentLoop = practice_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
        if thisPractice_loop != None:
            for paramName in thisPractice_loop:
                globals()[paramName] = thisPractice_loop[paramName]
        
        # --- Prepare to start Routine "practice_task" ---
        # create an object to store info about Routine practice_task
        practice_task = data.Routine(
            name='practice_task',
            components=[deck_a_image_2, deck_b_image_2, deck_c_image_2, deck_d_image_2, arrow_image_2, practice_response, practice_info_display],
        )
        practice_task.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for practice_response
        practice_response.keys = []
        practice_response.rt = []
        _practice_response_allKeys = []
        # Run 'Begin Routine' code from arrow_movement_2
        # Set arrow position at the start of each trial
        arrow_image_2.pos = (deck_positions[current_position][0], deck_positions[current_position][1] + arrow_offset_y)
        
        # Run 'Begin Routine' code from code_3
        # This code runs once at the beginning of the routine
        feedback_text_2 = ''
        
        # Update the display text to show current total and previous choice for practice
        practice_info_text = f"جمع پول شما: {(net_worth_practice)}\n\nانتخاب قبلی شما: {(previous_outcome_practice)}"
        practice_info_display.setText(practice_info_text)  # Update the text component with info_text_practice
        
        
        # store start times for practice_task
        practice_task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_task.tStart = globalClock.getTime(format='float')
        practice_task.status = STARTED
        thisExp.addData('practice_task.started', practice_task.tStart)
        practice_task.maxDuration = None
        # keep track of which components have finished
        practice_taskComponents = practice_task.components
        for thisComponent in practice_task.components:
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
        
        # --- Run Routine "practice_task" ---
        # if trial has changed, end Routine now
        if isinstance(practice_loop, data.TrialHandler2) and thisPractice_loop.thisN != practice_loop.thisTrial.thisN:
            continueRoutine = False
        practice_task.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *deck_a_image_2* updates
            
            # if deck_a_image_2 is starting this frame...
            if deck_a_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_a_image_2.frameNStart = frameN  # exact frame index
                deck_a_image_2.tStart = t  # local t and not account for scr refresh
                deck_a_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_a_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_a_image_2.started')
                # update status
                deck_a_image_2.status = STARTED
                deck_a_image_2.setAutoDraw(True)
            
            # if deck_a_image_2 is active this frame...
            if deck_a_image_2.status == STARTED:
                # update params
                pass
            
            # *deck_b_image_2* updates
            
            # if deck_b_image_2 is starting this frame...
            if deck_b_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_b_image_2.frameNStart = frameN  # exact frame index
                deck_b_image_2.tStart = t  # local t and not account for scr refresh
                deck_b_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_b_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_b_image_2.started')
                # update status
                deck_b_image_2.status = STARTED
                deck_b_image_2.setAutoDraw(True)
            
            # if deck_b_image_2 is active this frame...
            if deck_b_image_2.status == STARTED:
                # update params
                pass
            
            # *deck_c_image_2* updates
            
            # if deck_c_image_2 is starting this frame...
            if deck_c_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_c_image_2.frameNStart = frameN  # exact frame index
                deck_c_image_2.tStart = t  # local t and not account for scr refresh
                deck_c_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_c_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_c_image_2.started')
                # update status
                deck_c_image_2.status = STARTED
                deck_c_image_2.setAutoDraw(True)
            
            # if deck_c_image_2 is active this frame...
            if deck_c_image_2.status == STARTED:
                # update params
                pass
            
            # *deck_d_image_2* updates
            
            # if deck_d_image_2 is starting this frame...
            if deck_d_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deck_d_image_2.frameNStart = frameN  # exact frame index
                deck_d_image_2.tStart = t  # local t and not account for scr refresh
                deck_d_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deck_d_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deck_d_image_2.started')
                # update status
                deck_d_image_2.status = STARTED
                deck_d_image_2.setAutoDraw(True)
            
            # if deck_d_image_2 is active this frame...
            if deck_d_image_2.status == STARTED:
                # update params
                pass
            
            # *arrow_image_2* updates
            
            # if arrow_image_2 is starting this frame...
            if arrow_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_image_2.frameNStart = frameN  # exact frame index
                arrow_image_2.tStart = t  # local t and not account for scr refresh
                arrow_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow_image_2.started')
                # update status
                arrow_image_2.status = STARTED
                arrow_image_2.setAutoDraw(True)
            
            # if arrow_image_2 is active this frame...
            if arrow_image_2.status == STARTED:
                # update params
                pass
            
            # *practice_response* updates
            waitOnFlip = False
            
            # if practice_response is starting this frame...
            if practice_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_response.frameNStart = frameN  # exact frame index
                practice_response.tStart = t  # local t and not account for scr refresh
                practice_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_response.started')
                # update status
                practice_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practice_response.status == STARTED and not waitOnFlip:
                theseKeys = practice_response.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _practice_response_allKeys.extend(theseKeys)
                if len(_practice_response_allKeys):
                    practice_response.keys = _practice_response_allKeys[-1].name  # just the last key pressed
                    practice_response.rt = _practice_response_allKeys[-1].rt
                    practice_response.duration = _practice_response_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_3
            conditions = {
                'deck_a_2': {'Reward': 100, 'Penalty': -250},
                'deck_b_2': {'Reward': 100, 'Penalty': -1150},
                'deck_c_2': {'Reward': 50, 'Penalty': -25},
                'deck_d_2': {'Reward': 50, 'Penalty': -200},
            }
            def to_persian_number(number):
                english_to_persian = {
                    '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
                    '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
                }
            
            
            if practice_response.keys:
                if 'f' in practice_response.keys:
                    chosen_action = 'deck_' + chr(97 + current_position) + '_2'  # Dynamically select the deck based on arrow position
                    print(f"Chosen Action: {chosen_action}")
                    outcome = simulateOutcome(chosen_action, conditions)
                    print(f"Outcome: {outcome}")
                    net_worth_practice += outcome
                    print(f"Net Worth Practice: {net_worth_practice}")
                    previous_choice_practice = chosen_action 
                    previous_outcome_practice = outcome
                    feedback_text_2 = f"شما بازی کردید\n\n نتیجه:  {(outcome)}\n\n  جمع پول شما اکنون:  {(net_worth_practice)}"
                elif 'j' in practice_response.keys:
                    chosen_action = 'pass'
                    previous_choice_practice = chosen_action 
                    previous_outcome_practice = 0
                    feedback_text_2 = f"شما بازی نکردید\n\n  جمع پول شما اکنون:  {(net_worth_practice)}"
            
                feedback_display_2.setText(feedback_text_2)  # Update the text component with feedback_text_2
                print(f"Feedback Text: {feedback_text_2}")
            
                # Randomly move the arrow to a new position for the next trial
                current_position = random.randint(0, len(deck_positions) - 1)
                
                continueRoutine = False  # End the routine after making a choice
            
            
            
            
            
            # *practice_info_display* updates
            
            # if practice_info_display is starting this frame...
            if practice_info_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_info_display.frameNStart = frameN  # exact frame index
                practice_info_display.tStart = t  # local t and not account for scr refresh
                practice_info_display.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_info_display, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_info_display.started')
                # update status
                practice_info_display.status = STARTED
                practice_info_display.setAutoDraw(True)
            
            # if practice_info_display is active this frame...
            if practice_info_display.status == STARTED:
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
                practice_task.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_task.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_task" ---
        for thisComponent in practice_task.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_task
        practice_task.tStop = globalClock.getTime(format='float')
        practice_task.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_task.stopped', practice_task.tStop)
        # check responses
        if practice_response.keys in ['', [], None]:  # No response was made
            practice_response.keys = None
        practice_loop.addData('practice_response.keys',practice_response.keys)
        if practice_response.keys != None:  # we had a response
            practice_loop.addData('practice_response.rt', practice_response.rt)
            practice_loop.addData('practice_response.duration', practice_response.duration)
        # Run 'End Routine' code from code_3
        # Check if it’s the last practice trial
        if practice_loop.thisN == practice_loop.nTotal - 1:
            net_worth = 2000  # Reset net worth to 2000 after practice
            practice_completed = True  # Set the flag to indicate practice is completed
            print(f"End of Practice Loop: Net Worth Reset to {net_worth}")
        
        # the Routine "practice_task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback_2" ---
        # create an object to store info about Routine Feedback_2
        Feedback_2 = data.Routine(
            name='Feedback_2',
            components=[feedback_display_2],
        )
        Feedback_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Feedback_2
        Feedback_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Feedback_2.tStart = globalClock.getTime(format='float')
        Feedback_2.status = STARTED
        thisExp.addData('Feedback_2.started', Feedback_2.tStart)
        Feedback_2.maxDuration = None
        # keep track of which components have finished
        Feedback_2Components = Feedback_2.components
        for thisComponent in Feedback_2.components:
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
        
        # --- Run Routine "Feedback_2" ---
        # if trial has changed, end Routine now
        if isinstance(practice_loop, data.TrialHandler2) and thisPractice_loop.thisN != practice_loop.thisTrial.thisN:
            continueRoutine = False
        Feedback_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_display_2* updates
            
            # if feedback_display_2 is starting this frame...
            if feedback_display_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_display_2.frameNStart = frameN  # exact frame index
                feedback_display_2.tStart = t  # local t and not account for scr refresh
                feedback_display_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_display_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_display_2.started')
                # update status
                feedback_display_2.status = STARTED
                feedback_display_2.setAutoDraw(True)
            
            # if feedback_display_2 is active this frame...
            if feedback_display_2.status == STARTED:
                # update params
                pass
            
            # if feedback_display_2 is stopping this frame...
            if feedback_display_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_display_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_display_2.tStop = t  # not accounting for scr refresh
                    feedback_display_2.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_display_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_display_2.stopped')
                    # update status
                    feedback_display_2.status = FINISHED
                    feedback_display_2.setAutoDraw(False)
            
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
                Feedback_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback_2" ---
        for thisComponent in Feedback_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Feedback_2
        Feedback_2.tStop = globalClock.getTime(format='float')
        Feedback_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Feedback_2.stopped', Feedback_2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Feedback_2.maxDurationReached:
            routineTimer.addTime(-Feedback_2.maxDuration)
        elif Feedback_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice_loop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if practice_loop.trialList in ([], [None], None):
        params = []
    else:
        params = practice_loop.trialList[0].keys()
    # save data for this loop
    practice_loop.saveAsExcel(filename + '.xlsx', sheetName='practice_loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "after_practice" ---
    # create an object to store info about Routine after_practice
    after_practice = data.Routine(
        name='after_practice',
        components=[key_resp_4, after_practice_image],
    )
    after_practice.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_4
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # store start times for after_practice
    after_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    after_practice.tStart = globalClock.getTime(format='float')
    after_practice.status = STARTED
    thisExp.addData('after_practice.started', after_practice.tStart)
    after_practice.maxDuration = None
    # keep track of which components have finished
    after_practiceComponents = after_practice.components
    for thisComponent in after_practice.components:
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
    
    # --- Run Routine "after_practice" ---
    after_practice.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *after_practice_image* updates
        
        # if after_practice_image is starting this frame...
        if after_practice_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            after_practice_image.frameNStart = frameN  # exact frame index
            after_practice_image.tStart = t  # local t and not account for scr refresh
            after_practice_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(after_practice_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'after_practice_image.started')
            # update status
            after_practice_image.status = STARTED
            after_practice_image.setAutoDraw(True)
        
        # if after_practice_image is active this frame...
        if after_practice_image.status == STARTED:
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
            after_practice.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in after_practice.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "after_practice" ---
    for thisComponent in after_practice.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for after_practice
    after_practice.tStop = globalClock.getTime(format='float')
    after_practice.tStopRefresh = tThisFlipGlobal
    thisExp.addData('after_practice.stopped', after_practice.tStop)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "after_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop = data.TrialHandler2(
        name='loop',
        nReps=1.0, 
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
            components=[deck_a_image, deck_b_image, deck_c_image, deck_d_image, arrow_image, response_key, info_display],
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
        # Run 'Begin Routine' code from code_2
        if practice_completed:
            print(f"Before Main Task: Net Worth is {net_worth}")
            practice_completed = False  # Reset the flag
        
        # Update the display text to show current total and previous choice
        info_text = f"جمع پول شما: {(net_worth)}\n\nانتخاب قبلی شما: {(previous_outcome)}"
        info_display.setText(info_text)  # Update the text component with info_text
        
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
            
            # *info_display* updates
            
            # if info_display is starting this frame...
            if info_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                info_display.frameNStart = frameN  # exact frame index
                info_display.tStart = t  # local t and not account for scr refresh
                info_display.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(info_display, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'info_display.started')
                # update status
                info_display.status = STARTED
                info_display.setAutoDraw(True)
            
            # if info_display is active this frame...
            if info_display.status == STARTED:
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
                previous_choice = chosen_action
                previous_outcome = outcome
                log_data('main', chosen_action, outcome, net_worth)
                feedback_text = f"شما بازی کردید\n\n نتیجه:  {(outcome)}\n\n  جمع پول شما اکنون:  {(net_worth)}"
            elif 'j' in response_key.keys:
                chosen_action = 'pass'
                previous_choice = chosen_action 
                previous_outcome = 0
                log_data('main', chosen_action, 0, net_worth)
                feedback_text = f"شما بازی نکردید\n\n  جمع پول شما اکنون:  {(net_worth)}"
        
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
        
    # completed 1.0 repeats of 'loop'
    
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
    # Run 'Begin Routine' code from code
    final_message_text =f"پایان بازی\n\n مبلغ نهایی شما:{(net_worth)} \n\nپژوهشگران:\n Parinaz Khosravani \n Farzad Soleimani \n\n برای خروج کلید Esc را فشار دهید."
    final_message.setText(final_message_text)
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
