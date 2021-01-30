## Adding Data

If you do not see the vaccine you are concerned with in "vaccines.csv", add it in! Make sure to push the .csv back to this folder so that others can use it as well.

No data needs to be added to the covid19dh.csv as it automatically updates each time the model parameters are called to be fit.

samplefittingdata.npy contains data as [population,pars,final_state] for Kentucky, Texas, Arizona, Michigan and Colorado as dictionaries, respectively. Can be used for any testing if you want to avoid waiting for fitting. Similarly, countriesexamples.npy contains data of the same format for the United States, Canada, United Kingdom, Germany and Japan as dictionaries, respectively.
