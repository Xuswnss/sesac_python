
    let currentPage = 1;
    let totalPages = 1;
    let error = document.getElementById('error')

    const search_form = document.getElementById('user-select-form')
    document.addEventListener("DOMContentLoaded", () => {
        fetchStore(1); // 1페이지부터 시작
    });

    // #fetchUser (pagination)
    function fetchStore(page) {
        fetch(`/stores/api?page=${page}&per_page=10`)
            .then(res => {
                if (!res.ok) {
                    console.log(res.status)
                }
                return res.json();
            })
            .then(data => {
                const result = document.getElementById('result');
                result.innerHTML = ''; // 기존 내용 초기화

                if (data.stores && data.stores.length > 0) {
                    data.stores.slice(1).forEach(store => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td><a href ='/stores/store-detail/${store.id}'>${store.id || ''}</a></td>
                            <td>${store.type || ''}</td>
                            <td>${store.name || ''}</td>
                            <td>${store.address || ''}</td>
                            <td><a href='/stores/order-menu/${store.id}'>주문하러 가기</a></td>
        
                        `;
                        result.appendChild(row);
                    });
                } else {
                    const row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
                }

                currentPage = data.page;
                totalPages = data.pages;
                console.log('current-Page :' , data.page, 'total Page:', data.pages)
                
                updatePaginationControls();
                updatePageInfo()
            })
            .catch(error => {
                console.log('error : ', error)
            });
    }
   function updatePaginationControls() {
    const paginationContainer = document.getElementById('page-numbers');
    paginationContainer.innerHTML = '';
    
    const prevBtn = document.createElement('button');
    prevBtn.innerHTML = '&laquo;';
    prevBtn.className = 'page-btn prev-btn';
    prevBtn.disabled = currentPage === 1;
    if (currentPage > 1) {
        prevBtn.onclick = () => fetchStore(currentPage - 1);
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
            pageBtn.onclick = () => fetchStore(pageNum);
        }
        
        paginationContainer.appendChild(pageBtn);
    });
    
    // 다음 버튼
    const nextBtn = document.createElement('button');
    nextBtn.innerHTML = '&raquo;';
    nextBtn.className = 'page-btn next-btn';
    nextBtn.disabled = currentPage === totalPages ;
    if (currentPage < totalPages) {
        nextBtn.onclick = () => fetchStore(currentPage + 1);
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
        for (let i = start; i < end ; i++) {
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
        pageInfo.innerHTML = `${currentPage} / ${totalPages}`;

    }
}



