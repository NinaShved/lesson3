students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
a = len(students)
a1 = a
n = 0
n1 = 0

n_st = []
for n in range(a):
    name = students[n]['first_name']
    n_st = n_st.append[name]


    s = 0
    n1 = 0
    a1 = len(students)
    for n1 in range(a1):
        name1 = students[n1]['first_name']
        if name == name1:
            s += 1
    print(name,s)
    print(n_st)
