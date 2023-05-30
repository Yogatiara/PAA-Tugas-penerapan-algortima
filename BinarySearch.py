
import math

class BinarySearch:
  def swap(self, my_list, index1, index2):
      my_list[index1],  my_list[index2] = my_list[index2],  my_list[index1]


  def pivot(self, my_list, pivot_index, end_index):
      swap_index = pivot_index
      for i in range(pivot_index+1, end_index+1):
          if my_list[i] < my_list[pivot_index]:
              swap_index += 1
              self.swap(my_list, swap_index, i)
      self.swap(my_list, pivot_index, swap_index)
      return swap_index


  def quicksort_helper(self, my_list, left, right):
      if left < right:
          pivot_index = self.pivot(my_list, left, right)
          self.quicksort_helper(my_list, left, pivot_index-1)
          self.quicksort_helper(my_list, pivot_index+1, right)
      return my_list

  def quicksort(self, my_list):
      return self.quicksort_helper(my_list, 0, len(my_list)-1)

  def binarySearch(self, array, value, target):
      start = 0
      end = len(array)-1
      middle = math.floor((start+end)/2)
      while not(array[middle]==value) and start<=end:
          if value < array[middle]:
              end = middle - 1
          else:
              start = middle + 1 
          middle = math.floor((start+end)/2)
      if array[middle] == value:
          if middle == 0:
            print(f"{target} prioritas pertama penyerangan")
          if middle == 1:
            print(f"{target} prioritas kedua penyerangan")
          if middle == 2:
            print(f"{target} prioritas ketiga penyerangan")
          if middle == 3:
            print(f"{target} prioritas keempat penyerangan")
          if middle == 4:
            print(f"{target} prioritas kelima penyerangan")     
      else:
          print("Target tidak didalam list")
