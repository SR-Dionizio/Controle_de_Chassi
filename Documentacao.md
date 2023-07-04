# Documentação do Controle de Chassi

O Controle de Chassi é um sistema desenvolvido em Python que permite o controle e registro de chassis de veículos. Com ele, é possível cadastrar novos chassis, consultar informações existentes, atualizar dados e gerar relatórios personalizados. Esta documentação fornece uma visão geral do sistema, instruções de instalação e exemplos de uso.

## Funcionalidades

- Cadastro de chassis: Permite o registro de informações relacionadas aos chassis dos veículos, como número do chassi, modelo, ano de fabricação, cor, entre outros.

- Consulta de chassis: Permite a busca e visualização de informações de chassis previamente cadastrados.

- Atualização de chassis: Permite a modificação e atualização dos dados de um chassis específico.

- Exclusão de chassis: Permite a remoção de chassis que não são mais relevantes para o controle.

- Geração de relatórios: Permite a criação de relatórios personalizados com base nos chassis cadastrados.

## Tecnologias Utilizadas

O Controle de Chassi foi desenvolvido utilizando as seguintes tecnologias e bibliotecas:

- Python: Linguagem de programação utilizada para desenvolver o sistema.
- SQLite: Banco de dados embutido utilizado para armazenar as informações dos chassis.
- PyQt: Framework utilizado para a criação da interface gráfica.
- Pandas: Biblioteca utilizada para manipulação e análise de dados.
- Matplotlib: Biblioteca utilizada para geração de gráficos e visualização de dados.

## Instalação

Siga as instruções abaixo para instalar e executar o Controle de Chassi em seu ambiente local:

1. Certifique-se de ter o Python instalado em sua máquina. Caso ainda não tenha, você pode fazer o download no site oficial do Python: https://www.python.org/

2. Faça o download ou clone este repositório em seu ambiente local.

3. Abra um terminal ou prompt de comando e navegue até o diretório raiz do projeto.

4. Crie um ambiente virtual (opcional, mas recomendado) executando o seguinte comando:
   ```
   python -m venv venv
   ```

5. Ative o ambiente virtual recém-criado. Dependendo do seu sistema operacional, o comando pode variar:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No macOS e Linux:
     ```
     source venv/bin/activate
     ```

6. Instale as dependências do projeto executando o seguinte comando:
   ```
   pip install -r requirements.txt
   ```

7. Após a instalação das dependências, você estará pronto para executar o Controle de Chassi.

## Executando o Controle de Chassi

Siga as etapas abaixo para executar o Controle de Chassi:

1. Certifique-se de que o ambiente virtual (se criado) esteja ativado.

2. Navegue até o diretório raiz do projeto.

3. Execute o seguinte comando para iniciar o sistema:
   ```
   python main.py
   ```

4. O Controle de Chassi será iniciado e a interface gráfica será exibida.

5. Utilize as opções do menu para cadastrar, consultar, atualizar e excluir chassis, além de gerar relatórios.

6. Siga as instruções apresentadas na interface para realizar as operações desejadas.

