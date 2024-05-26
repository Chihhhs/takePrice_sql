$(document).ready(function() {
    $.get('/api/products', function(data) {
        let productsHtml = '<ul class="list-group">';
        data.forEach(function(product) {
            productsHtml += `<li class="list-group-item" data-id="${product.id}">${product.name} (${product.category})</li>`;
        });
        productsHtml += '</ul>';
        $('#products').html(productsHtml);
        
        $('.list-group-item').on('click', function() {
            let productId = $(this).data('id');
            $.get(`/api/prices/${productId}`, function(prices) {
                let pricesHtml = '<h2>Prices</h2><ul class="list-group">';
                prices.forEach(function(price) {
                    pricesHtml += `<li class="list-group-item">${price.store}: $${price.price} (updated at ${price.updated_at})</li>`;
                });
                pricesHtml += '</ul>';
                $('#prices').html(pricesHtml);
            });
        });
    });
});
