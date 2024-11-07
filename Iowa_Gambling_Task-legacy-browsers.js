/*************************** 
 * Iowa_Gambling_Task *
 ***************************/


// store info about the experiment session:
let expName = 'Iowa_Gambling_Task';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.0196, 0.2549, 0.0196]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionRoutineBegin());
flowScheduler.add(InstructionRoutineEachFrame());
flowScheduler.add(InstructionRoutineEnd());
const loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loopLoopBegin(loopLoopScheduler));
flowScheduler.add(loopLoopScheduler);
flowScheduler.add(loopLoopEnd);



flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'conditions.xlsx', 'path': 'conditions.xlsx'},
    {'name': 'Card.jpg', 'path': 'Card.jpg'},
    {'name': 'arrow.png', 'path': 'arrow.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var InstructionClock;
var instruction;
var key_resp;
var Main_TaskClock;
var deck_a_image;
var deck_b_image;
var deck_c_image;
var deck_d_image;
var arrow_image;
var deck_positions;
var current_position;
var response_key;
var FeedbackClock;
var feedback_display;
var EndClock;
var thank_you_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instruction"
  InstructionClock = new util.Clock();
  instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction',
    text: 'در این بازی\nهدف شما این است که تا حد ممکن پول برنده شوید.\n\n برای هر دور\n نشان داده خواهد شد  یک فلش زرد، بالای یکی از چهار دسته کارت\nبه واسطه آن، میتوانید بین بازی کردن یا رد کردن آن کارت تصمیم بگیرید.\n\n اگر بازی کنید، می\u200cتوانید پول ببرید، اما همچنین ممکن است پول از دست بدهید (یا نه پول ببرید و نه از دست بدهید).\n اگر رد کنید، نه پول می\u200cبرید و نه پول از دست می\u200cدهید.\n\n برخی از دسته\u200cها سودآورتر از دیگر دسته\u200cها خواهند بود.\n',
    font: 'B koodak',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Main_Task"
  Main_TaskClock = new util.Clock();
  deck_a_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'deck_a_image', units : undefined, 
    image : 'Card.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.5), 0], 
    draggable: false,
    size : [0.25, 0.35],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  deck_b_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'deck_b_image', units : undefined, 
    image : 'Card.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.17), 0], 
    draggable: false,
    size : [0.25, 0.35],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  deck_c_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'deck_c_image', units : undefined, 
    image : 'Card.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.17, 0], 
    draggable: false,
    size : [0.25, 0.35],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  deck_d_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'deck_d_image', units : undefined, 
    image : 'Card.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.5, 0], 
    draggable: false,
    size : [0.25, 0.35],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  arrow_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'arrow_image', units : undefined, 
    image : 'arrow.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 1], 
    draggable: false,
    size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  // Run 'Begin Experiment' code from arrow_movement
  deck_positions = [[(- 0.5), 0], [0.5, 0], [(- 0.5), (- 0.5)], [0.5, (- 0.5)]];
  current_position = 0;
  arrow_image.pos = [deck_positions[current_position][0], (deck_positions[current_position][1] + 0.1)];
  
  response_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  feedback_display = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_display',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  thank_you_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'thank_you_text',
    text: 'Any text\n\nincluding line breaks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var InstructionMaxDurationReached;
var _key_resp_allKeys;
var InstructionMaxDuration;
var InstructionComponents;
function InstructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    InstructionMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('Instruction.started', globalClock.getTime());
    InstructionMaxDuration = null
    // keep track of which components have finished
    InstructionComponents = [];
    InstructionComponents.push(instruction);
    InstructionComponents.push(key_resp);
    
    InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction' ---
    // get current time
    t = InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction* updates
    if (t >= 0.0 && instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction.tStart = t;  // (not accounting for frame time here)
      instruction.frameNStart = frameN;  // exact frame index
      
      instruction.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction' ---
    InstructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var loop;
function loopLoopBegin(loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions.xlsx',
      seed: undefined, name: 'loop'
    });
    psychoJS.experiment.addLoop(loop); // add the loop to the experiment
    currentLoop = loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop.forEach(function() {
      snapshot = loop.getSnapshot();
    
      loopLoopScheduler.add(importConditions(snapshot));
      loopLoopScheduler.add(Main_TaskRoutineBegin(snapshot));
      loopLoopScheduler.add(Main_TaskRoutineEachFrame());
      loopLoopScheduler.add(Main_TaskRoutineEnd(snapshot));
      loopLoopScheduler.add(FeedbackRoutineBegin(snapshot));
      loopLoopScheduler.add(FeedbackRoutineEachFrame());
      loopLoopScheduler.add(FeedbackRoutineEnd(snapshot));
      loopLoopScheduler.add(loopLoopEndIteration(loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Main_TaskMaxDurationReached;
var _response_key_allKeys;
var Main_TaskMaxDuration;
var Main_TaskComponents;
function Main_TaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Main_Task' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Main_TaskMaxDurationReached = false;
    // update component parameters for each repeat
    response_key.keys = undefined;
    response_key.rt = undefined;
    _response_key_allKeys = [];
    psychoJS.experiment.addData('Main_Task.started', globalClock.getTime());
    Main_TaskMaxDuration = null
    // keep track of which components have finished
    Main_TaskComponents = [];
    Main_TaskComponents.push(deck_a_image);
    Main_TaskComponents.push(deck_b_image);
    Main_TaskComponents.push(deck_c_image);
    Main_TaskComponents.push(deck_d_image);
    Main_TaskComponents.push(arrow_image);
    Main_TaskComponents.push(response_key);
    
    Main_TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Main_TaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Main_Task' ---
    // get current time
    t = Main_TaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *deck_a_image* updates
    if (t >= 0.0 && deck_a_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      deck_a_image.tStart = t;  // (not accounting for frame time here)
      deck_a_image.frameNStart = frameN;  // exact frame index
      
      deck_a_image.setAutoDraw(true);
    }
    
    
    // *deck_b_image* updates
    if (t >= 0.0 && deck_b_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      deck_b_image.tStart = t;  // (not accounting for frame time here)
      deck_b_image.frameNStart = frameN;  // exact frame index
      
      deck_b_image.setAutoDraw(true);
    }
    
    
    // *deck_c_image* updates
    if (t >= 0.0 && deck_c_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      deck_c_image.tStart = t;  // (not accounting for frame time here)
      deck_c_image.frameNStart = frameN;  // exact frame index
      
      deck_c_image.setAutoDraw(true);
    }
    
    
    // *deck_d_image* updates
    if (t >= 0.0 && deck_d_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      deck_d_image.tStart = t;  // (not accounting for frame time here)
      deck_d_image.frameNStart = frameN;  // exact frame index
      
      deck_d_image.setAutoDraw(true);
    }
    
    
    // *arrow_image* updates
    if (t >= 0.0 && arrow_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arrow_image.tStart = t;  // (not accounting for frame time here)
      arrow_image.frameNStart = frameN;  // exact frame index
      
      arrow_image.setAutoDraw(true);
    }
    
    if (((t % 1) === 0)) {
        current_position = ((current_position + 1) % deck_positions.length);
        arrow_image.pos = [deck_positions[current_position][0], (deck_positions[current_position][1] + 0.1)];
    }
    
    
    // *response_key* updates
    if (t >= 0.0 && response_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_key.tStart = t;  // (not accounting for frame time here)
      response_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response_key.clearEvents(); });
    }
    
    if (response_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = response_key.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _response_key_allKeys = _response_key_allKeys.concat(theseKeys);
      if (_response_key_allKeys.length > 0) {
        response_key.keys = _response_key_allKeys[_response_key_allKeys.length - 1].name;  // just the last key pressed
        response_key.rt = _response_key_allKeys[_response_key_allKeys.length - 1].rt;
        response_key.duration = _response_key_allKeys[_response_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Main_TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Main_TaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Main_Task' ---
    Main_TaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Main_Task.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(response_key.corr, level);
    }
    psychoJS.experiment.addData('response_key.keys', response_key.keys);
    if (typeof response_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('response_key.rt', response_key.rt);
        psychoJS.experiment.addData('response_key.duration', response_key.duration);
        routineTimer.reset();
        }
    
    response_key.stop();
    // the Routine "Main_Task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackMaxDurationReached;
var FeedbackMaxDuration;
var FeedbackComponents;
function FeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Feedback' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    FeedbackMaxDurationReached = false;
    // update component parameters for each repeat
    feedback_display.setText(feedback_text);
    psychoJS.experiment.addData('Feedback.started', globalClock.getTime());
    FeedbackMaxDuration = null
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(feedback_display);
    
    FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function FeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Feedback' ---
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_display* updates
    if (t >= 0.0 && feedback_display.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_display.tStart = t;  // (not accounting for frame time here)
      feedback_display.frameNStart = frameN;  // exact frame index
      
      feedback_display.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_display.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_display.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Feedback' ---
    FeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Feedback.stopped', globalClock.getTime());
    if (FeedbackMaxDurationReached) {
        FeedbackClock.add(FeedbackMaxDuration);
    } else {
        FeedbackClock.add(1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndMaxDurationReached;
var EndMaxDuration;
var EndComponents;
function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    EndMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('End.started', globalClock.getTime());
    EndMaxDuration = null
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(thank_you_text);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End' ---
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thank_you_text* updates
    if (t >= 0.0 && thank_you_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thank_you_text.tStart = t;  // (not accounting for frame time here)
      thank_you_text.frameNStart = frameN;  // exact frame index
      
      thank_you_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (thank_you_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thank_you_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End' ---
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('End.stopped', globalClock.getTime());
    if (EndMaxDurationReached) {
        EndClock.add(EndMaxDuration);
    } else {
        EndClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
