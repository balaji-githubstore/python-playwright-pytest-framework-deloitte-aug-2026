from utilities import data_reader
import os
from config import Config


class DataSource:
    data_invalid_login = [
        ["saul", "saul123", "Invalid credentials"],
        ["kim", "kim123", "Invalid credentials"]
    ]

    data_valid_login = [
        ["Admin", "admin123", "Quick Launch"],
        ["Admin", "admin123", "Quick Launch"]
    ]

    data_invalid_login_csv = data_reader.get_csv_into_list(
        os.path.join(Config.DATA_DIR, "test_invalid_login.csv"))

    data_invalid_login_excel = data_reader.get_excel_sheet_into_list(
        os.path.join(Config.DATA_DIR, "orange_hrm_data.xlsx"), "test_invalid_login")
