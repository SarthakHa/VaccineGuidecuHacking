# Guide Vaccine

While COVID-19 cases continue to rise all over the globe, many of us have grown tired of staying inside and not seeing our friends. Luckily, with recent medical advancements governments are starting to distribute vaccines that will reduce the spread of the virus. However, for large countries, such as Canada and the United States, how best do these governments allocate the limited number of vaccines within their states in order to reduce deaths? Guide Vaccine is a website that finds the ***optimal vaccine distribution across a list of user selected places in order to minimise deaths using reinforcement learning***!

## The Problem
Large countries face the humongous task of distributing a limited number of vaccines across their population. As such, it is important to make sure that those vaccines are being given to the areas that need it the most, and will provide the largest impact. [Research done](https://pubmed.ncbi.nlm.nih.gov/33356933/) in partnership with the [Bill and Melinda Gates Foundation](https://www.mobs-lab.org/uploads/6/7/8/7/6787877/global_vax.pdf) has shown that our current distribution processes **have not been equitable** across countries that need it the most, rather it has been dominated by rich countries who have managed to outbid others. Even in rich countries, the administration and distribution of vaccines has been prioritised in wealthier regions compared to poorer ones. 

Defining what an equitable distribution of vaccines is rather hard, but we chose to define it as the distribution that would lead to the fewest deaths. Our motivation for this project was if given a list of places and a limited number of vaccines, could we use AI to predict what distribution of vaccines per day would lead to the fewest deaths? In short, we can! And that is how ***Guide Vaccine*** was born.

## How it Works

The user chooses their countries (or states/provinces for a specific country), the number of vaccines they would like to allocate per day, the number of days across which the distribution will be generated and the type of vaccine (which effects the vaccine's effectiveness e.g. Pfizzer and Moderna are ~95% effective, etc.). We then use a Python library called Covsirphy that automatically imports the latest COVID-19 data in order to find the parameters for our SIRD Model. 

SIRD stands for Susceptible, Infected, Recovered and Deceased and is a standard epidemic model to predict the spread of viruses. The model is described by a system of differential equations (shown below) and a set of parameters. 

<img src="https://render.githubusercontent.com/render/math?math=dS/dt = -\beta \frac{S(t)I(t)}{N}">
<img src="https://render.githubusercontent.com/render/math?math=dI/dt = \beta \frac{S(t)I(t)}{N} - (\gamma%2B\alpha)I(t)">
<img src="https://render.githubusercontent.com/render/math?math=dR/dt = \gamma I(t)">
<img src="https://render.githubusercontent.com/render/math?math=dD/dt = \alpha I(t)">

We use Covsirphy's fitting function to fit the data and find the parameters using regression statistics. However, before we fit, we must recognise that our parameters are not gonna remain constant over time as quarantine measures changes, air traffic changes and so on. Therefore, we first split our data up into regions called “Phases”. Covsirphy is used to describe the different phases when the parameters are changing (using S-R trend analysis) and find the optimal parameter values within these phases. More detail can be found on our website! 

After that we wrap up each of the learned models into a larger environment that is akin to a markov decision process (MDP) where on each stage the action is to choose a distribution for the vaccines being given that day. We do this by making a custom OpenAI gym environment using the parameters we calculated before to model the transition function for the MDP.This is now a reinforcement learning problem which we train our agent on using the Proximal Policy Optimization. Our agents policy is given by a neural network of 2 fully connected layers of 5 units followed by a softmax function for the output. 

Results are given to the user as:

- A **pie chart** displaying the distribution of vaccines to each country over time. 
- A **bar plot** comparing the results of different protocols to that with no vaccine.

The user can also learn more about the simulation and the model used by scrolling down the page to the sections "Learn About the Model" and "Learn about the Simulation". It is important to note that the model assumes that people, once infected, can only recover or pass away according to their proportionality coefficients, &gamma; and &alpha;, respectively. Furthermore, the model ignores demographic differences, air traffic, transportation time etc. However, our model provides the building blocks for future models to improve as we acquire more data and learn more about COVID-19. As well all take part in this medical journey, it is important to consider the fact that data science provides a realistic path towards a quicker and less costly, victory.

## Web App Creation
To create the webapp, we coded up the front-end using figma for design and react for the animations. We wrote a lot of CSS code to make smooth animations and a clean layout.We used Chart.js for the plotting of the pie chart and the bar chart to make it look quite interactive. We coded the back-end framework in python and used flask for the front-end and back-end integration. The webapp was then hosted on a Heryoku server. 

To handle the training of the data, we setup a multi-threaded server on a google cloud machine which handled training requests for the AI agent and also sent the trained policy and its evaluation back to the Heryoku server to display it on the front-end.  

## Real World Impact
Guide Vaccine aims to provide real world advice to government officials about how best to allocate their limited vaccines. Although the model used is limited as of now, given longer training time and more complicated models, the results would be more accurate and could provide real world benefit in this global time of need. Our solution is very modular which means that these assumptions only impact the environment we make for the AI agent and that the training will essentially remain the same. This makes it very easy for us to update our model in the future as more data becomes available, making our product adaptable and versatile.

## Limitations
The approach used is not the best solution yet, since our proposed distribution only works as well as the model for the environment we made, which makes many assumptions about the data produced by the governments as well as how the vaccine will reduce death rates. We made a few assumptions in our approach, namely that there are no asymptomatic cases and that the vaccine is instantly and randomly distributed across demographics, not prioritised to certain patients. These assumptions can be relaxed once more data is found that predicts the spread of COVID-19 better, as well as the effects of prioritised vaccinations on certain demographics.

## Tips for training model
In case someone wants to replicate our work and train their own models in a more granular way using our code, here are some tips we identified along the way:

1. Train for around atleast 200k - 300k iterations to get good results that surpass naive stratergies like distributing based off population 
2. Need to have softmax as the output layer for the policy function, otherwise training dies as the output is a distribution

## Future Work

- Display more results from the fitting so that users are more likely to trust our results.
- Allow the user to download a .csv file that gives the distribution of vaccines for each country per day.
- Improve the efficiency of training. 
- Fix general UI bugs.

## Try it Out!
Check the [Guide Vaccine](https://vaccineguide.herokuapp.com/) website out!

## Installing dependencies

The basic prerequisites for running the repo are:
●	node v14 (LTS) and npm v6+
●	pipenv v2018
●	heroku CLI v7

To get everything running for the first time, you’ll need to make sure that the command line software above is properly installed on your machine. 

First, make sure that you are using Node 14.15.0. If you don’t have Node installed, you can install it from the NodeJS website. You can check your version by running: 

node -v
> 14.15.0

This should also install npm for you automatically. You can check by running:

npm -v
> 6.xx.x

Now we also need to install pipenv. Pipenv is a package manager for python packages. It’s similar to npm but for python. If you’re not using a Mac, follow the system-specific instructions for installing pipenv - this section is just added as a reference. 

The easiest way to install pipenv on Mac is to use Brew. You can install brew by following the instructions on the brew website. This is the version of brew that I’m running:

`brew -v`
> Homebrew 2.1.2
> Homebrew/homebrew-core (git revision 1b95; last commit 2019-05-15)

Now use brew to install pipenv:

`brew install pipenv`

After installing, this is the version of pipenv that I’m running on my machine:

pipenv --version
> pipenv, version 2018.11.26

You don’t necessarily have to have the same exact version for it to work properly, but I’m just listing the version I have here for completeness sake (and if something doesn’t work for you, you can try switching to the version listed here). 

Great! You should now have pipenv, node, and npm installed on your machine. Now we will use these binaries to install the dependencies to run the project. Navigate to the root directory of the VaccineGuidecuHacking repo:

`cd VaccineGuidecuHacking`

Use pipenv to install the server dependencies:

`pipenv install`

Now that we’ve installed the server dependencies, we also need to install the client side dependencies:

```
npm install
npm run build
```

You might get a number of warnings due to slightly outdated packages, but it should compile correctly in the end. Now that the dependencies are installed, we can run both servers to start our app. The first server is the flask server that handles requests. The other server is a local webpack server that makes it easy to develop within React. In the root directory, type:

npm run start

If everything works properly, your browser should automatically open and be navigated to http://localhost:3000/. If not, let us know, and we can help! You should see the basic project homepage:

 

Optional: If you are running into issues running the client and server in the same tab, you can alternatively try running the servers separately. In two separate terminal windows, you can run:

```
npm run start-client
npm run start-server
```

These are alias commands and you can see the commands that they are actually running in package.json. If you are having a specific issue, it might be helpful to run the commands in separate windows to see if there is a specific error. 

The next step is to push this website to the internet. Heroku is an awesome service with a free tier that allows you to easily push projects online. 

If you’ve never used Heroku before, visit their website and create an account. You’ll use your account credentials to push the site online. Then, install the Heroku Cli: 

`brew tap heroku/brew && brew install heroku`
`heroku login`

Now that the cli is installed, we’ll create a Heroku app and push the site online. The Heroku CLI should provide a URL that you can visit to view your site online. In my case, the URL is https://protected-beach-47576.herokuapp.com/. 

`heroku create`

Add the appropriate buildpacks (make sure to add python first, then nodejs, as follows):

`heroku buildpacks:add heroku/python`
`heroku buildpacks:add heroku/nodejs`

Now push the site to Heroku:

`git push heroku main`

Awesome, you have successfully set up the project and pushed it live to the internet!

Be sure to deploy early and often. Errors often will arise in the deployment process, but if you deploy every time you push to main, that will make your life much easier!
