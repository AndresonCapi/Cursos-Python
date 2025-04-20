// Desafios JavaScript na DIO tem funções "gets" e "print" acessíveis globalmente;
// "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
// "print": imprime um texto de saída (output), pulando linha.

// lê os valores de Entrada:
const valorSalario = parseFloat(gets());
const valorBeneficio = parseFloat(gets());

// Calcule o imposto através da função "calcularImposto":
const valorImposto = calcularImposto(valorSalario);

// Calcula e imprime a Saída (com 2 casas decimais):
const saida = valorSalario - valorImposto + valorBeneficio;
print(saida.toFixed(2));

// Função útil para o calculo do imposto (baseado nas alíquotasa).
function calcularImposto(salario) {
    let aliqota;
    if (salario >= 0 && salario <=1100) {
        aliquota = 0.05;
    } else if (salario >= 1100.0 && salario <=2500) {
        aliquota = 0.10;
    } else aliquota = 0.15;
    return aliqota * salario
    
}
