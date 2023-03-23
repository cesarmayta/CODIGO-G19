import NavBar from "../components/Navbar";
import CartList from "../components/CartList";
import Footer from "../components/Footer";


function Cart() {
    return(
        <>
            <NavBar/>
            <section className="py-5">
                <div className="container px-4 px-lg-5 mt-5">
                    <CartList/>
                </div>
            </section>
            <Footer/>
        </>
    )
}

export default Cart