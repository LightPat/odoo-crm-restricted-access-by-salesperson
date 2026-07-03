# CRM Restricted Access by Salesperson

Restrict CRM users (e.g. viewers, managers, or claims staff) to see **only** the opportunities assigned to specific salespeople you choose per user.

## Features
- Adds a clean "Can View Opportunities Assigned To" Many2many field on the res.users form (new tab "CRM Access Restrictions")
- Works with standard Odoo record rules using `user.allowed_crm_salesperson_ids.ids`
- Fully configurable by the owner/admin via the user profile — no code changes needed after initial setup
- Matches the clean structure of other addons in this stack (uv + pyproject.toml + minimal dependencies)

## Installation
1. Clone or pull this repo into your Odoo `addons` path (alongside your other custom modules).
2. Restart Odoo (or use `-u` / Apps > Update Apps List).
3. Install the module **"CRM Restricted Access by Salesperson"** from Apps.

## Setup (One-time, UI only)
1. Activate Developer Mode.
2. Go to **Settings > Users & Companies > Groups > Create**.
   - Name: `CRM / User: Specific Salespeople Only`
   - Application: CRM (or Sales)
3. In the group, add **Access Rights**:
   - `crm.lead` → Read = Yes (Write/Create/Unlink = No for a viewer role)
   - Also add Read for related models you see errors for: `res.partner`, `res.users`, `crm.stage`
4. Create a **Record Rule** (in the group or via Technical > Security > Record Rules):
   - Model: `crm.lead`
   - Groups: select your new group
   - Domain (exact):
     ```
     [('user_id', 'in', user.allowed_crm_salesperson_ids.ids)]
     ```
     Optional (for opportunities only):
     ```
     [('type', '=', 'opportunity'), ('user_id', 'in', user.allowed_crm_salesperson_ids.ids)]
     ```
5. For the target user:
   - Go to their form → Access Rights tab → add only the new restricted group (remove broader CRM groups)
   - Go to new **"CRM Access Restrictions"** tab → select the specific salespeople they should see

## Usage
- The restricted user will now only see opportunities assigned to the selected salespeople in the Pipeline.
- To change who they can see: simply edit the user and update the Many2many field. Changes take effect immediately.
- If the allowed list is empty, the user sees nothing (safe default).

## Notes
- This module provides the configuration field and view. The security group + record rule are created manually in the UI so you have full control and can name them to match your existing groups.
- Test thoroughly in an incognito window with the restricted user.
- You may need to grant additional Read access on related models (res.partner, etc.) as you test the Kanban/list views.
- Compatible with Odoo 19 Community.

## Author
Patrick Seeman

## License
LGPL-3
