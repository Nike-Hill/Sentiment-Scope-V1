/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function showLoader() {
  document.getElementById("loader").style.display = "block";
  document.getElementById("spinner").style.display = "block";
}

document.querySelectorAll('.team-member').forEach(member => {
  member.addEventListener('click', () => {
    const target = member.dataset.target;
    document.getElementById(target).scrollIntoView({ behavior: 'smooth' });
  });
});