# Atividade Mastertech


## 1 - Cadastro de usuário
### Requisição
Requisição para o cadastro de usuario. A entrada de dados sera realizada fornecendo os seguinte dados: "nome_completo", "cpf" e "email", o ID do usuario sera gerado automáticamente pelo banco de dados.

![Image](/image/cadastro_usuario.png)


### Resposta

![Image](/image/resposta_Cadastro.png)


### Requisição
Com o campo cpf faltando no corpo da requisição

![Image](/image/cadastro_error.png)


### Resposta
Como resposta, resposta notifica a falta do campo cpf

![Image](/image/respota_cadastro_error.png)


## 2 - Listar Usuários
### Requisição
Requisição para visualizar todos os usuários com as suas informações

![Image](/image/lista_usuario.png)

### Resposta
Retorna a lista de todos os usuários cadastrados comas informações

![Image](/image/resposta_lista_usuario.png)


## 3 - Listar um único Usuário
## Requisição
requisição retorna os dados de um usuário especifico: users{id_user}
![Image](/image/lista_usuario_unico.png)

### Resposta
Como resposta, obtém-se uma mensagem de erro, dizendo que o hotel não foi encontrado.

![Image](/image/resposta_usuario_unico.png)


## Requisição
Usuário que não existe na base de dados 

![Image](/image/lista_usuario_unico_error.png)


### Resposta
Para um usuário não cadastrado é exibido a massagem “User not found”

![Image](/image/resposta_alterar_usuario_erro.png)


## 4 - Alterar de Usuário
### Requisição
Nessa requisição os campos que podem ser alterados são nome_completo, cpf e email

![Image](/image/alterar_usuario.png)

### Antes
![Image](/image/antes.png)



### Resposta
A reposta retorna o cadastro do usuário atualizado

![Image](/image/atualizado.png)

### Requisição
Usuário não cadastrado

![Image](/image/alterar_usuario_error.png)

### Resposta
Para um usuário não cadastrado é exibido a massagem “User not found”

![Image](/image/resposta_alterar_usuario_erro.png)

## 5 - Bater Ponto

### Requisição
Nessa requisição, é feita o restiro da batida de ponto de um usuário fornecendo : {id_user}


![Image](/image/bater_ponto_start.png)


### Resposta
Retorna as informações do ponto que foi batido

![Image](/image/Resposta_bater_ponto.png)

### Apenas as opções (Entrada e Saida) são permitidas

![Image](/image/request_erro.png)

### Resposta

![Image](/image/Bater_ponto_error_opc.png)

### Requisição
Caso seja informado um usuario não cadastrado na base de dados 

![Image](/image/requisao_erro_user.png)

### Resposta
Retorna o status code 404

![Image](/image/erro_404_opcao.png)


## 7 - Lista Pontos de Usuarios

### Requisição
É forncessido o id do usuario que para listar os pontos que foram batido no id_user do mesmo

![Image](/image/doc_checks.png)


### Resposta
Retorna os dados do ponto que foi batido, o id da batida o usuario resposavel, tipo da batida e data e hora da batida

![Image](/image/resposta_check_users.png)

### Requisição
Uma requisição com um id que não existe na base de dados 

![Image](/image/requisicao_erro_checks.png)

### Resposta
Retorna a messagem "User not Found"

![Image](/image/resposta_alterar_usuario_erro.png)







