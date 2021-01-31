import React from 'react'
import {Pie} from 'react-chartjs-2'



const Chart =({record,countries}) =>{
    
    const onClickEvent = (event,element) =>{
       
       //console.log("index",index)
    }
    return (
    <div>
       <Pie
        data={{
            labels:countries,
            datasets: [{
                label: '# of Votes',
                data: record,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ]
            }]
            
        }}
        
        height={400}
        width={400}
        options={{
            maintainAspectRatio:false
        }}
       >

       </Pie>
                 
    </div>
    )
}

export default Chart