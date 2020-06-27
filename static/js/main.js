function validateForm() {
    var x = document.forms["fform"]["fnumber"].value;
    if (x < 0) {
        alert("Numero debe ser mayor que cero")
        return false;
    }
};

document.getElementById("fsubmit").addEventListener("click", validateForm);