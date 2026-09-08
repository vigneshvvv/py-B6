# pip install pandas
# python -m pip install pandas

import pandas as pd

df = pd.read_csv("studentDetails.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.head(3))
# print(df.shape)
# print(df.columns)

# print(df.dtypes)

# print(df.info())

# print(df.describe())

# print(df["name"])

# print(df[["name", "Department"]])

# print(df.iloc[2])

# print(df.iloc[0:3])

# print(df.iloc[0,1])


# result = df[df["Marks"] > 400]
# print(result)

# result = df[(df["Marks"] > 400) & (df["Department"] == "EEE")]
# print(result)

# result = df[df["Department"].isin(["EEE", "ECE"])]
# print(result)

# result = df.sort_values("Marks")
# print(result)

# result = df.sort_values("Marks", ascending=False)
# print(result)

# df["percentage"] = df["Marks"] / 5
# print(df)

# df = df.drop("Marks", axis=1)
# df = df.drop(["Marks", "Department"], axis=1)
# print(df)

# df = df.drop(1)

# df = df.drop_duplicates()
# print(df)

# print(df["Department"].value_counts())

# print(df["Department"].unique())

# print(df["Marks"].sum())

# print(df["Marks"].mean())

# print(df["Marks"].max())

# result = df.groupby("Department")["Marks"].mean()
# print(result)

result = df.groupby("Department")["Marks"].agg(["min", "max", "mean", "sum", "count"])
# print(result)

# df["name"] = df["name"].str.upper()
# print(df)

# df.to_csv("student_output.csv", index= False)

# dk = pd.read_csv("student_output.csv")
# print(dk)

result.to_csv("student_output.csv", mode="a", index=False, header=False)
dk = pd.read_csv("student_output.csv")
print(dk)