import pandas

# df=pandas.read_csv(filepath_or_buffer=r"D:\Mine\Company\Deloitte Aug 2026\EmployeeManagementAutomation\test_data\test_invalid_login.csv",delimiter=";")


# print(df)

# print(df.to_string().upper())

# # we want to use df.values.tolist()
# print(df.values.tolist())


# print(df.index)
# ls=[]
# for i in df.index:
#     print(df.loc[i].tolist())
#     ls.append(df.loc[i].tolist())


# print(ls)


# df=pandas.read_csv(filepath_or_buffer=r"D:\Mine\Company\Deloitte Aug 2026\EmployeeManagementAutomation\test_data\test_invalid_login.csv",delimiter=";")
# print(df.values.tolist())

from config import Config
import os

print(os.path.join(Config.DATA_DIR,"test_invalid_login.csv"))

df=pandas.read_csv(filepath_or_buffer=os.path.join(Config.DATA_DIR,"test_invalid_login.csv"),delimiter=";")
print(df.values.tolist())


df=pandas.read_excel(io=r"D:\Mine\Company\Deloitte Aug 2026\EmployeeManagementAutomation\test_data\orange_hrm_data.xlsx",sheet_name="test_add_valid_employee")
print(df)
print(df.values.tolist())