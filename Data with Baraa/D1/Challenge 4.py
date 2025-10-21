#  COnvert the messy phone number Into
#  a clean number format with only digits
# "+49 (176) 123-4567"
# 00491761234567

number = "+49 (176) 123-4567"

print(number.replace("+", "00")
      .replace(" ", "")
      .replace("(", "")
      .replace(")", "")
      .replace("-", ""))

#  i could have cleaned this with re.sub() and strip but it wasn't discussed yet