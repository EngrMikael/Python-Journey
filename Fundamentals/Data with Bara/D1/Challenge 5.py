#  turn messy string into a single clean
#  summary with name, role, and age
 
#  "968-Maria, ( D@t@ Engineer );; 27y  "
#  "name: maria | role: data engineer | age: 27"

text = "968-Maria, ( D@t@ Engineer );; 27y  "

print(text.rstrip()
      .replace("-", " ")
      .replace(",", " |")
      .replace("(", "role:")
      .replace(")", "|")
      .replace("@", "a")
      .replace(";;", " age:")
      .replace("y", "")
      .replace("968", "name:")
      .lower())