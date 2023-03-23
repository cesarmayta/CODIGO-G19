import { createBrowserRouter } from "react-router-dom";
import Home from "../pages/home";
import Cart from "../pages/cart";
import Auth from "../pages/Auth";
import Admin from "../pages/Admin";

const router = createBrowserRouter([
    {
        path:"/",
        element:<Home/>
    },
    {
        path:"/carrito",
        element:<Cart/>
    },
    {
        path:"/auth",
        element:<Auth/>
    },
    {
        path:"/admin",
        element:<Admin/>
    }
])

export default router