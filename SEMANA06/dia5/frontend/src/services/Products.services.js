import axios from 'axios'
import { API_URL } from '../lib/Enviroments'

class ProductService{

    
    
    getAll(){
        return axios.get(API_URL+"/producto")
        .then(res=>{
            return res.data;
        })
    }
}

export default new ProductService();