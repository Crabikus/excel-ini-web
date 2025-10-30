import pandas as pd

excel_path = r'C:\Users\mikhail.zernov\Documents\routingconfig\RoutingMAP-CGW_V5.2.0_20250705.xlsx'

excel_file = pd.ExcelFile(excel_path)
print('Sheet names:', excel_file.sheet_names)

sheet_name = "RouteTable"
print(f'\nAnalyzing sheet: {sheet_name}\n')

df = pd.read_excel(excel_path, sheet_name=sheet_name)

print('Column headers:')
print(list(df.columns))

print('\nSample rows:')
print(df.head(5).to_string(index=False))