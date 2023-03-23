import Footer from "../components/Footer";
import AdminProducts from "../components/AdminProducts";
import NavBar from "../components/Navbar";

function Admin() {
    return(
        <>
            <NavBar/>
            <section className="py-5">
                <div className="container px-4 px-lg-5 mt-5">
                    <AdminProducts/>
                </div>
            </section>
            <Footer/>
        </>
    )
}

export default Admin