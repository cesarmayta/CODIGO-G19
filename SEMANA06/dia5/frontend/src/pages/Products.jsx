import Header from "../components/Header"
import Sidebar from "../components/Sidebar"

const Products = () => {
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
                                                <th>#</th>
                                                <th>First Name</th>
                                                <th>Last Name</th>
                                                <th>Username</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <th scope="row">1</th>
                                                <td>Mark</td>
                                                <td>Otto</td>
                                                <td>@mdo</td>
                                            </tr>
                                            <tr>
                                                <th scope="row">2</th>
                                                <td>Jacob</td>
                                                <td>Thornton</td>
                                                <td>@fat</td>
                                            </tr>
                                            <tr>
                                                <th scope="row">3</th>
                                                <td>Larry</td>
                                                <td>the Bird</td>
                                                <td>@twitter</td>
                                            </tr>
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