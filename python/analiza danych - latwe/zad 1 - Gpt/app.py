import pandas as pd
import time

def calculate_statistics(csv_file):
    # Load data from CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    # Calculate mean
    mean = numeric_df.mean()

    # Calculate median
    median = numeric_df.median()

    # Calculate standard deviation
    std_dev = numeric_df.std()

    return mean, median, std_dev

def main():
    # Path to your CSV file
    csv_file = 'data.csv'

    # Start measuring compilation time
    start_compilation_time = time.time()

    # Calculate statistics
    mean, median, std_dev = calculate_statistics(csv_file)

    # Display statistics
    print("Mean:")
    print(mean)
    print("\nMedian:")
    print(median)
    print("\nStandard Deviation:")
    print(std_dev)

    # Stop measuring compilation time
    end_compilation_time = time.time()
    compilation_time = end_compilation_time - start_compilation_time
    print("\nTotal compilation time:", compilation_time, "seconds")

if __name__ == "__main__":
    main()
