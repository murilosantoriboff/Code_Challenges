name = input()
tam = len(name)
letters = list(l for l in name)

rep_let = list()
number_no_rep = 0

for let in letters:
    if name.count(let) > 1:
        if let in rep_let:
            pass
        else:
            number_no_rep -= 1
            rep_let.append(let)
    elif name.count(let) <= 1:
        number_no_rep += 1
        
if number_no_rep % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')