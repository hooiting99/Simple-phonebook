import './App.css';
import {useState, useEffect} from 'react';

function App() {

  const [phonebook, setPhonebook] = useState([])

  useEffect(()=>{
    fetch('http://localhost:5000/get',{
      'methods': 'GET',
      headers:{
        'Content-Type':'application/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => setPhonebook(resp))
    .catch(error => console.log(error))
  },[])

  const addPhonebook = () => {
    
  }


  return (
    <div className="App">
      <h1>Simple Phone Book</h1>
      {phonebook.map(phonebook =>{
        return(
          <div key ={phonebook.id}>
            <h2>{phonebook.name}</h2>
            <p>{phonebook.phoneNo}</p>
          </div>
        )
      })}
    </div>
  );
}

export default App;
