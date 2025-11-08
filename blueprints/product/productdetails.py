from .route import product_module
from handlers import productshandler
from flask import request

@product_module.route('/allproducts', methods = ['GET'])
def all_products():
    return productshandler().all_products()

@product_module.route('/addproducts',methods = ['POST'])
def add_products():
    return productshandler().add_products(request=request)

@product_module.route('/deleteproduct', methods = ['POST'])
def delete_products():
    return productshandler().delete_products(request=request)

@product_module.route('/updateproducts', methods = ['POST'])
def update_products():
    return productshandler().update_products(request=request)

@product_module.route('/getsingleproduct',methods = ['POST'])
def get_single_product():
    return productshandler().getsingleproducts(request=request)
