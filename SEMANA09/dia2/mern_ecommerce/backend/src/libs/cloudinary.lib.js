const {config} = require('../config')

const cloudinary = require('cloudinary').v2

// Configuration 
cloudinary.config({
    cloud_name: config.cloudinary.cloud_name,
    api_key: config.cloudinary.api_key,
    api_secret: config.cloudinary.api_secret
});
  
  // Upload
  
async function uploadImage(uploadPath){
    await cloudinary.uploader.upload(uploadPath, (error,result)=>{
        console.log(result.url)
        return result.url
    })
}

module.exports = {uploadImage}
  
  