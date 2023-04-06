
var chartColors = {
  red: 'rgb(255, 99, 132)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  info: '#41B1F9',
  blue: '#3245D1',
  purple: 'rgb(153, 102, 255)',
  grey: '#EBEFF6'
};

var config1 = {
  type: "line",
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Balance",
        backgroundColor: "#fff",
        borderColor: "#fff",
        data: [20, 40, 20, 70, 10, 50, 20],
        fill: false,
        pointBorderWidth: 100,
        pointBorderColor: "transparent",
        pointRadius: 3,
        pointBackgroundColor: "transparent",
        pointHoverBackgroundColor: "rgba(63,82,227,1)",
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false, 
    layout: {
      padding: {
        left: -10,
        top: 10,
      },
    },
    legend: {
      display: false,
    },
    title: {
      display: false,
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    scales: {
      xAxes: [
        {
          gridLines: {
            drawBorder: false,
            display: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
      yAxes: [
        {
          gridLines: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
    },
  },
};
var config2 = {
  type: "line",
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Revenue",
        backgroundColor: "#fff",
        borderColor: "#fff",
        data: [20, 800, 300, 400, 10, 50, 20],
        fill: false,
        pointBorderWidth: 100,
        pointBorderColor: "transparent",
        pointRadius: 3,
        pointBackgroundColor: "transparent",
        pointHoverBackgroundColor: "rgba(63,82,227,1)",
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: -10,
        top: 10,
      },
    },
    legend: {
      display: false,
    },
    title: {
      display: false,
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    scales: {
      xAxes: [
        {
          gridLines: {
            drawBorder: false,
            display: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
      yAxes: [
        {
          gridLines: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
    },
  },
};
var config3 = {
  type: "line",
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Orders",
        backgroundColor: "#fff",
        borderColor: "#fff",
        data: [20, 40, 20, 200, 10, 540, 723],
        fill: false,
        pointBorderWidth: 100,
        pointBorderColor: "transparent",
        pointRadius: 3,
        pointBackgroundColor: "transparent",
        pointHoverBackgroundColor: "rgba(63,82,227,1)",
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: -10,
        top: 10,
      },
    },
    legend: {
      display: false,
    },
    title: {
      display: false,
      text: "Chart.js Line Chart",
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    scales: {
      xAxes: [
        {
          gridLines: {
            drawBorder: false,
            display: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
      yAxes: [
        {
          gridLines: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
    },
  },
};
var config4 = {
  type: "line",
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "My First dataset",
        backgroundColor: "#fff",
        borderColor: "#fff",
        data: [20, 40, 20, 70, 10, 5, 23],
        fill: false,
        pointBorderWidth: 100,
        pointBorderColor: "transparent",
        pointRadius: 3,
        pointBackgroundColor: "transparent",
        pointHoverBackgroundColor: "rgba(63,82,227,1)",
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false, 
    layout: {
      padding: {
        left: -10,
        top: 10,
      },
    },
    legend: {
      display: false,
    },
    title: {
      display: false,
      text: "Chart.js Line Chart",
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    scales: {
      xAxes: [
        {
          gridLines: {
            drawBorder: false,
            display: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
      yAxes: [
        {
          gridLines: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            display: false,
          },
        },
      ],
    },
  },
};

var randomScalingFactor = function() {
  return (Math.random() > 0.5 ? 1.0 : 1.0) * Math.round(Math.random() * 100);
};