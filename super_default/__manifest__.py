{
    'name': 'super',
    'version': '13.0.0.0',
    'category': 'Tools',
    'summary': "Proyecto super",
    'author': 'Sdeh',
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',
    'dbfilter': 'erp.confiteriasuper.com.ar',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/sistemasdehudson/cl-super',
        'https://github.com/regaby/odoo-custom.git',
        'https://github.com/regaby/sdeh-pos.git',
        'https://github.com/jobiols/odoo-addons.git',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/odoo-argentina-ce.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/website.git',
        'https://github.com/OCA/account-financial-reporting.git',
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/server-ux.git',
        'https://github.com/OCA/mis-builder.git',
        'https://github.com/OCA/sale-workflow.git',
        'https://github.com/OCA/web.git',
        ##
        'https://github.com/ctmil/contract.git',
        'https://github.com/CybroOdoo/CybroAddons.git',
        ## 'https://github.com/itpp-labs/pos-addons.git',
        'https://github.com/odoomates/odooapps.git',
        ##
        'https://github.com/sistemasdehudson/sdehposaddons.git',
        ##
        'https://github.com/jromeroarg/itpp-labs_pos-addons',
    ],

    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
