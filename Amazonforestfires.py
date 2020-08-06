import pandas as pd
import numpy as np  
from texttable import Texttable
import matplotlib.pyplot as plt  

dataset1 = pd.read_csv("amazon.csv", thousands = '.')

print(dataset1)