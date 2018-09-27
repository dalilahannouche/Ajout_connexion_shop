{
    'name': 'Add login / Signup Popup in Shop page',
    'category': 'Website',
    'summary': 'The user can register and login in Shop page',
    'website': 'https://www.kissa.dz',
    'version': '1.0',
    'description': """
The user can register and login in Shop page.
======================
        """,
    	'author'	: 'Dalila Hannouche',
    	'depends'	: ['website', 'sale', 'payment','website_sale','auth_oauth'],
    	'data'	: [
		'views/template.xml',
    		],
    	'qweb'	: ['static/src/xml/*.xml'],

	'images': ['static/description/logo.png'],
    	'installable': True,
    	'application': True,
	'price': 10.00,
	'currency': 'EUR'
}
