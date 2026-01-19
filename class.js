// Form events - allows to validate and prevent before submition using js

const handleSubmit = (event) => {
    event.preventDefault()
    console.log("Form Submitted")
}

const form = document.querySelector('form')
form.addEventListener('submit', handleSubmit)

