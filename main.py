#Used for punctuation
import string

#open bible
f = open("bible.txt")
contents = f.read()
f.close() 

contents = contents.lower()

#get rid of punctuations
after_pun = contents.translate(str.maketrans('', '', string.punctuation))

#separate each word 
after_split = after_pun.split()

#Calculate the total words of bible
bible_len = len(after_split)

#Ask for the search term 
user_input = input("Please enter a word or phrase you want to search: ")
user_input = user_input.split()
user_len = len(user_input)

#take the length of the unser's input and compute for the bible
split_parts = [str(after_split[i:i+user_len]) for i in range(0, len(after_split), 1)]
print(split_parts)

#Convert them into a ditionary, key is the word or phrase, value is the frequency 
di = {}
for lin in split_parts:
  di[lin] = di.get(lin,0) + 1

#1. convert split_parts list to a string list in order to compare user_input to the strings in the list
#2. If user_input is in the list, get the value of the corresponding key in the dictionary. 
#3. Calculate the frequency per 1000 words 
#frequency = value * 1000 / bible_len
#percentage_frequency = frequency * 100, "%"