import React,{Fragment,useState,useEffect,createRef} from 'react'
import './App.css';

const App = ()=> {

  return (
    <div className="background">
       <div className="grid-container">
         <main className="main">
         Guide Vaccine
         </main>
  
     <div className="intro">
       Find the optimal vaccine distribution across your own chosen places
     </div>
     <div className="choose-btn">
       <button>Choose your Places!</button>
     </div>
    <div className="vabar">
      <h3>Home</h3>
      <h3>Selection</h3>
      <h3>The Model</h3>
      <h3>The Simulation</h3>
      
    </div>

    </div>
    </div>
   
  )
}

export default App;
