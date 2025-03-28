{
    'name': 'Bookmark Module',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Add fields for product.product model',
    'description': """
        Bookmark Module
    """,
    'author': 'Samiha',
    'depends': ['base','product','purchase','sale'],   
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_form_view.xml',
        'views/product_template.xml',
        'views/purchase_order_line_view.xml',
    ],
    'installable': True,
    'application': True,
    
}