import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp
from lmfit import minimize, Parameters, Parameter, report_fit
matplotlib.use("TKAGG")

""""
Step 1 : Import the data and create a data set that can be worked on (might need to create a data set for this)
Step 2 : Transfer function that determines what our data set will look like after a period of time
Step 3 : Figuring out how to minimise a variable, e.g. deaths for example by allocation of a limited 
         number of vaccines to different areas
Step 4 : Return a .csv file of the optimal vaccine allocation plan that will reduce deaths the most.
"""

#Import data
data = np.genfromtxt("data/michigan-history.csv", names=True, delimiter=",")[::-1]

#Modified SIR model
def SIR(t,x,pars):
    S = x[0]
    I = x[1]
    A = x[2]
    R = x[3]
    D = x[4]
    dSdt = -S*pars[0]*(A+pars[1]*I)
    dIdt = pars[2]*A - (pars[3]+pars[4])*I
    dAdt = pars[0]*S*A - (pars[2]+pars[5])*A
    dRdt = pars[3]*I + pars[5]*A
    dDdt = pars[4]*I
    return [dSdt,dIdt,dAdt,dRdt,dDdt]

def SIRD_T(t,x,pars):
    S = x[0]
    I = x[1]
    R = x[2]
    D = x[3]
    N = S+I+R+D
    try:
        beta = pars['beta'].value
        gamma_R = pars['gamma_R'].value
        gamma_D = pars['gamma_D'].value
        omega = pars['omega'].value
    except:
        beta, gamma_R, gamma_D, omega = pars
    beta *= np.exp(-omega*t)
    dSdt = -beta*S*I/N
    dIdt = -dSdt - (gamma_R+gamma_D)*I
    dRdt = gamma_R*I
    dDdt = gamma_D*I
    return [dSdt,dIdt,dRdt,dDdt]

def solver(model,t,x0,pars):
    return solve_ivp(model,t_span=(t[0],t[-1]),y0=x0,method="RK45",t_eval=t,args=(pars,))

Deaths = data["death"]
Recovered = data["recovered"]
Infected = data["positive"] - Recovered - Deaths
Asymptomatic = 0
Population = 6.732e6
Succeptible = Population - Infected - Recovered - Deaths - Asymptomatic

def mcmc(d,model,t,x0,pars,pars_step,chi_cur,nstep=5000):
    print("Starting Markov")
    npar = len(pars)
    n_success = 0 #so we can determine acceptance rate
    chain = np.zeros([nstep,npar])
    chivec = np.zeros(nstep)
    for i in range(nstep):
        print("\t" + "Step #" + str(i+1))
        par_step = np.asarray(pars)*pars_step#*np.random.randn(6) 
        pars_trial = pars.copy()
        pars_trial += par_step*0.5 #Our step size is too large -> arbitrarily adjust for each chain
        new_model = solver(model,t,x0,pars_trial).y[1]
        chi_trial = np.sum((d-new_model)**2/d)#np.sum((d-new_model)**2)
        accept_prob = np.exp(-0.5*(chi_trial-chi_cur)) #decide if we take the step
        if (np.random.rand(1)<accept_prob): #accept the step with appropriate probability + don't accept if tau<0. 
            pars = pars_trial
            chi_cur = chi_trial
            n_success += 1
            print("\t\t"+"Success! Pars=", pars, "Chi=", chi_cur)
        else:
            print("\t\t"+"Fail :(")
        chain[i,:] = pars
        chivec[i] = chi_cur
    return chain, chivec, (n_success/nstep)*100

def newton(d,model,t,x0,pars,pred,delx): 
    r = d-pred #residual array
    #We next look to calculate all the derivatives
    dA = np.empty(shape=(len(d),len(pars)))
    for i in range(len(pars)): #Calculating the derivatives for each parameter
        print("\t\t"+"Parameter " + str(i+1))
        pars1, pars2 = list(pars), list(pars)
        pars1[i] += delx[i]
        pars2[i] -= delx[i]
        fxplus = solver(model,t,x0,pars1).y[1]
        fxminus = solver(model,t,x0,pars2).y[1]
        dA[:,i] = (fxplus-fxminus)/(2*delx[i])
    #We now have our derivatives, however if we are not concerned with tau, we do not need that column of the matrix. Proceeding with Newton's
    cov = np.linalg.inv(dA.transpose() @dA) #to calculate the errors
    dm = cov @ (dA.transpose() @r)
    return pars+dm, cov, dA

