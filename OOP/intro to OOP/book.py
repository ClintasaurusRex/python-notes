class Book:
  # The init method is a special method that automatically runs when the new object is made and gives it these default attributes. Its called a constructor method
  
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages