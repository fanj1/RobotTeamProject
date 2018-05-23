import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():

    root = tkinter.Tk()
    root.title("MQTT Remote")
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    main_frame = ttk.Frame(root, padding=50, relief='raised')
    main_frame.grid()

    speed_Label = ttk.Label(main_frame, text="Enter Speed (0-200)")
    speed_Label.grid(row=0, column=1)
    speed = ttk.Entry(main_frame, width=8)
    speed.insert(0, "200")
    speed.grid(row=1, column=1)




    # start running
    # start = ttk.Button(main_frame,text = "Common Mode")
    # start.grid(row =2, column=0)
    #
    # start['command'] = lambda: start_running(mqtt_client, speed)
    # root.bind('<Left>', lambda event: start_running(mqtt_client, speed))

    # searching mode
    searching = ttk.Button(main_frame, text="Mission Start")
    searching.grid(row=2, column=1)
    searching['command'] = lambda: searching_mode(mqtt_client, speed)
    root.bind('<Right>', lambda event: searching_mode(mqtt_client, speed))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Close window only")
    q_button.grid(row=3, column=1)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Finish")
    e_button.grid(row=4, column=1)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


# def start_running(mqtt_client, speed):
#     print("start running")
#     white_value = 2
#     black_value = 1
#     mqtt_client.send_message("start_running",[int(speed.get()),white_value,black_value])

def searching_mode(mqtt_client, speed):
    print("searching mode start")
    white_value = 2
    black_value = 1
    mqtt_client.send_message("searching_mode",[int(speed.get()),white_value,black_value])

def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()

main()
