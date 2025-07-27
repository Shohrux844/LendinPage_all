$(document).ready(function () {
    /* scroll */
    $('.toform').click(function () {
        $("html, body").animate({scrollTop: $(".form").offset().top}, 1000);
        return false;
    });


    /* set price */
    $('[name="country"]').on('change', function () {
        var geoKey = $(this).find('option:selected').val();
        var data = $jsonData.prices[geoKey];
        var price = data.price;
        var oldPrice = data.old_price;
        var currency = data.currency;
        $("[value = " + geoKey + "]").attr("selected", true).siblings().attr('selected', false);

        $('.price_land_s1').text(price);
        $('.price_land_s2').text(oldPrice);
        $('.price_land_curr').text(currency);
    });

    initializeClock('timer1', getDayEnd());
    initializeClock('timer2', getDayEnd());
});
