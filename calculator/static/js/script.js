function addItem(clicked_id){
    tbody = document.getElementById("table-body");
    find = document.getElementById(clicked_id+"1");
    if (find !== null){
        find.value++;
    }
    else {
        row = tbody.insertRow(0);
        // 사진
        cell1 = row.insertCell(0); 
        element1 = document.getElementById(clicked_id).childNodes[1].cloneNode();
        cell1.appendChild(element1);
        // 이름
        cell2 = row.insertCell(1);
        element2 = document.createElement("input");
        element2.readOnly = "readonly";
        element2.value = clicked_id;
        element2.className = "item_name_input";
        element2.id = clicked_id;
        element2.name = "name";
        cell2.appendChild(element2);
        // 수량
        cell3 = row.insertCell(2);
        element3 = document.createElement("input");
        element3.type = "number";
        element3.id = clicked_id+"1";
        element3.value = 1;
        element3.min = "1";
        element3.name = "nums";
        cell3.appendChild(element3);
        // 종류
        cell4 = row.insertCell(3);
        element4 = document.createTextNode(document.getElementById(clicked_id).parentNode.parentNode.parentNode.parentNode.childNodes[0].textContent);
        cell4.appendChild(element4);
        // 삭제
        cell5 = row.insertCell(4);
        element5 = document.createElement("input");
        element5.type = "button";
        element5.id = clicked_id;
        element5.value = "삭제";
        element5.onclick = function(){
            deleteItem(clicked_id);
        }
        cell5.appendChild(element5);
    }
}

function deleteItem(clicked_id){
    tbody = document.getElementById("table-body");
    rowcnt = tbody.rows.length;
    for(let i = 0; i < rowcnt; i++){
        let row = tbody.rows[i];
        let rowObj = row.cells[1].childNodes[0];
        if(rowObj.id == clicked_id){
            tbody.deleteRow(i);
            rowcnt--;
            break;
        }
    }
}

function drawTree(numoftree){
    let ctx = document.getElementById('canvas').getContext('2d');
    let img = new Image();
    img.src = '/static/img/tree1.png';
    img.width = '30px';
    img.height='100px';

    for(var i = 0; i < numoftree; i++){
        ctx.drawImage(img, i, i, 50, 50);
    }
}