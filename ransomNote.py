class Solution(object):
    
  def canSpell(self, magazine, word):
      result = True
      dictMag = {}
      for letter in magazine:
          amount = 1
          if letter in dictMag:
             amount += 1 
          dictMag[letter] = amount

      for letter in word:
          if letter in dictMag and dictMag[letter] >= 1:
            dictMag[letter] = dictMag[letter] -1 
          else:
            result = False
            break

      return result

magazine = ["a", "b", "c", "d", "e", "d"]
word = ["b", "e", "d"]

print(Solution().canSpell(magazine, word))

magazine = ["a", "b", "c", "d", "e", "d"]
word = ["b", "e", "d", "r", "o"]

print(Solution().canSpell(magazine, word))