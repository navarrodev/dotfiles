var numeroSecreto = parseInt(Math.random() * 11);
var count = 4;

function Chutar(){
  var elementoResultado = document.getElementById("resultado");
  var chute = parseInt(document.getElementById("valor").value);
  console.log(chute);
  if (chute == numeroSecreto){
    elementoResultado.innerHTML = "Você Acertou"
  } else if (chute > 10 || chute <0){
    elementoResultado.innerHTML = "Digite um número de 0 a 10";
  } else{if (numeroAleatorio < chute) {
      contador = contador - 1;
      elementoResultado.innerHTML =
        "Controle seus pensamentos tente um número menor, Você ainda possui " +
        contador +
        " tentativas";
    }
    if (numeroAleatorio > chute) {
      contador = contador - 1;
      elementoResultado.innerHTML =
        "Concentre-se pense em um número maior, Ainda restam " + t + " tentativas";
    }
    if (contador == 0) {
      elementoResultado.innerHTML =
        "Treine mais seus poderes mentais padawan, o número secreto era: " +
        numeroSecreto +
        ".";
    }

  }
}
