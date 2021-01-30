import React,{Fragment,useState,useEffect,createRef} from 'react'
import './App.css';

const App = ()=> {

  return (
    <div className="background">
       <div className="grid-container">
         <main className="main">
         <div className="guide-vaccine"> <h1>Guide</h1><h1>Vaccine</h1></div>
         <div><h2>Find the optimal vaccine distribution across your own chosen places</h2></div>
         <div className="choose-btn-div">  <button> <h3>Choose your Places!</h3></button> </div>
        
         </main>
  
  
    <div className="navbar">
      <h3>Home</h3>
      <h3>Selection</h3>
      <h3>The Model</h3>
      <h3>The Simulation</h3>
      
    </div>

    <div className="image-div">
    <img className="main-image" src="https://cdn.animaapp.com/projects/6015a5662fef2ded030dfd20/releases/6015af349a9b7cfb373827ee/img/ellipse-1@2x.svg"/>
    </div>
  
    </div>
    </div>
   
  )
}

export default App;
