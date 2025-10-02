document.addEventListener("DOMContentLoaded", () => {
  const profileMenu = document.querySelector(".profile-menu");

  // Cuando haces clic en el icono del perfil
  profileMenu.addEventListener("click", () => {
    profileMenu.classList.toggle("active");
  });

  // Cuando haces clic fuera, se cierra el menú
  document.addEventListener("click", (e) => {
    if (!profileMenu.contains(e.target)) {
      profileMenu.classList.remove("active");
    }
  });
});
// Gráfico de barras
const ctxBar = document.getElementById('barChart');
new Chart(ctxBar, {
  type: 'bar',
  data: {
    labels: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    datasets: [{
      label: 'Últimos 6 días',
      data: [5, 7, 6, 8, 10, 9, 8, 7, 6, 8, 7, 9],
      backgroundColor: '#4c6fff'
    }, {
      label: 'Última semana',
      data: [4, 6, 5, 7, 8, 7, 6, 6, 5, 7, 6, 7],
      backgroundColor: '#d9d9d9'
    }]
  },
  options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
});

// Gráfico de donut
const ctxDonut = document.getElementById('donutChart');
new Chart(ctxDonut, {
  type: 'doughnut',
  data: {
    labels: ['Tarde 40%', 'Noche 32%', 'Mañana 28%'],
    datasets: [{
      data: [40, 32, 28],
      backgroundColor: ['#4c6fff', '#7a74f5', '#38c3e8']
    }]
  },
  options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
});

// Gráfico de línea
const ctxLine = document.getElementById('lineChart');
new Chart(ctxLine, {
  type: 'line',
  data: {
    labels: ['01', '02', '03', '04', '05', '06'],
    datasets: [{
      label: 'Últimos 6 días',
      data: [3, 4, 6, 5, 7, 6],
      borderColor: '#4c6fff',
      fill: false,
      tension: 0.4
    }, {
      label: 'Última semana',
      data: [4, 3, 5, 6, 5, 7],
      borderColor: '#d9d9d9',
      fill: false,
      tension: 0.4
    }]
  },
  options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
});
