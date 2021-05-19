// User Order Details
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

// Function For User Order Bar Graph
var chart1 = new Chartist.Pie(
  ".userOrderGraph",
  {
    series: [userbykCnt, usercarCnt, usercamCnt],
    labels: [userbykCnt, usercarCnt, usercamCnt],
    // labels: [1, 2, 3],
  },
  {
    donut: true,
    donutWidth: 65,
    showLabel: true,
  }
);

chart1.on("draw", function (data) {
  if (data.type === "slice") {
    // Get the total path length in order to use for dash array animation
    var pathLength = data.element._node.getTotalLength();

    // Set a dasharray that matches the path length as prerequisite to animate dashoffset
    data.element.attr({
      "stroke-dasharray": pathLength + "px " + pathLength + "px",
    });

    // Create animation definition while also assigning an ID to the animation for later sync usage
    var animationDefinition = {
      "stroke-dashoffset": {
        id: "anim" + data.index,
        dur: 1000,
        from: -pathLength + "px",
        to: "0px",
        easing: Chartist.Svg.Easing.easeOutQuint,
        // We need to use `fill: 'freeze'` otherwise our animation will fall back to initial (not visible)
        fill: "freeze",
        loop: false,
      },
    };

    // If this was not the first slice, we need to time the animation so that it uses the end sync event of the previous animation
    if (data.index !== 0) {
      animationDefinition["stroke-dashoffset"].begin =
        "anim" + (data.index - 1) + ".end";
    }

    // We need to set an initial value before the animation starts as we are not in guided mode which would do that for us
    data.element.attr({
      "stroke-dashoffset": -pathLength + "px",
    });

    // We can't use guided mode as the animations need to rely on setting begin manually
    // See http://gionkunz.github.io/chartist-js/api-documentation.html#chartistsvg-function-animate
    data.element.animate(animationDefinition, false);
  }
});

// For the sake of the example we update the chart every time it's created with a delay of 8 seconds
chart1.on("created", function () {
  if (window.__anim21278907124) {
    clearTimeout(window.__anim21278907124);
    window.__anim21278907124 = null;
  }
  window.__anim21278907124 = setTimeout(chart.update.bind(chart), 10000);
});

// Total Order Graph
var chart2 = new Chartist.Pie(
  ".totalOrderGraph",
  {
    series: [totalbykCnt, totalcarCnt, totalcamCnt],
    labels: [totalbykCnt, totalcarCnt, totalcamCnt],
    // labels: [1, 2, 3],
  },
  {
    donut: true,
    donutWidth: 80,
    showLabel: true,
  }
);

chart2.on("draw", function (data) {
  if (data.type === "slice") {
    // Get the total path length in order to use for dash array animation
    var pathLength = data.element._node.getTotalLength();

    // Set a dasharray that matches the path length as prerequisite to animate dashoffset
    data.element.attr({
      "stroke-dasharray": pathLength + "px " + pathLength + "px",
    });

    // Create animation definition while also assigning an ID to the animation for later sync usage
    var animationDefinition = {
      "stroke-dashoffset": {
        id: "anim" + data.index,
        dur: 1000,
        from: -pathLength + "px",
        to: "0px",
        easing: Chartist.Svg.Easing.easeOutQuint,
        // We need to use `fill: 'freeze'` otherwise our animation will fall back to initial (not visible)
        fill: "freeze",
        loop: false,
      },
    };

    // If this was not the first slice, we need to time the animation so that it uses the end sync event of the previous animation
    if (data.index !== 0) {
      animationDefinition["stroke-dashoffset"].begin =
        "anim" + (data.index - 1) + ".end";
    }

    // We need to set an initial value before the animation starts as we are not in guided mode which would do that for us
    data.element.attr({
      "stroke-dashoffset": -pathLength + "px",
    });

    // We can't use guided mode as the animations need to rely on setting begin manually
    // See http://gionkunz.github.io/chartist-js/api-documentation.html#chartistsvg-function-animate
    data.element.animate(animationDefinition, false);
  }
});

// For the sake of the example we update the chart every time it's created with a delay of 8 seconds
chart2.on("created", function () {
  if (window.__anim21278907124) {
    clearTimeout(window.__anim21278907124);
    window.__anim21278907124 = null;
  }
  window.__anim21278907124 = setTimeout(chart.update.bind(chart), 10000);
});
