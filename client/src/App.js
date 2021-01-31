import React,{Fragment,useState,useEffect,createRef} from 'react'
import { Multiselect } from 'multiselect-react-dropdown';
import InputSection from './components/InputSection'
import WorldIcon from '@material-ui/icons/Public';
import LocationCityIcon from '@material-ui/icons/LocationCity';
import DisplaySection from './components/DisplaySection'

import Button from '@material-ui/core/Button'
import './App.css';

const App = ()=> {

  const data = [[1000,2000,3000,4000,5000],[3000,2000,1000,500,100],[5000,1000,2000,4000,5000]]
  const contries= ["USA","UK","Canada", "Russia","South Africa"]

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


  return (
    <div className="background">
       <div className="main-grid-container">
         <main className="main">
         <div className="guide-vaccine"> <h1>Guide</h1><h1>Vaccine</h1></div>
         <div><h2>Find the optimal vaccine distribution across your own chosen places</h2></div>
         <div className="choose-btn-div">  <button onClick={scrollSelectionDivHandler}> <h3>Choose your Places!</h3></button> </div>
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
            <InputSection/>
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

      <div className="chart-grid-container">
        
        <div className="display-section-div">
          <DisplaySection data={data} countries={contries}/>
          </div>
      

      </div>

      <div className="third-grid-container" ref={scrollModalDiv}>
          <div className="text">
            <h1>Learn About the Modal</h1>
            
            <h3> The model we have used to fit and simulate the data is called an SIRD model. SIRD stands for Susceptible, Infected, Recovered and Deceased and is a standard epidemic model (note that N is the total population and is assumed to be unchanging). This model has been chosen due to its relatively quick optimization time when running and due to the generally poorly compiled COVID-19 data sets that do not contain the statistics necessary
            for more complicated models. Mathematically, the SIRD model is represented by a system of ODEs: (Read More...)</h3>
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
