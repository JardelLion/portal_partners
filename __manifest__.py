{
    "name": "Portal Partners",
    'summary': "show Parterns in Portal",
    'odoo_version': '18.0.0',
    'version': '1.0.0',
    'depends':['website','contacts'],
    "data": [
        'views/website_menu.xml',
        'views/templates.xml'
    ],
    'assets':{
        'web.assets_frontend':[
            "/portal_partners/static/src/js/partner_listing.js",
            "/portal_partners/static/src/xml/partner_listing.xml"
        ]
    },
    'installable': True,
    'auto_install': False
}