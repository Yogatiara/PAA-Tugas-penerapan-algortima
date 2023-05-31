


class HAshing:
  def modASCII(self,string, cellNumber):
      total = 0
      for i in string:
          total += ord(i)
      print(f"{string} = {total % cellNumber}")

