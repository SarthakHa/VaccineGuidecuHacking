## Model Fitting

The model fitting works using an SIRD model. This model is defined below:

<img src="https://render.githubusercontent.com/render/math?math=dS/dt = -\beta \frac{S(t)I(t)}{N}">
<img src="https://render.githubusercontent.com/render/math?math=dI/dt = \beta \frac{S(t)I(t)}{N} - (\gamma%2B\alpha)I(t)">
<img src="https://render.githubusercontent.com/render/math?math=dR/dt = \gamma I(t)">
<img src="https://render.githubusercontent.com/render/math?math=dD/dt = \alpha I(t)">

S: Succeptible Population, I: Infected Population, R: Recovered Population, D: Deceased Population and N: Total Population.

The library covsirphy is used to describe the different phases when the parameters are changing (using S-R trend analysis) and optimize the different parameter values within these phases. https://lisphilar.github.io/covid19-sir/covsirphy.html 

Sample plots have been shown to prove the accuracy of the fits. Infected data is not fit as accurately as other variables as the model does not take into account asymptomatic cases and other features. Furthermore, poor data collection also results in strange bumps and jumps in data that makes it tougher to model. Thankfully, as we are breaking down the data into small phases, this effect is not as devestating. 

The results of the model fitting are the unknown parameter values. These values can then be used in our optimization to find the best vaccine distribution.
