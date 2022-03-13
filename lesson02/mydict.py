

my_dict = dict()
my_dict['hp'] = 10
my_dict['str'] = 22

print (my_dict)
print(my_dict['hp'])
my_dict['hp']  = my_dict['hp']  - 1
print(my_dict['hp'])


grades = { 'math': 10, 'dutch': 7, 'italian': 6, 'programming': 10}

for subject in ['math', 'latin']:
    grade =  grades.get(subject, 0)
    print('Subject {}, grade {}'.format(subject, grade))


school =[
    {'name': 'Mark', 'grades': dict(grades)},
    {'name': 'Jan', 'grades': dict(grades)},
]

school[0]['grades']['math'] = 5

print(school)
