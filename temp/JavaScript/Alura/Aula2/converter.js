function Converter() {
  var valorElemento = document.getElementById("valor");
  var valor = valorElemento.value;
  var valorEmDolarNumerico = parseFloat(valor);


  var valorEmReal = valorEmDolarNumerico * 5;
  console.log(valorEmReal)
  var elementoValorConvertido = document.getElementById("valorConvertido");
  var valorConvertido = "O valor em reais é R$: " + valorConvertido;
  elementoValorConvertido.innerHML = valorConvertido;
}
