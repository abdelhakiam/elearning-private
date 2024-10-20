odoo.define('mx_elearning_plus.extended', function (require) {
    'use strict';

    var Fullscreen = require('@website_slides/js/slides_course_fullscreen_player');

    Fullscreen.include({
        _onChangeSlideRequest: function (ev) {
            this._super.apply(this, arguments);
            var slideData = ev.data;
            var $data = this.$el.prevObject.find('.js_publish_btn:visible').closest(".js_publish_management");

            this._rpc({
                route: '/website/publish/slide',
                params: {
                    id: slideData.id,
                },
            }).then(function (result) {
                if (result && result.published) {
                    $data.removeClass("css_unpublished").addClass("css_published");
                    $data.find('input').prop("checked", true);
                    $data.parents("[data-publish]").attr("data-publish", 'on');
                } else {
                    $data.removeClass("css_published").addClass("css_unpublished");
                    $data.find('input').prop("checked", false);
                    $data.parents("[data-publish]").attr("data-publish", 'off');
                }
            });
        }
    });
});
