

document.addEventListener("DOMContentLoaded",()=>{
    fetchOrderItem(1)
})

function fetchOrderItem(page){
    fetch(`/orderitems/api/get-orderitems?page=${page}&per_page=10`)
        .then(res=>res.json())
        .then(data => {
            const resultDiv = document.getElementById('result')
            resultDiv.innerHTML = '' 
        
            console.log(data)
            if(data){
                data.orderitems.slice(1).forEach( orderitem => {
                const row = document.createElement('tr')
                row.innerHTML = `
                            <td>${orderitem.id || ''}</td>
                            <td><a href = '/orders/order-detail/${orderitem.order_id || ''}'>${orderitem.order_id || ''}</a></td>
                            <td><a href='/items/item-detail/${orderitem.item_id || ''}'>${orderitem.item_id || ''}</a></td>
                `
                resultDiv.appendChild(row)
                })
            }else{
                 const row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
            }


           currentPage = data.page;
                totalPages = data.pages;
                console.log('current-Page :' , data.page, 'total Page:', data.pages)
              updatePaginationControls(); 
              updatePageInfo()    


        }
    
    )
}

 
    function updatePaginationControls() {
    const paginationContainer = document.getElementById('page-numbers');
    paginationContainer.innerHTML = '';
    
    const prevBtn = document.createElement('button');
    prevBtn.innerHTML = '&laquo;';
    prevBtn.className = 'page-btn prev-btn';
    prevBtn.disabled = currentPage === 1;
    if (currentPage > 1) {
        prevBtn.onclick = () => fetchOrderItem(currentPage - 1);
    }
    paginationContainer.appendChild(prevBtn);
    
    
    const pageNumbers = generatePageNumbers(currentPage, totalPages);
    pageNumbers.forEach(pageNum => {
        const pageBtn = document.createElement('button');
        pageBtn.innerHTML = pageNum;
        pageBtn.className = 'page-btn';
        
        if (pageNum === currentPage) {
            
            pageBtn.style.color = 'red';
        } else {
            pageBtn.onclick = () => fetchOrderItem(pageNum);
        }
        
        paginationContainer.appendChild(pageBtn);
    });
    
    // 다음 버튼
    const nextBtn = document.createElement('button');
    nextBtn.innerHTML = '&raquo;';
    nextBtn.className = 'page-btn next-btn';
    nextBtn.disabled = currentPage === totalPages ;
    if (currentPage < totalPages) {
        nextBtn.onclick = () => fetchOrderItem(currentPage + 1);
    }
    paginationContainer.appendChild(nextBtn);
}

// 페이지 번호 생성
function generatePageNumbers(current, total) {
    const pages = [];
    const maxVisible = 11;
        pages.push(1);
        
        const halfVisible = Math.floor((maxVisible - 2) / 2); // 첫/마지막 페이지 제외한 가운데 영역
        let start = Math.max(2, current - halfVisible);
        let end = Math.min(total - 1, current + halfVisible);
        
        
        const middleCount = maxVisible - 2;
        if (end - start + 1 < middleCount) {
            if (start === 2) {
                end = Math.min(total - 1, start + middleCount - 1);
            } else if (end === total - 1) {
                start = Math.max(2, end - middleCount + 1);
            }
        }
        
        // 가운데 페이지들 추가
        for (let i = start; i <= end -1; i++) {
            if (i !== 1 && i !== total && !pages.includes(i)) {
                pages.push(i);
            }
        }
        

        if (total -1 > 1) {
            pages.push(total -1);
        }
    
    
    return pages;
}

// 페이지 정보 표시
function updatePageInfo() {
    const pageInfo = document.getElementById('page-info');
    if (pageInfo) {    
        pageInfo.innerHTML = `${currentPage} / ${totalPages }`;

    }
}

