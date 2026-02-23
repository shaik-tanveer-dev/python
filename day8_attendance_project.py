n=5
absent=0
present=0
for i in range(1,n+1,1):
    val = int(input(f"Enter a roll number {i} attendance: "))
    if val==0:
        absent+=1
    if val==1:
        present+=1
print(f"number of absents: {absent}")
print(f"number of presents: {present}")
percentage=(present/10)*100
print(f"average present: {percentage}")
'''output:
Enter a roll number 1 attendance:  1
Enter a roll number 2 attendance:  0
Enter a roll number 3 attendance:  1
Enter a roll number 4 attendance:  1
Enter a roll number 5 attendance:  0
number of absents: 2
number of presents: 3
average present: 30.0'''