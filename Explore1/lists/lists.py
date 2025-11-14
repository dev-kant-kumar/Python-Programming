papers = ['Multimedia','Operating System','Visual Programming','HTML','Networking']

print(f"No of papers : {len(papers)} " )
print(papers[1])
print(papers[1:3])
papers[1] = "C++"
print("Current papers",papers)
papers[1:3]= ["C programming","Java"]
print("Current papers",papers)


# list comprehension
new_papers = [x.lower() for x in papers]
print("new papers",new_papers)
papers.sort()
print(papers)

print("\n================================================\n")
numbers = [55,6,89,66,45,33,90]

print("Number : ",numbers)
numbers.sort()
print("Number in ascending order : ",numbers)
numbers.sort(reverse = True)
print("Numbers in descending order : ",numbers)