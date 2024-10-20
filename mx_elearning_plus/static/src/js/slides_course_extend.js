odoo.define('mx_elearning_plus.course_extended', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');
    
    publicWidget.registry.websiteCourseExtended = publicWidget.Widget.extend({
        selector: '.o_course_extended',

        /**
         * @override
         */
        start: function () {
            var self = this; // تخزين السياق

            this.$el.on('click', '#collapse_div', function () {
                var id = this.dataset.target.split('-')[1];
                var $slide = $('#slide-' + id);
                var $icon = $(this).find('i'); // العثور على الأيقونة داخل العنصر

                if ($slide.hasClass('show')) {
                    $icon.removeClass('fa-minus').addClass('fa-plus');
                } else {
                    $icon.removeClass('fa-plus').addClass('fa-minus');
                }
            });
        }
    });
});
