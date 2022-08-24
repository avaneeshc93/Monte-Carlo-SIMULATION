import random as r
import matplotlib.pyplot as plt

doors = [1,2,3]

ginti = 0
loopy = 5000
x = [0]
y = [0]
z = [0]
for i in range(loopy):
    car = r.choice(doors)
    guess = r.choice(doors)
    show = r.choice([x for x in doors if x != car and x != guess])
    switch = r.choice([x for x in doors if x != show and x!= guess])
    print(car, guess, show,switch)
    if switch == car:
        ginti+=1
    if i != 0:
        prob = ginti/(i+1)
        loss = 1 - prob 
        x = x + [i]
        y = y + [prob] 
        z = z + [loss]
print(x,y,z)
plt.plot(x,y,'k-',z, 'r-', linewidth = 1)
plt.xlabel("number of iterations")
plt.legend(['winning','losing'])
plt.ylabel("probablity")
plt.title("Monte-Carlo simulation of Monty Hall problem")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.ylim([0,1])
plt.show()
