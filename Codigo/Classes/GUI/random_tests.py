import customtkinter as ctk

# class MyFrame(customtkinter.CTkScrollableFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # add widgets onto the frame...
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=0, column=0, padx=20)


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.my_frame = MyFrame(master=self, width=300, height=200)
#         self.my_frame.grid(row=0, column=0, padx=20, pady=20)


# app = App()
# app.mainloop()



# a = ctk.CTk()
# # m = ctk.CTkTextbox(a, fg_color="red", height=1, activate_scrollbars=False, )
# m = ctk.CTkToplevel(a)
# m.focus()
# a.mainloop()


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.button_1 = ctk.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


app = App()
app.mainloop()