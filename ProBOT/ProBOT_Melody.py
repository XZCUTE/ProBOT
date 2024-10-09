import tkinter as tk
import datetime
import webbrowser
import subprocess
import pyttsx3
import speech_recognition as sr
import threading  
import queue
import pytube
import time

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ProBOT Melody")
        self.root.geometry("800x600")
        self.root.configure(bg='#eba4e2')
        self.root.resizable(False, False)

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 140)
        self.engine.setProperty('volume', 1)

        self.voice_mode = False

        self.speak_queue = queue.Queue()
        threading.Thread(target=self.process_speech_queue, daemon=True).start()

        self.Melody_frame = tk.Frame(root, bg='#6a48a0', bd=2, relief="groove")
        self.Melody_frame.place(x=10, y=10, width=200, height=230)

        self.Melody_label = tk.Label(self.Melody_frame, text="Melody", bg='#6a48a0', fg="White", font=("Arial", 12, "bold"))
        self.Melody_label.pack()

        self.load_Melody_image()

        self.voice_button = tk.Button(root, text="Voice Mode", command=self.toggle_voice_mode, bg='white', fg='black', font=("Arial", 12, "bold"))
        self.voice_button.place(x=25, y=450, width=180, height=50)

        self.text_display = tk.Text(root, bg='#ea80fc', fg='white', font=("Arial", 12), wrap='word')
        self.text_display.place(x=220, y=10, width=570, height=500)
        self.text_display.config(state=tk.DISABLED)

        self.input_field = tk.Entry(root, bg='white', fg='black', font=("Arial", 12))
        self.input_field.place(x=10, y=520, width=780, height=50)
        self.input_field.bind("<Return>", self.process_command)

        self.append_text("Melody: Hello, I'm Melody. How can I assist you today?")
        self.speak("Hello, I'm Melody. How can I assist you today?")
    
    def load_Melody_image(self):
        self.Melody_img = tk.PhotoImage(file="images/melody.png")  
        self.Melody_image_label = tk.Label(self.Melody_frame, image=self.Melody_img, bg='#d9b0d9')
        self.Melody_image_label.pack()

    def toggle_voice_mode(self):
        self.voice_mode = not self.voice_mode

        if self.voice_mode:
            self.append_text("Melody: Voice mode activated.")
            self.speak("Voice mode activated.")
            threading.Thread(target=self.listen_voice).start()
        else:
            self.append_text("Melody: Voice mode deactivated.")

    def listen_voice(self):
        if not self.voice_mode:
            return

        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.append_text("Melody is listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            self.append_text(f"User: {command}")
            self.process_command_voice(command)
            self.toggle_voice_mode()
        except sr.UnknownValueError:
            self.append_text("Melody: Sorry, I didn't catch that.")
            self.speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            self.append_text("Melody: Sorry, there seems to be an issue with the voice service.")
            self.speak("Sorry, there seems to be an issue with the voice service.")
            
        time.sleep(3)
        
        if self.voice_mode:
            threading.Thread(target=self.listen_voice).start()

    def append_text(self, text):
        self.text_display.config(state=tk.NORMAL)
        self.text_display.insert(tk.END, text + "\n")
        self.text_display.config(state=tk.DISABLED)
        self.text_display.yview(tk.END)
        self.root.update()

    def speak(self, text):
        self.speak_queue.put(text) 

    def process_speech_queue(self):
        while True:
            text = self.speak_queue.get()  
            self.engine.say(text)          
            self.engine.runAndWait()       
            self.speak_queue.task_done()   

    def process_command(self, event):
        command = self.input_field.get().lower().strip()
        self.append_text(f"User: {command}")
        self.input_field.delete(0, tk.END)
        self.process_command_common(command)

    def process_command_voice(self, command):
        self.process_command_common(command)

    def process_command_common(self, command):
        if "time" in command:
            self.tell_time()
        elif "open" in command:
            self.open_app(command)
        elif "weather" in command:
            self.show_weather()
        elif "search" in command:
            search_query = command.replace("search", "").strip()
            self.search_fallback(search_query)
        elif "play" in command:
            video_query = command.replace("play", "").strip()
            self.play_youtube_music(video_query)
        elif "creates you" in command or "your creator" in command:
            response = ("My creator is Mark Joshua Kylee P. Sta. Rosa, currently a 2nd-year IT student, born on November 5, 2004, under the Scorpio zodiac sign.")
            self.append_text(f"Melody: {response}")
            self.speak(response)
        elif "your purpose" in command:
            response = ("My purpose is to help and assist you, and also to serve as a final project for CC03 subject.")        
            self.append_text(f"Melody: {response}")
            self.speak(response)
        elif "group members" in command:
            response = ("Group Members: Leader: Mark Joshua Kylee P. Sta. Rosa, Members: Nathan Joel M. Lopez, Christian S. Narral, Justine Paul P. Tañada, Micaella P. Turado, Eloisa Mae R. Montenegro, Mariel G. Arca, Ma. Mikaela A. Del Rosario, Joseph Marny B. Corral, Gerry Gil B. Fatallar Jr. and Ma. Marthy D. Articulo")
            self.append_text(f"Melody: {response}")
            self.speak(response)
        elif "exit" in command or "quit" in command or "close" in command:
            self.root.destroy()
        else:
            response = f"Let me search that for you."
            self.append_text(f"Melody: {response}")
            self.speak(response)
            self.search_fallback(command)
            
        
        return "continue"
            
    def tell_time(self):
        now = datetime.datetime.now()
        current_time = now.strftime('%I:%M %p')
        response = f"The current time is {current_time}"
        self.append_text(f"Melody: {response}")
        self.speak(response)

    def open_app(self, app_name):
        if "microsoft edge" in app_name:
            subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
            self.append_text("Melody: Opening Microsoft edge")
            self.speak("Opening Microsoft edge")
        elif "chrome" in app_name:
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])   
            self.append_text("Melody: Opening Chrome")
            self.speak("Opening Chrome")
        elif "calculator" in app_name:
            subprocess.Popen('calc.exe')
            self.append_text("Melody:Opening Calculator")
            self.speak("Opening Calculator")
        elif "settings" in app_name:
            subprocess.Popen("start ms-settings:", shell=True)
            self.append_text("Melody: Opening Settings")
            self.speak("Opening Settings")
        elif "file explorer" in app_name:
            subprocess.Popen("explorer")
            self.append_text("Melody: Opening File Explorer")
            self.speak("Opening File Explorer")
        elif "task manager" in app_name:
            subprocess.Popen("taskmgr.exe")
            self.append_text("Melody: Opening Task Manager")
            self.speak("Opening Task Manager")
        elif "notepad" in app_name:
            subprocess.Popen("notepad.exe")
            self.append_text("Melody: Opening Notepad")
            self.speak("Opening Notepad")
        elif "paint" in app_name:
            subprocess.Popen("mspaint.exe")
            self.append_text("Melody: Opening Paint")
            self.speak("Opening Paint")
        elif "wordpad" in app_name:
            subprocess.Popen("write.exe")
            self.append_text("Melody: Opening Wordpad")
            self.speak("Opening Wordpad")
        elif "control panel" in app_name:
            subprocess.Popen("control.exe")
            self.append_text("Melody: Opening Control Panel")
            self.speak("Opening Control Panel")                           
        else:
            response = "Sorry!, I can't open that application."
            self.append_text(f"Melody: {response}")
            self.speak(response) 

    def show_weather(self):
        url = "https://www.weather.com/"
        webbrowser.open(url)
        response = "Here is the current weather information."
        self.append_text(f"Melody: {response}")
        self.speak(response)

    def play_youtube_music(self, query):
        yt = pytube.Search(query)
        video = yt.results[0]
        video_url = video.watch_url
        webbrowser.open(video_url)
        response = f"Playing {query} on YouTube Music."
        self.append_text(f"Melody: {response}")
        self.speak(response)

    def search_fallback(self, query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        response = f"Here are the results for {query} on Google."
        self.append_text(f"Melody: {response}")
        self.speak(response)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
