import { LoginService } from "../services/AuthServices";
import { useState,useContext } from "react";
import { AdminContext } from "../context/AdminContext";
import { useNavigate } from "react-router-dom";


function Login(){
    const [userCredentials,setUserCredentials] = useState({
        username:"",
        password:""
    })
    const {authentication,setAuthentication} = useContext(AdminContext);

    const navigate = useNavigate();

    const handleInputChange = (e) => {
        const {name,value} = e.currentTarget;

        setUserCredentials({
            ...userCredentials,
            [name]:value,
        })
    }

    const handleLogin = async (e) =>{
        e.preventDefault();
        const response = await LoginService(userCredentials);
        console.log(response);
        if(response.status === 200 && response.data.status === true){
            localStorage.setItem("token",response.data.content);
            console.log("login correcto")
            setAuthentication({
                ...authentication,
                isAuthenticated: true,
                isError:false,
                successMessage : "login correcto"
            })
            navigate("/admin")
        }
        else{
            console.log("credenciales no validas")
            setAuthentication({
                ...authentication,
                isAuthenticated: false,
                isError:true,
                errorMessage : response.data.content
            })
        }
    }

    return(
        <>
        <form className="form-signin" onSubmit={handleLogin}>
            <h1 className="h3 mb-3 font-weight-normal">Login</h1>
            <label htmlFor="username" className="sr-only">Email address</label>
            <input type="email" id="username" name="username" 
            className="form-control" 
            placeholder="Email address" 
            onChange={handleInputChange}
            />
            <label htmlFor="password" className="sr-only">Password</label>
            <input type="password" id="password" name="password"
            className="form-control" 
            placeholder="Password"
            onChange={handleInputChange}
            />
            <button className="btn btn-lg btn-primary btn-block" type="submit">Login</button>
        </form>
        {authentication.isError && (
            <div className="alert alert-danger" role="alert">
                {authentication.errorMessage}
            </div>
            )
        }
        </>
    )
}

export default Login;