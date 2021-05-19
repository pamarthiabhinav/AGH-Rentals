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

function initFreshChat() {
  window.fcWidget.init({
    token: "cb42b721-f165-47bc-be86-6cd81f8b87d3",
    host: "https://wchat.in.freshchat.com",
  });
}
function initialize(i, t) {
  var e;
  i.getElementById(t)
    ? initFreshChat()
    : (((e = i.createElement("script")).id = t),
      (e.async = !0),
      (e.src = "https://wchat.in.freshchat.com/js/widget.js"),
      (e.onload = initFreshChat),
      i.head.appendChild(e));
}
function initiateCall() {
  initialize(document, "freshchat-js-sdk");
}
try {
  window.addEventListener
    ? window.addEventListener("load", initiateCall, !1)
    : window.attachEvent("load", initiateCall, !1);
} catch (error) {}
