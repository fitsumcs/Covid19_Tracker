const form = document.getElementById("myform");
const countries = document.getElementById("countries");

form.addEventListener('submit', resetSelect);

function resetSelect(e) {
    // e.preventDefault();
    var x = countries.value;
    countries.value = x;
}