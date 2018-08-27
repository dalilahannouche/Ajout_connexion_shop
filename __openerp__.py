{
    'name': 'Ajout inscription/connexion dans la page Boutique',
    'category': 'Website',
    'summary': 'Permettre inscription/connexion au client',
    'website': 'https://www.kissa.dz',
    'version': '1.0',
    'description': """
Connexion à la page boutique. Inscription avec fenêtre Popup.
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
}
