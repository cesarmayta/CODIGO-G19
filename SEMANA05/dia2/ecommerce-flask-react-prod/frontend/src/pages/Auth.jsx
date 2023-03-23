import Footer from "../components/Footer";
import Login from "../components/Login";
import NavBar from "../components/Navbar";

function Auth() {
    return(
        <>
            <NavBar/>
            <section className="py-5">
                <div className="container px-4 px-lg-5 mt-5">
                    <Login/>
                </div>
            </section>
            <Footer/>
        </>
    )
}

export default Auth