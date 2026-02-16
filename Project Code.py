from email import message
import tkinter
import cv2
from PIL import Image, ImageTk
from datetime import datetime
import os
import pygame
import mysql.connector
from tkinter import ttk

# Initialize pygame mixer for sound
pygame.mixer.init()

# Create application window
tk = tkinter.Tk()
tk.geometry('1000x900')  # Increased window height to accommodate larger image
tk.title("Presensi Universitas Negeri Yogyakarta")
tk.configure(bg="white")

def update_time():
    now = datetime.now()
    formatted_time = now.strftime("%A, %d %B %Y | %H:%M:%S")
    label_time.config(text=formatted_time)
    tk.after(1000, update_time)

# Create header frame
header_frame = tkinter.Frame(tk, bg="#1e3a8a", width=1500, height=140)
header_frame.pack(fill="x")

# Add time label (right-aligned)
label_time = tkinter.Label(header_frame, font=("Arial", 14), fg="white", bg="#1e3a8a")
label_time.pack(side="right", padx=20, pady=10)
update_time()

# Left-aligned logo container
logo_container = tkinter.Frame(header_frame, bg="#1e3a8a")
logo_container.pack(side="left", padx=20)

# Try to load and display larger logo
try:
    logo_img = Image.open("Logo_UNY.png")
    logo_img = logo_img.resize((100, 100))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tkinter.Label(logo_container, image=logo_photo, bg="#1e3a8a")
    logo_label.image = logo_photo
    logo_label.pack()
except:
    logo_label = tkinter.Label(logo_container, text="LOGO", font=("Arial", 14, "bold"), 
                              width=10, height=5, bg="white", fg="#1e3a8a")
    logo_label.pack()

# Center header text container
header_text = tkinter.Frame(header_frame, bg="#1e3a8a")
header_text.pack(expand=True, pady=10)

# Header labels
welcome_label = tkinter.Label(header_text, text="Selamat Datang di Laman", 
                            font=("Arial", 18), fg="white", bg="#1e3a8a")
welcome_label.pack()

university_label = tkinter.Label(header_text, text="Universitas Negeri Yogyakarta", 
                               font=("Arial", 24, "bold"), fg="#ffd700", bg="#1e3a8a")
university_label.pack()

faculty_label = tkinter.Label(header_text, text="Fakultas Vokasi", 
                            font=("Arial", 22, "bold"), fg="white", bg="#1e3a8a")
faculty_label.pack()

department_label = tkinter.Label(header_text, text="Departemen Elektro dan Elektronika", 
                                font=("Arial", 20), fg="white", bg="#1e3a8a")
department_label.pack()

# Initialize camera with higher resolution
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1100)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 550)

def create_placeholder_image(width, height, text="Foto akan muncul di sini"):
    # Create a blank image with specified size
    img = Image.new('RGB', (width, height), color='lightgray')
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    
    # Add text to the center of image
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()
        
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw text in dark gray
    draw.text((x, y), text, fill='#666666', font=font)
    
    return img

def validate_prodi(prodi):
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'db_presensi',
        'raise_on_warnings': True
    }
    try:
        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            cursor = cnx.cursor()
            query = "SELECT * FROM tb_member WHERE prodi = %s"
            cursor.execute(query, (prodi,))
            result = cursor.fetchall()
            cnx.close()
            return len(result) > 0  # Jika prodi ditemukan, return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return False

# Fitur tambahan: Validasi Rombel (V1, V2, V3)
def validate_rombel(rombel):
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'db_presensi',
        'raise_on_warnings': True
    }
    
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        cursor = cnx.cursor()
        query = "SELECT * FROM tb_member WHERE rombel = %s"
        cursor.execute(query, (rombel,))
        result = cursor.fetchall()
        cnx.close()
        return len(result) > 0  # Jika rombel ada, return True
    return False

def play_sound(success=True):
    if success:
        # Play a success sound (you can use your own sound file)
        pygame.mixer.Sound("Sound_benar.wav").play()
    else:
        # Play an error sound (you can use your own sound file)
        pygame.mixer.Sound("Sound_salah.wav").play()

