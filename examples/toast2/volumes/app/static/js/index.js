$(function() {
    $('#info').click(() => {
        $.ajax({
            url: '/info',
            type: 'POST',
        });
    });
    $('#success').click(() => {
        $.ajax({
            url: '/success',
            type: 'POST',
        });
    });
    $('#warning').click(() => {
        $.ajax({
            url: '/warning',
            type: 'POST',
        });
    });
    $('#error').click(() => {
        $.ajax({
            url: '/error',
            type: 'POST',
        });
    });
});