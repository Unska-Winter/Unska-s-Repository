def trans_str_to_numberlist(str,n):
  str_split = str.split()
  number_list = []
  for i in range(0,n):
    number_list.append(int(str_split[i]))
  return number_list
