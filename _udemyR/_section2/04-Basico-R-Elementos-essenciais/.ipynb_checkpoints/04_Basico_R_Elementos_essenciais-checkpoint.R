############################################################################
## R na Prática
## Elementos essenciais
## Lopes
############################################################################

## Ajuda no R

# Exibe links principais do R
help.start()

# Axibe o help da função informada
help(nome_funcao)

# Interrogação à esquerda de uma função também exibe ajuda
?nome_funcao

# Algumas funções precisam estar entre aspas para ajuda
?"{"

# Ajuda com demonstrações de recursos de pacotes
demo()

## Pacotes

# Pacotes disponíveis
x <- as.data.frame(available.packages())
x <- subset(x, select = c("Package","Version","License"))
nrow(x); head(x); tail(x)

# Instalação de pacotes;
install.packages("tidyr")
install.packages(c("plyr", "tidyr", "dplyr"))

# Remoção de pacotes;
remove.packages("tidyr")
remove.packages(c("plyr", "tidyr", "dplyr"))

## Alguns elementos importantes "( ), [ ], { }"

mean(0:5)

{
  x <- 5
  y <- 1 + round(runif(x), 2)
  z <- 1 + y
}

z[1:2]

k <- as.list(z); k[1:2]

fn <- function(x) {
  return(mean(x))
}

## Versão, ambiente, citação e diretórios importantes

# Exibe a versão do R e outros dados
version
# Citação do R em formato BibTeX
citation()
# Mostra tudo que está carregado no ambiente
ls()
# Obtem o caminho local da sessão
getwd() 
# Lista pastas e arquivos do caminho
dir()  
# Define novo local para a sessão atual
setwd()

############################################################################
## Fim do script
############################################################################

