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