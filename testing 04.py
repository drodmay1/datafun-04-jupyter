import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("penguins")

grades_dict = {
    'Wally': [87, 96, 70],
    'Eva': [100, 87, 90],  # Fixed the single quote here
    'Sam': [94, 77, 90],
    'Katie': [100, 81, 82],
    'Bob': [83, 65, 85]
}

grades = pd.DataFrame(grades_dict)
print(grades)

