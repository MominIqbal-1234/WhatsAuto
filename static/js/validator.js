document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    console.log(form);

    form.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevents form submission to observe validation

        // Basic field validation
        const username = document.querySelector('input[name="username"]');
        const password = document.querySelector('input[name="password"]');
        const firstName = document.querySelector('input[name="first_name"]');
        const email = document.querySelector('input[name="email"]');
        const phoneNumber = document.querySelector('input[name="phone_number"]');
        const cnic = document.querySelector('input[name="cnic"]');
        const father_name = document.querySelector('input[name="father_name"]');
        const department = document.querySelector('input[name="department"]');
        const designation = document.querySelector('input[name="designation"]');
        const bio = document.querySelector('input[name="bio"]');
        const address = document.querySelector('input[name="address"]');
        const paymentsummary = document.querySelector('input[name="paymentsummary"]');
        const date_of_birth = document.querySelector('input[name="date_of_birth"]');
        const joining_date = document.querySelector('input[name="joining_date"]');
        
        let validationFailed = false;

        // Clear all previous invalid indicators
        document.querySelectorAll('.is-invalid').forEach(function(element) {
            element.classList.remove('is-invalid');
        });

        if (!username.value || !password.value || !firstName.value || !email.value) {
            // alert("Username, password, full name, and email are required.");
            [username, password, firstName,phoneNumber,joining_date,date_of_birth,paymentsummary,cnic,father_name,department,designation,bio,address].forEach(field => {
                if (!field.value) {
                    field.classList.add('is-invalid');
                }
            });
            validationFailed = true;
        }

        // Phone number validation (integer only)
        if (!/^\d+$/.test(phoneNumber.value)) {
            // alert("Phone number must be an integer.");
            phoneNumber.classList.add('is-invalid');
            validationFailed = true;
        }

        // CNIC validation (integer only)
        if (!/^\d+$/.test(cnic.value)) {
            // alert("CNIC must be an integer.");
            cnic.classList.add('is-invalid');
            validationFailed = true;
        }

        if (!validationFailed) {
            // Form is valid, submit it or do further processing
            console.log("Form is valid. Proceed with form submission or further processing.");
            // form.submit(); Uncomment this to allow the form to be submitted after validation
        }
    });
});
