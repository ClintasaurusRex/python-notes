# Dictionaries Part 1





print("-------------------------------------Accessing Values-----------------------------")
def get_capital(country_capitals, country_name):
  # This function takes a dictionary of country capitals and a country name (key).
  # It returns the capital city (value) for the given country.
  # Example: get_capital({"Norway": "Oslo"}, "Norway") returns "Oslo"
  return country_capitals[country_name]

country_capitals = {"Norway": "Oslo", "Sweden": "Stockholm", "Denmark": "Copenhagen"}
print(get_capital(country_capitals, "Norway"))  # Output: Oslo



print("-----------------------------------Create Book Dict--------------------------")
def create_book_dict(title, author, year):
  return{"title": title, "author": author, 'year': year}


print("-----------------------------------Create Students Dict--------------------------")
def create_student_dict(name, age, major):
  # Creating a dictionary with keys and values:
  # Each key (e.g., "name") is a string that describes the data.
  # Each value (e.g., name) is the variable passed to the function.
  # This allows you to store related information together in a structured way.
  return {
    "name": name,    # The student's name (string)
    "age": age,      # The student's age (number)
    "major": major   # The student's major/field of study (string)
  }