## remove o firefox do pacote snap e instala o firefox do gerenciador pacote apt 
source .installFirefox.sh

# cria e instala o ambiente virtual
VENV_NAME=".env"
echo "=== Criando ambiente virtual Python: $VENV_NAME ==="

# Verificar se o módulo venv está disponível
python3 -m venv --help &> /dev/null
if [ $? -ne 0 ]; then
    echo "O módulo venv não está disponível. Instalando..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
fi

# Criar ambiente virtual
python3 -m venv $VENV_NAME
if [ $? -ne 0 ]; then
    echo "Falha ao criar o ambiente virtual."
    exit 1
fi

echo "Ambiente virtual criado com sucesso!"

# Ativar o ambiente virtual
source $VENV_NAME/bin/activate
if [ $? -ne 0 ]; then
    echo "Falha ao ativar o ambiente virtual."
    exit 1
fi

echo "Ambiente virtual ativado com sucesso!"

# Atualizar pip
pip install --upgrade pip
echo "pip atualizado para a versão mais recente."

# Verificar se o arquivo requirements.txt existe
if [ -f "requirements.txt" ]; then
    echo "Instalando pacotes do arquivo requirements.txt..."
    pip install -r requirements.txt
    
    if [ $? -eq 0 ]; then
        echo "Todos os pacotes foram instalados com sucesso!"
    else
        echo "Ocorreu um erro ao instalar alguns pacotes. Verifique o arquivo requirements.txt."
    fi
else
    echo "Arquivo requirements.txt não encontrado no diretório atual."
    echo "Você pode criar um arquivo requirements.txt ou instalar pacotes manualmente com 'pip install <nome-do-pacote>'."
fi

echo ""
echo "=== Ambiente virtual Python configurado! ==="
echo "Para desativar o ambiente virtual, digite 'deactivate'"
echo "Para ativar novamente, execute 'source $VENV_NAME/bin/activate'"

# roda o codigo
python3 main.py

