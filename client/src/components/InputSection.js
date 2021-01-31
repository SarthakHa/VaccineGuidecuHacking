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
    
    const vaccinesInfo = [{name:"Comirnaty,Pfizer/BioNTech,95.0%"},{name:"mRNA-1273,Moderna,94.1%"},{name:"CoronaVac,Sinovac,78.0%"},{name:"AZD1222,BARDA,70.4%"},{name:"Sputnik V,Gamaleya Research Institute,94.1%"},{name:"BBIBP-CorV,Sinopharm/Beijing Institute of Biological Products,79.3%"}] 
    const JapanStates = [{name: 'Aichi'},{name: 'Akita'},{name: 'Aomori'},{name: 'Chiba'},{name: 'Ehime'},{name: 'Fukui'},{name: 'Fukuoka'},{name: 'Fukushima'},{name: 'Gifu'},{name: 'Gunma'},{name: 'Hiroshima'},{name: 'Hokkaido'},{name: 'Hyogo'},{name: 'Ibaraki'},{name: 'Ishikawa'},{name: 'Iwate'},{name: 'Kagawa'},{name: 'Kagoshima'},{name: 'Kanagawa'},{name: 'Kochi'},{name: 'Kumamoto'},{name: 'Kyoto'},{name: 'Mie'},{name: 'Miyagi'},{name: 'Miyazaki'},{name: 'Nagano'},{name: 'Nagasaki'},{name: 'Nara'},{name: 'Niigata'},{name: 'Oita'},{name: 'Okayama'},{name: 'Okinawa'},{name: 'Osaka'},{name: 'Saga'},{name: 'Saitama'},{name: 'Shiga'},{name: 'Shimane'},{name: 'Shizuoka'},{name: 'Tochigi'},{name: 'Tokushima'},{name: 'Tokyo'},{name: 'Tottori'},{name: 'Toyama'},{name: 'Wakayama'},{name: 'Yamagata'},{name: 'Yamaguchi'},{name: 'Yamanashi'}]
    const CanadaStates =  [{name: 'Alberta'},{name: 'British Columbia'},{name:'Manitoba'}, {name:'New Brunswick'},{name:'Newfoundland and Labrador'}, {name:'Northwest Territories'}, {name:'Nova Scotia'}, {name:'Ontario'}, {name:'Prince Edward Island'}, {name:'Quebec'}, {name:'Saskatchewan'}, {name:'Yukon'}]
    const RussiaStates = [{name: 'Altay republic'},{name: 'Altayskiy kray'},{name: 'Amursk oblast'},{name: 'Arkhangelsk oblast'},{name: 'Astrahan oblast'},{name: 'Belgorod oblast'},{name: 'Briansk oblast'},{name: 'Chechen republic'},{name: 'Cheliabinsk oblast'},{name: 'Chukotskiy autonomous oblast'},{name: 'Habarovskiy kray'},{name: 'Hanty-Mansiyskiy Autonomous Okrug'},{name: 'Ingushetia republic'},{name: 'Irkutsk oblast'},{name: 'Ivanovo oblast'},{name: 'Jewish Autonomous oblast'},{name: 'Kaliningrad oblast'},{name: 'Kaluga oblast'},{name: 'Kamchatskiy kray'},{name: 'Kemerovo oblast'},{name: 'Kirov oblast'},{name: 'Komi republic'},{name: 'Kostroma oblast'},{name: 'Krasnodarskiy kray'},{name: 'Krasnoyarskiy kray'},{name: 'Kurgan oblast'},{name: 'Kursk oblast'},{name: 'Leningradskaya oblast'},{name: 'Lipetsk oblast'},{name: 'Magadan oblast'},{name: 'Moscow'},{name: 'Moscow oblast'},{name: 'Murmansk oblast'},{name: 'Nenetskiy autonomous oblast'},{name: 'Nizhegorodskaya oblast'},{name: 'Novgorod oblast'},{name: 'Novosibirsk oblast'},{name: 'Omsk oblast'},{name: 'Orel oblast'},{name: 'Orenburg oblast'},{name: 'Pensa oblast'},{name: 'Perm oblast'},{name: 'Primorskiy kray'},{name: 'Pskov oblast'},{name: 'Republic of Adygeia'},{name: 'Republic of Bashkortostan'},{name: 'Republic of Buriatia'},{name: 'Republic of Chuvashia'},{name: 'Republic of Crimea'},{name: 'Republic of Dagestan'},{name: 'Republic of Hakassia'},{name: 'Republic of Kabardino-Balkaria'},{name: 'Republic of Kalmykia'},{name: 'Republic of Karachaevo-Cherkessia'},{name: 'Republic of Karelia'},{name: 'Republic of Mariy El'},{name: 'Republic of Mordovia'},{name: 'Republic of North Osetia - Alania'},{name: 'Republic of Tatarstan'},{name: 'Republic of Tyva'},{name: 'Republic of Udmurtia'},{name: 'Rostov oblast'},{name: 'Ryazan oblast'},{name: 'Saint Petersburg'},{name: 'Sakha (Yakutiya) Republic'},{name: 'Sakhalin oblast'},{name: 'Samara oblast'},{name: 'Saratov oblast'},{name: 'Sevastopol'},{name: 'Smolensk oblast'},{name: 'Stavropolskiy kray'},{name: 'Sverdlov oblast'},{name: 'Tambov oblast'},{name: 'Tomsk oblast'},{name: 'Tula oblast'},{name: 'Tumen oblast'},{name: 'Tver oblast'},{name: 'Ulianovsk oblast'},{name: 'Vladimir oblast'},{name: 'Volgograd oblast'},{name: 'Vologda oblast'},{name: 'Voronezh oblast'},{name: 'Yamalo-Nenetskiy Autonomous Okrug'},{name: 'Yaroslavl oblast'},{name: 'Zabaykalskiy kray'}]
    const SouthAlfricaStates = [{name: 'Eastern Cape'},{name: 'Free State'},{name: 'Gauteng'},{name: 'KwaZulu-Natal'},{name: 'Limpopo'},{name: 'Mpumalanga'},{name: 'North West'},{name: 'Northern Cape'},{name: 'Western Cape'}]
    const UnitedStatesStates =[{name: 'Alabama'},{name: 'Alaska'},{name: 'American Samoa'},{name: 'Arizona'},{name: 'Arkansas'},{name: 'California'},{name: 'Colorado'},{name: 'Connecticut'},{name: 'Delaware'},{name: 'District of Columbia'},{name: 'Florida'},{name: 'Georgia'},{name: 'Guam'},{name: 'Hawaii'},{name: 'Idaho'},{name: 'Illinois'},{name: 'Indiana'},{name: 'Iowa'},{name: 'Kansas'},{name: 'Kentucky'},{name: 'Louisiana'},{name: 'Maine'},{name: 'Maryland'},{name: 'Massachusetts'},{name: 'Michigan'},{name: 'Minnesota'},{name: 'Mississippi'},{name: 'Missouri'},{name: 'Montana'},{name: 'Nebraska'},{name: 'Nevada'},{name: 'New Hampshire'},{name: 'New Jersey'},{name: 'New Mexico'},{name: 'New York'},{name: 'North Carolina'},{name: 'North Dakota'},{name: 'Northern Mariana Islands'},{name: 'Ohio'},{name: 'Oklahoma'},{name: 'Oregon'},{name: 'Pennsylvania'},{name: 'Puerto Rico'},{name: 'Rhode Island'},{name: 'South Carolina'},{name: 'South Dakota'},{name: 'Tennessee'},{name: 'Texas'},{name: 'Utah'},{name: 'Vermont'},{name: 'Virgin Islands'},{name: 'Virginia'},{name: 'Washington'},{name: 'West Virginia'},{name: 'Wisconsin'},{name: 'Wyoming'}]
    //const RussiaStates = [{name:'Altay republic'},{name:'Altayskiy kray'},{name:'Amursk oblast'},{name:"Arkhangelsk oblast"},{name:"Astrahan oblast"},{name:'Belgorod oblast'},{name:'Briansk oblast'},{name:'Chechen republic'},{name:'Cheliabinsk oblast'},{name:'Chukotskiy autonomous oblast' },{name:'Habarovskiy kray'}]
    const listOfCountriesOptions = [{key:1,name: 'Canada'},{key:2,name: 'Russia'},{key:3,name:"South Africa"},{key:4,name:"Japan"},{key:5,name:"United States"}]
    
    

    

    const toggleCountries =(e)=>{
        setSelectContries(true)
        setCurentCountry("")
        setNumberOfSteps(0)
        setNumberOfVaccinePerDay(0)
        setVaccineSelected("")
        setStates(new Array())
        setSelectStates(false)
    }

    const toggleStates =(e)=>{
        setSelectContries(false)
        setNumberOfSteps(0)
        setNumberOfVaccinePerDay(0)
        setVaccineSelected("")
        setStates(new Array())
        setCountries(new Array())
        setSelectStates(true)
    }

    const convertArrayToJsonObj =(items)=>{
        var arrayOfObject=new Array();
        for(var i=0; i < items.length;i++){
            var obj = new Object();
            obj.name = items[i];
            arrayOfObject.push(obj)
        }
        var jsonArray = JSON.parse(JSON.stringify(arrayOfObject));
        //console.log("jsonArray",jsonArray)
        return jsonArray
    }

    const onCountriesSelect =(selectedList,selectedItem)=>{
       // console.log("2",selectedItem.name)
        setCountries(countries=>[...countries,selectedItem.name])
    }

    
    const onCountriesRemove =(selectedList,selectedItem)=>{
        setCountries(countries.filter(country=>country !== selectedItem.name))
     }


     const onStatesSelect =(selectedList,selectedItem)=>{
        // console.log("2",selectedItem.name)
         setStates(states=>[...states,selectedItem.name])
     }


    const onStatesRemove =(selectedList,selectedItem)=>{
       setStates(states.filter(state=>state !== selectedItem.name))
    }

    const onSelectCountry =(e)=>{
        setCurentCountry(e.target.value)
        setStates(new Array())
    }

    const onSubmit=async()=>{
        
        var data = new Object()
        if(countries.length ===0){
          data.countries = null
        }else{
          data.countries = countries
        }

        if(states.length ===0){
          data.states = null
        }else{
          data.states=states
        }

        if(currentCountry.length ===0){
          data.currentCountry = null
        }else{
          data.currentCountry = new Array()
          data.currentCountry[0] = currentCountry
        }
    
        data.numberOfSteps = numberOfSteps
        data.numberOfVaccinePerDay = numberOfVaccinePerDay
        data.vaccineSelected = vaccineSelected

        
        console.log("data",data)
        const response= await fetch('/test',{
          method:'POST',
          headers:{
            'Content-Type':'application/json'
          },
          body: JSON.stringify(data)
        })
        console.log("response",response)
        console.log("response.body",response.body)
        if(response.ok){
          console.log("responsed")
        }else{
          console.log("fail")
        }

      
        

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
          label="Number of steps (from 1-180)"
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
              <div style={{width:"100%"}}>
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
            <div style={{width:"85%",marginTop:"2%"}}>
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