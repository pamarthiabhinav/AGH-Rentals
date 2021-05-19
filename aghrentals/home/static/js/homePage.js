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
