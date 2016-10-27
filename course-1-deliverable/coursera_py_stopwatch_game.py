import simplegui

counter = 0
stop = True
success_attempts = 0
total_attempts = 0

def increment():
    global counter
    counter += 1

def format(t):
    tenth_sec = (t) % 10
    sec = int(t / 10) % 10
    minutes = int(t / 600) % 600
    ten_min = int(t / 100) % 6
    time_formatted = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return time_formatted
  
def start():
    timer.start()

def stop():
    global success_attempts, total_attempts, stop, tenth_sec
    if stop:
        if counter % 10 == 0 and counter != 0:
            success_attempts += 1
            total_attempts += 1
        elif counter != 0:
            total_attempts += 1
        stop = False
    else:                
        if counter % 10 == 0 and counter != 0:
            total_attempts += 1
            success_attempts += 1
        elif counter != 0:
            total_attempts += 1
        stop = True
    timer.stop()

def reset():
    global counter, success_attempts, total_attempts
    success_attempts = 0
    total_attempts = 0
    counter = 0
    stop = True
    timer.stop()


    
def draw(canvas):
    global time_formatted, stop
    time_formatted = format(counter)
    canvas.draw_text(str(time_formatted), [130,150], 20, "white")
    canvas.draw_text(str(success_attempts) + "/" + str(total_attempts), [260,20], 20, "white")

frame = simplegui.create_frame("test", 300,300)
frame.set_draw_handler(draw)
frame.add_button("Start/Resume", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
timer = simplegui.create_timer(100,increment)
frame.start()
