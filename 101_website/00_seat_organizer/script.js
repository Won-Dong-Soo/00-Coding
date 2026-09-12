let currentShuffle = [];

function generateTable() {
  const start = parseInt(document.getElementById("start").value);
  const end = parseInt(document.getElementById("end").value);
  const rows = parseInt(document.getElementById("rows").value);
  const cols = parseInt(document.getElementById("cols").value);

  if (isNaN(start) || isNaN(end) || start > end) {
    alert("번호 범위를 올바르게 입력하세요!");
    return;
  }

  // 번호 배열 생성
  const numbers = [];
  for (let i = start; i <= end; i++) numbers.push(i);

  if (numbers.length > rows * cols) {
    alert("자리가 부족합니다!");
    return;
  }

  // 랜덤 섞기
  currentShuffle = numbers.sort(() => Math.random() - 0.5);

  renderTable(rows, cols);
}

function renderTable(rows, cols) {
  const table = document.createElement("table");
  let idx = 0;
  for (let r = 0; r < rows; r++) {
    const tr = document.createElement("tr");
    for (let c = 0; c < cols; c++) {
      const td = document.createElement("td");
      td.textContent = currentShuffle[idx] || "";
      tr.appendChild(td);
      idx++;
    }
    table.appendChild(tr);
  }

  const result = document.getElementById("result");
  result.innerHTML = "";
  result.appendChild(table);
}

document.getElementById("generate").addEventListener("click", generateTable);
document.getElementById("shuffle").addEventListener("click", () => {
  const rows = parseInt(document.getElementById("rows").value);
  const cols = parseInt(document.getElementById("cols").value);
  currentShuffle.sort(() => Math.random() - 0.5); // 다시 섞기
  renderTable(rows, cols);
});