import pandas as pd

excel_file_1 = 'export-8-23.xlsx'

df = pd.read_excel(excel_file_1, sheet_name='partmstr')

df.loc[0:1087, ["part_code","part_desc","part_price","part_grp","part_subgrp","part_subgrp2","part_subgrp3","add_date","long_desc1"]].to_excel('output.xlsx', engine='xlsxwriter')
#xlswriter helps debug unicode objects










