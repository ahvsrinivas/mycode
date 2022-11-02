
import pandas as pd

df = pd.read_csv('annualcheeseconsumed.txt')
df = df.set_index('Year')
short_df = df[["Cheddar","Swiss","Muenster"]]
recentdf = short_df.sort_values(["Year"], ascending=False)
print(recentdf.head(2))

#print(short_df.shape)
#print(short_df.head(2))