def newton_chi(d,model,t,x0,pars,pred,dx,chimin):
    delchi = 1000
    covbef = 0 #Defining so that previous covariance can be outputted if delchi<0
    n = 1
    while delchi>chimin and n<10: #Condition that gives us the accuracy that we desire, yet also does not allow the loop to continue forever
        print("Chi " + str(n) + ":")
        delx = [i*dx for i in pars] #Calculating the new delx for each iteration
        solbef = solver(model,t,x0,pars).y[1]
        chibef = np.sum((d-solbef)**2/d)#np.sum((d-solbef)**2) #/err**2) #Calculating chi2 before change in pars
        newtonpars, cov = newton(d,model,t,x0,pars,solbef,delx)[:2] #Calling our previous function to calculate new pars
        solaft = solver(model,t,x0,newtonpars).y[1]
        chiaft = np.sum((d-solaft)**2/d)#/err**2) #Calulating chi2 after change in pars
        delchi = chibef-chiaft #chibef-chiaft should always be positive. However, if it's negative, we should return the previous pars.
        print("\t\t" + "chi" + str(n) + "=", chiaft, "\n")
        if delchi<0: #Returning previous pars if negative
            return pars, covbef, chibef, delchi, solbef
        pars = list(newtonpars)
        n += 1 #Just so that we do not loop forever
        covbef = cov.copy() #taking the previous covariance so that it can be outputted if delchi<0
    return pars, cov, chiaft, delchi, solaft

#Test solve
time = np.linspace(0,len(Infected),len(Infected))
t = np.linspace(0,len(Infected),10000)
if (False):#SIR model
    pars = [1e-7,0.16,0.2,0.15,0.04,0.8]
    x0 = [Succeptible[0], Infected[0], Infected[0]*1.5, Recovered[0], Deaths[0]]
if (True):#SIRD_T model
    pars = [0.1,0.15,0.04,0.1]
    x0 = [Succeptible[0], Infected[0], Recovered[0], Deaths[0]]

#sol = solver(SIRD_T,time,x0,pars)

#Calling Newton Solver
#newpars, parserrs, chisqafter, chichange, sol = newton_chi(Infected,SIRD_T,time,x0,pars,sol.y[1],0.0001,10)

"""#Calling MCMC Solver
mcmcsol = mcmc(Infected,SIRD_T,time,x0,pars,1,np.sum((Infected-sol.y[1])**2/Infected),100)
chain = mcmcsol[0]
avgparams = chain[-1]
solnew = solver(SIRD_T,time,x0,avgparams)"""

#Other best fit method
params = Parameters()
params.add('beta', value=pars[0], min=0, max=0.1)
params.add('gamma_R', value=pars[1], min=0, max=0.1)
params.add('gamma_D', value=pars[2], min=0, max=0.1)
params.add('omega', value=pars[3], min=0)

def residual(paras, t, x0, data, model):
    result = solver(model,t,x0,paras)
    # you only have data for one of your variables
    x = [result.y[1],result.y[-1],result.y[-2]]
    print("Running...")
    return (x[0]-data[0])**2 + (x[1]-data[1])**2 + (x[2]-data[2])**2

# fit model
result = minimize(residual, params, args=(time,x0,[Infected,Deaths,Recovered],SIRD_T), method='nelder')
data_fitted = solver(SIRD_T,t,x0,result.params)

fig = plt.figure()
plt.subplot(2,2,1)
plt.ylabel("Infected")
plt.plot(time,Infected)
plt.plot(t,data_fitted.y[1])

plt.subplot(2,2,2)
plt.ylabel("Deaths")
plt.plot(time,Deaths)
plt.plot(t,data_fitted.y[-1])

plt.subplot(2,2,3)
plt.ylabel("Succeptible")
plt.plot(time,Succeptible)
plt.plot(t,data_fitted.y[0])

plt.subplot(2,2,4)
plt.ylabel("Recovered")
plt.plot(time,Recovered)
plt.plot(t,data_fitted.y[-2])
plt.show()

print(result.params)
print(Succeptible[-1],Infected[-1],Recovered[-1],Deaths[-1],Population)
