import axios from 'axios';

const API_URL = 'http://localhost:5000'


class CategoriaService{

    getAll(){
        return axios
        .get(API_URL+"/categoria")
        .then(res=>{
            return res.data.content;
        })
    }

    setNew(data){
        return axios
        .post(API_URL+"/categoria",data)
        .then(res=>{
            return res.data.content;
        })
    }
}

export default new CategoriaService();