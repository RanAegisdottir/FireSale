/* search shop item */
$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault()
        let searchText = $('#search-box').val();
        $.ajax({
            url: '/shop?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                let newHTML = resp.data.map(d => {
                    if (d.priceidea > d.heighestoffer){
                        price = d.priceidea;
                    }else {
                        price = d.heighestoffer;
                    }
                    return `<div class="product">
                            <a href="/shop/${ d.id }">
                            <img class="item-img" src="${ d.image }" alt="item-img"/>
                            <h4>${ d.name }</h4>                           
                            <p>$ ${price}</p>
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
    /* dropdown for filtering shop items */
    $('#answer-sort-dropdown-select-menu').on('change', function (e) {
        console.log(this.value)
        let value = this.value;
        e.preventDefault()
        $.ajax( {
            url: '/shop?order=' + value,
            type: 'GET',
            success: function (resp) {
                let newHTML = resp.data.map(d => {
                    if (d.priceidea > d.heighestoffer){
                        price = d.priceidea;
                    }else {
                        price = d.heighestoffer;
                    }
                    return `<div class="product">
                            <a href="/shop/${ d.id }">
                            <img class="item-img" src="${ d.image }" alt="item-img"/>
                            <h4>${ d.name }</h4>
                            <p>$ ${ price }</p>
                            </a>
                            </div>`
                });
                $('.products').html(newHTML.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});