# **Automação de Lançamento de DANFEs no ERP TOTVS Microsiga**  

## 📌 **Descrição do Projeto**  
Este projeto tem como objetivo **automatizar o processo de lançamento de DANFEs (Documento Auxiliar de Nota Fiscal Eletrônica) no ERP TOTVS Microsiga**. A automação **extrai dados do XML** de cada nota fiscal e insere, valida, ou corrige esses dados no sistema, garantindo que todas as **regras de negócio** sejam atendidas.  

### Fluxo de Trabalho:  
✅ O código acessa o portal interno (portal do compras) e coleta a chave de acesso da DANFE.  
✅ Busca o XML correspondente no repositório local.  
✅ Extrai os dados do XML, como valores dos itens, impostos e filial de entrega.  
✅ Abre o processo de lançamento no Microsiga e insere os dados extraídos.  
✅ Verifica e corrige discrepâncias entre os valores do pedido interno e da NF.  
✅ Finaliza o lançamento e inicia o próximo processo.  

## 🖥 **Tecnologias Utilizadas**  
- **Python** – Linguagem principal da automação.  
- **Selenium** – Automação do portal interno vinculado ao Microsiga.  
- **Pyautogui** – Interação com a interface gráfica do ERP.  
- **Pyperclip** – Manipulação da área de transferência para inserção e validação dos dados.  
- **xmltodict** – Extração de dados estruturados dos arquivos XML.  

## ⚙️ **Pré-requisitos**  
Antes de rodar o projeto, certifique-se de ter instalado:  
- **Python 3.x**    
- **ERP TOTVS Microsiga** instalado e acessível  
- Conta no **Portal interno** - *acessível via navegador* -

## 📥 **Instalação**  

1. **Clone este repositório**  
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
   
2. **Crie um ambiente virtual (opcional, mas recomendado)**  
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
   
3. **Instale as dependências**  
   ```sh
   pip install -r requirements.txt
   ```
   

## 🚀 **Como Executar**  

1. Certifique-se de que o **ERP Microsiga e o portal do compras estão acessíveis e já logados**. O Microsiga precisa estar aberto na tela principal da rotina **Processo Pagamento**.  
2. Coloque os **arquivos XML** das notas na pasta configurada como **repositório**.  
3. **Execute o script principal**:  
   ```sh
   python main.py
   ```
4. Acione o botão **Inicializar Usuário** e aguarde até que o programa tenha feito login no portal do compras. Depois feche o **navegador Selenium** onde foi efetuado o login.
5. Acione o botão **Play** e acompanhe o processo na interface do Microsiga e do portal do compras.


## **Observações**  

1. O código gera logs para apontar os processos com algum empecilho que ele encontrou. Em sua interface, ele exibe as quantidades de processos errados por categoria: Sem Boleto, Processo Bloqueado e Processo Errado, e, ele armazena o link dos processos do portal. Para acessar esses processos basta clicar no botão correspondente (Sem Boleto, Processo Bloqueado, XML Indecifrável, Processo Errado) presente na interface.
2. Além disso, ele também envia o link do processo impedido por E-mail para o grupo Entrada de Documentos.
   
