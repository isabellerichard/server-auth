import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-server-auth",
    description="Meta package for oca-server-auth Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-auth_admin_passkey',
        'odoo14-addon-auth_api_key',
        'odoo14-addon-auth_ldaps',
        'odoo14-addon-auth_session_timeout',
        'odoo14-addon-auth_user_case_insensitive',
        'odoo14-addon-user_log_view',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
