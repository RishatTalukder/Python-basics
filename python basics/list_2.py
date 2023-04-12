motorcycle = ['suzuki','hunk','kawasaki']
motorcycle.append("herley")
motorcycle.append("ITVAYA")

motorcycle.insert(2,'ducati')
motorcycle.insert(4,"honda")

del motorcycle[4]

popped = motorcycle.pop(3)
motorcycle.remove('hunk')

print(motorcycle)

print(popped)