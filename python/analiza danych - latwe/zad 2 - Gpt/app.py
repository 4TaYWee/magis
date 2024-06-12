import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values_bar = [23, 45, 56, 78]  # Bar chart values
values_line = [10, 20, 30, 40]  # Line chart values

# Creating a bar chart
plt.figure(figsize=(10, 5))  # Adjust size as needed
plt.bar(categories, values_bar, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.grid(True)
plt.show()

# Creating a line chart
plt.figure(figsize=(10, 5))  # Adjust size as needed
plt.plot(categories, values_line, marker='o', color='orange', linestyle='-')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Line Chart Example')
plt.grid(True)
plt.show()
