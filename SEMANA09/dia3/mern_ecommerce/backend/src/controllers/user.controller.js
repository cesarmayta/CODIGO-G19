const userController = {}

const bcrypt = require('bcryptjs')
const userModel = require('../models/user.model')

userController.create = async (req,res) =>{
    try{
        const hash = await bcrypt.hash(req.body.userPassword,10)
        req.body.userPassword = hash
        const newUser = new userModel(req.body)
        await newUser.save()
        res.json({
            success:true,
            message:'user added successfully',
            content:{
                'id':newUser._id,
                'userName':newUser.userName
            }
        })
    }catch(err){
        res.status(502).json({
            success:false,
            message:'erry creating a new user',
            content:err
        })
    }
}

module.exports = userController