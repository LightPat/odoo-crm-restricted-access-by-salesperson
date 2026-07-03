{
    "name": "CRM Restricted Access by Salesperson",
    "version": "19.0.1.0.0",
    "category": "CRM",
    "summary": "Restrict users to see only opportunities assigned to selected salespeople via a configurable field on res.users",
    "author": "Patrick Seeman",
    "license": "LGPL-3",
    "depends": ["base", "crm"],
    "data": [
        "views/res_users_views.xml",
    ],
    "installable": True,
    "application": False,
}