def process():
    global img
    global image_
    nim = entry.get()  # Ambil input NIM
    nama = entry1.get()  # Ambil input Nama (label Nama)
    prodi = entry2.get()
    rombel = rombel_combobox.get()  # Ambil input rombel

    if not validate_rombel(rombel):
        notif1.set('Rombel tidak valid!')
        play_sound(success=False)
        return

    # Validasi Prodi
    if not validate_prodi(prodi):
        notif1.set('Prodi tidak valid!')
        play_sound(success=False)
        return

    if nim.isnumeric():  # Pastikan NIM hanya berisi angka
        config = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1',
            'database': 'db_presensi',
            'raise_on_warnings': True
        }

        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            cursor = cnx.cursor()
            
            # Query untuk mengecek apakah NIM dan Nama ada di database
            query = "SELECT * FROM tb_member WHERE id_nim = %s AND nama_mahasiswa = %s"
            cursor.execute(query, (nim, nama))
            rows = cursor.fetchall()
            
            if len(rows) == 0:  # Jika NIM atau Nama tidak ditemukan
                notif1.set('Data tidak sesuai atau tidak ada')
                play_sound(success=False)
            else:
                # Jika data valid, lanjutkan proses presensi
                _, image = vid.read()
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
                current_time = current_datetime.strftime("%H:%M:%S")
                current_date = current_datetime.strftime("%Y-%m-%d")
                current_day = current_datetime.strftime("%A")

                # Simpan foto hasil presensi
                x1, y1 = 425, 200
                x2, y2 = 925, 700
                cropped_image = image[y1:y2, x1:x2]
                cv2.imwrite(f"file_{formatted_datetime}.png", cropped_image)

                name_file = f"file_{formatted_datetime}.png"
                sql = "INSERT INTO tb_presensi (id_user, hari_kedatangan, tanggal_kedatangan, waktu_kedatangan, image) VALUES (%s, %s, %s, %s, %s)"
                val = (nim, current_day, current_date, current_time, name_file)
                cursor.execute(sql, val)
                cnx.commit()

                # Tampilkan data presensi
                for row in rows:
                    notif1.set('Nama: ' + row[1])  # Menampilkan nama
                    notif2.set('NIM: ' + row[0])  # Menampilkan NIM
                    notif3.set('Waktu: ' + current_time)
                    notif4.set('Hari: ' + current_day)
                    notif5.set('Tanggal: ' + current_date)

                img = Image.open(f"file_{formatted_datetime}.png")
                resized_image = img.resize((125, 160))
                image_ = ImageTk.PhotoImage(resized_image)
                canvas1.create_image(40, 80, image=image_)
                notif6.set('Anda Berhasil Presensi')
                play_sound(success=True)

            cnx.close()
        else:
            notif1.set('Koneksi ke database gagal')
            play_sound(success=False)
    else:
        notif1.set('Masukkan NIM dengan benar')
        play_sound(success=False)


# Fungsi untuk mengisi daftar nama dari database ke Label Nama
def fill_nama_from_database():
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'db_presensi',
        'raise_on_warnings': True
    }

    try:
        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            cursor = cnx.cursor()
            # Query untuk mengambil semua nama di database
            query = "SELECT nama FROM tb_member"
            cursor.execute(query)
            rows = cursor.fetchall()
            
            # Isi nama-nama ke drop-down atau pilihan input
            nama_list = [row[0] for row in rows]
            nama_menu['values'] = nama_list  # Mengisi ComboBox dengan nama

            cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def open_camera():
    """Update camera feed."""
    ret, frame = vid.read() 
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    captured_image = Image.fromarray(opencv_image) 
    photo_image = ImageTk.PhotoImage(image=captured_image)
    canvas.create_image(100, 0, image=photo_image, anchor=tkinter.CENTER)
    canvas.image = photo_image
    tk.after(10, open_camera)

notif1 = tkinter.StringVar()
notif2 = tkinter.StringVar()
notif3 = tkinter.StringVar()
notif4 = tkinter.StringVar()
notif5 = tkinter.StringVar()
notif6 = tkinter.StringVar()

notif1.set('')
notif2.set('')
notif3.set('')
notif4.set('')
notif5.set('')
notif6.set('')

canvas = tkinter.Canvas(tk, width=360, height=350)
canvas.pack(anchor=tkinter.W)
canvas.place(x=700, y=300)

canvas1 = tkinter.Canvas(tk, width=100, height=120)
canvas1.pack(expand=tkinter.YES)
canvas1.place(x=1200, y=300)

button = tkinter.Button(tk, text="Presensi", width=30, height=2, command=process)
button.place(x=1200, y=740)

entry = tkinter.Entry(tk, width=29)
entry.place(x=1200,y=550)

entry1 = tkinter.Entry(tk, width=29)
entry1.place(x=1200,y=490)

entry2 = tkinter.Entry(tk, width=29)
entry2.place(x=1200,y=610)

label_input = tkinter.Label(tk, text="Masukkan NIM")
label_input.place(x=1270,y=520)

label_input1 = tkinter.Label(tk, text="Masukkan Nama")
label_input1.place(x=1270,y=460)

# Add ComboBox untuk Rombel
label_input2 = tkinter.Label(tk, text="Pilih Rombel")
label_input2.place(x=1270, y=640)
rombel_combobox = ttk.Combobox(tk, values=["V1", "V2", "V3"], width=27)
rombel_combobox.place(x=1200, y=670)

# Tambahkan ComboBox untuk Prodi di GUI
label_input_prodi = tkinter.Label(tk, text="Pilih Prodi")
label_input_prodi.place(x=1270, y=580)


label_notif1 = tkinter.Label(tk, textvariable=notif1)
label_notif1.place(x=1330,y=300)

label_notif2 = tkinter.Label(tk, textvariable=notif2)
label_notif2.place(x=1330,y=330)

label_notif3 = tkinter.Label(tk, textvariable=notif3)
label_notif3.place(x=1330,y=360)

label_notif4 = tkinter.Label(tk, textvariable=notif4)
label_notif4.place(x=1330,y=390)

label_notif5 = tkinter.Label(tk, textvariable=notif5)
label_notif5.place(x=1330,y=420)

label_notif6 = tkinter.Label(tk, textvariable=notif6)
label_notif6.place(x=820,y=670)

# Start camera feed
open_camera()

tk.mainloop()