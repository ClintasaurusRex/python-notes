shopping_list = ["bread", "eggs", "milk", "butter"]

def loop_list(items):
  sorted_items = sorted(items)
  for item in sorted_items:
    print(item)

loop_list(shopping_list)