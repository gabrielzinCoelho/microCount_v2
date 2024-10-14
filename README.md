# MicroCount

Sistema auxilar para a contagem de elementos capturados em placas via images microscópicas.

<p align="center">
    <img src="./assets/demoMicroCount.png" width="700px" height="375px">
</p>

## Sobre o Projeto

O projeto consiste de uma aplicação desenvolvida em Python e utilizando a biblioteca de processamento de imagens OpenCV visando auxilar a contagem manual de elementos capturados em placas via images microscópicas. 

Uma técnica comumente utilizada na área de bioinformática é a divisão da imagem original em áreas menores, denominadas setores. Assim, a contagem individual de cada setor é realizada e, ao final, a contagem geral é obtida pela soma das parcelas de cada setor.

A ideia do projeto é automatizar parte desse processo, facilitando a divisão precisa da imagem em setores e fornecendo ferramentas para que o usuário possa marcar e contar os elementos manualmente dentro de cada setor. Isso permitirá uma contagem mais rápida e organizada, com a opção de ajustar e visualizar os setores de forma interativa. O objetivo final é melhorar a precisão e eficiência do processo de contagem, além de garantir que os resultados sejam facilmente registrados e exportados para futuras análises.

## Funcionamento

### Selecione uma imagem

```
*************** Escolha uma imagem ***************

1) SE11 - 1.jpg
2) BT 06 - quad 96 h- 5uL- corada.jpg
3) LCBM 6 - 2.jpg
4) T24_48h_foto2.jpg
5) 23.1 - 1.2.jpg


Escolha uma opcao:     2
```

### Imagem sob análise

<p align="center">
    <img src="./assets/demoMicroCount.png" width="350px" height="190px">
    <img src="./assets/demoMicroCount_2.png" width="350px" height="190px">
    <img src="./assets/demoMicroCount_3.png" width="350px" height="190px">
</p>

### Setor Selecionado

<p align="center">
    <img src="./assets/demoSetor.png" width="500px" height="268px">
    <img src="./assets/demoSetor_2.png" width="500px" height="268px">
</p>

### Informe a contagem

```
Setor 41 - Contagem: 17
```

### Exporte os resultados

<p align="center">
    <img src="./assets/exportContagem.png" width="500px" height="268px">
</p>
