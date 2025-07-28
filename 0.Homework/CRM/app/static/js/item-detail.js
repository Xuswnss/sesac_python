

document.addEventListener("DOMContentLoaded",()=>{
      const itemInfo = document.getElementById('item-info')
    const itemId = itemInfo.dataset.itemId
    console.log('itemId : ', itemId)
    fetchItems(itemId)
    fetchMonthSales(itemId)

})

function fetchItems(item_id){
    fetch(`/items/api/get-item-detail/${item_id}`)
        .then(res=>res.json())
        .then(data => {
            const resultDiv = document.getElementById('item-result')
            resultDiv.innerHTML = ''   
            console.log(data)
            console.log(data[0])
            data = data[0]
            if(data){
    
                const row = document.createElement('tr')
                
                row.innerHTML = `
                            <td>${data.name || ''}</td>
                            <td>${data.unit_price || ''}</td>
                `
                resultDiv.appendChild(row)
                
            }else{
                 const row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
            }


     
        }
    
    )
}

function fetchMonthSales(item_id){
    fetch(`/items/api/get-months-sales-data/${item_id}`)
        .then(res => res.json())
        .then(data =>{
            console.log('get-data-Month_sales : ', data)
            const resultDiv = document.getElementById('sales-result')
            resultDiv.innerHTML = ''
            if(data){
                renderMonthSalesChart(data)
                data.forEach(e => {
                    const row = document.createElement('tr')
                    row.innerHTML = `
                        <td>${e.date}</td>
                        <td>${e.total_revenue}</td>
                        <td>${e.count}</td>`

                    
                    resultDiv.append(row)
                    
                });
            }
        })
}

function renderMonthSalesChart(data){
    const labels = data.map(e => e.date);
    const revenues = data.map(e => e.total_revenue);
    const counts = data.map(e => e.count);

    const ctx = document.getElementById('monthSalesChart').getContext('2d');



    // 중복 방지
    if(window.monthSalesChartInstance){
        window.monthSalesChartInstance.destroy();
    }

    window.monthSalesChartInstance = new Chart(ctx, {
        data: {
            labels: labels,
            datasets: [
                {
                    type: 'bar',
                    label: 'Item Count',
                    data: counts,
                    backgroundColor: 'rgba(30, 0, 255, 0.8)',
                    yAxisID: 'y2'
                },
                {
                    type: 'line',
                    label: 'Total Revenue',
                    data: revenues,
                    borderColor: 'rgba(60, 252, 46, 0.9)',
                    backgroundColor: 'rgba(30, 144, 255, 0.3)',
                    fill: false,
                    yAxisID: 'y1'
                }
            ]
        },
        options: {
            responsive: false,
            interaction: { mode: 'index', intersect: false },
            plugins: {
                title: {
                    display: true,
                    text: '월별 매출액 그래프'
                }
            },
            scales: {
                y1: {
                    type: 'linear',
                    position: 'left',
                    title: { display: true, text: '매출액' }
                },
                y2: {
                    type: 'linear',
                    position: 'right',
                    grid: { drawOnChartArea: false },
                    title: { display: true, text: '아이템 개수' }
                }
            }
        }
    });
}

