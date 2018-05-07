"""
The  DIGITAL SENSORS   workshop.
Also covers the ev3.Sound, ev3.Leds, and ev3.Screen classes.

Person 1: ev3.TouchSensor
Person 2: ev3.Button
Person 3: ev3.RemoteControl

Authors: David Fisher, David Mutchler and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2.  With your instructor, learn how to:
#   -- PAIR PROGRAM (perhaps as a trio today)
#   -- Use ITERATIVE ENHANCEMENT.

# When your   ** ENTIRE TEAM **   understands those concepts,
# change this TO-DO to DONE.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 3. Using pair programming and iterative enhancement,
#   with everyone on the team contributing and periodically changing typist,
#   implement and test   main  as specified below.
#   Introduce your OWN functions as appropriate as you do so.
# -----------------------------------------------------------------------------


def main():
    """
    When your program starts it should:
      -- SAY "Starting the IR Remote program"
      -- Call the   print_instructions   function (ALREADY IMPLEMENTED FOR YOU)

    Then, the program should use the IR Beacon as a remote control, as follows:

    In channel 1, the IR Beacon's buttons drive the robot around, as follows:

        -- PRESSING   RED_UP:
             - Makes the  LEFT LED   turn  GREEN
                 and starts the  LEFT motor   moving  FORWARD   at 75% speed.

        -- PRESSING   RED_DOWN:
             - Makes the  LEFT LED   turn  RED
                 and starts the  LEFT motor   moving  BACKWARD  at 75% speed.

        -- PRESSING   BLUE_UP:
             - Makes the  RIGHT LED  turn  GREEN
                 and starts the  RIGHT motor  moving  FORWARD   at 75% speed.

       -- PRESSING   BLUE_DOWN:
             - Makes the  RIGHT LED  turn  RED
                 and starts the  RIGHT motor  moving  BACKWARD  at 75% speed.

        -- RELEASING any button:
             - TURNS OFF the corresponding LED
                 and STOPS the corresponding motor.

           For example, releasing the RED_UP button turns off the LEFT LED
             and stops the LEFT motor.

    The user should be able to use one RED button (for the LEFT motor)
    and one BLUE button (for the RIGHT motor) at the same time.
    For example:
      - while pressing both RED_UP and BLUE_DOWN,
          the robot should SPIN clockwise
          with the LEFT LED being GREEN and the RIGHT LED being RED.

    In channel 2, the IR Beacon's buttons control the robot's ARM/CLAW,
    as follows:

        -- PRESSING   RED_UP    (in channel 2):
             causes the arm/claw to go UP until the touch sensor is pressed

        -- PRESSING   RED_DOWN  (in channel 2):
             causes the arm/claw to go DOWN 14.2 revolutions of the motor

        -- PRESSING  BLUE_UP    (in channel 2):
             -- does a RED_UP action followed by a BLUE_DOWN action.

    Pressing the BACK button:
      -- STOPS both motors.
      -- Turns ON both LEDs to AMBER.
      -- SAYS "Goodbye"
      -- exits the program.
    """

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
