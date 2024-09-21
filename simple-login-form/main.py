import sqlite3
import tkinter as tk
from tkinter import messagebox

class SimpleLogin:
    def __init__(self):
        self.login_window = tk.Tk()
        self.login_window.title('Simple Login Application')
        self.login_window.geometry('400x250')
        self.login_window.configure(bg='#2C2F33')

        title = tk.Label(self.login_window, text='LogiPortal', font=('Arial', 18), bg='#2C2F33', fg='#FFFFFF')
        title.pack(pady=20)

        username_frame = tk.Frame(self.login_window, bg='#2C2F33')
        username_frame.pack(pady=10)
        tk.Label(username_frame, text='Username:', font=('Arial', 12), bg='#2C2F33', fg='#FFFFFF').grid(row=0, column=0, padx=10, pady=5)
        self.username = tk.Entry(username_frame, width=30, font=('Arial', 12), bd=2, fg='#000000', bg='#D3D3D3', insertbackground='#000000')
        self.username.grid(row=0, column=1, padx=10, pady=5)

        password_frame = tk.Frame(self.login_window, bg='#2C2F33')
        password_frame.pack(pady=10)
        tk.Label(password_frame, text='Password:', font=('Arial', 12), bg='#2C2F33', fg='#FFFFFF').grid(row=1, column=0, padx=10, pady=5)
        self.password = tk.Entry(password_frame, show='*', width=30, font=('Arial', 12), bd=2, fg='#000000', bg='#D3D3D3', insertbackground='#000000')
        self.password.grid(row=1, column=1, padx=10, pady=5)

        button_frame = tk.Frame(self.login_window, bg='#2C2F33')
        button_frame.pack(pady=20)

        self.loginbtn = tk.Button(button_frame, text='Login', font=('Arial', 12), command=self.authenticate,
                                  bg='#7289DA', fg='#000000', width=10, bd=0, padx=5, pady=5)
        self.loginbtn.grid(row=0, column=0, padx=10)

        self.exitbtn = tk.Button(button_frame, text='Exit', font=('Arial', 12), command=self.login_window.quit,
                                 bg='#FF5555', fg='#000000', width=10, bd=0, padx=5, pady=5)
        self.exitbtn.grid(row=0, column=1, padx=10)

        self.login_window.mainloop()

    def authenticate(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        username = self.username.get()
        password = self.password.get()

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?;', (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo('Login Success', 'Successfully logged in!')
            self.show_profile(user)
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password')

        conn.close()

    def show_profile(self, user):
        self.login_window.destroy()
        self.profile_window = tk.Tk()
        self.profile_window.title(f'Profile of {user[0]}')
        self.profile_window.geometry('400x300')
        self.profile_window.configure(bg='#2C2F33')

        profile_frame = tk.Frame(self.profile_window, bg='#2C2F33')
        profile_frame.pack(expand=True)

        tk.Label(profile_frame, text=f'Name: {user[2]}', font=('Arial', 14), bg='#2C2F33', fg='#FFFFFF').pack(pady=10)
        tk.Label(profile_frame, text=f'E-Mail: {user[3]}', font=('Arial', 14), bg='#2C2F33', fg='#FFFFFF').pack(pady=10)

        login_again_btn = tk.Button(profile_frame, text='Login Again', font=('Arial', 12), command=self.login_again,
                                    bg='#7289DA', fg='#000000', width=12, bd=0, padx=5, pady=5)
        login_again_btn.pack(pady=20)

        self.profile_window.mainloop()

    def login_again(self):
        self.profile_window.destroy()
        self.__init__()

if __name__ == '__main__':
    SimpleLogin()