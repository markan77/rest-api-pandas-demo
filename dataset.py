import pandas as pd


def get_country_data(dataset_path: str = "facts_countries.csv") -> pd.DataFrame:
    df = pd.read_csv(dataset_path, sep=";", skiprows=[1])

    for column in df.columns:
        df[column].fillna(0, inplace=True)

    df_transposed = df.transpose()
    df_transposed.columns = df_transposed.iloc[0]
    df_transposed.columns = map(str.lower, df_transposed.columns)
    df_transposed = df_transposed[1:]

    return df_transposed


if __name__ == "__main__":
    df = get_country_data()
    print(df)



import json

from flask import Flask
from flask.json import jsonify

from dataset import get_country_data


app = Flask(__name__)


@app.route("/api")
def country_data():
    data_df = get_country_data()
    data_dict = json.loads(data_df.to_json())
    return jsonify(data_dict)

@app.route("/api/<country>")
def country_specific_data(country):
    data_df = get_country_data()
    data_dict = json.loads(data_df.to_json())

    country_data = data_dict.get(country.lower(), {})
    
    return jsonify(country_data)
