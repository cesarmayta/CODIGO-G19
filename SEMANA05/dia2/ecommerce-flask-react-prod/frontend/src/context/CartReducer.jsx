const CartReducer = (state,action) =>{
    switch(action.type){
        case "ADD":
            return {...state,cart:[...state.cart,action.payload]}
        case "REMOTE":
            return {
                ...state,
                cart: [...state.cart.filter((c)=> c.id !== action.payload.id)],
            }
        case "CLEAR":
            return {cart: []}
        default:
            return state
    }
    console.log(state)
}

export default CartReducer