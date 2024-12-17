# 📚 **NovelCopy** 📚

Este repositório contém um script Python para copiar informações e capítulos de uma light novel de um site específico e, em seguida, gerar um arquivo EPUB. O processo automatiza o download dos capítulos e a criação de um arquivo EPUB usando a ferramenta `Pandoc`.

## 📝 **Índice**

1. [🔧 Requisitos](#requisitos)
2. [⚙️ Configuração](#configuração)
3. [💻 Uso](#uso)
4. [📄 Funções Principais](#funções-principais)
5. [🔄 Processo de Criação do EPUB](#processo-de-criação-do-epub)
6. [🚀 Contribuição](#contribuição)
7. [📄 Licença](#licença)

<h2 id="requisitos">🔧 Requisitos</h2>

Antes de usar o script, certifique-se de que você tem os seguintes requisitos instalados:

- **Python 3.x** (recomendado a versão mais recente)
- **Selenium**: para interação com a página web.
  ```bash
  pip install selenium
  ```
- **WebDriver Manager**: para facilitar o gerenciamento do driver do navegador.
  ```bash
  pip install webdriver-manager
  ```
- **Pandoc**: para converter arquivos Markdown em EPUB.
  - [Instalar o Pandoc](https://pandoc.org/installing.html)

<h2 id="configuração">⚙️ Configuração</h2>

1. **Perfil do Firefox**: O script usa um perfil do Firefox customizado para realizar a cópia. Altere a variável `FIREFOX_PROFILE_PATH` no código para o caminho do seu próprio perfil do Firefox.

2. **Instalação do WebDriver**: O script usa o `GeckoDriverManager` para gerenciar a instalação do `GeckoDriver`, necessário para o Selenium interagir com o Firefox.

<h2 id="uso">💻 Uso</h2>

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu_usuario/light-novel-scraping.git
   cd light-novel-scraping
   ```

2. **Execute o script**:

   Após configurar seu perfil do Firefox, execute o script Python:

   ```bash
   python scraping.py
   ```

3. **Informe os dados necessários**:

   - O nome da novel que deseja copiar.
   - O capítulo inicial a partir do qual o scraping deve começar.

4. **Criação do EPUB**:

   Após completar o scraping dos capítulos, o script cria automaticamente o arquivo `.bat` necessário para gerar o EPUB. Execute o arquivo `create_epub.bat` gerado para criar o arquivo EPUB da sua light novel.

<h2 id="funções-principais">📄 Funções Principais</h2>

### `get_valid_input()`

Função que valida a entrada do usuário, garantindo que os dados fornecidos estejam no formato correto.

### `scrape_info(link)`

Função responsável por copiar as informações gerais da novel (nome, autor, descrição) e salvar no arquivo `metadata.txt`.

### `scrape_chapter()`

Função que copia o conteúdo de um capítulo individual e o salva em um arquivo Markdown.

### Fluxo de Execução:

1. **Entrada de Dados**: O usuário informa o nome da novel e o capítulo inicial.
2. **Cópia de Dados**: O script percorre os capítulos da novel e os salva em arquivos `.md`.
3. **Criação do EPUB**: Um arquivo `.bat` é gerado automaticamente para usar o Pandoc e criar o arquivo EPUB.

<h2 id="processo-de-criação-do-epub">🔄 Processo de Criação do EPUB</h2>

Após a cópia dos capítulos, o script gera um arquivo `.bat` que contém o comando para usar o **Pandoc** e criar um arquivo EPUB a partir dos arquivos Markdown. O comando `Pandoc` pega o arquivo `metadata.txt` e todos os arquivos `.md` dos capítulos para compor o arquivo EPUB final.

<h2 id="contribuição">🚀 Contribuição</h2>

Se você deseja contribuir com este projeto, siga as etapas abaixo:

1. **Faça um Fork** deste repositório.
2. Crie uma branch para suas modificações (`git checkout -b feature/nova-funcionalidade`).
3. **Commit** suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um **Pull Request** para que possamos revisar suas modificações.

## 📄 **Licença**

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

**Aproveite a automação de cópia de novels! 😄📖**
