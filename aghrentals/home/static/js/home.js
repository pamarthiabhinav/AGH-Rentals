const html = document.querySelector("html");
const mode = document.querySelector(".mode");

const yearObj = document.querySelector("#yearObj");
var d = new Date();
yearObj.innerHTML = d.getFullYear();

html.dataset.theme = localStorage.getItem("mode");
if (html.dataset.theme === "dark") {
  mode.classList.add("dark");
} else {
  mode.classList.remove("dark");
}

mode.addEventListener("click", function () {
  mode.classList.toggle("dark");
  if (html.dataset.theme === "dark") {
    localStorage.setItem("mode", "light");
    html.dataset.theme = `light`;
  } else {
    localStorage.setItem("mode", "dark");
    html.dataset.theme = `dark`;
  }
});

function myValidate() {
  var email = document.f.email;
  var mobile = document.f.mobile;
  var count = 0;
  var mailformat =
    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  var mobileformat = /^\d{10}$/;
  if (!email.getAttribute("disabled")) {
    if (email.value.match(mailformat)) {
      email.classList.remove("invalidFormat");
    } else {
      email.classList.add("invalidFormat");
      count++;
    }
  }
  if (mobile.value.match(mobileformat)) {
    mobile.classList.remove("invalidFormat");
  } else {
    mobile.classList.add("invalidFormat");
    count++;
  }
  if (count > 0) {
    return false;
  } else {
    return true;
  }
}
