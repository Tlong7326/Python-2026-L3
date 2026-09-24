def remove_dollar_sign(s):
    result = s.replace("$", "")
    if result == "":
        return "none"
    return result

text = input("Enter a string: ")
print(remove_dollar_sign(text))
