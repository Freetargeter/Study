def bestSeller(bookNum, book):
  
  max = -1
  selling = dict()
  bestSellerBook = list()
  
  for i in book:
    if i not in selling:
      selling[i] = 0
    else:
      selling[i] += 1 
    if selling[i] > max: 
      max = selling[i]
    
  for j in selling:
    if selling[j] == max:
      bestSellerBook.append(j)
      
  for k in bestSellerBook:
    print(k)


bookNum1 = 5
book1 = ['top', 'top', 'top', 'top', 'kimtop']
# bestSeller(bookNum1, book1)

bookNum2 = 9
book2 = ['table', 'chair', 'table', 'table', 'lamp', 'door', 'lamp', 'table', 'chair']
# bestSeller(bookNum2, book2)

bookNum3 = 8
book3 = ['icecream', 'peanuts', 'peanuts', 'chocolate', 'candy', 'chocolate', 'icecream', 'apple']
bestSeller(bookNum3, book3)