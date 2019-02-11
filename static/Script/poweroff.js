function poweroff() {
    $.getJSON('/background_process', {
    power: "off"
    });
    return false;
};
