/**
 * @param {Array.<number>} lista Um array de números para seus valores serem somados.
 */
const somaLista = (lista) => {
	let soma = 0;
	for (let i = 0; i < lista.length; i++) {
		soma += lista[i];
	}
	return soma;
}

let variavel = [5, 3, 9, 21, 2, 55];
console.log(somaLista(variavel));
