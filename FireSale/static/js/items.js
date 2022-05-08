$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault()
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/shop?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    return '<div class="well item">' +
                        '<a href="/shop/${d.id}"></a>' +
                        '<img class="item-img" src="${d.image}"/>' +
                        '<h4>${d.name}</h4>' +
                        '</div>'
                });
                $('.products').html(newHTML.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});