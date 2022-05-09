$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault()
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/shop?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                let newHTML = resp.data.map(d => {
                    return `<div class="product">
                            <a href="/shop/${ d.id }">
                            <img class="item-img" src="${ d.image }" />
                            <h4>${ d.name }</h4>
                            <p>$ ${ d.priceidea }</p>
                            </a>
                            </div>`
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