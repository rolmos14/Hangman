students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Solution with union():
# subjects = set(Belov).union(set(Smith)).union(set(Sarada))

# Solution with update():
# subjects = set()
# subjects.update(Belov, Smith, Sarada)

# Solution joining lists:
subjects = set(Belov + Smith + Sarada)

print(len(subjects))
