import pickle
import  tkinter as tk
from tkinter import filedialog 
import numpy as np
import pandas as pd


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
df = pd.read_pickle(file_path)

print(file_path)