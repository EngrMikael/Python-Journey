# this is an example:
# names = ["Eseng", "John", "a", "Naz", None]

# for name in range(len(names)):
#     if names[name] is None or names[name] == "":
#         print(f"Found a missing name at: index {name}")
#         break
# else:
#     print("There is no missing name")

# this is the challenge, print Dubplicate Found if a duplicate exists,
# otherwise print All Fiels are Unique

file_list = [
    "report.csv",
    "data.xlsx",
    "summary.docx",
    "report.csv",
    "data.csv"
]
seen = {}
for file in file_list:
    if file in seen:
        seen[file] += 1
    else:
        seen[file] = 1

for file, count in seen.items():
    if count > 1:
        print(f"The Duplicate is: {file} it was repeated: {count} times")
        break
else:
    print("There are no Duplicates")