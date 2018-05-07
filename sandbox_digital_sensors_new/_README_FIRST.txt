The modules in this workshop help you learn:

  -- What DIGITAL sensors are, and how to use them:
       -- By POLLING the sensor's STATE, or
       -- By setting a CALLBACK function to run when the sensor's state CHANGES
            (EVENT-DRIVEN programming)

  -- How to use the particular digital sensors:
       -- ev3.TouchSensor
       -- ev3.Button (controls the 4 buttons on the ev3 BRICK)
       -- ev3.RemoteControl (each such object controls the 4 buttons on the Infrared (IR) Beacon,
            under 1 of its four CHANNELS)

   -- How to use these other devices on the ev3 robot:
       -- ev3.Sound
       -- ev3.Leds
       -- ev3.Screen

THE BIG PICTURE:

------------------------ What will I LEARN from this module? ------------------------

  - A DIGITAL sensor is a sensor that returns 1 or 0.
      - You can interpret the 1 and 0 as True/False, On/Off, Open/Shut, Pressed/Not-Pressed, etc.
      
  - Your EV3 robot has the following digital sensors:
       - A TOUCH sensor (ev3.TouchSensor)
       - 4 BUTTONS on the ev3 BRICK (all 4 are controlled by a SINGLE ev3.Button object)
       - 4 BUTTONS on the ev3 Infrared (IR) Beacon
           - All 4 are controlled by a SINGLE ev3.RemoteControl object
           - The IR Beacon has 4 independent channels (set by the red SWITCH on the IR Beacon).
             Each ev3.RemoteControl object specifies ONE channel.

  - Digital sensors have a STATE (1 or 0).
      - The code can ask for a digital sensor's state at any time.
      - The exact mechanism for doing so depends on the type of digital sensor.  See the handout.

  - The code can interact with a digital sensor in either of two ways:
  
      1. POLLING using the digital sensor's STATE.
           This means running a WHILE loop that repeatedly asks the digital sensor for its current state,
           breaking out of the loop when the state changes to the desired state, e.g.:
           
              touch_sensor = ev3.TouchSensor()
              while True:
                  if touch_sensor.is_pressed:
                      break
           
      2. RESPONDING to the EVENT of the digital sensor CHANGING its state (from 1 to 0, or from 0 to 1).
           - This approach uses CALLBACK functions that are "called back" when the event occurs.
               Using this approach is called EVENT-DRIVEN programming.
           - The exact mechanism for doing so depends on the type of digital sensor.  See the handout.
           - Not all sensors allow this EVENT-DRIVEN approach.
           
           Here is a short example that we will study in detail later:
           
           def blah(state):
              # The code in  foo  (below) arranges for this function to be called when the RIGHTMOST
              # of the 4 buttons on the ev3 BRICK changes state (i.e., is pressed, or is released).
              #   The parameter  state  will be set to 1 (aka True, pressed, etc) by the caller
              #   if the digital sensor just changed state to 1, else it will be set to 0 (aka False, released, etc).
              ...
              
            def foo():
              brick_buttons_sensor = ev3.Button()
              brick_buttons_sensor.on_right = blah

  - You will also learn how to make images appear on the ev3 brick's SCREEN (ev3.
