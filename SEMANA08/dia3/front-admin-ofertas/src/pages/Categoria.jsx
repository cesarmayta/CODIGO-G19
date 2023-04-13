import { useState,useEffect } from "react"
import Header from "../components/Header"
import Sidebar from "../components/Sidebar"
import CategoriaServices from "../services/Categoria.services"

const Categoria = () => {
    const [data,setData] = useState([])
    const [newData,setnewData] = useState({
        id:"",
        descripcion:""
    })
    const [refreshData,setRefreshData] = useState(false)
    const [dataId,setDataId] = useState(0)

    const tab = <>&nbsp;&nbsp;</>;

    useEffect(()=>{
        CategoriaServices.getAll().then(
            (res)=>{
                setData(res);
                setRefreshData(false)
            }
        )
    },[refreshData])

    const handleInputChange = (e) =>{
        const {name,value} = e.target
        return setData({
            ...data,[name]:value
        })
    }

    /*
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
*/
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
                                <h4>CATEGORIAS</h4>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-xl-6">
                                <div className="card">
                                    <div className="card-body">
                                        <form>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Codigo</label>
                                                <input type="text" 
                                                id="simpleinput" 
                                                className="form-control"
                                                name="id" 
                                                placeholder=""
                                                value={data.id}
                                                onChange={handleInputChange}
                                                />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Descripción</label>
                                                <input type="text" 
                                                id="simpleinput" 
                                                className="form-control"
                                                name="descripcion" 
                                                placeholder=""
                                                value={data.descripcion}
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
                                                <th>Acciones</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {data.map(dt => {
                                                return (
                                                    <tr key={dt.id}>
                                                        <td>{dt.id}</td>
                                                        <td>{dt.descripcion}</td>
                                                        <td>
                                                            <button className="btn btn-success"
                                                            >
                                                                Editar
                                                            </button>
                                                            {tab}
                                                            <button className="btn btn-danger"
                                                            >
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

export default Categoria