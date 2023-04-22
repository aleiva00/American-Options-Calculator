# American-Options-Calculator
Defining a Python function to quickly price an american option with binomial trees given the option's main parameters. 


# Parameters used:

```
option_price = american_option_pricer(
    spot=55.0,
    strike=50.0,
    rate=0.05,
    vol=0.3,
    expiry=1.0,
    steps=100,
    option_type="call",)
    
```

# Description
The binomial option pricing model is a mathematical model used to calculate the theoretical price of an option, based on various factors such as the current stock price, strike price, time to expiration, volatility, and interest rate. The model uses a binomial tree to represent the possible price paths of the underlying asset, and calculates the option price by working backwards from the final nodes of the tree.

In a binomial tree, each node represents a possible price of the underlying asset at a given point in time, and the number of branches from each node represents the number of possible price movements (up or down) that can occur during each time step. The more branches there are, the more accurate the model can be in capturing the potential price movements of the underlying asset.

By increasing the number of steps or branches in the binomial tree, we are effectively increasing the granularity of the model, which allows for a more accurate representation of the possible price movements of the underlying asset. This in turn leads to a more accurate calculation of the option price.

However, increasing the number of steps or branches also increases the computational complexity of the model, and can require more time and resources to calculate. As such, there is often a trade-off between model accuracy and computational efficiency, and the optimal number of steps or branches may depend on the specific application and requirements of the model.

#Results using 100 branches

![100 steps](https://user-images.githubusercontent.com/82245658/233804036-45655e1f-b01c-40fe-b23c-c750e8ecb546.png)


# Results using 1000 branches
![1000 steps](https://user-images.githubusercontent.com/82245658/233804057-1c1f7139-4e38-42eb-ac05-5cade2cd359b.png)

