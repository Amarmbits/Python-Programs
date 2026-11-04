s=input("Enter a string:\n")
print(s)
char=s[0]
s=s.replace(char,'$')
s='$'+s[1:]
print(s)
