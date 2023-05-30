#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


class HAshing:
  def modASCII(self,string, cellNumber):
      total = 0
      for i in string:
          total += ord(i)
      print(f"{string} = {total % cellNumber}")

