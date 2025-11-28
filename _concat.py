import pandas as pd



table_a_path = "_5.xlsx"
table_b_path = "_6.xlsx"
# table_c_path = "steel_3.xls"
# table_d_path = "steel_4.xls"
df_a =pd.read_excel(table_a_path,sheet_name="Sheet1")
df_b = pd.read_excel(table_b_path,sheet_name="Sheet1")
# df_c = pd.read_excel(table_c_path,sheet_name="Sheet1")
# df_d = pd.read_excel(table_d_path,sheet_name="Sheet1")
df_combined = pd.concat([df_a,df_b],ignore_index=True)

# 重新索引
# df_combined.reset_index(drop=True,inplace=True)

output_path = "_5.xlsx"
df_combined.to_excel(output_path,sheet_name="Sheet1",index=False)
print("Done!")