const categoryController = {}

const CategoryModel = require('../models/category.model')

categoryController.create = async (req,res)=>{
    try{
        const newCategory = new CategoryModel(req.body)
        await newCategory.save()
        res.status(201).json({
            success:true,
            message:'category added successfully',
            content:newCategory
        })
    }catch(err){
        res.status(502).json({
            success:false,
            message:'error by entering a new Category',
            content:err
        })
    }
}

module.exports = categoryController