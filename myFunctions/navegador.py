def navegador_firefox(headless=0, firefox_options=None) -> any:
    '''Função para abrir o navegador com todas config
    já configuradas'''

    import subprocess
    from selenium import webdriver
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.service import Service as GeckoService

    from myFunctions.arrumaScrapper import dir_download
    
    print('\n###############################\n')
    print('         Bem vindo(a)!           ')
    print('\n###############################\n')
    print('Abrindo navegador..\n')

    firefox_binary_path = '/usr/bin/firefox'
    link_geckodriver = 'https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz' 

    # checa versão do seu firefox para baixar o geckodriver certo
    firefox_version = subprocess.check_output('firefox --version', shell=True, stderr=subprocess.STDOUT).decode()
    print(f'Voce está usando o firefox versão:\n{firefox_version[-8:-1]}\n')

    # MIME type for the file you want to download

    # if headless:
    #     firefox_options.add_argument('--headless')
    # firefox_options.add_argument('--disable-dev-shm-usage')
    # firefox_options.add_argument("disable-infobars")

    # create service to GECKODRIVER
    service = GeckoService(GeckoDriverManager(url = link_geckodriver,
                                              version='v0.34.0').install(),
                                              service_log_path = './downloads/')

    # Creating the Firefox driver
    navegador = webdriver.Firefox(
        service = service,
        options = firefox_options
    )

    print('Navegador aberto.\n')

    return navegador