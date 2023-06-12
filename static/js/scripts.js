const backgroundColor = "{{ background_color }}";
document.body.style.backgroundColor = backgroundColor;

// This script toggles a class on an HTML element using Flask and Jinja2

const element = document.getElementById("element-id");
element.addEventListener("click", function() {
  element.classList.toggle("class-name");
});


// This script enables smooth scrolling for anchor links using Flask and Jinja2

const links = document.querySelectorAll('a[href^="#"]');
for (const link of links) {
  link.addEventListener("click", function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth"
    });
  });
}


// This script shows or hides the password field using Flask and Jinja2

const passwordField = document.getElementById("password-field");
const showPassword = document.getElementById("show-password");

showPassword.addEventListener("change", function() {
  if (this.checked) {
    passwordField.type = "text";
  } else {
    passwordField.type = "password";
  }
});



// This script loads content dynamically using Flask and Jinja2

const contentContainer = document.getElementById("content-container");
const loadButton = document.getElementById("load-button");

loadButton.addEventListener("click", function() {
  fetch("{{ url_for('load_content') }}")
    .then(response => response.text())
    .then(data => {
      contentContainer.innerHTML = data;
    });
});


// This script performs client-side form validation using Flask and Jinja2

const form = document.getElementById("my-form");
const input = document.getElementById("my-input");

form.addEventListener("submit", function(e) {
  if (input.value === "") {
    e.preventDefault();
    alert("Please enter a value.");
  }
});

// This script creates an image gallery with a lightbox using Flask and Jinja2

const images = document.querySelectorAll(".gallery-image");
const lightbox = document.getElementById("lightbox");
const lightboxImage = document.getElementById("lightbox-image");

images.forEach(image => {
  image.addEventListener("click", function() {
    lightbox.style.display = "block";
    lightboxImage.src = this.src;
  });
});

lightbox.addEventListener("click", function() {
  lightbox.style.display = "none";
});


// This script creates a responsive navigation menu using Flask and Jinja2

const menuToggle = document.getElementById("menu-toggle");
const navMenu = document.getElementById("nav-menu");

menuToggle.addEventListener("click", function() {
  navMenu.classList.toggle("open");
});



// This script creates an automatic slideshow using Flask and Jinja2

const slides = document.querySelectorAll(".slide");
let currentSlide = 0;

function showSlide() {
  slides.forEach(slide => slide.style.display = "none");
  slides[currentSlide].style.display = "block";
  currentSlide = (currentSlide + 1) % slides.length;
}

setInterval(showSlide, 3000);



// This script creates a countdown timer using Flask and Jinja2

const countdown = document.getElementById("countdown");

function updateTimer() {
  const currentDate = new Date();
  const targetDate = new Date("{{ target_date }}");
  const remainingTime = targetDate - currentDate;

  const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
  const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

  countdown.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

setInterval(updateTimer, 1000);

// Add this code at the end of the JavaScript file

const selectFunction = document.getElementById("select-function");
const exampleContainer = document.getElementById("example-container");

selectFunction.addEventListener("change", function() {
  const selectedValue = this.value;

  // Clear the previous example
  exampleContainer.innerHTML = "";

  // Add the example based on the selected value
  switch (selectedValue) {
    case "1":
      // Example for Function 1: Dynamic Background Color
      exampleContainer.innerHTML = `<div style="width: 200px; height: 200px; background-color: yellow;"></div>`;
      break;
    case "2":
      // Example for Function 2: Toggle Class
      exampleContainer.innerHTML = `<button id="element-id" class="class-name">Toggle Class</button>`;
      break;
    case "3":
      // Example for Function 3: Smooth Scrolling
      exampleContainer.innerHTML = `<a href="#target-element">Scroll to Target</a>`;
      break;
    case "4":
      // Example for Function 4: Show/Hide Password
      exampleContainer.innerHTML = `
        <input type="password" id="password-field" />
        <label for="show-password">Show Password</label>
        <input type="checkbox" id="show-password" />
      `;
      break;
    case "5":
      // Example for Function 5: Dynamic Content Loading
      exampleContainer.innerHTML = `<button id="load-button">Load Content</button>`;
      break;
    case "6":
      // Example for Function 6: Client-side Form Validation
      exampleContainer.innerHTML = `
        <form id="my-form">
          <input type="text" id="my-input" />
          <button type="submit">Submit</button>
        </form>
      `;
      break;
    case "7":
      // Example for Function 7: Image Gallery with Lightbox
      exampleContainer.innerHTML = `
        <img class="gallery-image" src="example1.jpg" alt="Image 1" />
        <img class="gallery-image" src="example2.jpg" alt="Image 2" />
        <img class="gallery-image" src="example3.jpg" alt="Image 3" />
      `;
      break;
    default:
      break;
  }
});


