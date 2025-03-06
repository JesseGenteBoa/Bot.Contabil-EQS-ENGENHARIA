# **Automação de Lançamento de DANFEs no ERP TOTVS Microsiga**  

## 📌 **Descrição do Projeto**  
Este projeto tem como objetivo **automatizar o processo de lançamento de DANFEs (Documento Auxiliar de Nota Fiscal Eletrônica) no ERP TOTVS Microsiga**. A automação **extrai informações do XML** de cada nota fiscal e insere, valida, ou corrige esses dados no sistema, garantindo que todas as **regras de negócio** sejam atendidas.  

A automação é responsável por:  
✅ Acessar um **portal interno** vinculado ao ERP, onde estão armazenados boletos, PDFs de NF, chave de acesso e prazos de pagamento. Isso é feito através da biblioteca **Selenium**.
✅ Buscar o **XML da NF** correspondente na pasta de repositório.  
✅ Extrair as informações do XML.  
✅ Realizar o **lançamento no ERP TOTVS Microsiga** usando **Pyautogui e Pyperclip**, inserindo, validando ou corrigindo os dados no sistema.
✅ Repetir o processo até que todas as notas sejam lançadas.  

## 🖥 **Tecnologias Utilizadas**  
- **Python** – Linguagem principal da automação.  
- **Selenium** – Automação do portal interno vinculado ao Microsiga.  
- **Pyautogui** – Interação com a interface gráfica do ERP.  
- **Pyperclip** – Manipulação da área de transferência para inserção de dados.  
- **LXML** – Extração de dados estruturados dos arquivos XML.  

## ⚙️ **Pré-requisitos**  
Antes de rodar o projeto, certifique-se de ter instalado:  
- **Python 3.x**    
- **ERP TOTVS Microsiga** instalado e acessível  
- Conta no **Portal interno** - acessível via navegador -

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

1. **Certifique-se de que o ERP Microsiga e o portal interno estão acessíveis**.  
2. **Coloque os arquivos XML das notas na pasta configurada como repositório**.  
3. **Execute o script principal**:  
   ```sh
   python main.py
   ```
4. **Acompanhe o processo na interface do Microsiga e do portal interno**.  

## ⚠️ **Erros Comuns e Soluções**  

| Erro | Causa Possível | Solução |
|------|---------------|---------|
| `selenium.common.exceptions.WebDriverException` | ChromeDriver desatualizado | Baixe a versão correta do ChromeDriver |
| `pyautogui.FailSafeException` | Mouse movido para o canto superior esquerdo | Remova a segurança (`FAILSAFE=False`) se necessário |
| `Arquivo XML não encontrado` | XML da NF não está na pasta de repositório | Verifique se o XML foi salvo corretamente |

## 📌 **Contribuição**  
Sinta-se à vontade para sugerir melhorias, abrir **issues** ou enviar **pull requests**.  

## 📜 **Licença**  
Este projeto é de uso **interno** e não possui licença pública.  
