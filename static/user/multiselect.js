$(function () {
    opts = $('#optlist option').map(function () {
        return [[this.value, $(this).text()]];
    });
    opts1 = $('#optlist1 option').map(function () {
        return [[this.value, $(this).text()]];
    });



    $('#someinput').keyup(function () {

        var rxp = new RegExp($('#someinput').val(), 'i');
        var optlist = $('#optlist').empty();
        opts.each(function () {
            if (rxp.test(this[1])) {
                optlist.append($('<option/>').attr('value', this[0]).text(this[1]));
            } else{
                optlist.append($('<option/>').attr('value', this[0]).text(this[1]).addClass("hidden"));
            }
        });
        $(".hidden").toggleOption(false);

    });
        $('#someinput1').keyup(function () {

        var rxp = new RegExp($('#someinput1').val(), 'i');
        var optlist = $('#optlist1').empty();
        opts1.each(function () {
            if (rxp.test(this[1])) {
                optlist.append($('<option/>').attr('value', this[0]).text(this[1]));
            } else{
                optlist.append($('<option/>').attr('value', this[0]).text(this[1]).addClass("hidden"));
            }
        });
        $(".hidden").toggleOption(false);

    });
    $('.select-cities').click(function () {
        $('.select-cities option:selected').remove().appendTo('.chosen-cities');
        opts = $('#optlist option').map(function () {
            return [[this.value, $(this).text()]];
        });
        opts1 = $('#optlist1 option').map(function () {
        return [[this.value, $(this).text()]];
    });
    });

    $('.chosen-cities').click(function () {
        $('.chosen-cities option:selected').remove().appendTo('.select-cities');
        opts = $('#optlist option').map(function () {
            return [[this.value, $(this).text()]];
        });
        opts1 = $('#optlist1 option').map(function () {
        return [[this.value, $(this).text()]];
    });
    });


});

jQuery.fn.toggleOption = function( show ) {
    jQuery( this ).toggle( show );
    if( show ) {
        if( jQuery( this ).parent( 'span.toggleOption' ).length )
            jQuery( this ).unwrap( );
    } else {
        if( jQuery( this ).parent( 'span.toggleOption' ).length == 0 )
            jQuery( this ).wrap( '<span class="toggleOption" style="display: none;" />' );
    }
};