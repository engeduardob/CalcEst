# calcEst

O programa buscará auxiliar o engenheiro estrutural em verificações, dimensionamentos, detalhamentos, etc de estruturas de concreto armado e protendido.

## Sumário


- [Introdução](#introdução)
- [Propriedade dos Materiais: func_PropriedadesMateriais.py](#propriedade-dos-materiais)
  - [Concreto (classe: Concreto)](#concreto)
  - [Aço (clase: Aco)](#aço)
  - [Protensão (classe: Prot)](#protensão)


# Introdução

O programa se divide em diversas funções básicas. Dessas são geradas outras mais complexas para temas mais específicos. O desenvolvimento é baseado especialmente na NBR 6118:2023. Quando a norma não é clara ou não há nada mais explicito, são indicadas as referências bibliográficas.

# Propriedade dos Materiais

```
func_PropriedadesMateriais.py
```

**EM DESENVOLVIMENTO**

Dividida em:

- Concreto (classe: Concreto)
- Aço (clase: Aco)
- Protensão (classe: Prot) - Não desenvolvdo

## Concreto

A classe se chama:

```
Concreto
```

Tenta reunir as diversas propriedades básicas do concreto.

### INPUTS

São divididos em Obrigatório e Opcionais. Os Obrigatórios devem sempre ser inseridos manualmente, já os Opcionais vem com um valor pré-definido (que deve ser avaliado se está adequado) que pode ser observado no tópico mais adiante.

```
concXX = Concreto(fck, dias = 28, gama_c = 1.4, alfa_e = 0.8, alfa_fator = 1.5, epsilon_c = 0.002, epsilon_t = 0.00015):
```

- **Obrigatórios**:

>***fck= ___***:  
Resistência característica à compressão em MPa.

- **Opcionais**:

>***dias = 28***:  
Data que se deseja avaliar o concreto;  

>***gama_c = 1.4***:  
Coeficiente de ponderação de resistência do concreto;  

>***alfa_e = 0.8***:  
Fator alfa e que varia conforme o agregado utilizado no concreto (ver NBR 6118:2023 - 8.2.8). A sugestão inicial é 0.8, valor aproximado para o Rio de Janeiro;  

>***alfa_fator = 1.5***:  
Fator alfa, associado a forma geométrica do elemento analisado. É utilizado para determinar o momento de fissuração, entre outras aplicações. Ver NBR 6118:2023 - 17.3.1;  

>***epsilon_c = 0.002***:  
Deformação específica que a peça está imposta, caso comprimida;  

>***epsilon_t = 0.00015***:  
Deformação específica que a peça está imposta, caso tracionada.  


A seguir algumas formas de atribuir a uma variável uma classe (#HOLD: depois ver a forma correta tecnicamente de escrever isso).


```
#Ex 1 (input simplificado, apenas definindo o fck e aceitando opcionais conforme configurado):
c30 = Concreto(30)

#Ex 2 (input completo):
c35 = Concreto(fck = 35, dias = 14, gama_c = 1.1, alfa_e = 0.9, alfa_fator = 1.2, epsilon_c = 0.001, epsilon_t = 0.0001)

#Ex 3 (dependendo de outra variável):
conc = 40
c40 = Concreto(fck = conc)

#Ex 4 (conforme ordem dos inputs):
c45 = Concreto(45, 7, 1.4, 1.0)
```

### OUTPUTS

>***.taxaMinima()***:   
Taxa mínima para armadura de flexão (ro,mín) (NBR 6118:2023 - 17.3.5.2.1 - Tabela 17.3)  

>***.fckj()***:  
Resistência do concreto a compressão em determinada data menor que 28dias (NBR 6118:2023 - 12.3.3)  

>***.fctm()***:  
Resistência média à tração do concreto (NBR 6118:2023 - 8.2.5)  

>***.fctmj()***:  
Resistência média à tração do concreto em data inferior aos 28 dias, desde que fckj >= 7MPa (NBR 6118:2023 - 8.2.5)  

>***.fctkinf()***:  
Resistência inferior à tração do concreto (NBR 6118:2023 - 8.2.5)  

>***.fctkinfj()***:  
Resistência inferior à tração do concreto em data inferior aos 28 dias, desde que fckj >= 7MPa (NBR 6118:2023 - 8.2.5)  

>***.fctksup()***:  
Resistência superior à tração do concreto (NBR 6118:2023 - 8.2.5)  

>***.fctksupj()***:  
Resistência superior à tração do concreto em data inferior aos 28 dias, desde que fckj >= 7MPa (NBR 6118:2023 - 8.2.5)  

>***.fcd()***:  
Resistência de cálculo à compressão do concreto (NBR 6118:2023 - 12.3.3)

>***fctd()***:  
Resistência de cálculo à tração do concreto (NBR 6118:2023 - 9.3.2.1)

>***.Eci()***:  
Módulo de elasticidade ou módulo de deformação tangente inicial do concreto (NBR 6118: 2023 - 8.2.8)  

>***.Ecij()***:  
Módulo de elasticidade ou módulo de deformação tangente inicial do concreto no instante j (NBR 6118: 2023 - 8.2.8)

>***.Ecs()***:  
Módulo de deformação secante do concreto (NBR 6118: 2023 - 8.2.8)

>***.sigma_max_c_ato()***:  
ELU do concreto protendido no ATO (NBR 6118:2023 - 17.2.4.3.2): Tensão máxima de compressão

>***.sigma_max_t_ato()***:  
ELU do concreto protendido no ATO (NBR 6118:2023 - 17.2.4.3.2): Tensão máxima de tração  

>***.sigma_max_c_els_qperm()***:  
ELS - Limite de tensão de compressão do concreto - Na combinação quase permanente (NBR 6118:2023 - 17.2.4.4.1)  

>***.sigma_max_c_els_freq()***:  
ELS - Limite de tensão de compressão do concreto - Na combinação frequente (NBR 6118:2023 - 17.2.4.4.1)  

>***.sigma_max_c_els_rara()***:  
ELS - Limite de tensão de compressão do concreto - Na combinação rara (válida só para PROT COMPLETA (nível 3)) (NBR 6118:2023 - 17.2.4.4.1)  

>***.sigma_max_t_els_f()***:  
ELU de formação de fissuras, tensão na qual a seção passa a trabalhar no Estádio II - seção fissurada (NBR 6118:2023 - 17.2.4.4.2)  

>***.sigma_max_t_els_d()***:  
ELS-D - ELU de descompressão, tensão de tração limite nula (NBR 6118:2023 - 17.2.4.4.2)  

>***.alfav2()***:  
Parâmetro do concreto utilizado para cálculo de resistências do concreto (V,Rd2, T,Rd2, f,cd1, fcd2, fcd3, etc) (NBR 6118: 17.5.1.5)  

>***.fcd1()***:  
Resistências a compressão do concreto de cálculo de bielas e regiões nodais (NBR 6118:2023 - 22.3.2) - Para bielas prismáticas ou nós CCC  

>***.fcd2()***:  
Resistências a compressão do concreto de cálculo de bielas e regiões nodais (NBR 6118:2023 - 22.3.2) - Para bielas atravessadas por mais de um tirante, ou nós CTT/TTT  

>***.fcd3()***:  
Resistências a compressão do concreto de cálculo de bielas e regiões nodais (NBR 6118:2023 - 22.3.2) - Para bielas atravessadas por um único tirante, ou nós CCT  

>***.epsilonc2()***:  
Deformação específica de encurtamento do concreto (no início do patamar plástico e de ruptura), para análises no ELU (NBR 6118:2023 8.2.10.1)  

>***.epsiloncu()***:  
Deformação última de encurtamento do concreto, para análises no ELU (NBR 6118:2023 8.2.10.1)  

>***.etac()***:  
Parâmetros para o cálculo da Tensão-deformação do concreto - Compressão (NBR 6118:2023 8.2.10.1)  

>***.nc()***:  
Parâmetros para o cálculo da Tensão-deformação do concreto - Compressão (NBR 6118:2023 8.2.10.1)  

>***.sigma_c2()***:  
Tensão no início do patamar plástico - Tensão-deformação do concreto - Compressão (NBR 6118:2023 8.2.10.1)  

>***.sigma_c()***:  
tensão imposta no concreto, dado o encurtamente o epsilon_c - Tensão-deformação do concreto - Compressão (NBR 6118:2023 8.2.10.1)  

>***.epsilon_tu()***:   
Deformação última - Deformação de tração do concreto (bilinear), para concreto não fissurado (NBR 6118:2023 8.2.10.2)  

>***.epsilon_t2()***:  
Deformação que separa o diagrama bilinear (foi adotado fctk como fctk_inf pois considera-se o concreto como não fissurado) - Deformação de tração do concreto (bilinear), para concreto não fissurado (NBR 6118:2023 8.2.10.2)  

>***.sigma_t()***:  
Tensão dada uma deformação epsilon_t - Deformação de tração do concreto (bilinear), para concreto não fissurado (NBR 6118:2023 8.2.10.2)  

>***.massaEspecifica()***:  
Massa específica (concreto armado) - (NBR 6118:2023 8.2.2)  

>***.coefDilatacaoTermica()***:  
Coeficiente de dilatação térmica (NBR 6118:2023 8.2.3)  

>***.poisson()***:  
Coeficiente de poisson (0.2 é um valor válido para tensões menores que 0.5fc e tensões de tração menores que fct) - (NBR 6118:2023 8.2.9)  

>***.Gc()***:  
Módulo de elasticidade transversal - (NBR 6118:2023 8.2.9)  

>***Os próprios inputs podem ser usados como outputs.***:  
.fck  
.dias  
.gama_c  
.alfa_e  
.alfa_fator  
.epsilon_c  
.epsilon_t

A seguir algumas formas de chamar uma propriedade (#HOLD: depois ver a forma correta tecnicamente de escrever isso).

```
#Ex 1 (simples):
c30 = Concreto(30) #input
c30.fctm() #output

#Ex 2 (chamar um input como output):
c35 = Concreto(fck = 35, dias = 14, gama_c = 1.1, alfa_e = 0.9, alfa_fator = 1.2, epsilon_c = 0.001, epsilon_t = 0.0001) #input
c35.gama_c #output (observar que para chamar um input como output não é necessário o uso do parêntesis () )
```



## Aço


## Protensão