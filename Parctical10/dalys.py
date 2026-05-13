import pandas as pd
import matplotlib.pyplot as plt
# Load dataset (the CSV file must be in the same folder as this Python file)
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# Look at the beginning of the dataframe
print(dalys_data.head(5))
# Show information about the dataframe
print(dalys_data.info())
# Show summary statistics for the dataframe
print(dalys_data.describe())
# Use describe / summary functions to answer basic questions
print("Max DALYs:", dalys_data["DALYs"].max())
print("Min DALYs:", dalys_data["DALYs"].min())
print("First year:", dalys_data["Year"].min())
print("Most recent year:", dalys_data["Year"].max())
# Show the third and fourth columns (Year and DALYs) for the first 10 rows
first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)
# Find the year with the maximum DALYs in the first 10 Afghanistan rows
max_row = first_10.loc[first_10["DALYs"].idxmax()]
print("Year with max DALYs (first 10 Afghanistan rows):", max_row["Year"])
# COMMENT: The maximum DALYs in the first 10 Afghanistan rows was in 1998.
# Use a Boolean to show all years for which DALYs were recorded in Zimbabwe
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_years)
print("Zimbabwe first year:", zimbabwe_years.min())
print("Zimbabwe last year:", zimbabwe_years.max())
# COMMENT: Zimbabwe DALYs data were recorded from 1990 to 2019.
# -------------------------------
# 2019 data (Entity + DALYs only)
# -------------------------------
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
# Find the country with the maximum DALYs in 2019
max_country = recent_data.loc[recent_data["DALYs"].idxmax()]
print("Country with max DALYs (2019):", max_country["Entity"])
# Find the country with the minimum DALYs in 2019
min_country = recent_data.loc[recent_data["DALYs"].idxmin()]
print("Country with min DALYs (2019):", min_country["Entity"])
# COMMENT: In 2019, Lesotho had the maximum DALYs and Singapore had the minimum DALYs.
# Plot DALYs over time for one of the countries identified above
country_name = max_country["Entity"]
country_data = dalys_data.loc[dalys_data["Entity"] == country_name]
plt.plot(country_data["Year"], country_data["DALYs"], 'bo')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {country_name}")
plt.xticks(rotation=-90)
plt.show()
# QUESTION SECTION: Distribution of DALYs across all countries in 2019
plt.figure()
plt.hist(recent_data["DALYs"], bins=20)
plt.xlabel("DALYs")
plt.ylabel("Frequency")
plt.title("Distribution of DALYs across countries in 2019")
plt.show()
