# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    require_attachment = fields.Boolean(string='Require Attachment', config_parameter='purchase_attachments.require_attachment')

