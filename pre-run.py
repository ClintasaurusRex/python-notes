lst = input().split(",") # 1,2,3,4,5,6,7,8,9,10
lst_len = len(lst)
if lst_len % 2 == 0:
  mid = lst_len // 2
  result = lst[mid-1:mid+1]
  print(result)
else:
  mid = lst_len // 2
  result = lst[mid-1:mid+2]
  print(result)

# cat,dog,bird,fish,hamster,snake,rabbit,turtle,mouse




  





