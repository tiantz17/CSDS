# CSDS

This is for class select dialogue system

## How to get a column of data?

```python
import pandas as pd

data = pd.read_csv('2017-2018-2-graduate-0.csv', sep='\t')
data.info() // display information
dept = data['开课院系']
name = data['课程名']
for i in dept.index:
  print(dept[i])
```
