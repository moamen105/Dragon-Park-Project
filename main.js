function maketable() {
  const table = document.createElement('table');
  table.classList.add('grid-table'); 
  const roww = document.createElement('tr');
  for (let i = 0; i < 26; i++) {
    const headd = document.createElement('th');
    headd.textContent = String.fromCharCode(65 + i);
    roww.appendChild(headd);
  }
  table.appendChild(roww);
  for (let i = 0; i < 16; i++) {
    const row = document.createElement('tr');
    for (let j = 0; j < 26; j++) {
      const data = document.createElement('td');
      data.textContent = `${String.fromCharCode(65 + j)}${i}`;
      data.classList.add('dataas');
      row.appendChild(data);
    }
    table.appendChild(row);
  }
  return table;
}
function checkColorsAndPrint() {
  const outt = document.querySelectorAll('.dataas');
  outt.forEach(data => {
    const color = getComputedStyle(data).backgroundColor;
    console.log(`data: ${data.textContent}, Color: ${color}`);
  });
  const currentDate = new Date();
  localStorage.setItem('lastCheckedDate', currentDate.toString());
}
function checkIfColorsShouldBeChecked() {
  const lastCheckedDate = localStorage.getItem('lastCheckedDate');
  if (lastCheckedDate) {
    const lastChecked = new Date(lastCheckedDate);
    const time = Math.abs(new Date() - lastChecked);
    const day = Math.ceil(time / (1000 * 60 * 60 * 24));
    if (day >= 30) {
      checkColorsAndPrint();
    }
  } else {
    checkColorsAndPrint();
  }
}
checkIfColorsShouldBeChecked();
setInterval(checkIfColorsShouldBeChecked, 24 * 60 * 60 * 1000);
const container = document.getElementById('grid-container');
const table = maketable();
container.appendChild(table);