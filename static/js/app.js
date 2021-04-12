$(document).ready(function() {
    $('#countries').select2({
        placeholder: 'Select a Country',
        theme: "classic"
    });
});

// const text = document.getElementById("countries");
// const form = document.getElementById("myform");

// form.addEventListener('submit', checkEmpty)

// function checkEmpty(e) {
//     e.preventDefault();
//     var strUser = text.value;


//     if (strUser.length === 0) {
//         console.log(strUser);
//         alert("Enter Choice " + strUser)
//     }
// }