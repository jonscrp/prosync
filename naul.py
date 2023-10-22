import tkinter as tk
#import ast
import os
import genEvent
from dotenv import load_dotenv
import gc_createEvent
import openAIrequest
from PIL import Image, ImageTk
import os
import json

opeAi_key = "OPEN_AI_KEY_GO's Here"

def work():
    openAIEventResponse = openAIrequest.sendPrompt(opeAi_key, entry.get())
    # print(openAIEventResponse)
    # in the future we could attempt to store multiple events
    json_dict = json.loads(openAIEventResponse)
    genEvent.createEvent(json_dict)
    gc_createEvent.saveToCalendar(genEvent.createEvent(json_dict))
    
    

# Create the main application window
root = tk.Tk()
root.title("ProSync")

# Load and convert the PNG image
image_path = r"C:\Users\jsuco\OneDrive\Desktop\hackHarvard\src\prosynclogo.png"  # Replace with the path to your PNG image
image = Image.open(image_path)
image = image.resize((200, 200))  # Adjust the size as needed
photo = ImageTk.PhotoImage(image)

# Create a Label to display the image
image_label = tk.Label(root, image=photo)
image_label.pack()

# Create a label for user instructions (make the text larger)
instruction_label = tk.Label(root, text="Enter a prompt:", font=("Roboto", 32))
instruction_label.pack()

# Create an entry widget for user input (make it wider)
entry = tk.Entry(root, width=40)
entry.pack()

# Create a button to trigger the action
button = tk.Button(root, text="Perform Action", command=work)
button.pack()

# Start the Tkinter event loop
root.mainloop()
