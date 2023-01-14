#0 -> neutral
#1 -> cool/ light
#2 -> warm/ dark


results = []

def compute_hc() -> None:
    light_hc = ['chesnut', 'dark brown', 'red', 'strawberry', 'blonde', 'amber']
    dark_hc = ['black', 'ashy brown', 'grey', 'ashy blonde']

    while True:
        hc = input("")
        if hc in light_hc:
            results.append(1)
            return
        elif hc in dark_hc:
            results.append(2)
            return
        else:
            print("invalid color: please enter a new one")

print("Please choose from one of the following hair colors:")
print("chesnut | ashy brown | grey | blonde | chesnut")
print("dark brown | red | ashy blonde | amber | black")

compute_hc()

print("Do you wear glasses?")
print("yes | no")

    










