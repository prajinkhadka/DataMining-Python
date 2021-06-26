import pandas as pd

student = "https://github.com/TrainingByPackt/Data-Science-with-Python/blob/master/Chapter01/Data/student.csv"

marks = "https://github.com/TrainingByPackt/Data-Science-with-Python/blob/master/Chapter01/Data/mark.csv"

student_dataframe = pd.read_csv(student, header = 0)

marks_dataframe = pd.read_csv(marks, header = 0)

# StudnetID is common in both dataframe.
# So, we would merge with respect to Studnet_id column using pd.merge() function


new_dataframe = pd.merge(student_dataframe, marks_dataframe)

