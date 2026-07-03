from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.users"

    allowed_crm_salesperson_ids = fields.Many2many(
        "res.users",
        "res_users_allowed_crm_salesperson_rel",
        "viewer_user_id",
        "salesperson_user_id",
        string="Can View Opportunities Assigned To",
        help="Select the salespeople whose opportunities this user is allowed to see. "
             "Used together with a custom security group and record rule on crm.lead.",
    )
