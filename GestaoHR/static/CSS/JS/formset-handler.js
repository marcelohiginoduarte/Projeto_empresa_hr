document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function() {
        const extraForms = document.querySelectorAll('.form-row[data-new="true"]');
        extraForms.forEach(form => form.remove());
    });
});