import os

currentDir = os.getcwd();
print(f"Your current directior is : {currentDir}")

print(os.listdir(currentDir))
print(os.cpu_count())
print(os.getlogin())
print(os.__file__)
