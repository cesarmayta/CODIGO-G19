import { useState,useEffect } from "react"
import Header from "../components/Header"
import Sidebar from "../components/Sidebar"
import ProductsServices from "../services/Products.services"

const Products = () => {
    const [productos,setProductos] = useState([])
    const [producto,setProducto] = useState({
        producto_codigo:"",
        producto_descripcion:"",
        producto_precio:0,
        producto_usuario_log:"admin"
    })
    const [refreshProductos,setRefreshProductos] = useState(false)

    useEffect(()=>{
        ProductsServices.getAll().then(
            (res)=>{
                console.log(res);
                setProductos(res);
                setRefreshProductos(false)
            }
        )
    },[refreshProductos])

    const handleInputChange = (e) =>{
        const {name,value} = e.target
        return setProducto({
            ...producto,[name]:value
        })
    }

    const createProduct = (e) =>{
        e.preventDefault();
        ProductsServices.setNew(producto).then(
            (res)=>{
                console.log(res)
                setRefreshProductos(true)
                setProducto({
                    producto_codigo:"",
                    producto_descripcion:"",
                    producto_precio:0,
                    producto_usuario_log:"admin"
                })
            }
        )
    }

    const editProduct = (cod) =>{
        ProductsServices.getOne(cod).then(
            (res)=>{
                setProducto({
                    producto_codigo:res.producto_codigo,
                    producto_descripcion:res.producto_descripcion,
                    producto_precio:res.producto_precio,
                    producto_usuario_log:"admin"
                })
            }
        )
    }

    return(
        <div id="layout-wrapper">
            <Header />
            <div className="vertical-menu">
                <div data-simplebar className="h-100">
                    <div className="navbar-brand-box">
                        <a href="index.html" className="logo">
                            FACTURACION
                        </a>
                    </div>
                    <Sidebar />
                </div>
            </div>
            <div className="main-content">
                <div className="page-content">
                    <div className="container-fluid">
                        <div className="row">
                            <div className="col-12">
                                <h4>PRODUCTOS</h4>
                            </div>
                        </div>
                        <div className="row">
                            <div className="table-responsive">
                                <table className="table mb-0">
                                    <thead>
                                        <tr>
                                            <th>Codigo</th>
                                            <th>Descripcion</th>
                                            <th>Precio</th>
                                            <th>Acciones</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {productos.map(prod => {
                                            return (
                                                <tr>
                                                    <td>{prod.producto_codigo}</td>
                                                    <td>{prod.producto_descripcion}</td>
                                                    <td>{prod.producto_precio}</td>
                                                    <td>
                                                        <button className="btn btn-success"
                                                        onClick={()=>editProduct(prod.producto_id)}>
                                                            Editar
                                                        </button>
                                                    </td>
                                                </tr>
                                            )
                                        })}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <br/>
                        <div className="row">
                            <div className="col-xl-6">
                                <div className="card">
                                    <div className="card-body">
                                        <h4 className="card-title">Nuevo Producto </h4>
                                        <form onSubmit={createProduct}>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Codigo</label>
                                                <input type="text" 
                                                id="simpleinput" 
                                                className="form-control"
                                                name="producto_codigo" 
                                                placeholder="Enter your text"
                                                value={producto.producto_codigo}
                                                onChange={handleInputChange}
                                                />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Descripción</label>
                                                <input type="text" 
                                                id="simpleinput" 
                                                className="form-control"
                                                name="producto_descripcion" 
                                                placeholder="Enter your text"
                                                value={producto.producto_descripcion}
                                                onChange={handleInputChange}
                                                />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Precio</label>
                                                <input type="text" 
                                                id="simpleinput" 
                                                className="form-control"
                                                name="producto_precio"
                                                placeholder="Enter your text"
                                                value={producto.producto_precio}
                                                onChange={handleInputChange}
                                                />
                                            </div>
                                            <button type="submit" className="btn btn-primary waves-effect waves-light">Guardar</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Products