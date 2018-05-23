def follow_white_line(self, speed, white_level, black_level):
    while True:
        intensity = self.color_sensor.ambient_light_intensity
        if intensity <= black_level:
            self.stop()
            self.turn_left(speed / 2, 1.5 * speed)
        elif intensity >= white_level:
            self.go_forward(speed, speed)
