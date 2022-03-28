class Solution:
   def plusOne(digits: list) -> list:
      num = ""
      for i in digits:
         num += str(i)
      num = int(num)
      num += 1
      num = str(num)
      answer = []
      for i in num:
         answer.append(int(i))
      return answer
digits = [1, 2, 3]
print(Solution.plusOne(digits))