import numpy as np

# Given data
daily_steps = np.array([6532, 8741, 5403, 7829, 9126, 6087, 7324, 8560, 5972, 7645, 6891, 8102, 7456, 6213, 9034])

# 1. Sort the array in descending order
sorted_steps = np.sort(daily_steps)[::-1]
print("1. Sorted Daily Steps (Descending Order):", sorted_steps)
print()  # Skip a line

# 2. Calculate the mean and standard deviation (rounded to the nearest whole number)
mean_steps = np.mean(daily_steps)
std_dev_steps = np.std(daily_steps)

# Displaying results
print("2. Mean Daily Steps (Rounded):", round(mean_steps))
print("   Standard Deviation of Daily Steps (Rounded):", round(std_dev_steps))
print()  # Skip a line

# 3. Calculate the 25th, 50th (median), and 75th percentiles
percentile_25 = np.percentile(daily_steps, 25)
percentile_50 = np.percentile(daily_steps, 50)
percentile_75 = np.percentile(daily_steps, 75)

# Displaying percentile results
print("3. 25th Percentile:", percentile_25)
print("   50th Percentile (Median):", percentile_50)
print("   75th Percentile:", percentile_75)
print()  # Skip a line

# 4. Find how many participants averaged more than 7500 steps daily
count_above_7500 = np.sum(daily_steps > 7500)
print("4. Number of participants averaging more than 7500 steps daily:", count_above_7500)
