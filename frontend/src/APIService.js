export default class APIService {
    static addContact(phoneNo){
        return fetch('http://localhost:5000/add',{
            'method': 'POST',
            headers:{
                'Content-Type':'application/json'
            },
            phoneNo: JSON.stringify(phoneNo)
        })
        .then(resp => resp.json())
    }
}