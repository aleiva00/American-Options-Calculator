# Packages

import numpy as np


# Create the function

def american_option_pricer(spot, strike, rate, vol, expiry, steps, option_type):
    # Calculate the time interval and the up and down factors
    dt = expiry / steps
    u = np.exp(vol * np.sqrt(dt))
    d = 1 / u

    # Calculate the risk-neutral probability
    p = (np.exp(rate * dt) - d) / (u - d)

    # Create the binomial price tree
    price_tree = np.zeros((steps + 1, steps + 1))
    for i in range(steps + 1):
        price_tree[i, -1] = spot * (u ** (steps - i)) * (d**i)

    # Calculate the option value at each node
    option_tree = np.zeros_like(price_tree)
    if option_type.lower() == "call":
        option_tree[:, -1] = np.maximum(price_tree[:, -1] - strike, 0)
    elif option_type.lower() == "put":
        option_tree[:, -1] = np.maximum(strike - price_tree[:, -1], 0)
    else:
        raise ValueError("Option type must be either 'call' or 'put'.")

    # Traverse the tree backward to find the option price today
    for t in range(steps - 1, -1, -1):
        for i in range(t + 1):
            exercise = 0
            if option_type.lower() == "call":
                exercise = price_tree[i, t] - strike
            elif option_type.lower() == "put":
                exercise = strike - price_tree[i, t]

            hold = np.exp(-rate * dt) * (
                p * option_tree[i, t + 1] + (1 - p) * option_tree[i + 1, t + 1]
            )
            option_tree[i, t] = np.maximum(exercise, hold)

    return option_tree[0, 0]

# Example:

option_price = american_option_pricer(
    spot=55.0,
    strike=50.0,
    rate=0.05,
    vol=0.3,
    expiry=1.0,
    steps=100,
    option_type="call",
)    


# Playing w/ parameters ----

#Steps in binomial tree
steps_list = [i for i in range(1,101)]
prices_steps=[]

for i in steps_list:
    option_price = american_option_pricer(
        spot=55.0,
        strike=50.0,
        rate=0.05,
        vol=0.3,
        expiry=1.0,
        steps=i,
        option_type="call",
    )       
    
    prices_steps.append(option_price)

# Viz results

import matplotlib.pyplot as plt

import statistics as stats

mean= stats.mean(prices_steps)

means=[]
for i in range(100):
    i=mean
    means.append(i)

plt.style.use('seaborn')
# Plot the scatter plot

fig = plt.figure()
plt.plot(steps_list, prices_steps)
plt.plot(steps_list, means, linestyle="--", color="r", alpha=0.7)
# Add labels to the x and y axis
plt.xlabel("Amount of steps in tree")
plt.ylabel("Call Option Price")
# Show the plot
plt.show()

#SAVE FIGURE AS image--------------------------------------------

fig.savefig('100 steps.png', format="png", bbox_inches='tight')

#---------------------------------------------------------------







