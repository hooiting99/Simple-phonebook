import React, {useState} from 'react'
import APIService from './APIService'

function addPhonebook() {

    const [name, setName] = useState()
    const [phoneNo, setPhoneNo] = useState()

    const insertContact = () =>{
        APIService.insertContact({name, phoneNo})
        .then(resp=> console.log(resp))
        .catch(error=>console.error(error))
    }
    

    return (
        <div>
            <label htmlForm = 'name' className='form-label'>Name</label>
            <input type='text' className='form-control' placeholder='Enter Name'/>

        </div>
    )
}

export default addPhonebook
