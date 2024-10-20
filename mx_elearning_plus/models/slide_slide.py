# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class Slide(models.Model):
    _inherit = 'slide.slide'

    is_published = fields.Boolean(string='Published', default=False)

    def action_publish(self):
        self.write({'is_published': True})

    def action_unpublish(self):
        self.write({'is_published': False})
