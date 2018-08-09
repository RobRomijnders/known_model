# Question for Reddit

[D] What if I knew the physical model, how to use machine learning?

Say a physicist comes up to us and ask to infer the parameters of his model. He actually knows the model and needs uncertainty bounds on his parameters. How would we do that?

More explanation:
For many of our problems, we get to choose our model. In classifying cats from dogs, we get to choose between neural nets and SVMs. In finding clusters, we get to choose between K-means or PCA. Now what if a domain expert has an actual model, but needs to find the parameters.

Example:
Let's say the known model is 

`y(x) = exp(-a*x) + b*x + sin(c*x) + d` 



  * where sample points  `x_i ~ Uniform(0, 1)` and 
  * observations `y_{i} ~ y(x_i) + Normal(0, variance)`

Here are some images:
![examples](https://github.com/RobRomijnders/known_model/blob/master/known_model/im/example.png?raw=true)

and [here](https://github.com/RobRomijnders/known_model) is the code for generating these images


TL;DR How to find confidence bounds on `a`, `b`, `c`, and `d`?