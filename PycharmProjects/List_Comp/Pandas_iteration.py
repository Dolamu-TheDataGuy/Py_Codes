student_dict = {
    "student": ["Angela", "James","Lily"],
    "score": [56,76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
        print(value)

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame -> Iterrows
for (index, rows) in student_data_frame.iterrows():
    if rows.student == "Angela":
        print(rows.score)

