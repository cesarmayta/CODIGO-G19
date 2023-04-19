const {Router} = require('express')
const router = Router()

const {create} = require('../controllers/product.controller')

router.route('/')
    .post(create)

module.exports = router