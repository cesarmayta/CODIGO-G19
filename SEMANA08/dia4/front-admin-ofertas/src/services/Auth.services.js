import axios from 'axios'

import {API_URL} from '../lib/Enviroments'

class AuthService{
    login(usuario,password){
        return axios.post(API_URL + "/auth",{
            usuario:usuario,
            password:password
        })
        .then(res=>{
            if(res.data.content){
                console.log(res.data.content)
                return res.data.content
            }
        })
    }
}

export default new AuthService