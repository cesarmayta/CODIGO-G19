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
    const [productoId,setProductoId] = useState(0)

    const tab = <>&nbsp;&nbsp;</>;

    useEffect(()=>{
        ProductsServices.getAll().then(
            (res)=>{
                //console.log(res);
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

    const createUpdateProduct = (e) =>{
        e.preventDefault();
        if(productoId > 0){
            ProductsServices.updateOne(productoId,producto).then(
                (res)=>{
                    setRefreshProductos(true);
                    setProducto({
                        producto_codigo:"",
                        producto_descripcion:"",
                        producto_precio:0,
                        producto_usuario_log:"admin"
                    })
                    setProductoId(0)
                }
            )
        }
        else{
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
                    setProductoId(0)
                }
            )
        }
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
                setProductoId(cod)
            }
        )
    }

    const deleteProduct = (cod) =>{
        ProductsServices.deleteOne(cod).then(
            (res)=>{
                setRefreshProductos(true);
                setProducto({
                    producto_codigo:"",
                    producto_descripcion:"",
                    producto_precio:0,
                    producto_usuario_log:"admin"
                })
                setProductoId(cod)
            }
        )
    }

    return(
        <div id="layout-wrapper">
            <Header />
            <div className="vertical-menu">
                <div data-simplebar className="h-100">
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
                            <div className="col-xl-6">
                                <div className="card">
                                    <div className="card-body">
                                        <form onSubmit={createUpdateProduct}>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Codigo</label>
                                                <input type="text" 
                                                id="simpleinput" 
                                                className="form-control"
                                                name="producto_codigo" 
                                                placeholder=""
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
                                                placeholder=""
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
                            <div className="col-xl-6">
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
                                                    <tr key={prod.producto_id}>
                                                        <td>{prod.producto_codigo}</td>
                                                        <td>{prod.producto_descripcion}</td>
                                                        <td>{prod.producto_precio}</td>
                                                        <td>
                                                            <button className="btn btn-success"
                                                            onClick={()=>editProduct(prod.producto_id)}>
                                                                Editar
                                                            </button>
                                                            {tab}
                                                            <button className="btn btn-danger"
                                                            onClick={()=>deleteProduct(prod.producto_id)}>
                                                                Eliminar
                                                            </button>
                                                        </td>
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
        </div>
    )
}

export default Products