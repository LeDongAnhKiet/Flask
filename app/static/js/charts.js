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
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
function RevStats(labels, data) {
    const ctx = document.getElementById('revStats');
//    const rndNum = () => Math.floor(Math.random() * (255 - 50 + 1) + 50);
//    const rndRGBA = () => `rgba(${rndNum()}, ${rndNum()}, ${rndNum()}, 0.7)`;
    new Chart (ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Doanh thu',
                data: data,
                borderWidth: 1,
                backgroundColor: ['red', 'blue', 'green']
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}