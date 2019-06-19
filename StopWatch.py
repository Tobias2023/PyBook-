#Gui library
import tkinter as tk

timer = -1
running = False
def timer_label(label):
    def count():
        if running:
            global timer

            # This is for the inital delay.
            if timer ==-1:
                display="3 2 1..."
            else:
                display=str(timer)

            label['text']=display #Alternative: label.config(text=display)
            label.after(1000, count)
            timer += 1
    #Start counting... 
    count()

#Start function 
def Start(label):
    global running
    running=True
    timer_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

#Stop Function
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
        

#Reset function
def Reset(label):
    global counter
    counter=-1
        
                
    # Reset pressed after stop
    if running ==False:
        reset['state']='disable'
        label['text']='Stopwatch'

    #Reset while stopwatch is counting
    else:
        label['text']='Starting...'

root = tk.Tk()
root.title("Stopwatch")

#Gui Window
root.minsize(width=350, height=170)
root.configure(background='black')
label = tk.Label(root, text="Stopwatch", fg="white", bg="black", font="Verdana 30 bold")
label.pack()
start = tk.Button(root, text='Start', width=15, command=lambda: Start(label))
stop = tk.Button(root, text='Stop', width=15, state='disabled', command=Stop)
reset = tk.Button(root, text='Reset', width=15, state='disabled', command=lambda:Reset(label))
start.pack()
stop.pack()
reset.pack()
root.mainloop()
    
    
