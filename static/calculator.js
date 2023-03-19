let current_number = "";
let calc_array = [];

function updateDisplay(number) {
    current_number += number;
    document.getElementById("output").innerHTML = current_number;
}

function clearData() {
    calc_array = []
    current_number = "";
    document.getElementById("output").innerHTML = "0";
}

function appendToArray(operator) {
    calc_array.push(parseFloat(current_number));
    calc_array.push(operator);
    current_number = "";
}

function sendCalculation() {
    calc_array.push(parseFloat(current_number));
    $.ajax({
        url: '/calculate',
        type: 'POST',
        data: JSON.stringify(calc_array),
        contentType: 'application/json',
        success: function (response) {
            document.getElementById("output").innerHTML = response;
            calc_array = [];
        }
    });
}
