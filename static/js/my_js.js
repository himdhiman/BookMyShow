function watchTrailer(name, url) {
    var html1 = '<iframe width="1165" height="545" src="' + url + '" frameborder="0" allowfullscreen></iframe>';
    $(document).ready(function() {
        $('<div />').html(html1).dialog({
            resizable: false,
            height: 600,
            title: name,
            width: 1200,
            modal: true,
            close: function() { $(this).remove(); }
        });
    });
}