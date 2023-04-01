import Header from "../../components/Header"
import Sidebar from "../../components/Sidebar"

const FacturaForm = () => {
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
                                <div className="page-title-box d-flex align-items-center justify-content-between">
                                    <h4 className="mb-0 font-size-18">Nueva Factura</h4>
                                </div>
                            </div>
                        </div>
                        <div className="row">
                                <div className="col-xl-6">
                                    <div className="card">
                                        <div className="card-body">
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">RUC</label>
                                                <input type="text"
                                                    id="simpleinput"
                                                    className="form-control"
                                                    name="producto_codigo"
                                                    placeholder=""
                                                />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Razón Social</label>
                                                <input type="text"
                                                    id="simpleinput"
                                                    className="form-control"
                                                    name="producto_descripcion"
                                                    placeholder=""
                                                />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Dirección</label>
                                                <input type="text"
                                                    id="simpleinput"
                                                    className="form-control"
                                                    name="producto_precio"
                                                    placeholder=""
                                                />
                                            </div>
                                            
                                        </div>
                                    </div>
                                </div>
                                <div className="col-xl-6">
                                    <div className="card">
                                        <div className="card-body">
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Fecha Emisión</label>
                                                <input type="text"
                                                    id="simpleinput"
                                                    className="form-control"
                                                    name="producto_descripcion"
                                                    placeholder=""
                                                />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Nro Documento</label>
                                                <input type="text"
                                                    id="simpleinput"
                                                    className="form-control"
                                                    name="producto_descripcion"
                                                    placeholder=""
                                                />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="simpleinput">Moneda</label>
                                                <input type="text"
                                                    id="simpleinput"
                                                    className="form-control"
                                                    name="producto_precio"
                                                    placeholder=""
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                        </div>
                        <div className="row">
                                <div className="col-xl-10">
                                    <div className="card">
                                        <div className="card-body">
                                            <div className="form-group">
                                                <label for="exampleFormControlTextarea1">Observaciones</label>
                                                <textarea className="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="col-xl-2">
                                    <div className="card">
                                        <div className="card-body">
                                            <div class="form-group row">
                                                <div class="col-sm-2">
                                                </div>
                                                <label for="colFormLabelSm" class="col-sm-5 col-form-label col-form-label-sm">SUBTOTAL</label>
                                                <div class="col-sm-5">
                                                    <input type="text" 
                                                    class="form-control form-control-sm" 
                                                    id="colFormLabelSm" 
                                                    placeholder="1000.00"/>
                                                </div>
                                            </div>
                                            <div class="form-group row">
                                                <div class="col-sm-3">
                                                </div>
                                                <label for="colFormLabelSm" class="col-sm-4 col-form-label col-form-label-sm">IGV</label>
                                                <div class="col-sm-5">
                                                    <input type="text" 
                                                    class="form-control form-control-sm" 
                                                    id="colFormLabelSm" 
                                                    placeholder="180.00"/>
                                                </div>
                                            </div>
                                            <div class="form-group row">
                                                <div class="col-sm-3">
                                                </div>
                                                <label for="colFormLabelSm" class="col-sm-4 col-form-label col-form-label-sm">TOTAL</label>
                                                <div class="col-sm-5">
                                                    <input type="text" 
                                                    class="form-control form-control-sm" 
                                                    id="colFormLabelSm" 
                                                    placeholder="1180.00"/>
                                                </div>
                                            </div>
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

export default FacturaForm