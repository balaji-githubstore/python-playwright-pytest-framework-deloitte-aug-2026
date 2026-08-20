import pandas


def get_csv_into_list(csv_file_path: str):
    df = pandas.read_csv(filepath_or_buffer=csv_file_path, delimiter=";")
    return df.values.tolist()


def get_excel_sheet_into_list(excel_file_path: str, sheetname: str):
    df = pandas.read_excel(io=excel_file_path,sheet_name=sheetname)
    return df.values.tolist()
