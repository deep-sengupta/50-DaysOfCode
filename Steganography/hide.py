from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from io import BytesIO
import os

class Stegno:

    output_image_size = 0

    def main(self, root):
        root.title('Image Steganography')
        root.geometry('400x350')
        root.resizable(width=False, height=False)
        f = Frame(root)
        f.place(relx=0.5, rely=0.5, anchor=CENTER)

        title = Label(f, text='Image Steganography')
        title.config(font=('Helvetica', 24))
        title.pack(pady=10)

        b_encode = Button(f, text="Encode", command=lambda: self.frame1_encode(f), padx=14, bg='#4CAF50')
        b_encode.config(font=('Helvetica', 12))
        b_decode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_decode(f), bg='#f44336')
        b_decode.config(font=('Helvetica', 12))

        b_encode.pack(pady=12)
        b_decode.pack(pady=12)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = Frame(root)
        d_f2.place(relx=0.5, rely=0.5, anchor=CENTER)

        l1 = Label(d_f2, text='Select Image with Hidden text:')
        l1.config(font=('Helvetica', 14))
        l1.pack(pady=10)
        bws_button = Button(d_f2, text='Select', command=lambda: self.frame2_decode(d_f2), bg='#2196F3')
        bws_button.config(font=('Helvetica', 12))
        bws_button.pack(pady=5)
        back_button = Button(d_f2, text='Cancel', command=lambda: Stegno.home(self, d_f2), bg='#f44336')
        back_button.config(font=('Helvetica', 12))
        back_button.pack(pady=10)

    def frame2_decode(self, d_f2):
        d_f3 = Frame(root)
        d_f3.place(relx=0.5, rely=0.5, anchor=CENTER)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            file_name = os.path.basename(myfile)
            l4 = Label(d_f3, text=f'Selected Image: {file_name}', wraplength=350)
            l4.config(font=('Helvetica', 14))
            l4.pack(pady=10)

            hidden_data = self.decode(Image.open(myfile))
            l2 = Label(d_f3, text='Hidden data is:')
            l2.config(font=('Helvetica', 14))
            l2.pack(pady=10)
            text_area = Text(d_f3, width=40, height=8, font=('Helvetica', 12))
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.pack()

            back_button = Button(d_f3, text='Cancel', command=lambda: self.page3(d_f3), bg='#f44336')
            back_button.config(font=('Helvetica', 10))
            back_button.pack(pady=10)

            show_info = Button(d_f3, text='More Info', command=self.info, bg='#2196F3')
            show_info.config(font=('Helvetica', 10))
            show_info.pack(pady=5)

            d_f2.destroy()

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())
        while True:
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                binstr += '0' if i % 2 == 0 else '1'
            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_encode(self, f):
        f.destroy()
        f2 = Frame(root)
        f2.place(relx=0.5, rely=0.5, anchor=CENTER)

        l1 = Label(f2, text='Select the Image in which \nyou want to hide text:')
        l1.config(font=('Helvetica', 14))
        l1.pack(pady=10)

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2), bg='#2196F3')
        bws_button.config(font=('Helvetica', 12))
        bws_button.pack(pady=5)
        back_button = Button(f2, text='Cancel', command=lambda: Stegno.home(self, f2), bg='#f44336')
        back_button.config(font=('Helvetica', 12))
        back_button.pack(pady=10)

    def frame2_encode(self, f2):
        ep = Frame(root)
        ep.place(relx=0.5, rely=0.5, anchor=CENTER)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            file_name = os.path.basename(myfile)
            l3 = Label(ep, text=f'Selected Image: {file_name}', wraplength=350)
            l3.config(font=('Helvetica', 14))
            l3.pack(pady=10)

            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = Image.open(myfile).size

            l2 = Label(ep, text='Enter the message:')
            l2.config(font=('Helvetica', 14))
            l2.pack(pady=15)
            text_area = Text(ep, width=40, height=8, font=('Helvetica', 12))
            text_area.pack()

            back_button = Button(ep, text='Encode', command=lambda: [self.enc_fun(text_area, Image.open(myfile)), Stegno.home(self, ep)], bg='#4CAF50')
            back_button.config(font=('Helvetica', 10))
            back_button.pack(pady=10)

            encode_button = Button(ep, text='Cancel', command=lambda: Stegno.home(self, ep), bg='#f44336')
            encode_button.config(font=('Helvetica', 10))
            encode_button.pack(pady=5)

    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}\nheight: {}'.format(self.output_image_size.st_size/1000000,
                                    self.o_image_w, self.o_image_h,
                                    self.d_image_size/1000000,
                                    self.d_image_w, self.d_image_h)
            messagebox.showinfo('info', str)
        except:
            messagebox.showinfo('Info', 'Unable to get the information')

    def genData(self, data):
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self, pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                    pix[j] -= 1
                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)
        for pixel in self.modPix(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self, text_area, myimg):
        data = text_area.get("1.0", "end-1c")
        if len(data) == 0:
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=[('png', '*.png')], defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = newimg.size

    def page3(self, frame):
        frame.destroy()
        self.main(root)

root = Tk()
o = Stegno()
o.main(root)
root.mainloop()