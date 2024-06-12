import matplotlib.pyplot as plt
import time

# Sample data (replace with your own data)
x_data = ["Cat", "Dog", "Bird"]
y_data = [5, 3, 2]

# Choose between bar chart or line chart
chart_type = "bar"  # Change to "line" for line chart

def generate_chart(data_x, data_y, chart_type):
  start_time = time.time()  # Record start time

  # Create the plot
  plt.figure(figsize=(8, 6))
  if chart_type == "bar":
      plt.bar(data_x, data_y)
  else:
      plt.plot(data_x, data_y)

  # Rest of your customization code (labels, title, etc.)

  # Stop time measurement
  end_time = time.time()
  execution_time = end_time - start_time

  # Print execution time (you can modify this to display elsewhere)
  print(f"Chart creation time: {execution_time:.4f} seconds")

  # Display the chart
  plt.tight_layout()
  plt.show()

# Call the function to generate chart and measure time
generate_chart(x_data, y_data, chart_type)
