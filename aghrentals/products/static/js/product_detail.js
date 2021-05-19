function validate() {
  var bookdays = document.placeForm.bookDays;
  var inp2 = document.getElementById("input2");
  if (bookdays.value.length == 0) {
    inp2.classList.add("has-error");
    return false;
  }
  return true;
}

// var price = document.getElementById("price");
// price.addEventListener("click", function () {
//   var bookdays = document.placeForm.bookDays;
//   var inp2 = document.getElementById("input2");
//   var submitBtn = document.getElementById("submitBtn");
//   var orgPrice = document.getElementById("orgPrice");
//   if (bookdays.value.length != 0) {
//     // document.getElementById("original-price").innerHTML = orgPrice.textContent;
//     var tax = (orgPrice.textContent * 2) / 100;
//     var taxPrice = document.getElementById("tax-price");
//     taxPrice.innerHTML = tax;
//     var totPrice = parseInt(orgPrice.textContent) + parseInt(tax + 1);
//     document.getElementById("total-price").innerHTML = totPrice;
//     document.getElementById("full-price").innerHTML =
//       parseInt(bookdays.value) * totPrice * 24;
//     document.getElementById("discount").innerHTML =
//       (parseInt(document.getElementById("full-price").textContent) * 9) / 100;

//     document.getElementById("full-price-aft-disc").innerHTML =
//       parseInt(document.getElementById("full-price").textContent) -
//       parseInt(document.getElementById("discount").textContent);
//     price.style.display = "none";
//     submitBtn.style.display = "block";
//     document.getElementById("prices").style.display = "block";
//   } else {
//     inp2.classList.add("has-error");
//   }
// });
