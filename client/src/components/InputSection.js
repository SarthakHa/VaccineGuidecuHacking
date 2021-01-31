import React,{Fragment, useState,useEffect} from 'react'
import Button from '@material-ui/core/Button'
import WorldIcon from '@material-ui/icons/Public';
import LocationCityIcon from '@material-ui/icons/LocationCity';
import { Multiselect } from 'multiselect-react-dropdown';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';

import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import InputLabel from '@material-ui/core/InputLabel';

import "./InputSection.css"

const useStyles = makeStyles((theme) => ({
    formControl: {
      margin: theme.spacing(1),
      minWidth: 120,
    },
    selectEmpty: {
      marginTop: theme.spacing(2),
    },root: {
        '& .MuiTextField-root': {
          margin: theme.spacing(1),
          width: '25ch',
        }},
        button: {
            margin: theme.spacing(1),
          },
        
    
  }));


const InputSection= ()=>{
    const classes = useStyles();
    const [selectCountries,setSelectContries]= useState(false);
    const [selectStates,setSelectStates]= useState(false);
    const [states, setStates ] = useState(new Array())
    const [countries,setCountries] = useState(new Array())
    const [currentCountry,setCurentCountry] = useState("")
    const [numberOfSteps,setNumberOfSteps] = useState(0)
    const [numberOfVaccinePerDay, setNumberOfVaccinePerDay] = useState(0)
    const [vaccineSelected,setVaccineSelected] = useState(0)
    
    const vaccinesInfo=[] 
    const JapanStates =[]
    const CanadaStates = []
    const RussiaStates =[]
    const SouthAlfricaStates = [] 
    const UnitedStatesStates= []
   
    const listOfCountriesOptions =[]
    
    

    

    const toggleCountries =(e)=>{
    
    }

    const toggleStates =(e)=>{
    
    }

    const convertArrayToJsonObj =()=>{

    }

    const onCountriesSelect =()=>{
    }

    
    const onCountriesRemove =()=>{

     }


     const onStatesSelect =()=>{
    
     }


    const onStatesRemove =()=>{
    }

    const onSelectCountry =()=>{
    }

    const onSubmit=async()=>{
    }

    return (
        <Fragment>

        <div className="btn-div">
            <Button style={{marginRight:"5rem",width:"40%"}}  variant ="contained"  startIcon={<WorldIcon/>} onClick={toggleCountries}>
                <h1>Countries</h1>
            </Button>
             <Button style={{width:"40%"}} variant ="contained" startIcon={<LocationCityIcon/>} onClick={toggleStates}>
                <h1>States/Provinces</h1> 
            </Button>
        </div>

        <form className={classes.root} noValidate autoComplete="off" style={{ marginTop:"5%"}}>

        <div>
        <TextField
            required
          id="standard-number"
          label="Number of days (from 1-180)"
          type="number"
          onChange={e=>setNumberOfSteps(e.target.value)}
          InputLabelProps={{
            shrink: true,
          }}
        /> 
        <TextField
            required
          id="standard-number"
          label="Number of vaccines per day (0<2millions)"
          type="number"
          onChange={e=>setNumberOfVaccinePerDay(e.target.value)}
          InputLabelProps={{
            shrink: true,
          }}
        /> 
        <br/>
        <FormControl className={classes.formControl}>
            <InputLabel id="demo-simple-select-label">Vaccine</InputLabel>
            <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={vaccineSelected}
            onChange={e=>{setVaccineSelected(e.target.value)}}
            >
            <MenuItem value={0.95}>Comirnaty,Pfizer/BioNTech,95.0%</MenuItem>
            <MenuItem value={0.941}>mRNA-1273,Moderna,94.1%</MenuItem>
            <MenuItem value={0.78}>CoronaVac,Sinovac,78.0%</MenuItem>
            <MenuItem value={0.704}>AZD1222,BARDA,70.4%</MenuItem>
            <MenuItem value={0.941}>Sputnik V,Gamaleya Research Institute,94.1%</MenuItem>
            <MenuItem value={0.7934}>BBIBP-CorV,Sinopharm/Beijing Institute of Biological Products,79.3%</MenuItem>
              </Select>
              </FormControl>
        </div>
        
        </form>
        {selectStates ?(
            <div style={{ marginTop:"1%"}}>
            <FormControl className={classes.formControl}>
            <InputLabel id="demo-simple-select-label">Country</InputLabel>
           
            <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={currentCountry}
            onChange={e=>{onSelectCountry(e)}}
            >
            <MenuItem value={"Russia"}>Russia</MenuItem>
            <MenuItem value={"United States"}>United States</MenuItem>
            <MenuItem value={"Japan"}>Japan</MenuItem>
            <MenuItem value={"South Alfrica"}>South Alfrica</MenuItem>
            <MenuItem value={"Canada"}>Canada</MenuItem>
              </Select>
              </FormControl>
              <div style={{width:"50%"}}>
            {currentCountry === "United States" &&
                 <Multiselect
                 options={UnitedStatesStates} // Options to display in the dropdown
                 //selectedValues={} // Preselected value to persist in dropdown
                 onSelect={onStatesSelect} // Function will trigger on select event
                 onRemove={onStatesRemove} // Function will trigger on remove event
                 displayValue="name" // Property name to display in the dropdown options
                 />
            }
              {currentCountry === "Japan" &&
                 <Multiselect
                 options={JapanStates} // Options to display in the dropdown
                 //selectedValues={} // Preselected value to persist in dropdown
                 onSelect={onStatesSelect} // Function will trigger on select event
                 onRemove={onStatesRemove} // Function will trigger on remove event
                 displayValue="name" // Property name to display in the dropdown options
                 />
            }
              {currentCountry === "South Alfrica" &&
                 <Multiselect
                 options={SouthAlfricaStates} // Options to display in the dropdown
                 //selectedValues={} // Preselected value to persist in dropdown
                 onSelect={onStatesSelect} // Function will trigger on select event
                 onRemove={onStatesRemove} // Function will trigger on remove event
                 displayValue="name" // Property name to display in the dropdown options
                 />
            }
              {currentCountry === "Russia" &&
                 <Multiselect
                 options={RussiaStates} // Options to display in the dropdown
                 //selectedValues={} // Preselected value to persist in dropdown
                 onSelect={onStatesSelect} // Function will trigger on select event
                 onRemove={onStatesRemove} // Function will trigger on remove event
                 displayValue="name" // Property name to display in the dropdown options
                 />
            }
             {currentCountry === "Canada" &&
                 <Multiselect
                 options={CanadaStates} // Options to display in the dropdown
                 //selectedValues={} // Preselected value to persist in dropdown
                 onSelect={onStatesSelect} // Function will trigger on select event
                 onRemove={onStatesRemove} // Function will trigger on remove event
                 displayValue="name" // Property name to display in the dropdown options
                 />
            }
            </div>
            </div>
            
        ):null }
        

        {selectCountries ?(
            <Fragment>
            <div style={{width:"40%",marginTop:"2%"}}>
            <label>Countries</label>
           
            <Multiselect
            options={listOfCountriesOptions} // Options to display in the dropdown
            //selectedValues={} // Preselected value to persist in dropdown
            onSelect={onCountriesSelect} // Function will trigger on select event
            onRemove={onCountriesRemove} // Function will trigger on remove event
            displayValue="name" // Property name to display in the dropdown options
            />
             </div>
            </Fragment>
        ):null }
       
        <div className="simulate-btn-div">
            <Button
            onClick={onSubmit}
            >
        <h1>Simulate</h1>
        </Button>
        </div>
        
        </Fragment>
       
    )
    
}

export default InputSection