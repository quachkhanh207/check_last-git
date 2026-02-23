A=["Python", "Java", "SQL", "Git"]
B=["Java", "Docker", "Go", "SQL"]
cung_co=set(A) & set(B)
print(cung_co)
only_A=set(A) - set(B)
print(only_A)
tat=set(A) | set(B)
print(tat)