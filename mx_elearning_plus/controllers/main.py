# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request


class SlideController(http.Controller):

    @http.route('/website/publish/slide', type='json', auth="user", website=True)
    def publish(self, id):
        # التأكد من أن id صالح
        slide_id = request.env['slide.slide'].browse(id)
        if not slide_id.exists():
            return {'error': 'Slide not found'}

        # إعادة حالة النشر
        return {'published': bool(slide_id.website_published)}
