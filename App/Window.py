import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from Model import Detector

class Window(tk.Tk):
    cam_on = False
    vid = None
    start = False

    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Eye Refresh App')
        self.resizable(0,0)

        # Greetings words
        self.greetings = ttk.Label(text = "Hello welcome to the App")
        self.greetings.grid(row = 0, column = 0)

        # Webcam
        self.canvas = tk.Canvas(bg = "black", height=480, width=640)
        self.canvas.create_text(330, 240, text="Camera is Turned Off", fill="white")
        self.canvas.grid(row = 1, column = 0)

        # button
        self.button1 = ttk.Button(text="Toggle Webcam", command = self.toggle_webcam)
        self.button1.grid(row = 2, column = 0)

        # timer options
        self.timer_label = ttk.Label(text="Select Time Threshold")
        self.timer_label.grid(row=3, column=0)
        self.n_time = tk.StringVar()
        self.time_choosen = ttk.Combobox(width = 20, textvariable = self.n_time)
        self.time_choosen['values'] = ('20 minutes', '45 minutes', '60 minutes')
        self.time_choosen.current(0)
        self.time_choosen.grid(row=4, column=0)

        # Start button
        self.start_btn = ttk.Button(text="Start", command = self.start_btn_action)
        self.start_btn.grid(row=5, column=0)

        # Stop Button
        self.stop_btn = ttk.Button(text = "Stop", command = self.stop_btn_action)
        self.stop_btn.grid(row=6, column=0)


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

        self.canvas.grid(row = 1, column = 0)
    
    def start_btn_action(self):
        self.start = True
    
    def stop_btn_action(self):
        self.start = False


    def show_frame(self):
        if(self.cam_on):

            ret, _ = self.vid.read()
            if(ret):

                # Get the latest frame and convert into Image
                cv2image = cv2.cvtColor(self.vid.read()[1],cv2.COLOR_BGR2RGB)
                rendered_image = Detector.test(cv2image) if self.start else cv2image
                img = Image.fromarray(rendered_image)

                # Convert image to PhotoImage
                imgtk = ImageTk.PhotoImage(image = img)
                self.canvas.imgtk = imgtk
                self.canvas.configure(image=imgtk)

                # Repeat after an interval to capture continiously
                self.canvas.after(20, self.show_frame)


       







