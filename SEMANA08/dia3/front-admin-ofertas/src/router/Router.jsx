import {createBrowserRouter} from "react-router-dom"
import Home from "../pages/Home"
import Login from  "../pages/Login"
import Categoria from "../pages/Categoria"
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
    path:"/categoria",
    element:<Categoria/>
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