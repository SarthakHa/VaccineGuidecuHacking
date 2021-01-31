import React,{Fragment,useState,useEffect,createRef} from 'react'
import InputSection from './components/InputSection'
import DisplaySection from './components/DisplaySection'
import PacmanLoader from "react-spinners/PacmanLoader";
import BarChart from "./components/BarChart"

import Button from '@material-ui/core/Button'
import './App.css';

const App = ()=> {
  const [data,setData] = useState ([])
  const [contries,setContries]= useState( [])

  const [policyNames, setPolicyNames] = useState([])
  const [policyComparison, setPolicyComparison] = useState([])
  const [readyToDisplay, setReadyToDisplay] = useState(false);
  const [simulateClick,setSimulateClick] = useState(false)
  const [userID,setUserID] = useState("")
  const [TBLink, setTBLink] = useState("")


  const scrollSelectionDiv =createRef();
  const scrollHomeDiv =createRef();
  const scrollModalDiv =createRef();
  const scrollSimulateDiv =createRef();
  const scrollLoadingDiv =createRef();

  const scrollSelectionDivHandler = () => {
    scrollSelectionDiv.current.scrollIntoView({ behavior: "smooth" });
  };
  const scrollHomeDivHandler = () => {
    scrollHomeDiv.current.scrollIntoView({ behavior: "smooth" });
  };
  const scrollModalDivHandler = () => {
    scrollModalDiv.current.scrollIntoView({ behavior: "smooth" });
  };

  const scrollSimulateDivHandler = () => {
    scrollSimulateDiv.current.scrollIntoView({ behavior: "smooth" });
  };
  
  const scrollLoadingDivHandler = () => {
    scrollLoadingDiv.current.scrollIntoView({ behavior: "smooth" });
  };

  const handleSimulateClick=(bool)=>{
    setSimulateClick(bool)

  }

  const setDataHandler =(actions)=>{
    setData(actions)
  }

  const setContriesHandler = (contries) =>{
    setContries(contries);
  }

  const setPolicyNamesHandler = (names) =>{
    setPolicyNames(names)
  }

  const setComparisonsHandler = (comparisons) =>{
    setPolicyComparison(comparisons)
  }

  const setReadyToDisplayHandler = (bool)=>{
    setReadyToDisplay(bool)
  }

  const setTBLinkHandler =(link) =>{
    setTBLink(link)
  }

  useEffect(() => {
    
    setUserID(Date.now())
  },[]);


  return (
    <div className="background">
       <div className="main-grid-container" ref={scrollHomeDiv}>
         <main className="main">
         <div className="guide-vaccine"> <h1>Guide</h1><h1>Vaccine</h1></div>
         <div><h2>Find the optimal vaccine distribution across your own chosen places</h2></div>
         <div className="choose-btn-div">  <Button onClick={scrollSelectionDivHandler}> <h3>Choose your Places!</h3></Button> </div>
         </main>
          <div className="navbar">
            <h3 onClick={scrollHomeDivHandler}>Home</h3>
            <h3 onClick={scrollSelectionDivHandler}>Selection</h3>
            <h3 onClick={scrollModalDivHandler}>The Model</h3>
            <h3 onClick={scrollSimulateDivHandler}>The Simulation</h3>
      
          </div>

          <div className="image-div">
            <img className="main-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/ellipse-1@2x.svg"/>
          </div>
        
          <div className="cloud-footer-div">
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>  
          </div>
      </div>
      
      <div className="second-grid-container" ref={scrollSelectionDiv}>
        <div className="second-image-div"> <img src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/undraw-data-input-fxv2-2@1x.png"></img>  </div>
        <div className="instruction">
          <h1 className="instruction-text">Instruction</h1>
          <h3>Select either countries or states/provinces. Make your selection of places and then enter: the number of vaccines allocated per day, the number of days over which you would like the simulation to run, and the specific vaccine you want to use (this changes the vaccine’s effectiveness according to the percentage stated). Let’s save some lives!</h3>
          <div className="input-section">
            <InputSection userID={userID} scrollLoadingDivHandler={scrollLoadingDivHandler} setDataHandler={setDataHandler} setContriesHandler={setContriesHandler} setTBLinkHandler={setTBLinkHandler} setReadyToDisplayHandler={setReadyToDisplayHandler} setPolicyNamesHandler={setPolicyNamesHandler}  setComparisonsHandler={setComparisonsHandler} simulateClick={handleSimulateClick} scrollLoadingDivHandler ={scrollLoadingDivHandler} />
          </div>
        </div>
        <div className="warning-div">
          <h1 className="warning-word">Warning</h1>
          <h2 className="warning-text"> Depending on the data for the places chosen, the initial parameter fitting can take up to <strong>1 minute per place</strong>. Choosing fewer places is a better method to get quicker results... </h2>
        </div>
          <div className="cloud-footer-div-second" ref={scrollLoadingDiv}>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/> 
          </div>
      </div>

      {simulateClick? ( <div className="chart-grid-container">
      {readyToDisplay? ( <div className="display-section-div">
          <DisplaySection data={data} countries={contries}/>
          <div className="bar-chart-div"> <BarChart  policyComparison={policyComparison} policyNames={policyNames}/></div>
          </div>): 
            <div className="loader">
              <h1>Simulating...</h1>
               Watch the model train! {TBLink}
              <h2>This could take hours to simulate.</h2>
             <PacmanLoader  size={150} color="#6c63ff" loading={!readyToDisplay} />
              
            </div>}

            
      </div> ): null}
      
          

      <div className="third-grid-container" ref={scrollModalDiv}>
          
          <div className="cloud-footer-div-below">
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/> 
          </div>

          <div className="text">
            <h1>Learn About the Model</h1>
            
            <h3> The model we have used to fit and simulate the data is called an SIRD model. SIRD stands for Susceptible, Infected, Recovered and Deceased and is a standard epidemic model (note that N is the total population and is assumed to be unchanging). This model has been chosen due to its relatively quick optimization time when running and due to the generally poorly compiled COVID-19 data sets that do not contain the statistics necessary for more complicated models. Mathematically, the SIRD model is represented by a system of ordinary differential equations (ODE's):</h3>

            <div className="math-image-div">
              <img src="https://anima-uploads.s3.amazonaws.com/projects/6015a5662fef2ded030dfd20/releases/6016981261c5c6a19e304f05/img/group-1@2x.png" width="auto" height="200vh"></img>
           </div>

            <h3>  
            <p>The coefficients (β, γ, and α) are parameters that will be fit using the library covsirphy in Python. However, before we fit, we must recognise that our parameters are not gonna remain constant over time as quarantine measures changes, air traffic changes and so on. Therefore, we first split our data up into regions called “Phases”. </p>

            <p>A phase refers to sequential dates within which the parameters of our SIRD model are fixed. We can find these phases using S-R trend analysis with covsirphy. This technique comes from the mathematics behind SIR-derived models whereby the logarithm of S and R are directly proportional. Therefore, if we were to plot the logarithm of S on the y-axis and R on the x-axis, we should get a straight line. The slope of this line depends on the parameter values, therefore if we detect where the slope of this line changes, we can determine when in time our parameter values are changing. These breaking points are where we define our different phases. </p>

            <p>Now, with our phases in hand, we can optimize our model and get the best fit parameters over each different phase. For our vaccination simulation we only care about the most recent phase (as this is the phase after which we begin simulating) and therefore, we can save some time by not optimizing our parameters during the other phases.</p>

            <p>It should be noted that our model makes a few basic assumptions: </p>
              <ol>
                <li>The parameter values do not change as we simulate the future (which is improbable), i.e. lockdown measures and etc. do not change during the time period.</li>
                <li>Every case that exists is in the data set (i.e. no asymptomatic people who have not been tested).</li>
                <li>We ignore time taken to distribute and assume all people get the vaccine immediately.</li>
                <li>When simulating, we assume vaccine effectiveness does not depend on age and that there are no possible negative repercussions.</li>
              </ol>
           
            </h3>
          </div>
          
           <div className="teacher-image-div">
              <img src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015b1d432dc2026365d46b6/img/professor@1x.png"></img>
           </div>

           <div className="cloud-footer-div-third">
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/> 
          </div>

      </div>

      <div className="fourth-grid-container" ref={scrollSimulateDiv}>
            <div className="simulationtext">
              <h1>Learn About the Simulation</h1>
              
              <h3> A reinforcement learning AI agent then trains on the simulated environment we made, where the agent can choose the vaccine distribution to the chosen places per day. The agent now to optimally reduce deaths needs to balance the growth of the virus in places, the mortality rate of COVID as well as how many people are susceptible to COVID when deciding how to provide the vaccines. The agent is trained on the data using the PPO algorithm (implementation taken from stable_baselines) for a user defined iterations with the reward being how many deaths the agent can reduce. With a small number of training iterations, we found that the learned model generally performs worse than other simple strategies like choosing based off the population ratio. However with enough training time, the agent is able to learn will enough to outperform those strategies as it can learn about the dynamics of COVID spread and use that to then reduce deaths.</h3>
            </div>

            <div className="vr-image-div">
              <img src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015b1d432dc2026365d46b6/img/vr@1x.svg" height="auto" width="500vw"></img>
           </div>
      </div>
      
  </div>
  )
}

export default App;