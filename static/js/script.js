document.getElementById('addiction-form').addEventListener('submit', function(event) {
    var form = event.target;
    var isValid = true;

    // Validate each form field
    for (var i = 0; i < form.elements.length; i++) {
        var element = form.elements[i];

        if (element.type !== "submit" && element.value.trim() === "") {
            alert("Please fill in all fields.");
            isValid = false;
            break;
        }

    }

    if (!isValid) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
