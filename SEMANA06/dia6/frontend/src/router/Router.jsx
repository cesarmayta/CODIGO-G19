import {createBrowserRouter} from "react-router-dom"
import Home from "../pages/Home"
import Login from  "../pages/Login"
import Products from "../pages/Products"
import FacturaList from "../pages/factura/Factura"
import FacturaForm from "../pages/factura/FacturaForm"

const router = createBrowserRouter([
{
    path:"/",
    element:<Home/>,
},
{
    path:"/login",
    element:<Login/>
},
{
    path:"/products",
    element:<Products/>
},
{
    path:"/invoices",
    element:<FacturaList/>
},
{
    path:"/invoice/new",
    element:<FacturaForm/>
}
])

export default router