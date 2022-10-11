import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from Model import Detector


class Window(tk.Tk):
    cam_on = False
    vid = None
    start = False
    counter = 0
    face_is_detected = False
    eye_is_detected = False
    time_threshold = 0

    def __init__(self):
        super().__init__()
        
        # Set Azure Theme
        self.style = ttk.Style(self)
        self.tk.call('source', 'App/azure.tcl')
        self.style.theme_use('azure')

        # configure the root window
        self.title('Eye Refresh App')
        self.resizable(0,0)

        # Webcam
        self.canvas = tk.Canvas(bg = "black", height=480, width=640)
        self.canvas.create_text(330, 240, text="Camera is Turned Off", fill="white")
        self.canvas.grid(row = 0, column = 0, padx=10, pady=10, rowspan = 9)

        # button
        self.button1 = ttk.Button(text="Toggle Webcam", command = self.toggle_webcam)
        self.button1.grid(row = 0, column = 1)

        # timer options
        self.timer_label = ttk.Label(text="Select Time Threshold")
        self.timer_label.grid(row = 1, column = 1)
        self.n_time = tk.StringVar()
        self.time_choosen = ttk.Combobox(width = 20, textvariable = self.n_time)
        self.time_choosen['values'] = ('10 Seconds', '15 Seconds', '20 Seconds')
        self.time_choosen.current(0)
        self.time_choosen.grid(row = 2, column = 1, pady = 1)

        # Start button
        self.start_btn = ttk.Button(text="Start", command = self.start_btn_action)
        self.start_btn.grid(row=3, column=1,pady=1)

        # Stop Button
        self.stop_btn = ttk.Button(text = "Stop", command = self.stop_btn_action)
        self.stop_btn.grid(row=4, column=1, pady=1)

        # Reset Button
        self.reset_btn = ttk.Button(text = "Reset", command = self.reset_btn_action)
        self.reset_btn.grid(row = 5, column=1)

        # Timer info
        self.timer_label = ttk.Label(text= "Time of Eye interacted with The Screen :")
        self.timer_label.grid(row=6, column=1, padx=(0,10))
        self.timer_minutes = tk.Label(text = "00 Mins", font=("Helvetica", 20))
        self.timer_minutes.grid(row=7, column=1)
        self.timer_seconds = tk.Label(text = "00 Secs", font=("Helvetica", 20))
        self.timer_seconds.grid(row=8, column=1)

    
    def toggle_webcam(self):
        if(self.cam_on):
            self.cam_on = False
            self.vid.release()
            self.canvas = tk.Canvas(bg = "black", height=480, width=640)
            self.canvas.create_text(330, 240, text="Camera is Turned Off", fill="white")
        else :
            self.cam_on = True
            self.vid = cv2.VideoCapture(0) 
            self.canvas = ttk.Label()
            self.show_frame()
            self.start = False

        self.canvas.grid(row = 0, column = 0, padx=2, pady=2, rowspan=9)
    

    def start_btn_action(self):
        if (self.cam_on) :
            self.start = True
            self.set_selected_time_threshold()
            print(self.time_threshold)
            self.counter_label()
    
    
    def set_selected_time_threshold(self):
        if(self.time_choosen.get() == "10 Seconds"):
            self.time_threshold = 10
        elif(self.time_choosen.get() == "15 Seconds"):
            self.time_threshold = 15
        else:
            self.time_threshold = 20


    def counter_label(self):
        def count():
            if(self.start and self.cam_on):
                secs = self.counter % 60
                mins = self.counter // 60
                new_label_seconds = str(secs) if secs > 9 else "0" + str(secs)
                new_label_minutes = str(mins) if mins > 9 else "0" + str(mins)
                self.timer_minutes['text'] = new_label_minutes + " Mins"
                self.timer_seconds['text'] = new_label_seconds + " Secs"

                if(self.counter == self.time_threshold):
                    messagebox.showinfo("Time is Up","Lets see around before you get back into the screen")
                    return 

                print("Face is Detected : ",self.face_is_detected)
                print("Eye is Detected : ",self.eye_is_detected)

                if(not(self.face_is_detected or self.eye_is_detected)):
                    self.counter -= 1

                self.counter += 1

                self.timer_seconds.after(1000, count)

        count()


    def stop_btn_action(self):
        self.start = False
    
    def reset_btn_action(self):
        self.counter = 0
        self.timer_minutes['text'] = "00 Mins"
        self.timer_seconds['text'] = "00 Secs"

    def show_frame(self):
        if(self.cam_on):

            ret, _ = self.vid.read()
            if(ret):

                # Get the latest frame and convert into Image
                cv2image = cv2.cvtColor(self.vid.read()[1],cv2.COLOR_BGR2RGB)
                cv2image = cv2.resize(cv2image, (640,480))

                if (self.start):
                    rendered_image, self.face_is_detected, self.eye_is_detected = Detector.get_face_and_eye(cv2image)
                else:
                    rendered_image = cv2image

                img = Image.fromarray(rendered_image)

                # Convert image to PhotoImage
                imgtk = ImageTk.PhotoImage(image = img)
                self.canvas.imgtk = imgtk
                self.canvas.configure(image=imgtk)

                # Repeat after an interval to capture continiously
                self.canvas.after(20, self.show_frame)
