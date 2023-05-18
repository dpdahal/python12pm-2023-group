students = [
    {
        "name": "Mark", "age": 23,
        "address": {
            "country": [{"name": "USA"},
                        {"name": "Nepal"}
                        ]        }
    },
    {
        "name": "Hari", "age": 50, "address":
        {"country": [{"name": "India"},
                     {"name": "China"}
                     ]
         }}
]
for student in students:
    print(student["name"])
    print(student["address"]["country"][0]["name"])

# oop
