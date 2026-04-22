import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (must be in same folder)
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")


print(dalys_data.head(5))

print(dalys_data.info())

print(dalys_data.describe())

print("Max DALYs:", dalys_data["DALYs"].max())
print("Min DALYs:", dalys_data["DALYs"].min())
print("First year:", dalys_data["Year"].min())
print("Most recent year:", dalys_data["Year"].max())

first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)

# Find year with max DALYs (first 10 Afghanistan rows)
max_row = first_10.loc[first_10["DALYs"].idxmax()]
print("Year with max DALYs (first 10 rows):", max_row["Year"])

zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_years)

print("Zimbabwe first year:", zimbabwe_years.min())
print("Zimbabwe last year:", zimbabwe_years.max())

# COMMENT:
# Zimbabwe data starts and ends in the years printed above.

# -------------------------------
# 2019 data (Entity + DALYs only)
# -------------------------------
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

# Max country
max_country = recent_data.loc[recent_data["DALYs"].idxmax()]
print("Country with max DALYs (2019):", max_country["Entity"])

# Min country
min_country = recent_data.loc[recent_data["DALYs"].idxmin()]
print("Country with min DALYs (2019):", min_country["Entity"])


country_name = max_country["Entity"]
country_data = dalys_data.loc[dalys_data["Entity"] == country_name]

plt.plot(country_data["Year"], country_data["DALYs"], 'bo')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {country_name}")
plt.xticks(rotation=-90)
plt.show()
plt.figure()
plt.hist(recent_data["DALYs"], bins=20)
plt.xlabel("DALYs")
plt.ylabel("Frequency")
plt.title("Distribution of DALYs across countries in 2019")
plt.show()