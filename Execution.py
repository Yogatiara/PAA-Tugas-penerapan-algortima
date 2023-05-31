import Dijkstra as distance
import BinarySearch as target
import SortingAlgorithms as formation
import Hashing as hash
import Trie as search


class Execution:

  # Pemilihan sasaran prioritas penyerangan
  print(".::{Titik prioritas penyerangan}::.\n")
  dictionaryTarget = {
      "Telecommunication Station" : 10,
      "Weapon Warehouse" : 4,
      "Weapon Vactory" : 7,
      "Airport" : 3 ,
      "Oil Resource" : 8
  }

  listPriorityPoint = []

  for i in dictionaryTarget:
    listPriorityPoint.append(dictionaryTarget[i])
        
  targetPrioirty = target.BinarySearch()
  sortedPonts = targetPrioirty.quicksort(listPriorityPoint)

  target = "Oil Resource"
  targetPrioirty.binarySearch(sortedPonts, dictionaryTarget[target], target)
  target = "Telecommunication Station"
  targetPrioirty.binarySearch(sortedPonts, dictionaryTarget[target], target)
  target = "Weapon Warehouse"
  targetPrioirty.binarySearch(sortedPonts, dictionaryTarget[target], target)
  target = "Weapon Vactory"
  targetPrioirty.binarySearch(sortedPonts, dictionaryTarget[target], target)
  target = "Airport"
  targetPrioirty.binarySearch(sortedPonts, dictionaryTarget[target], target)

  print("\n")
  # Melakukan pengaturan formasi penyerangan
  print(".::{formasi penyerangan}::.\n")
  troops = {
      "Medic" : 2,
      "Tank troops " : 5,
      "Sniper" : 3,
      "Assult" : 4 ,
      "navy" : 1
  }

  listTroopsIndex = []

  for i in troops:
    listTroopsIndex.append(troops[i])

  troopsFormation = formation.sorting()
  troopsFormation.heapSort(listTroopsIndex)


  listTroops = [list(troops.keys())[list(troops.values()).index(listTroopsIndex[0])], list(troops.keys())[list(troops.values()).index(listTroopsIndex[1])], list(troops.keys())[list(troops.values()).index(listTroopsIndex[2])], list(troops.keys())[list(troops.values()).index(listTroopsIndex[3])], list(troops.keys())[list(troops.values()).index(listTroopsIndex[4])]]
  print(f"""Formasi yang dibentuk untuk melakukan penyerangan yaitu dengan urutan posisi: 
{listTroops}""")
  

# Menentukan jalur tercepat untuk menempuh titik lokasi tempur
print("\n")
print(".::{Jalur menuju medan perang}::.\n")
nodeA = distance.Node("A")
nodeB = distance.Node("B")
nodeC = distance.Node("C")
nodeD = distance.Node("D")
nodeE = distance.Node("E")
nodeF = distance.Node("F")
nodeG = distance.Node("G")
nodeH = distance.Node("H")

nodeA.add_edge("A", 5, nodeB, "B")
nodeA.add_edge("A", 10, nodeC, "C")
nodeA.add_edge("A", 6, nodeD, "D")

nodeB.add_edge("B", 5, nodeD, "D")
nodeB.add_edge("B", 16, nodeE, "E")
nodeB.add_edge("B", 13, nodeF, "F")

nodeC.add_edge("C", 10, nodeD, "D")
nodeC.add_edge("C", 5, nodeH, "H")
nodeC.add_edge("C", 19, nodeG, "G")

nodeD.add_edge("D", 8, nodeF, "F")
nodeD.add_edge("D",7, nodeH, "H")

nodeE.add_edge("E", 10, nodeG, "G")

nodeF.add_edge("F",4, nodeE, "E")
nodeF.add_edge("F", 17, nodeG, "G")

nodeH.add_edge("H", 8, nodeF, "F")
nodeH.add_edge("H",14, nodeG, "G")

determiningDistance = distance.Dijkstra()
determiningDistance.calculate(nodeB, "B")
determiningDistance.get_shortest_path(nodeG, "G")


# Melakukan pengiriman pesan dengan kriptografi
print("\n")
print(".::{Pengiriman pesan}::.\n")

randomMessage = hash.HAshing()
randomMessage.modASCII("Bantuan udara", 24)
randomMessage.modASCII("Perubahan formasi", 24)
randomMessage.modASCII("Bantuan Altileri", 24)
randomMessage.modASCII("Perubahan taktik", 24)
randomMessage.modASCII("Di depan ada musuh dengan senjata berat", 24)


# Melakukan pencarian kata yang berkaitan dengan taktik atau startegi perang
print("\n")
print(".::{Penyocokan pesan yang diterima}::.\n")
newTrie = search.Trie()
newTrie.insertString("bahaya")
newTrie.insertString("serang")
newTrie.insertString("maju")
newTrie.insertString("mundur")
newTrie.insertString("pindah")
newTrie.insertString("aman")
# deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("a"))
print(newTrie.searchString("bahaya"))
print(newTrie.searchString("baaya"))

