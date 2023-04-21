import { useContext, useEffect, useState } from "react";
import { AdminContext } from "../../../contexts/AdminContext";
import { getAllCategoriesService } from "../../../services/categoriesServices";
import { getToken } from "../../../services/authServices";
import { FaTrashAlt } from "react-icons/fa";
import {
  getAllProducts,
  postProduct,
  uploadProductImage,
} from "../../../services/productsServices";
import { IoIosArrowDown } from "react-icons/io";
import "./Products.scss";

export const Products = () => {
  const { setAdminTitle } = useContext(AdminContext);
  const [listOfProducts, setListOfProducts] = useState([]);
  const [listOfCategories, setListOfCategories] = useState([]);
  const [image, setImage] = useState();
  const [product, setProduct] = useState({
    productId:1,
    productName:"",
    productDescription:"",
    productPrice:0.0,
    productImage:"",
    productCategory:""
  });
  const [bandera, setBandera] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const token = getToken();
      const response = await getAllCategoriesService(token);
      if (response.status === 200) {
        setListOfCategories(response.data.content);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    setAdminTitle("Products");
    const fetchData = async () => {
      const token = getToken();
      const response = await getAllProducts(token);
      setListOfProducts(response.data.content);
    };
    fetchData();
  }, [bandera]);

  const createProduct = async (event) => {
    event.preventDefault();
    try {
      console.log("producto : ",product)
      const token = getToken();
      const response = await postProduct(product);
      console.log(response.content);
      if (response.success) {
        setBandera(!bandera);
        setProduct({
          productId:1,
          productName:"",
          productDescription:"",
          productPrice:0.0,
          productImage:"",
          productCategory:""
        });
      }
    } catch (error) {
      console.log(error);
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.currentTarget;
    if (name === "productPrice") {
      return setProduct({ ...product, [name]: parseFloat(value) });
    } else if (name === "productImage") {
      return setProduct({ ...product, [name]: event.target.files[0] });
    } else {
      return setProduct({ ...product, [name]: value });
    }
  };

  const handleFileChange = async (event) => {
    const { name,value } = event.target;
    const file = event.target.files[0];
    try {
      const response = await uploadProductImage(file);
      if (response.success) {
        console.log(response.content)
        return setProduct({ ...product, [name]: response.content });
      }
    } catch (error) {
      return console.log(error);
    }
  };

  return (
    <div className="Products">
      <h4 className="Products-subtitle">All products</h4>
      <div className="Products-table">
        <table>
          <thead>
            <tr>
              <th>Product name</th>
              <th>Product description</th>
              <th>Price</th>
              <th>Image</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {listOfProducts.length > 0 &&
              listOfProducts.map((product) => (
                <tr key={product.productId}>
                  <td>{product.productName}</td>
                  <td>{product.productDescription}</td>
                  <td>S/ {product.productPrice}</td>
                  <td>
                    <img
                      src={product.productImage}
                      alt="Product Preview"
                      loading={"lazy"}
                    />
                  </td>
                  <td>{product.stock}</td>
                  <td>
                    <button>
                      <FaTrashAlt/>
                    </button>
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>

      <h4 className="Products-subtitle">Create product</h4>
      <form className="Products-create-form" onSubmit={createProduct}>
        <div className="form-group">
          <label htmlFor="productoNombre">Product name</label>
          <input
            type="text"
            name="productName"
            id="productName"
            value={product.productName}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="productoDescripcion">Product description</label>
          <input
            type="text"
            name="productDescription"
            id="productDescription"
            value={product.productDescription}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="productoPrecio">Product price</label>
          <input
            type="number"
            min={0}
            step={0.1}
            name="productPrice"
            id="productPrice"
            value={product.productPrice}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="productoImagen">Product image</label>
          <input
            type="file"
            name="productImage"
            id="productImage"
            onChange={handleFileChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="categoriaId">Product category</label>
          <select
            name="productCategory"
            id="productCategory"
            value={product.productCategory}
            onChange={handleInputChange}
          >
            <option value="">Elegir Categoria</option>
            {listOfCategories?.map((category) => (
              <option key={category._id} value={category._id}>
                {category.nombre}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <button type="submit" className="Products-create-button">
            Create product
          </button>
        </div>
      </form>
    </div>
  );
};
