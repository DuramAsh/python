people = {
	"Akmaral Tazhiyeva": "12/30/2002",
	"Leo Messi": "06/24/1987",
	"Johnny Depp": "06/09/1963"
}


print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
for k, v in people.items():
	print(k)

inp = input(">>> Who's birthday do you want to look up?\n")
print(f">>> {inp}'s birthday is {people[inp]}.")