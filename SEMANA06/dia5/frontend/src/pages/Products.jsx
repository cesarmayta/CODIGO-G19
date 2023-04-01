import { useState,useEffect } from "react"
import Header from "../components/Header"
import Sidebar from "../components/Sidebar"
import ProductsServices from "../services/Products.services"

const Products = () => {
    const [productos,setProductos] = useState([])

    useEffect(()=>{
        ProductsServices.getAll().then(
            (res)=>{
                console.log(res);
                setProductos(res);
            }
        )
    },[])

    return(
        <div id="layout-wrapper">
            <Header/>
            <div className="vertical-menu">
                <div data-simplebar className="h-100">
                    <div className="navbar-brand-box">
                        <a href="index.html" className="logo">
                            FACTURACION
                        </a>
                    </div>
                    <Sidebar/>
                </div>
            </div>
            <div className="main-content">
                    <div className="page-content">
                        <div class="container-fluid">
                            <div className="row">
                                <div className="col-12">
                                    <h4>PRODUCTOS</h4>
                                </div>
                            </div>
                            <div className="row">
                                <div class="table-responsive">
                                    <table class="table mb-0">
                                        <thead>
                                            <tr>
                                                <th>Codigo</th>
                                                <th>Precio</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {productos.map(prod=>{
                                                return(
                                                    <tr>
                                                        <td>{prod.producto_codigo}</td>
                                                        <td>{prod.producto_precio}</td>
                                                        
                                                    </tr>
                                                )
                                            })}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
            </div>
            
        </div>
    )
}

export default Products