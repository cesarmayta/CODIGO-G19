import { createContext,useState } from "react";

export const AdminContext = createContext();

export const AdminContextProvider = ({children}) =>{
    const [authentication,setAuthentication] = useState({
        isAuthenticated:false,
        isLoading:false,
        isError:false,
        errorMessage:"",
        successMessage:"",
        user:{},
    })

    return(
        <AdminContext.Provider value={{authentication,setAuthentication}}>
            {children}
        </AdminContext.Provider>
    )
}