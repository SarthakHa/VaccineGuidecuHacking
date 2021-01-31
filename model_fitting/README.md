## Model Fitting

The model fitting works using an SIRD model. This model is defined below:

<img src="https://render.githubusercontent.com/render/math?math=dS/dt = -\beta \frac{S(t)I(t)}{N}">
<img src="https://render.githubusercontent.com/render/math?math=dI/dt = \beta \frac{S(t)I(t)}{N} - (\gamma%2B\alpha)I(t)">
<img src="https://render.githubusercontent.com/render/math?math=dR/dt = \gamma I(t)">
<img src="https://render.githubusercontent.com/render/math?math=dD/dt = \alpha I(t)">

S: Succeptible Population, I: Infected Population, R: Recovered Population, D: Deceased Population and N: Total Population.

The coefficients are parameters that will be fit using the library covsirphy in Python (https://lisphilar.github.io/covid19-sir/covsirphy.html). However, before we fit, we must recognise that our parameters are not gonna remain constant over time as quarantine measures changes, air traffic changes and so on. Therefore, we first split our data up into regions called “Phases”. Covsirphy is used to describe the different phases when the parameters are changing (using S-R trend analysis) and find the optimal parameter values within these phases. Note that the model assumes that people, once infected, can either recover or pass away according to their proportionality coefficients, &gamma; and &alpha;, respectively. For more information, check the website "Learn About the Model" section.

Sample plots have been shown to prove the accuracy of the fits. Infected data is not fit as accurately as other variables as the model does not take into account asymptomatic cases and other features. Furthermore, poor data collection also results in strange bumps and jumps in data that makes it tougher to model. Thankfully, as we are breaking down the data into small phases, this effect is not as devestating. 

The results of the model fitting are the unknown parameter values. These values can then be used in our optimization to find the best vaccine distribution.
