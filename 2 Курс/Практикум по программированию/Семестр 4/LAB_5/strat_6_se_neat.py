import pandas as pd
import joblib as j

def main(data_path):
    data = pd.read_csv(data_path, index_col=0).drop("collision", axis=1).values

    model = j.load(r'D:\Python\OmGTU\Practicum\LAB_3\es_neat_big.joblib')
    predictions = [round(model.activate(x)[0]) for x in data]

    return predictions
