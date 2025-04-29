import tkinter as tk
from tkinter import messagebox
import time

class KernelSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kernel Architecture Simulator")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")

        self.label = tk.Label(self, text="Kernel Architecture Simulation", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.output = tk.Text(self, height=12, width=70, font=("Courier", 10))
        self.output.pack(pady=10)

        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=10)

        mono_btn = tk.Button(button_frame, text="Run Monolithic Simulation", command=self.run_monolithic, width=25)
        micro_btn = tk.Button(button_frame, text="Run Microkernel Simulation", command=self.run_microkernel, width=25)

        mono_btn.grid(row=0, column=0, padx=10)
        micro_btn.grid(row=0, column=1, padx=10)

    def log(self, text):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.update()
        time.sleep(0.8)

    def clear_output(self):
        self.output.delete("1.0", tk.END)

    def run_monolithic(self):
        self.clear_output()
        self.log("=== Monolithic Kernel ===")
        self.log("[User] Requesting file read operation...")
        self.log("[Kernel] Direct call to File System Service.")
        self.log("[File System] Performing file read operation...")
        self.log("[Kernel] Direct call to Device Driver Service.")
        self.log("[Device Driver] Accessing hardware device...")
        self.log("[Monolithic Kernel] All services completed.")

    def run_microkernel(self):
        self.clear_output()
        self.log("=== Microkernel ===")
        self.log("[User] Sending request to kernel...")
        self.log("[Kernel] Message to File System Service: 'Read file'")
        self.log("[File System] Received message: 'Read file'")
        self.log("[File System] Processing file read...")
        self.log("[Kernel] Message to Device Driver Service: 'Access device'")
        self.log("[Device Driver] Received message: 'Access device'")
        self.log("[Device Driver] Processing device access...")
        self.log("[Microkernel] All messages processed.")

if __name__ == "__main__":
    app = KernelSimulator()
    app.mainloop()
