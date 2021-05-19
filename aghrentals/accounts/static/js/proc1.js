console.log("hello");
var userbykCnt = document.querySelector(
  ".userOrders .orderDetails .bike .cnt"
).textContent;
var usercarCnt = document.querySelector(
  ".userOrders .orderDetails .car .cnt"
).textContent;
var usercamCnt = document.querySelector(
  ".userOrders .orderDetails .camera .cnt"
).textContent;

// Total Order Details
var totalbykCnt = document.querySelector(
  ".totalOrders .orderDetails .bike .cnt"
).textContent;
var totalcarCnt = document.querySelector(
  ".totalOrders .orderDetails .car .cnt"
).textContent;
var totalcamCnt = document.querySelector(
  ".totalOrders .orderDetails .camera .cnt"
).textContent;

const userData = {
  labels: ["Bikes", "Cars", "Camera"],
  datasets: [
    {
      label: "Your Orders",
      data: [userbykCnt, usercarCnt, usercamCnt],
      backgroundColor: [
        "rgb(255, 99, 132)",
        "rgb(54, 162, 235)",
        "rgb(255, 205, 86)",
      ],
      hoverOffset: 4,
    },
  ],
};

const totalData = {
  labels: ["Bikes", "Cars", "Camera"],
  datasets: [
    {
      label: "Your Orders",
      data: [totalbykCnt, totalcarCnt, totalcamCnt],
      backgroundColor: [
        "rgb(255, 99, 132)",
        "rgb(54, 162, 235)",
        "rgb(255, 205, 86)",
      ],
      hoverOffset: 4,
    },
  ],
};

const config1 = {
  type: "doughnut",
  data: userData,
};

const config2 = {
  type: "doughnut",
  data: totalData,
};

var ctx1 = document.getElementById("myChart1").getContext("2d");
var ctx2 = document.getElementById("myChart2").getContext("2d");
var myChart = new Chart(ctx1, config1);
var myChart = new Chart(ctx2, config2);
