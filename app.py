import customtkinter as ctk
from date_time_plugin import DateTimePlugin
import threading

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("V-PRO")
        self.geometry("700x450")

        self.label = ctk.CTkLabel(self, text="SteelSeries Engine 3 - OLED Customizer")
        self.label.pack(fill="both", padx=20, pady=20)

        self.startbutton = ctk.CTkButton(self, text="start", command=self.start)
        self.startbutton.pack(fill="both", padx=20, pady=20)
        self.stopbutton = ctk.CTkButton(self, text="stop", command=self.stop)
        self.stopbutton.pack(fill="both", padx=20, pady=20)

        self.thread = None

    def start(self):
        if not self.thread or not self.thread.is_alive():
            self.thread = threading.Thread(target=DateTimePlugin.start_OLED_overwriting)
            self.thread.start()
            print("Starting")

    def stop(self):
        if self.thread and self.thread.is_alive():
            DateTimePlugin.stop_OLED_overwriting()
            self.thread.join()
            print("Stopped")

if __name__ == "__main__":
    app = App()
    app.mainloop()
    