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
        // element2 = document.createTextNode(clicked_id);
        element2 = document.createElement("input");
        element2.type = "text";

        cell2.appendChild(element2);
        // 수량
        cell3 = row.insertCell(2);
        // element3 = document.createTextNode("1");
        element3 = document.createElement("input");
        element3.type = "number";
        element3.id = clicked_id+"1";
        element3.value = 1;
        element3.min = "1";
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
    for(var i = 0; i < rowcnt; i++){
        var row = tbody.rows[i];
        var rowObj = row.cells[1].childNodes[0].textContent;
        if(rowObj == clicked_id){
            tbody.deleteRow(i);
            rowcnt--;
            break;
        }
    }
}