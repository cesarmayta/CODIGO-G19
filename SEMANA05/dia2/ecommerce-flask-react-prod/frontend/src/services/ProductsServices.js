import { API_URL } from "../lib/Enviroments";

//retornar todos los productos
export const GetAllProducts = async () =>{
    const response = await fetch(`${API_URL}/producto`);
    const status = response.status;
    const data = await response.json();
    console.log("lista de productos : ",data);
    return {data,status};
};