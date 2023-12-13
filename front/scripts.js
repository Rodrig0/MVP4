/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/passageiros';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.passageiros.forEach(item => insertList(item.name, 
                                                item.pclass, 
                                                item.age,
                                                item.sibsp,
                                                item.parch,
                                                item.fare,
                                                item.sex,
                                                item.embarkedc,
                                                item.embarkedq,
                                                item.embarkeds,
                                                item.outcome
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputPassenger, inputPclass, inputAge,
                        inputSibsp, inputParch, inputFare, 
                        inputSex, inputEmbarkedc, inputEmbarkedq, inputEmbarkeds) => {
    
  const formData = new FormData();
  formData.append('name', inputPassenger);
  formData.append('pclass', inputPclass);
  formData.append('age', inputAge);
  formData.append('sibsp', inputSibsp);
  formData.append('parch', inputParch);
  formData.append('fare', inputFare);
  formData.append('sex', inputSex);
  formData.append('embarkedc', inputEmbarkedc);
  formData.append('embarkedq', inputEmbarkedq);
  formData.append('embarkeds', inputEmbarkeds);


  let url = 'http://127.0.0.1:5000/passageiro';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/passageiro?name='+item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputPassenger = document.getElementById("newInput").value;
  let inputPclass = document.getElementById("newPclass").value;
  let inputAge = document.getElementById("newAge").value;
  let inputSibsp = document.getElementById("newSibsp").value;
  let inputParch = document.getElementById("newParch").value;
  let inputFare = document.getElementById("newFare").value;
  let inputSex = document.getElementById("newSex").value;
  let inputEmbarkedc = document.getElementById("newEmbarkedc").value;
  let inputEmbarkedq = document.getElementById("newEmbarkedq").value;
  let inputEmbarkeds = document.getElementById("newEmbarkeds").value;


  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/passageiros?nome=${inputPassenger}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.passageiros && data.passageiros.some(item => item.name === inputPassenger)) {
        alert("O passageiro já está cadastrado.\nCadastre o passageiro com um nome diferente ou atualize o existente.");
      } else if (inputPassenger === '') {
        alert("O nome do passageiro não pode ser vazio!");
      } else if (isNaN(inputPclass) || isNaN(inputAge) || isNaN(inputSibsp) || isNaN(inputParch) || isNaN(inputFare) || isNaN(inputSex) || isNaN(inputEmbarkedc) || isNaN(inputEmbarkedq) || isNaN(inputEmbarkeds)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputPassenger, inputPclass, inputAge, inputSibsp, inputParch, inputFare, inputSex, inputEmbarkedc, inputEmbarkedq, inputEmbarkeds);
        postItem(inputPassenger, inputPclass, inputAge, inputSibsp, inputParch, inputFare, inputSex, inputEmbarkedc, inputEmbarkedq, inputEmbarkeds);
        alert("Passageiro adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (namePassenger, pclass, age, sibsp, parch, fare, sex, embarkedc, embarkedq, embarkeds, outcome) => {
  var item = [namePassenger, pclass, age, sibsp, parch, fare, sex, embarkedc, embarkedq, embarkeds, outcome];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newInput").value = "";
  document.getElementById("newPclass").value = "";
  document.getElementById("newAge").value = "";
  document.getElementById("newSibsp").value = "";
  document.getElementById("newParch").value = "";
  document.getElementById("newFare").value = "";
  document.getElementById("newSex").value = "";
  document.getElementById("newEmbarkedc").value = "";
  document.getElementById("newEmbarkedq").value = "";
  document.getElementById("newEmbarkeds").value = "";

  removeElement();
}