import tkinter as tk
import time

class KernelSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kernel Architecture Simulator")
        self.geometry("950x700")
        self.configure(bg="#f0f0f0")

        # Updated Heading
        self.label = tk.Label(self, text="Kernel Architecture Simulation", font=("Arial", 32, "bold"), bg="#f0f0f0", fg="black")
        self.label.pack(pady=20)

        self.canvas = tk.Canvas(self, width=900, height=400, bg="white", highlightthickness=1, highlightbackground="gray")
        self.canvas.pack(pady=10)

        self.output = tk.Text(self, height=12, width=110, font=("Courier", 14))
        self.output.pack()

        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=10)

        # Updated Buttons: Bigger, 2D look, black border
        button_style = {"width": 30, "height": 2, "font": ("Arial", 14), "relief": "solid", "borderwidth": 2, "bg": "#ffffff", "fg": "black"}

        tk.Button(button_frame, text="Run Monolithic Simulation", command=self.run_monolithic, **button_style).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Run Microkernel Simulation (Step Mode)", command=self.start_microkernel_step_mode, **button_style).grid(row=0, column=1, padx=10)

        self.step_btn = tk.Button(self, text="Next Step", command=self.next_step, state=tk.DISABLED, **button_style)
        self.step_btn.pack(pady=5)

        self.micro_steps = []
        self.step_index = 0

    def log(self, text):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.update()

    def clear_output(self):
        self.output.delete("1.0", tk.END)

    def clear_canvas(self):
        self.canvas.delete("all")

    def animate_arrow(self, x1, y1, x2, y2, color="black"):
        arrow = self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, width=3, fill=color)
        self.update()
        time.sleep(0.8)
        return arrow

    def animate_box(self, x, y, text, color="#cce6ff"):
        box = self.canvas.create_rectangle(x-80, y-30, x+80, y+30, fill=color, outline="black")
        label = self.canvas.create_text(x, y, text=text, font=("Arial", 14), fill="black")
        self.update()
        time.sleep(0.5)
        return box, label

    def run_monolithic(self):
        self.clear_output()
        self.clear_canvas()
        self.log("=== Monolithic Kernel Simulation ===")

        user_box, _ = self.animate_box(200, 120, "User Application")
        kernel_box, _ = self.animate_box(600, 120, "Monolithic Kernel\n(File System + Driver)", color="#f0d0d0")

        self.animate_arrow(200, 120, 600, 120)
        self.log("[User] Requesting file read operation...")

        time.sleep(1)

        fs_box, _ = self.animate_box(600, 250, "File System Service", color="#ffe6cc")
        self.animate_arrow(600, 120, 600, 250)
        self.log("[Kernel] Direct call to File System Service.")
        self.log("[File System] Performing file read operation...")

        time.sleep(1)

        driver_box, _ = self.animate_box(600, 350, "Device Driver Service", color="#ffe6cc")
        self.animate_arrow(600, 250, 600, 350)
        self.log("[Kernel] Direct call to Device Driver Service.")
        self.log("[Device Driver] Accessing hardware device...")

        time.sleep(1)

        self.log("[Monolithic Kernel] All services completed.")

    def animate_message(self, text, x1, y1, x2, y2):
        label = self.canvas.create_text(x1, y1, text=text, anchor="w", fill="blue", font=("Arial", 12, "bold"))
        steps = 30
        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps
        for _ in range(steps):
            self.canvas.move(label, dx, dy)
            self.update()
            time.sleep(0.02)

    def start_microkernel_step_mode(self):
        self.clear_output()
        self.clear_canvas()
        self.step_index = 0
        self.micro_steps = [
            lambda: self.log("[User] Sending request to kernel..."),
            lambda: self.animate_message("Request", 100, 70, 320, 70),
            lambda: self.log("[Kernel] Message to File System Service: 'Read file'"),
            lambda: self.animate_message("Read file", 320, 70, 750, 60),
            lambda: self.log("[File System] Received message: 'Read file'"),
            lambda: self.log("[File System] Processing file read..."),
            lambda: self.log("[Kernel] Message to Device Driver Service: 'Access device'"),
            lambda: self.animate_message("Access device", 320, 70, 750, 160),
            lambda: self.log("[Device Driver] Received message: 'Access device'"),
            lambda: self.log("[Device Driver] Processing device access..."),
            lambda: self.log("[Microkernel] All messages processed.")
        ]

        self.canvas.create_rectangle(60, 50, 180, 110, fill="#d0f0c0", outline="black")
        self.canvas.create_text(120, 80, text="User", font=("Arial", 14), fill="black")

        self.canvas.create_rectangle(280, 50, 400, 110, fill="#f0d0d0", outline="black")
        self.canvas.create_text(340, 80, text="Microkernel", font=("Arial", 14), fill="black")

        self.canvas.create_rectangle(700, 30, 850, 90, fill="#d0d0f0", outline="black")
        self.canvas.create_text(775, 60, text="File System Service", font=("Arial", 14), fill="black")

        self.canvas.create_rectangle(700, 130, 850, 190, fill="#d0d0f0", outline="black")
        self.canvas.create_text(775, 160, text="Device Driver Service", font=("Arial", 14), fill="black")

        self.step_btn.config(state=tk.NORMAL)

    def next_step(self):
        if self.step_index < len(self.micro_steps):
            self.micro_steps[self.step_index]()
            self.step_index += 1
        else:
            self.step_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
        app = KernelSimulator()
        app.mainloop()
