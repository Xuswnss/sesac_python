document.addEventListener('DOMContentLoaded',()=>{
    const storeInfo = document.getElementById('store-info')
    const storeId = storeInfo.dataset.storeId
    console.log('storeId : ', storeId)
    fetchStoreDetail(storeId)
    fetchStoreData(storeId)
    // fetchCustomerList(storeId)??
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

function fetchStoreData(store_id, month = '') {
    // 1️⃣ 매출 데이터 URL 구성
    let salesUrl = `/stores/api/get-store-month-sales/${store_id}`;
    if (month) {
        salesUrl += `?month=${encodeURIComponent(month)}`;
    }
    console.log('[매출] month :', month);

    fetch(salesUrl)
        .then(res => res.json())
        .then(data => {
            console.log('get-data-Month_sales : ', data);
            const resultDiv = document.getElementById('sales-result');
            resultDiv.innerHTML = '';

            if (data && data.length > 0) {
                data.forEach(e => {
                    const row = document.createElement('tr');

                    let dateDisplay = e.date || '';
                    let dateLink = '';
                    if (!month) {
                        dateLink = `<a href="#" data-month="${dateDisplay}">${dateDisplay}</a>`;
                    } else {
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
                            fetchStoreData(store_id, selectedMonth); // ✅ 같은 month로 재호출
                        });
                    });
                }
            }
        });

    // 2️⃣ 고객 목록 URL 구성
    let customerUrl = `/stores/api/get-customer-list/${store_id}`;
    if (month) {
        customerUrl += `?month=${encodeURIComponent(month)}`;
    }

    console.log('[고객] month:', month);
    console.log('[고객] 요청 URL:', customerUrl);

    fetch(customerUrl)
        .then(res => res.json())
        .then(data => {
             
            console.log('고객 목록:', data);
            const resultDiv = document.getElementById('customer-result');
            resultDiv.innerHTML = '';

            if (data && data.length > 0) {
                data.sort((a, b) => b.frequency - a.frequency);

                data.forEach(c => {
                    const row = document.createElement('tr');
                   
                    row.innerHTML = `
                        <td><a href="/users/user-detail/${c.user_id||''}">${c.user_id||''}</a></td>
                        <td>${c.name}</td>
                        <td>${c.frequency}</td>
                    `;
                    resultDiv.append(row);
                });
            } else {
                resultDiv.innerHTML = '<tr><td colspan="3">해당 월에 고객이 없습니다.</td></tr>';
            }
        });
}
