
    let currentPage = 1;
    let totalPages = 1;
    let error = document.getElementById('error')

    const search_form = document.getElementById('user-select-form')
    document.addEventListener("DOMContentLoaded", () => {
        fetchUsers(1); // 1페이지부터 시작
    });

    // #fetchUser (pagination)
    function fetchUsers(page) {
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
                    data.stores.forEach(store => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${store.id || ''}</td>
                            <td>${store.type || ''}</td>
                            <td>${store.name || ''}</td>
                            <td>${store.address || ''}</td>
        
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
            })
            .catch(error => {
                console.log('error : ', error)
            });
    }
   // #updatePaginationControls
    function updatePaginationControls() {
        const pageNumbersDiv = document.getElementById('page-numbers');
        pageNumbersDiv.innerHTML = '';
        const pageNumbers = generatePageNumbers(currentPage, totalPages);
        
        pageNumbers.forEach(item => {
            if (item === '...') {
                const ellipsis = document.createElement('span');
                ellipsis.textContent = '...';
                ellipsis.className = 'page-ellipsis';
                pageNumbersDiv.appendChild(ellipsis);
            } else {
                const pageBtn = document.createElement('button');
                pageBtn.textContent = item;
                pageBtn.className = 'page-number';
                
                if (item === currentPage) {
                    pageBtn.classList.add('active');
                    pageBtn.disabled = true;
                } else {
                    pageBtn.onclick = () => fetchUsers(item);
                }
                
                pageNumbersDiv.appendChild(pageBtn);
            }
        });
    }
    // #generatePageNumbers
    function generatePageNumbers(current, total) {
        const delta = 2; // 현재 페이지 주변에 보여줄 페이지 수
        const range = [];
        const rangeWithDots = [];

        // 총 페이지가 7개 이하면 모두 표시
        if (total <= 7) {
            for (let i = 1; i <= total; i++) {
                range.push(i);
            }
            return range;
        }

        // 시작과 끝 페이지 계산
        const start = Math.max(1, current - delta);
        const end = Math.min(total, current + delta);

        // 첫 페이지 추가
        if (start > 1) {
            range.push(1);
            if (start > 2) {
                range.push('...');
            }
        }

        // 현재 페이지 주변 페이지들 추가
        for (let i = start; i <= end; i++) {
            range.push(i);
        }

        // 마지막 페이지 추가
        if (end < total) {
            if (end < total - 1) {
                range.push('...');
            }
            range.push(total);
        }

        return range;
    }

   