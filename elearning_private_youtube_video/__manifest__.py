# -*- coding: utf-8 -*-
{
    'name': "elearning private youtube video",
    'summary': """elearning private youtube video""",
    'description': """
       elearning private youtube video
    """,
    'author': 'David Montero Crespo',
    'license': 'AGPL-3',
    'category': 'Website',
    'version': '15.0.1.0.0',
    'website': "https://softwareescarlata.com/",
    'depends': ['base', 'website_slides', 'web'],
    'images': ['static/description/imagen.jpg'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',  # إضافة ملف القوالب
    ],
    'assets': {
        'web.assets_frontend': [
            'elearning_private_youtube_video/static/scss/style.scss',
            'elearning_private_youtube_video/static/js/slides_course_fullscreen_player_video.js',
        ],
    },
    'currency': 'EUR',
    'price': 25,
    'installable': True,
    'application': False,
}
