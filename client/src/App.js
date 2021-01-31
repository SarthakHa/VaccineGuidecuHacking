import React,{Fragment,useState,useEffect,createRef} from 'react'
import { Multiselect } from 'multiselect-react-dropdown';
import InputSection from './components/InputSection'
import WorldIcon from '@material-ui/icons/Public';
import LocationCityIcon from '@material-ui/icons/LocationCity';
import DisplaySection from './components/DisplaySection'

import Button from '@material-ui/core/Button'
import './App.css';

const App = ()=> {
  const [data,setData] = useState ([[1000,2000,3000,4000,5000],[3000,2000,1000,500,100],[5000,1000,2000,4000,5000]])
  const [contries,setContries]= useState( ["USA","UK","Canada", "Russia","South Africa"])
  const [readyToDisplay, setReadyToDisplay] = useState(false);
  const [simulateClick,setSimulateClick] = useState(false)
  const [userID,setUserID] = useState("")

  const scrollSelectionDiv =createRef();
  const scrollHomeDiv =createRef();
  const scrollModalDiv =createRef();

  const scrollSelectionDivHandler = () => {
    scrollSelectionDiv.current.scrollIntoView({ behavior: "smooth" });
  };
  const scrollHomeDivHandler = () => {
    scrollHomeDiv.current.scrollIntoView({ behavior: "smooth" });
  };
  const scrollModalDivHandler = () => {
    scrollModalDiv.current.scrollIntoView({ behavior: "smooth" });
  };

    const handleSimulateClick=()=>{
    setSimulateClick(true)
    console.log(simulateClick)
  }

  useEffect(() => {
    
    setUserID(Date.now())
  },[]);


  return (
    <div className="background">
       <div className="main-grid-container">
         <main className="main">
         <div className="guide-vaccine"> <h1>Guide</h1><h1>Vaccine</h1></div>
         <div><h2>Find the optimal vaccine distribution across your own chosen places</h2></div>
         <div className="choose-btn-div">  <Button onClick={scrollSelectionDivHandler}> <h3>Choose your Places!</h3></Button> </div>
         </main>
          <div className="navbar">
            <h3 onClick={scrollSelectionDivHandler}>Selection</h3>
            <h3 onClick={scrollModalDivHandler}>The Model</h3>
            <h3>The Simulation</h3>
      
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
            <InputSection userID={userID} simulateClick={handleSimulateClick}/>
          </div>
        </div>
        <div className="warning-div">
          <h1 className="warning-word">Warning</h1>
          <h2 className="warning-text"> Depending on the data for the places chosen, the initial parameter fitting can take up to <strong>1 minute per place</strong>. Choosing fewer places is a better method to get quicker results... </h2>
        </div>
          <div className="cloud-footer-div-second">
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/>
            <img className="cloud-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/vector@1x.svg"/> 
          </div>
      </div>

      {simulateClick? ( <div className="chart-grid-container">
      {readyToDisplay? ( <div className="display-section-div">
          <DisplaySection data={data} countries={contries}/>
          </div>): <div></div>}
      </div> ): null}
      
      <div className="third-grid-container" ref={scrollModalDiv}>
          <div className="text">
            <h1>Learn About the Model</h1>
            
            <h3> The model we have used to fit and simulate the data is called an SIRD model. SIRD stands for Susceptible, Infected, Recovered and Deceased and is a standard epidemic model (note that N is the total population and is assumed to be unchanging). This model has been chosen due to its relatively quick optimization time when running and due to the generally poorly compiled COVID-19 data sets that do not contain the statistics necessary
            for more complicated models. Mathematically, the SIRD model is represented by a system of ODEs: <span className="ellipsis">...</span> 
            <span className="moreText">
            The coefficients (β, γ, and α) are parameters that will be fit using the library covsirphy in Python. However, before we fit, we must recognise that our parameters are not gonna remain constant over time as quarantine measures changes, air traffic changes and so on. Therefore, we first split our data up into regions called “Phases”. 

            A phase refers to sequential dates within which the parameters of our SIRD model are fixed. We can find these phases using S-R trend analysis with covsirphy. This technique comes from the mathematics behind SIR-derived models whereby the logarithm of S and R are directly proportional. Therefore, if we were to plot the logarithm of S on the y-axis and R on the x-axis, we should get a straight line. The slope of this line depends on the parameter values, therefore if we detect where the slope of this line changes, we can determine when in time our parameter values are changing. These breaking points are where we define our different phases. 

            Now, with our phases in hand, we can optimize our model and get the best fit parameters over each different phase. For our vaccination simulation we only care about the most recent phase (as this is the phase after which we begin simulating) and therefore, we can save some time by not optimizing our parameters during the other phases. 

            It should be noted that our model makes a few basic assumptions:
            The parameter values do not change as we simulate the future (which is improbable), i.e. lockdown measures and etc. do not change during the time period.
            Every case that exists is in the data set (i.e. no asymptomatic people who have not been tested).
            We ignore time taken to distribute and assume all people get the vaccine immediately.
            When simulating, we assume vaccine effectiveness does not depend on age and that there are no possible negative repercussions.
            </span> <a className="more" href="#">read more</a></h3>
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

      


    

  </div>
  )
}

export default App;