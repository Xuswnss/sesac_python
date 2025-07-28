document.addEventListener('DOMContentLoaded',()=>{
    const storeInfo = document.getElementById('store-info')
    const storeId = storeInfo.dataset.storeId
    console.log('storeId : ', storeId)
    fetchStoreDetail(storeId)
    fetchStoreMonthSales(storeId)
})

function fetchStoreDetail(store_id){
    fetch(`/stores/api/get-store-detail/${store_id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            const result = document.getElementById('store-result')
            result.innerHTML = ''
            if(data){
                data.forEach(item => {
                const row = document.createElement('tr')
                row.innerHTML = `
                   <td>${item.name || ''}</td>
                   <td>${item.type || ''}</td>
                   <td>${item.address || ''}</td>
                    `
                result.append(row)
                })
            }
        })
}// end fetchStoreDetail(store_id)

function fetchStoreMonthSales(store_id, month = '') {
    let url = `/stores/api/get-store-month-sales/${store_id}`;
    if (month) {
        url += `?month=${encodeURIComponent(month)}`;
    }

    fetch(url)
        .then(res => res.json())
        .then(data => {
            console.log('get-data-Month_sales : ', data);
            const resultDiv = document.getElementById('sales-result');
            resultDiv.innerHTML = '';

            if (data && data.length > 0) {
                data.forEach(e => {
                    const row = document.createElement('tr');

                    // month가 있으면 일별 데이터(YYYY-MM-DD), 없으면 월별 데이터(YYYY-MM)
                    // 클릭 시 다시 fetch 하려면 링크 설정
                    let dateDisplay = e.date || '';
                    let dateLink = '';
                    if (!month) {
                        // 월별 리스트: 클릭하면 해당 월 일별 데이터 요청
                        dateLink = `<a href="#" data-month="${dateDisplay}">${dateDisplay}</a>`;
                    } else {
                        // 일별 리스트: 클릭 시 동작 없거나 상세 페이지로 이동 가능
                        dateLink = dateDisplay;
                    }

                    row.innerHTML = `
                       <td>${dateLink}</td>
                       <td>${e.total_revenue}</td>
                       <td>${e.count}</td>
                    `;
                    resultDiv.append(row);
                });

                // 월별 리스트일 때만 클릭 이벤트 등록
                if (!month) {
                    resultDiv.querySelectorAll('a[data-month]').forEach(anchor => {
                        anchor.addEventListener('click', (e) => {
                            e.preventDefault();
                            const selectedMonth = e.target.dataset.month;
                            fetchStoreMonthSales(store_id, selectedMonth);
                        });
                    });
                }
            }
        });
}
