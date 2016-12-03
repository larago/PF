names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print names

##PF

secret_names = map(hash ,names)

print secret_names