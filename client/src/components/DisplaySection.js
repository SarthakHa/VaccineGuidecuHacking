import React,{Fragment,useState,useEffect} from 'react'
import Chart from './Chart.js'
import Typography from '@material-ui/core/Typography';
import 'react-bootstrap-range-slider/dist/react-bootstrap-range-slider.css';
import RangeSlider from 'react-bootstrap-range-slider';
import './DisplaySection.css'




const DisplaySection =({data,countries})=>{

    const [numberOfSteps,setNumberOfSteps] = useState(1)
    const [dayToDisplay,setDayToDisplay] = useState(0)

    useEffect(() => {
        setNumberOfSteps(data.length)
        console.log("rerendered")
    }, [dayToDisplay])


    const onChange=(value)=>{
       
        setDayToDisplay(value)
        console.log(dayToDisplay)

    }

    

    return(
        <Fragment >
        <div className="slider-div">
      <Typography id="discrete-slider" gutterBottom>
        Day
      </Typography>
    
      <RangeSlider
        value={dayToDisplay}
        onChange={changeEvent => onChange(changeEvent.target.value)}
        min={0}
        step={1}
        style={{width:"50%"}}
        max={numberOfSteps}
        />
      </div>

        <div>
        {dayToDisplay>-1?( <Chart className="chart" record={data[dayToDisplay-1]} countries={countries}/>
        ):null}
        </div>
      </Fragment>

     

      
    
      
    )
}


export default DisplaySection