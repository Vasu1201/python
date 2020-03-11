def reverse(word):
      return word[::-1]

def palindrome(word):
      rev = reverse(word)
      if word == rev:
            print("palindrame")
            return True
      else:
            print("not a plaindrome")
      return False

palindrome(input("enter word:"))
