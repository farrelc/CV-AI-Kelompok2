import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk,ImageDraw, ImageFont
import cv2
from Model import Detector


class Window(tk.Tk):
    cam_on = False
    vid = None
    start = False
    counter = 0
    face_is_detected = False
    eyes_is_closed = False
    time_threshold = 0
    time_to_reset = 0

    def __init__(self):
        super().__init__()
        
        # Set Azure Theme
        self.style = ttk.Style(self)
        self.tk.call('source', 'App/azure.tcl')
        self.style.theme_use('azure')

        # configure the root window
        self.title('Eye Refresh Alert')
        self.resizable(0,0)

        # Add icon
        self.iconphoto(False, tk.PhotoImage(file = 'App/icon/eye-line.PNG'))

        # Webcam
        self.canvas = tk.Canvas(bg = "black", height=480, width=640)
        self.canvas.create_text(330, 240, text="The camera is turned off.", fill="white",font=("Helvetica", 15))
        self.canvas.grid(row = 0, column = 0, padx=10, pady=10, rowspan = 9)

        # button
        self.button1 = ttk.Button(text="Toggle Webcam", command = self.toggle_webcam)
        self.button1.grid(row = 0, column = 1)

        # timer options
        self.timer_label = ttk.Label(text="Select Time Threshold")
        self.timer_label.grid(row = 1, column = 1)
        self.n_time = tk.StringVar()
        self.time_choosen = ttk.Combobox(width = 20, textvariable = self.n_time)
        self.time_choosen['values'] = ('20 Minutes', '40 Minutes', '60 Minutes')
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
        self.reset_btn['state'] = 'disabled'

        # Timer info
        self.timer_label = ttk.Label(text= "Total time of the eyes interacting with the screen :")
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
            self.canvas.create_text(330, 240, text="The camera is turned off.", fill="white", font=("Helvetica", 15))
        else :
            self.cam_on = True
            self.vid = cv2.VideoCapture(0) 
            self.canvas = ttk.Label()
            self.show_frame()
            self.start = False
            

        self.canvas.grid(row = 0, column = 0, padx=2, pady=2, rowspan=9)
    

    def start_btn_action(self):
        if (self.cam_on and not self.start) :
            self.start = True
            self.set_selected_time_threshold()
            self.counter_label()
            self.reset_btn['state'] = 'disabled'
            
    
    def set_selected_time_threshold(self):
        if(self.time_choosen.get() == "20 Minutes"):
            self.time_threshold = 20*60
        elif(self.time_choosen.get() == "40 Minutes"):
            self.time_threshold = 40*60
        else:
            self.time_threshold = 60*60


    def counter_label(self):
        def count():
            if(self.start and self.cam_on):

                # Check face and eyes
                print(self.eyes_is_closed)
                if(self.face_is_detected == False or self.eyes_is_closed == True):
                    # if face is not deteced or eyes is closed then do not update time counter but update time reset
                    self.time_to_reset += 1
                else :
                    # Update counter if face or eyes is detected again
                    self.counter += 1
                    self.time_to_reset = 0

                # Update Second and Minutes from counter
                secs = self.counter % 60
                mins = self.counter // 60

                # Update Timer GUI
                new_label_seconds = str(secs) if secs > 9 else "0" + str(secs)
                new_label_minutes = str(mins) if mins > 9 else "0" + str(mins)
                self.timer_minutes['text'] = new_label_minutes + " Mins"
                self.timer_seconds['text'] = new_label_seconds + " Secs"
                
                # Reset time if face and eyes not deteced for certain time (This experiment using 5 minutes)              
                if(self.time_to_reset == 5*60):
                    self.start = False
                    self.time_to_reset = 0
                    self.reset_btn_action()
                    messagebox.showinfo("Reset", "We Reset the Timer because you were not in front of the Screen for 5 minutes")
                    return 

                # Check Time limit
                if(self.counter == self.time_threshold):
                    self.start = False
                    self.reset_btn_action()
                    messagebox.showinfo("Time is Up", f"It's been {self.time_choosen.get()}. Let's see around before you get back into the screen.")
                    return 
    
                # Call function recursively
                self.timer_seconds.after(1000, count)

        count()


    def stop_btn_action(self):
        if(self.start):
            self.start = False
            self.reset_btn['state'] = 'normal'
    

    def reset_btn_action(self):
        self.counter = 0
        self.timer_minutes['text'] = "00 Mins"
        self.timer_seconds['text'] = "00 Secs"
    
    
    def show_frame(self):
        if(self.cam_on):

            ret, frame = self.vid.read()
            if(ret):

                # Get the latest frame and convert into Image
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2image = cv2.resize(cv2image, (640,480), interpolation=cv2.INTER_CUBIC)

                if (self.start):
                    # Rander image from model/detector
                    rendered_image, self.face_is_detected, self.eyes_is_closed = Detector.get_face_and_eye(cv2image)
                    img = Image.fromarray(rendered_image)
                    final_img = self.face_eye_stats(img)
                else:
                    final_img = Image.fromarray(cv2image)


                # Convert image to PhotoImage
                imgtk = ImageTk.PhotoImage(image = final_img)
                self.canvas.imgtk = imgtk
                self.canvas.configure(image=imgtk)
                
                # Repeat after an interval to capture continiously
                self.canvas.after(20, self.show_frame)
    
    
    def face_eye_stats(self, frame):
        draw = ImageDraw.Draw(frame)
        if(self.face_is_detected):
            if(self.eyes_is_closed == False):
                text = "Face Detected and Eyes Opened"
            else:
                text = "Face Detected but Eyes Closed"
            padding_bottom = 5
        else:
            text = "Face Not Detected"
            padding_bottom = 10

        left, top, right, bottom = draw.textbbox((10,10), text = "Status: " + text, font= ImageFont.truetype('arial.ttf', 25))
        draw.rectangle((left-5, top-5, right+5, bottom+padding_bottom), fill="black")
        draw.text((10,10), text = "Status: " + text, font=ImageFont.truetype('arial.ttf', 25), fill="white")

        return frame