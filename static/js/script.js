// Optional JavaScript code for interactions and dynamic effects
document.addEventListener("DOMContentLoaded", function () {
    // Example: Animate elements on scroll or add more effects
    let elements = document.querySelectorAll('.animate-on-scroll');
    window.addEventListener('scroll', function () {
        elements.forEach(function (el) {
            let position = el.getBoundingClientRect().top;
            if (position < window.innerHeight) {
                el.classList.add('visible');
            }
        });
    });

    // // Step 1: Add an event listener for form submission to display the prediction as a popup
    // const form = document.querySelector('form');
    // form.addEventListener('submit', async function (event) {
    //     event.preventDefault(); // Prevent default form submission

    //     const formData = new FormData(form);

    //     try {
    //         const response = await fetch(form.action, {
    //             method: form.method,
    //             body: formData
    //         });

    //         if (!response.ok) {
    //             throw new Error('Failed to fetch prediction');
    //         }

    //         const result = await response.json();
    //         alert(result.prediction_text); // Display the prediction result in a popup
    //     } catch (error) {
    //         alert('An error occurred: ' + error.message); // Display error in a popup
    //     }
    // });
});



