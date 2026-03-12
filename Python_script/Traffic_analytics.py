import pandas as pd
df = pd.read_csv("website_traffic.csv")
print(df.head())

df.dropna(inplace=True)
df['Engagement Score'] = df['Page Views'] * df['Time on Page']
df['User Loyalty'] = df['Previous Visits'] / (df['Previous Visits'] + 1)
print(df.head())

df.to_csv("processed_traffic_data.csv", index=False)
print("Processing Completed")
