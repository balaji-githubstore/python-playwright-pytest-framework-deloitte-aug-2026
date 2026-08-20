import os

class Config:
    ROOT_DIR=os.path.dirname(os.path.abspath(__file__))
    DATA_DIR=os.path.join(ROOT_DIR,"test_data")
    REPORT_DIR=os.path.join(ROOT_DIR,"reports")
