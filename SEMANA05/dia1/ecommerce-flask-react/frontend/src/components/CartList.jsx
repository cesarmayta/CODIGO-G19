import {useContext} from "react"
import {CartContext} from "../context/CartContext"
import CartDetail from "./CartDetail"


function CartList(){
    const {state} = useContext(CartContext)

    return(
            <div className="container h-100 py-5">
                <div className="row d-flex justify-content-center align-items-center h-100">
                    <div className="col-10">

                        <div className="d-flex justify-content-between align-items-center mb-4">
                            <h3 className="fw-normal mb-0 text-black">Carrito de Compras</h3>
                        </div>

                        <div className="card rounded-3 mb-4">
                            {state.cart.map((prod)=>(
                                <CartDetail key={prod.id} product={prod}/>
                            ))}
                            
                        </div>
                        <div className="card">
                            <div className="card-body">
                                <button type="button" className="btn btn-warning btn-block btn-lg">Proceed to Pay</button>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
    )
}
export default CartList;