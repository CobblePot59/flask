$(function() {
    $('#gbutton').click(() => {
        $.ajax({
            url: '/data',
            type: 'GET',
            data: {
                'gbutton_key': $('#gbutton').text()
            },
            datatype: 'json',
            success: function(response){
                alert(response)
            }
        });
        // console.log($('#gbutton')[0].innerText);
    });
    $('#pbutton').click(() => {
        $.ajax({
            url: '/data',
            type: 'POST',
            data: {
                'pbutton_key' : $('#pbutton').text()
            },
            datatype: 'json',
            success: function(response){
                alert(response)
            }
        });
        // console.log($('#pbutton')[0].innerText);
    });
});