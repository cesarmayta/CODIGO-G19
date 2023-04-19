const productController = {}

const productModel = require('../models/product.model')


productController.create = async (req,res)=>{
    try{
        const newProduct = new productModel(req.body)
        await newProduct.save()
        res.json({
            success:true,
            message:'producto added successfully',
            content: newProduct
        })
    }catch(err){
        res.status(502).json({
            success:false,
            message:'error by registering a new product',
            content:err
        })
    }
}

productController.getAll = async (req,res)=>{
    const products = await productModel.find()
    res.json({
        success:true,
        message:"products have been loaded",
        content:products
    })
}

module.exports = productController