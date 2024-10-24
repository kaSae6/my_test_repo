import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


weather_df = pd.read_csv('wetter.csv')

#################### avg temp
avg_temp = round(weather_df['Temperatur'].mean(), 1)
print(f"The average overall temperature is: {avg_temp}")

################# avg july temp
# Convert 'Datum' column to datetime format, if necessary
weather_df['Datum'] = pd.to_datetime(weather_df['Datum'], format='%Y-%m-%d')

# Filter rows where the month is July
july_df = weather_df[weather_df['Datum'].dt.month == 7]

july_avg_temp = round(july_df['Temperatur'].mean(), 1)

print(f"The average overall temperature is: {avg_temp}")


################### july and may significant diff?
# Extract July temperatures
july_temps = weather_df[weather_df['Datum'].dt.month == 7]['Temperatur']

# Extract May temperatures
may_temps = weather_df[weather_df['Datum'].dt.month == 5]['Temperatur']



def check_significance(july_temps, may_temps):
    shapiro_july = stats.shapiro(july_temps)[1]
    shapiro_may = stats.shapiro(may_temps)[1]

    if shapiro_july > 0.05 or shapiro_may > 0.05:
        t_stat, p_value = stats.ttest_ind(july_temps, may_temps)
    else:
        t_stat, p_value = stats.mannwhitneyu(july_temps, may_temps)
    
    print(f'The average temp of July is {round(july_temps.mean(), 1)}')
    print(f'The average temp of May is {round(may_temps.mean(), 1)}')

    if p_value <= 0.05:
        print(f'The test p_value is {p_value} indicating a significant difference between the average month temps')
    
    else:
        print(f'The test p_value is {p_value} indicating no significant difference between the average month temps')


check_significance(july_temps, may_temps)

print()