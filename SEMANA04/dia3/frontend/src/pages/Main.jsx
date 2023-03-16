import React from 'react';
import NavBar from '../components/NavBar';
import SideBar from '../components/SideBar';
import Footer from '../components/Footer';
import CategoriaService from '../services/Categoria.service';

class Main extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            categorias : []
        }
    }

    componentDidMount(){
        CategoriaService.getAll().then(
            (res)=>{
                console.log(res);
                this.setState({
                    categorias : res
                })
            }
        )
    }

    render(){
        return(
            <>
                <NavBar/>
                <div id="layoutSidenav">
                    <SideBar/>
                    <div id="layoutSidenav_content">
                        <main>
                            <div className="container-fluid px-4">
                                <h1 className="mt-4">Categorias</h1>
                                <ol className="breadcrumb mb-4">
                                    <li className="breadcrumb-item"><a href="index.html">Dashboard</a></li>
                                    <li className="breadcrumb-item active">Static Navigation</li>
                                </ol>
                                <div className="card mb-4">
                                    <div className="card-body">
                                        <table className="table table-hover">
                                            <thead>
                                                <tr>
                                                    <th scope="col">#</th>
                                                    <th scope="col">Descripcion</th>
                                                    <th scope="col">...</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {this.state.categorias.map(categoria=>{
                                                    return(
                                                        <tr>
                                                            <th scope="row">{categoria.categoria_id}</th>
                                                            <td>{categoria.categoria_descripcion}</td>
                                                            <td>...</td>
                                                        </tr>
                                                    )
                                                })}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </main>
                        <Footer/>
                    </div>
                </div>
            </>
        )
    }
}

export default Main