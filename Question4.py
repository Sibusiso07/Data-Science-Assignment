import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2019', '2020', '2021', '2022', '2023']
fiction = np.array([120, 110, 130, 125, 140])
non_fiction = np.array([95, 100, 110, 115, 120])
childrens_books = np.array([55, 65, 70, 75, 80])
textbooks = np.array([80, 85, 75, 90, 95])

# Create the stacked bar graph
plt.figure(figsize=(10, 6))

# Stacking the bars
p1 = plt.bar(years, fiction, color='skyblue', label='Fiction')
p2 = plt.bar(years, non_fiction, bottom=fiction, color='orange', label='Non-Fiction')
p3 = plt.bar(years, childrens_books, bottom=fiction + non_fiction, color='green', label="Children's Books")
p4 = plt.bar(years, textbooks, bottom=fiction + non_fiction + childrens_books, color='red', label='Textbooks')

# Adding text labels on each segment
for i in range(len(years)):
    plt.text(i, fiction[i] / 2, str(fiction[i]), ha='center', color='black')
    plt.text(i, fiction[i] + non_fiction[i] / 2, str(non_fiction[i]), ha='center', color='black')
    plt.text(i, fiction[i] + non_fiction[i] + childrens_books[i] / 2, str(childrens_books[i]), ha='center', color='black')
    plt.text(i, fiction[i] + non_fiction[i] + childrens_books[i] + textbooks[i] / 2, str(textbooks[i]), ha='center', color='black')

# Adding labels
plt.xlabel('Year')
plt.ylabel('Sales in Thousands of Dollars')
# Adding title
plt.title('Bookstore Sales by Genre Over the Past Five Years')

# Adding legend
plt.legend()

# Display the plot
plt.show()
