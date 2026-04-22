# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        demo = self.env['ir.config_parameter'].sudo().get_param('purchase_attachments.require_attachment')
        print(type(demo))
        if demo == 'True':
            print("button_confirm")
            po_attach = self.env['ir.attachment'].search([]).mapped('res_id')
            po_attach_name = self.env['ir.attachment'].search([('res_id','=',self.id)]).name
            print(po_attach_name)
            if po_attach_name.endswith("pdf") or po_attach_name.endswith("jpeg") or po_attach_name.endswith("png"):
                if self.id in po_attach:
                    self.write({'state': 'purchase'})
                else:
                    raise ValidationError("Add an attachment")
            else:
                raise ValidationError("Attachment should be a pdf or jpg")
        else:
            self.write({'state': 'purchase'})
