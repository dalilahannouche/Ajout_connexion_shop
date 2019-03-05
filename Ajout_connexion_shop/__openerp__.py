{
    'name': 'Login / Signup Popup in Shop page',
    'category': 'Website',
    'summary': 'The user can register and login in Shop page',
    'website': 'https://www.linkedin.com/in/dalila-hannouche-8a6896143/',
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

	'images': ['static/description/banner.png'],
    	'installable': True,
    	'application': True,
}
