#"Stopwatch: The Game"

# define global variables
import simplegui
counter = 0
#the toal no of hits
stop_total = 0
#successive no of hits
stop_hit = 0
sec_temp = 0
msec_temp = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    milisec = t % 10
    second = int(t/10)
    minutes = int(second / 60)
    if (second == 60):
        second = 0
        second_str = str(second)
    if (second > 60):
        second = second % 60
    if ((second >=0) and (second <=9)):
        second_str = "0" + str(second)
    else:
        second_str = str(second)
        
    #stoping the watch when minutes equal to 10
    if (minutes == 10):
        timer.stop()
    # taking values of local var in global var.
    global sec_temp, msec_temp
    sec_temp = second
    msec_temp = milisec
    
    return str(minutes) + ":" + second_str + "." + str(milisec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def stop_timer():
    global sec, msec, stop_hit, stop_total
    #checking if the timer is runnign
    status = timer.is_running()
    #if timer was running then clicked for stop add one in total
    if (status == True):
        stop_total += 1
    #if second is whole no. and timer was running then add in win point
    if ((sec_temp > 0) and (msec_temp == 0) and (status == True)):
        stop_hit += 1
    timer.stop()
    
def reset_timer():
    #stoping timer and reseting all values to zero
    timer.stop()
    global counter, stop_hit, stop_total
    stop_hit = 0
    stop_total = 0
    counter = 0
    
def start_timer():
    timer.start()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), (90, 150), 50, 'Red')
    canvas.draw_text(str(stop_hit) + "/" + str(stop_total), (250,30), 30, 'Red')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
#Adding buttons
start_button = frame.add_button("Start", start_timer, 150)
stop_button = frame.add_button("Stop", stop_timer, 150)
reset_button = frame.add_button("Reset", reset_timer, 150)

# start frame
frame.start()

