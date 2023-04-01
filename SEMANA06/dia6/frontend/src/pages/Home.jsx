import Header from "../components/Header"
import Sidebar from "../components/Sidebar"

const Home = () => {
    return(
            <div id="layout-wrapper">
                <Header/>
                <div className="vertical-menu">

                    <div data-simplebar className="h-100">

                        <div className="navbar-brand-box">
                            <a href="index.html" className="logo">
                                <img src="assets/images/logo-light.png" />
                            </a>
                        </div>
                        <Sidebar/>
                        
                    </div>
                    <div className="main-content">

                        <div className="page-content">
                            <div className="container-fluid">

                               
                                <div className="row">
                                    <div className="col-12">
                                        <div className="page-title-box d-flex align-items-center justify-content-between">
                                            <h4 className="mb-0 font-size-18">Starter</h4>

                                            <div className="page-title-right">
                                                <ol className="breadcrumb m-0">
                                                    <li className="breadcrumb-item"><a href="#">Pages</a></li>
                                                    <li className="breadcrumb-item active">Starter</li>
                                                </ol>
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

export default Home