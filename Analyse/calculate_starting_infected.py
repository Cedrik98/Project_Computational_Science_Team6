# IMPORTING LIBRARIES:
import pandas as pd

# Functions:
# Return percentage x per 100k
def calculate_percentage(x):
    return x*100/100000

# CLEANING THE DATASET:
df = pd.read_csv (r'California_Daily_Stats.csv')
df = df.drop(columns=["area", "area_type", "vaccinated_hosp", "unvaccinated_hosp"
                     , "unvaccinated_deaths", "vaccinated_deaths", "vaccinated_hosp_per_100k"
                     , "unvaccinated_hosp_per_100k", "unvaccinated_deaths_per_100k"
                     ,"vaccinated_deaths_per_100k"])
df = df.fillna(0)

# print(df)

# List storing all percentages
unvaccinated_percentage_list = []
vaccinated_percentage_list = []
# Contagious duration in days:
contagious_duration = 5
for x, z in zip(df.unvaccinated_cases_per_100k, df.vaccinated_cases_per_100k):
    unvaccinated_percentage_list.append(round(calculate_percentage(x), 3))
    vaccinated_percentage_list.append(round(calculate_percentage(z), 3))
percentage_average_infected = (round(sum(unvaccinated_percentage_list[-8:]))/len(vaccinated_percentage_list[-8:])) + (round(sum(unvaccinated_percentage_list[-8:]))/len(vaccinated_percentage_list[-8:]))

# Starting percentage of infected people:
starting_percentage = percentage_average_infected*contagious_duration
print(f"The starting percentage of people being infected",starting_percentage)
