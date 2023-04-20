const {Router} = require('express')
const router = Router()

const {create,getAll,uploadProductImage} = require('../controllers/product.controller')

router.route('/')
    .post(create)
    .get(getAll)

router.route('/upload')
    .post(uploadProductImage)

module.exports = router