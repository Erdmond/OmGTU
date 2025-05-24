import pandas as pd
import joblib as j

def main(data_path):

    data = pd.read_csv(data_path).drop(columns=['Unnamed: 0'])

    model = j.load(r'D:\Python\OmGTU\Practicum\LAB_3\best_cart_ga.joblib')
    y_pred = model.predict(data).tolist()

    return y_pred
