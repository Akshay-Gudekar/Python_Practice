import numpy as np
import pandas as pd

# Generate 100 random integer values between 7000 and 7500 for each of the 5 columns
random_values = np.random.randint(15250, 22000, (200, 5))  # 100 rows, 5 columns

# Create a DataFrame for better visualization
df = pd.DataFrame(random_values, columns=[f'Column {i+1}' for i in range(5)])

# Display the DataFrame
df.to_csv("random_values")