mytupil=()
sample=()

for i in range(1,6):
    print("pls enter the details for group number",i)
    groupname=input("pls enter the group name")
    date=input("pls enter the date of the competition")
    sizeofgroup=int(input("pls enter the number of people"))
    venue=input("what is the venue adress")
    typeofmedal=input("what is the medal going to be made of")
    sample=(groupname,date,sizeofgroup,venue,typeofmedal)
    mytupil= mytupil+sample

print(mytupil)