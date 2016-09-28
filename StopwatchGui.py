import simplegui

#global
c,sec,mi=0,0,0
msg="0:0:0"
#handlers
def tick():
    global c,mi,sec
    s= str(mi)+":"+str(sec)+":"+str(c)
    
    update(s)
    c+=1
    if c is 10:
        sec=sec+1
        c=0
        if sec is 60:
            mi=mi+1
            sec=0
def update(s):
    global msg
    msg=s
def start():
    global t
    t=simplegui.create_timer(100,tick)
    tick()
    t.start()
    
def stop():
    global t
    t.stop()
def reset():
    global c,mi,sec,t
    c,sec,mi=0,0,0
    t.stop()
    tick()
def draw(can):
    global msg
    can.draw_text(msg,[150,150],40,"Red")
    #frame
f=simplegui.create_frame("Stopwatch",400,300)
f.set_draw_handler(draw)
f.add_button("Start",start,100)
f.add_button("Stop",stop,100)
f.add_button("Reset",reset,100)


f.start()
