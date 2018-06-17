import openml
import pandas as pd
apikey = '3cf8984da3879f7d43dace5524bbe4cb'
openml.config.apikey = apikey
tasks = openml.tasks.list_tasks(task_type_id=1)
tasks = pd.DataFrame.from_dict(tasks, orient='index')
#tasks.to_csv('MyTask.csv')
filtered_tasks = tasks.query('estimation_procedure == "10 times 10-fold Crossvalidation"')
filtered_tasks_2 = filtered_tasks.query('evaluation_measures == "predictive_accuracy"')
filtered_tasks_3 = filtered_tasks_2.query('NumberOfClasses == 2')
print(filtered_tasks_3.index)
print(len(filtered_tasks_3))
