# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }

family_member = dict()
family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ["running", "sky diving", "singing"]
family_member['age'] = '35'
family_member['children'] = [{
    'name': 'Alice',
    'age': '6'},
    {'name': 'Bob',
     'age': '8'}
]
print(family_member['children'][0].get('name'))
