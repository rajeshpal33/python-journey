
with open("jarvis_memory.txt", "w") as file:
    file.write("User Name: Rajesh\n")
    file.write("Status: Active\n")
    file.write("Project: Jarvis Automation\n")

print("Memory file successfully ban gayi hai! 👍")




print("\n---Reading The Data Inside The File ---")
with open("jarvis_memory.txt", "r") as file:
    data = file.read()  
    print(data)


with open("jarvis_memory.txt", "a") as file:
	file.write("Last Login: Wednesday, 06\n")
	file.write("current task: learning python\n")

print("new data added succesfully\n")

print("Updated file data\n")

with open("jarvis_memory.txt", "r") as file:
	print(file.read())
	
