import random
import string
from tkinter import *
from twilio.rest import Client
import os

# Initialize Tkinter
root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # Full screen mode
root.title("Random Password Generator App")
root.configure(bg="green")  # Change background color to dark blue

# Load Twilio credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'AC898b953d48d78f00409c7e8ac5ed7600')
auth_token = os.getenv('TWILIO_AUTH_TOKEN', '268d3dcbe5859c3cbafadf1789667121')
client = Client(account_sid, auth_token)

# Function to generate random password
def gen():
    try:
        num = int(password_length_spinbox.get())
        if num > 10:
            show_error("Password length cannot be more than 10")
            return
        
        characters = string.ascii_letters + string.digits
        password = ''.join(random.sample(characters, num))  # Generate password

        # Clear previous password label if exists
        for widget in app_frame.winfo_children():
            if isinstance(widget, Label) and widget['text'].startswith("Password : "):
                widget.destroy()

        # Display password in the GUI
        password_label_shadow = Label(app_frame, text="Password : ", font="time 12 bold", bg="black", fg="white")
        password_label_shadow.place(x=202, y=352)
        password_label = Label(app_frame, text="Password : ", font="time 12 bold", bg="black", fg="white")
        password_label.place(x=200, y=350)

        generated_password_label_shadow = Label(app_frame, text=password, font="time 15 bold", width=18, bg="black", fg="white")
        generated_password_label_shadow.place(x=302, y=352)
        generated_password_label = Label(app_frame, text=password, font="time 15 bold", width=18, bg="white")
        generated_password_label.place(x=300, y=350)
        
        send_button_shadow = Button(app_frame, text="Send Password", fg="white", width=26, bg="black", font="time 15 bold")
        send_button_shadow.place(x=202, y=392)
        send_button = Button(app_frame, text="Send Password", fg="white", width=26, bg="green", font="time 15 bold", command=lambda: send_sms("+919348966429", password, name_entry.get()))
        send_button.place(x=200, y=390)
    except ValueError:
        show_error("Please enter a valid number for password length")

def show_error(message):
    error_label_shadow = Label(app_frame, text=message, font="time 12 bold", fg="red", bg="#030922")
    error_label_shadow.place(x=202, y=272)
    error_label = Label(app_frame, text=message, font="time 12 bold", fg="red", bg="black")
    error_label.place(x=200, y=270)

# Function to send SMS
def send_sms(to_number, password, user_name):
    if not user_name or not password:
        print("User name or password cannot be empty.")
        return
    
    message_body = f"Hello {user_name},\nYour Random Password is: {password}\nThis password has been given by SBI bank. Do not share your password with anyone."
    try:
        message = client.messages.create(
            body=message_body,
            from_='+14247898525',  # Replace with your Twilio number
            to=to_number
        )
        print("SMS sent successfully. SID:", message.sid)
    except Exception as e:
        print("Failed to send SMS:", str(e))

# Create a frame to contain the app's elements with shadow
shadow_offset = 2

app_frame_shadow = Frame(root, bg="black", bd=5, relief=RIDGE)
app_frame_shadow.place(relx=0.5, rely=0.45, anchor=CENTER, width=800+shadow_offset, height=500+shadow_offset)
app_frame = Frame(root, bg="black", bd=5, relief=RIDGE)
app_frame.place(relx=0.5, rely=0.45, anchor=CENTER, width=800, height=500)

# GUI elements with shadow effect
title_label_shadow = Label(app_frame, text="Random Password Generator App", font="time 20 bold", bg="black", fg="white")
title_label_shadow.place(x=202, y=32)
title_label = Label(app_frame, text="Random Password Generator App", font="time 20 bold", bg="black", fg="white")
title_label.place(x=200, y=30)

name_label_shadow = Label(app_frame, text="Enter Your Name : ", font="time 12 bold", bg="black", fg="white")
name_label_shadow.place(x=202, y=92)
name_label = Label(app_frame, text="Enter Your Name : ", font="time 12 bold", bg="black", fg="white")
name_label.place(x=200, y=90)

name_entry_shadow = Entry(app_frame, width=35, bd=2, font="time 13 bold", bg="#032307", fg="white")
name_entry_shadow.place(x=202, y=122)
name_entry = Entry(app_frame, width=35, bd=2, font="time 13 bold")
name_entry.place(x=200, y=120)

mobile_label_shadow = Label(app_frame, text="Enter Mobile Number : ", font="time 12 bold", bg="black", fg="white")
mobile_label_shadow.place(x=202, y=152)
mobile_label = Label(app_frame, text="Enter Mobile Number : ", font="time 12 bold", bg="black", fg="white")
mobile_label.place(x=200, y=150)

mobile_number_entry_shadow = Entry(app_frame, width=35, bd=2, font="time 13 bold", bg="#030f23", fg="white")
mobile_number_entry_shadow.place(x=202, y=182)
mobile_number_entry = Entry(app_frame, width=35, bd=2, font="time 13 bold")
mobile_number_entry.place(x=200, y=180)

password_length_label_shadow = Label(app_frame, text="Enter Password Length : ", font="time 12 bold", bg="black", fg="white")
password_length_label_shadow.place(x=202, y=212)
password_length_label = Label(app_frame, text="Enter Password Length : ", font="time 12 bold", bg="black", fg="white")
password_length_label.place(x=200, y=210)

password_length_spinbox_shadow = Spinbox(app_frame, from_=1, to=10, width=33, bd=2, font="time 13 bold", bg="black", fg="white")
password_length_spinbox_shadow.place(x=202, y=242)
password_length_spinbox = Spinbox(app_frame, from_=1, to=10, width=33, bd=2, font="time 13 bold")
password_length_spinbox.place(x=200, y=240)

generate_button_shadow = Button(app_frame, text="Generate Password", fg="white", bg="black", font="time 15 bold", width=26)
generate_button_shadow.place(x=202, y=302)
generate_button = Button(app_frame, text="Generate Password", fg="white", bg="green", font="time 15 bold", width=26, command=gen)
generate_button.place(x=200, y=300)

root.mainloop()
