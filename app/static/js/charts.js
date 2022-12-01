function CateStats(labels, data) {
    const ctx = document.getElementById('cateStats');
    new Chart (ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Số lượng',
                data: data,
                borderWidth: 1
            }]

        },
        option: {
            scale: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
function RevStats(labels, data) {
    const ctx = document.getElementById('revStats');
    new Chart (ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Doanh thu',
                data: data,
                borderWidth: 1
                backgroundColor: ['red', 'blue', 'green', 'orange', 'rgba(200, 100, 50, 0.5)']
            }]

        },
        option: {
            scale: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}