function poweron() {
    $('a#process_input').bind('click', function() {
    $.getJSON('/background_process', {
    power: "on"
    });
    return false;
    });
};
