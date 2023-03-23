import NavBar from "../components/Navbar";
import Header from "../components/Header";
import Catalog from "../components/Catalog";
import Footer from "../components/Footer";


function Home() {
    return(
        <>
            <NavBar/>
            <Header/>
            <section className="py-5">
                <div className="container px-4 px-lg-5 mt-5">
                    <Catalog/>
                </div>
            </section>
            <Footer/>
        </>
    )
}

export default Home