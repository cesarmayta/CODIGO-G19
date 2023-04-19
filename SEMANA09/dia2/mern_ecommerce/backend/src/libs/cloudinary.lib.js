const {config} = require('../config')

const cloudinary = require('cloudinary').v2

// Configuration 
cloudinary.config({
    cloud_name: config.cloudinary.cloud_name,
    api_key: config.cloudinary.api_key,
    api_secret: config.cloudinary.api_secret
});
  
  // Upload
  
function uploadImage(uploadPath){
    const res = cloudinary.uploader.upload(uploadPath, {public_id: "shop_g19_products"})
    res.then((data) => {
        console.log(data);
        console.log(data.secure_url);
        return data.secure_url
    }).catch((err) => {
        console.log(err);
    });
}

module.exports = {uploadImage}
  
  