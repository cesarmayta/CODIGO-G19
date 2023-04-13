import Header from "../../components/Header"
import Sidebar from "../../components/Sidebar"
import { Link } from "react-router-dom"

const FacturaList = () => {
    return(
        <div id="layout-wrapper">
        <Header/>
        <div className="vertical-menu">
            <div data-simplebar className="h-100">
                <Sidebar/>
            </div>
        </div>
        <div className="main-content">
                <div className="page-content">
                    <div className="container-fluid">
                        <div className="row">
                            <div className="col-12">
                                <div className="page-title-box d-flex align-items-center justify-content-between">
                                    <h4 className="mb-0 font-size-18">Facturas</h4>
                                </div>
                            </div>
                        </div>
                        <div className="row>">
                            <Link to="/invoice/new" className="btn btn-primary">
                                Nueva Factura
                            </Link>
                        </div>
                    </div> 
                </div>
        </div>
    </div>
    )
}

export default FacturaList