import pandas as pd

def hello_world():
    print("Hola soy pau")
    print("hello world!")
    
    
    
def show_df(df):
    
    print(df.shape)
    display(df.head())
    display(df.describe())