for i in range(2):
    for j in range(2):
        print(f"[{i}, {j}]")
        
person = ["Eseng", 18, "Female"]
print(person)
person += ["Philppines"]
print(person)
name, *details, country = person
print(name, details, country)