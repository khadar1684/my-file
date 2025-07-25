import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        
        # Default brush settings
        self.brush_color = "black"
        self.brush_size = 5
        
        # Setup canvas
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(padx=10, pady=10)
        
        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonPress-1>", self.start_paint)
        
        # Initialize PIL image to save drawing
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)
        
        # UI controls
        control_frame = tk.Frame(root)
        control_frame.pack()
        
        # Brush size selector
        tk.Label(control_frame, text="Brush Size:").pack(side=tk.LEFT)
        self.size_scale = tk.Scale(control_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=self.change_brush_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(side=tk.LEFT, padx=5)
        
        # Color picker button
        self.color_btn = tk.Button(control_frame, text="Pick Color", command=self.choose_color)
        self.color_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_btn = tk.Button(control_frame, text="Clear", command=self.clear_canvas)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Save button
        self.save_btn = tk.Button(control_frame, text="Save", command=self.save_image)
        self.save_btn.pack(side=tk.LEFT, padx=5)
        
        self.last_x, self.last_y = None, None

    def start_paint(self, event):
        self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        if self.last_x and self.last_y:
            # Draw line on canvas
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size, fill=self.brush_color,
                                    capstyle=tk.ROUND, smooth=True)
            # Draw line on the PIL image
            self.draw.line([self.last_x, self.last_y, event.x, event.y],
                           fill=self.brush_color, width=self.brush_size)
            self.last_x, self.last_y = event.x, event.y

    def change_brush_size(self, val):
        self.brush_size = int(val)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose brush color")
        if color_code[1]:
            self.brush_color = color_code[1]

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 600, 400], fill="white")

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            try:
                self.image.save(file_path)
                messagebox.showinfo("Image Saved", f"Image saved successfully:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
