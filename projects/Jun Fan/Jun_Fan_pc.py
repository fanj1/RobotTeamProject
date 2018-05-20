"""
This is the final project of CSSE120, 2018 Spring

Author: Jun Fan
"""

import tkinter
from tkinter import ttk
import robot_controller as robo
import mqtt_remote_method_calls as com


def main():
    # DONE: 2. Setup an mqtt_client.  Notice that since you don't need to receive any messages you do NOT need to have
    # a MyDelegate class.  Simply construct the MqttClient with no parameter in the constructor (easy).

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    speed_label = ttk.Label(main_frame, text="Speed")
    speed_label.grid(row=0, column=1)
    speed_entry = ttk.Entry(main_frame, width=8)
    speed_entry.insert(0, "200")
    speed_entry.grid(row=1, column=1)

    number_label = ttk.Label(main_frame, text="Number to pick up")
    number_label.grid(row=0, column=0)
    number_entry = ttk.Entry(main_frame, width=8)
    number_entry.insert(0, "3")
    number_entry.grid(row=1, column=0)

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    # Buttons for start
    start_button = ttk.Button(main_frame, text="Start")
    start_button.grid(row=3, column=0)
    start_button['command'] = lambda: start(mqtt_client, speed_entry, number_entry)
    root.bind('<Up>', lambda event: start(mqtt_client, speed_entry, number_entry))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=4, column=1)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<Up>', lambda event: stop(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=0)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=1)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def start(mqtt_client, speed_entry, number_entry):
    print("start")
    mqtt_client.send_message("start", [speed_entry.get(), number_entry.get()])


def stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


def feedback(count):
    print('Cleaned one rubbish! Total amount cleaned:', count)
    print()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
