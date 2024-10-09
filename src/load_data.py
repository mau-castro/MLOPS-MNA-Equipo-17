import pandas as pd



def load_csv(path):
    Mutations_df = pd.read_csv(path)
    return Mutations_df
                       
