$(document).ready(function() {
    $('#search-button').on('click', function() {
        let productName = $('#product-name').val().trim();
        if (productName) {
            $.get(`/api/search?name=${productName}`, function(prices) {
                if (prices.message) {
                    $('#prices').html(`<div class="alert alert-danger">${prices.message}</div>`);
                } else {
                    let pricesHtml = '<h2>Prices</h2><ul class="list-group">';
                    prices.forEach(function(price) {
                        pricesHtml += `<li class="list-group-item">${price.store}: $${price.price} (updated at ${price.updated_at})</li>`;
                    });
                    pricesHtml += '</ul>';
                    $('#prices').html(pricesHtml);
                }
            }).fail(function() {
                $('#prices').html('<div class="alert alert-danger">Error fetching data</div>');
            });
        }
    });
});
