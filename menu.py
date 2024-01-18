import tkinter as tk
#from tkinter import ttk

from tkinter import filedialog, Text
from PIL import Image, ImageTk
import os

import cv2

# Tkinter penceresi oluştur
root= tk.Tk()
root.title("Aeroprocess")

# Kamerayı açmak için bir fonksiyon tanımla
def start_camera():
    global cap
    cap = cv2.VideoCapture(0)

# Kamerayı kapatmak için bir fonksiyon tanımla
def stop_camera():
    global cap
    cap.release()
    

# Canvas oluştur ve yerleştir
canvas = tk.Canvas(root, width=1920, height=1080, bg="#1F2C39")
canvas.pack()

""""
GÜNEŞ PANELİ 3D BOYUTLU
# Güneş paneli çizme işlemi
x, y = 100, 100
w, h = 200, 200
d = 30

# Sol çizgi
canvas.create_line(x, y, x, y + h, width=d, fill="#666")

# Üst çizgi
canvas.create_line(x, y, x + w, y, width=d, fill="#666")

# Sağ çizgi
canvas.create_line(x + w, y, x + w, y + h, width=d, fill="#666")

# Alt çizgi
canvas.create_line(x, y + h, x + w, y + h, width=d, fill="#666")

# Güneş paneli gölgelendirme
canvas.create_rectangle(x + w + 5, y + 10, x + w + 15, y + h + 10, fill="#000", outline="")
canvas.create_polygon(x + w + 15, y + 10, x + w + 25, y + 10, x + w + 15, y + h + 10, fill="#666", outline="")
canvas.create_rectangle(x + w + 25, y + 10, x + w + 35, y + h + 10, fill="#000", outline="")
canvas.create_polygon(x + w + 35, y + 10, x + w + 45, y + 10, x + w + 35, y + h + 10, fill="#666", outline="")
"""

""""
KÜP TASARIMI 3D BOYUTLU
#coords = [50, 50, 150, 50, 150, 150, 50, 150, 50, 50, 75, 75, 175, 75, 150, 150, 150, 50]
#canvas.create_polygon(coords, fill="#999", outline="#666", width=2)
"""

"""
DİKDÖRTGEN 3D BOYUTLU
#rect = canvas.create_rectangle(50, 50, 800, 600, fill="blue", outline="black")
"""

"""
DİKDÖRTGEN 3D BOYUTLU
# Güneş çizme işlemi
x, y = 150, 150
r = 100
d = 10


# Güneşin ortası
canvas.create_oval(x - r, y - r, x + r, y + r, fill="#FFC107", outline="#FFC107")

# Güneşin 3 boyutlu etkisi
canvas.create_oval(x - r, y - r, x + r - d, y + r - d, fill="white", outline="#FFC107")
canvas.create_oval(x - r + d, y - r + d, x + r, y + r, fill="orange", outline="")
"""

""""
style = ttk.Style()
style.configure("Oval.TButton", padding=6, relief="flat", background="#ccc", borderwidth=0)
"""

# Kamera açma düğmesini oluştur
start_button = tk.Button(root, text="Open Camera", command=start_camera, bg="green",  width=15, height=1)
start_button.pack()
start_button.place(x=80, y=600)

# Kamera kapatma düğmesini oluştur
stop_button = tk.Button(root, text="Close Camera", command=stop_camera, bg="red", width=15, height=1)
stop_button.pack()
stop_button.place(x=230, y=600)

# Çıkış düğmesini oluştur
exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="yellow", width=15, height=1)
exit_button.pack()
exit_button.place(x=370, y=600)

#################################################################################################################################
# Kamerayı başlat
cap = cv2.VideoCapture(0)

# Resimleri göstermek için değişkenler oluştur
img = None
photo = None

#frame =tk.Frame(root, bg="#3e646c")
#frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

""""
# Çıkış düğmesini oluştur
button = tk.Button(root, text="Exit", command=root.destroy)
button.pack()
"""

"""
def dur():
    for artis in range(1, 5):
        break
"""

# Kamera görüntüsünü al ve göster
def show_frame():
    global img, photo
    ret, frame = cap.read()
    
    """
    # Görüntü işleme işlemleri
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    color_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Görüntüleri PIL formatına dönüştürme
    original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_original = Image.fromarray(original)
    img_gray = Image.fromarray(gray)
    img_edges = Image.fromarray(color_edges)
    img_contours = Image.fromarray(color_edges)

    # Tkinter için ImageTk formatına dönüştürme
    imgtk_original = ImageTk.PhotoImage(image=img_original)
    imgtk_gray = ImageTk.PhotoImage(image=img_gray)
    imgtk_edges = ImageTk.PhotoImage(image=img_edges)
    imgtk_contours = ImageTk.PhotoImage(image=img_contours)

    # Görüntüleri ekrana çizme
    canvas.create_image(0, 0, anchor="nw", image=imgtk_original)
    canvas.create_image(640, 0, anchor="nw", image=imgtk_gray)
    canvas.create_image(0, 360, anchor="nw", image=imgtk_edges)
    canvas.create_image(640, 360, anchor="nw", image=imgtk_contours)
    #root.after(10, show_frame)
    # Tkinter penceresini güncelleme
    root.update()

    # Programdan çıkış
    if cv2.waitKey(1) & 0xFF == ord('q'):
           dur     
    """


    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(img))
        canvas.create_image(80, 80, image=photo, anchor=tk.NW)
    root.after(10, show_frame)
#################################################################################################################################

# Kamera görüntüsünü göstermek için döngüyü başlat
show_frame()

root.mainloop()

# Kamerayı serbest bırak
cap.release()


"""
import tkinter as tk
import cv2

class CameraApp:
    def _init_(self, master):
        self.master = master
        master.title("Kamera Uygulaması")

        self.camera_button = tk.Button(master, text="Kamerayı Başlat", command=self.start_camera)
        self.camera_button.pack()

    def start_camera(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

root = tk.Tk()
my_gui = CameraApp(root)
root.mainloop()
"""