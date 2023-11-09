'''a="adslkalkjdiwoenksvzdfsheioierqwhfakjhkdsgj"
k=['a','e','i','o','u']
sum=0
for i in range(len(a)):
   if i in k:
     sum=sum+1
     print(sum)'''
# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)

