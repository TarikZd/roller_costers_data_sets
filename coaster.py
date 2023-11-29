# Step 0: Imports and Reading Data

import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


df = pd.read_csv('coaster_db.csv')

print(df.shape)