import pandas as pd

data = [["Alex", 10], ["Bob", 12], ["Clara", 13]]
df = pd.DataFrame(data, columns=["Name", "Age"])
df.to_pickle("sample_data.pkl")
