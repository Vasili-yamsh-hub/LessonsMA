import weather
import customtkinter 

def information():
    c = qbox.get()
    b = weather.get_wether(c)
    txt.delete(1.0 , "end")
    txt.insert(1.0 , b)
    print(b)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

city = ["Ufa", "Kazan", "Sochi", "Novorosisk"]

app = customtkinter.CTk()
app.title("Программа Погода")
app.geometry("300x300")

qbox = customtkinter.CTkComboBox(app, values = city)
qbox.pack()

btt = customtkinter.CTkButton(app, text = "Узнать погоду", command = information)
btt.pack(side = "bottom")

txt = customtkinter.CTkTextbox(app)
txt.pack(side = "top")


app.mainloop()

