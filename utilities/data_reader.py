import pandas


def get_csv_into_list(csv_file_path:str):
    df = pandas.read_csv(filepath_or_buffer=csv_file_path, delimiter=";")
    return df.values.tolist()

