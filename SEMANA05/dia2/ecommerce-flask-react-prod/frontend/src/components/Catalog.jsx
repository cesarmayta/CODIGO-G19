import { useState,useEffect, useContext } from "react"
import { GetAllProducts } from "../services/ProductsServices"
import { CartContext } from "../context/CartContext";


function Catalog(){
    const [listOfProducts,setListOfProducts] = useState([]);
    const {dispatch} = useContext(CartContext);

    useEffect(()=>{
        const fetchData = async() =>{
            const response = await GetAllProducts();
            setListOfProducts(response.data.content);
            console.log(listOfProducts)
        };
        fetchData();
    },[])

    return(
        <>
            <div className="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">
                
                            {listOfProducts.length > 0 &&
                                listOfProducts.map((product)=>(
                                    <div className="col mb-5">
                                        <div className="card h-100">
                                            <img className="card-img-top" src={product.imagen} alt="..." />
                                            <div className="card-body p-4">
                                                <div className="text-center">
                                                    <h5 className="fw-bolder">{product.nombre}</h5>
                                                    ${product.precio}
                                                </div>
                                            </div>
                                            <div className="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                                <div className="text-center">
                                                    <a className="btn btn-outline-dark mt-auto" 
                                                    onClick={
                                                        ()=>{
                                                            dispatch({type:"ADD",payload:product})
                                                        }
                                                    }
                                                    >Agregar al Carrito</a>
                                                </div>
                                            </div>
                                        </div>        
                                    </div>
                                ))
                            } 
                     
            </div>
        </>
    )
}

export default Catalog