#Trabalho da Pryscilla
import time

'''
Tema: IA na Ciberseguraça
'''

div = "══════════════════════════════════════════════════════════════════════════════════════════"
opcoes = ["Sair", "Checar Saldo", "Torres", "Pergaminhos", "Desafio Absoluto"]
torres = ["Torre 1", "Torre 2", "Torre 3"]

pr1 = {
    "1. Como a Inteligência Artificial é utilizada para a defesa cibernética pelas empresas?": {

    "opcoes": 
    ("A - Aumentando a velocidade de conexões de internet e reduzindo o consumo de energia dos servidores corporativos.",
     "B - A IA analisa grandes volumes de dados em tempo real, identifica padrões suspeitos e isola ameaças automaticamente antes que causem danos.",
     "C - Substituindo completamente a necessidade de senhas de acesso por autenticação puramente baseada na localização geográfica do usuário."),

    "correta": "B",
    },

    "2. De que maneira os cibercriminosos também utilizam a IA para realizar ataques?": { 

    "opcoes":
    ("A - Criminosos usam IA para criar e-mails de phishing mais convincentes, programar malwares que burlam antivírus e encontrar falhas de segurança mais rápido.",
     "B - Criando firewalls ultra seguros para proteger os dados confidenciais dos próprios criminosos contra investigações policiais.",
     "C - Traduzindo automaticamente manuais de instruções de equipamentos de rede para outros idiomas."),

    "correta": "A",
    },

    "3. O que são ataques de Deepfake aplicados à engenharia social e quais os riscos?": {

    "opcoes":
    ("A - Instalando vírus de computador silenciosos que se espalham exclusivamente através de pen drives físicos deixados no estacionamento da empresa.",
     "B - Alterando o saldo bancário de contas correntes de forma invisível através de códigos de barra corrompidos em boletos.",
     "C - IA é usada para clonar rostos e vozes de executivos ou familiares, enganando vítimas para realizar transferências de dinheiro ou revelar senhas."),

    "correta": "C",

    },

    "4. O que é 'Envenenamento de Dados' (Data Poisoning) em sistemas de IA voltados para segurança?": {

    "opcoes":
    ("A - É a adulteração dos dados de treinamento da IA para 'cegá-la', fazendo com que ela ignore ataques reais e crie brechas no sistema.",
     "B - Formatando o disco rígido dos computadores da empresa toda vez que o antivírus detecta um arquivo suspeito.",
     "C - Copiando arquivos confidenciais para servidores externos sem criptografia para facilitar o acesso remoto."),

    "correta": "A",

    },

    "5. Qual é o papel humano na cibersegurança diante da automação por IA?": {

    "opcoes": 
    ("A - Substituir totalmente a equipe de tecnologia por robôs para que nenhuma pessoa precise trabalhar com segurança da informação.",
     "B - A IA automatiza tarefas e detecta ameaças, mas o especialista humano é quem toma as decisões estratégicas, analisa o contexto e corrige erros.",
     "C - Impedir que qualquer sistema use inteligência artificial para que os funcionários façam todas as análises de rede manualmente."),

     "correta": "B",

    },
}

pr2 = {
    "1. O que caracteriza uma falha de segurança do tipo 'Prompt Injection' em modelos de linguagem?": {

        "opcoes": 
        ("A - Quando um invasor manipula a entrada de texto para fazer a IA ignorar suas instruções originais e executar comandos maliciosos.",
        "B - Quando o servidor de IA desliga subitamente por falta de memória RAM durante o processamento de imagens.",
        "C - Quando a IA traduz textos técnicos do inglês para o português utilizando regras gramaticais incorretas.",),

        "correta": "A",

    },

    "2. Como funciona um ataque de 'Inversão de Modelo' (Model Inversion) contra sistemas de IA?": { 

        "opcoes": 
        ("A - Os criminosos alteram permanentemente a cor da interface gráfica para dificultar a leitura dos dados.",
        "B - O invasor utiliza as saídas e respostas do modelo para conseguir reconstruir dados confidenciais usados no seu treinamento.",
        "C - A IA começa a responder com mentiras propositais para confundir os administradores da rede corporativa.",),
    
        "correta": "B",

    },

    "3. O que são os chamados 'Ataques Adversariais' (Adversarial Attacks) em visão computacional?": {

        "opcoes": 
        ("A - Inserir pequenas alterações ou ruídos invisíveis a olho nu em imagens para fazer a IA classificar um objeto de forma totalmente errada.",
        "B - Roubar cabos físicos de fibra óptica de alta velocidade utilizando ferramentas de corte em data centers.",
        "C - Apagar todos os arquivos do sistema operacional do computador utilizando um vírus de computador tradicional.",),

        
        "correta": "A",

    },

    "4. Qual é o principal objetivo da técnica de 'Privacidade Diferencial' no desenvolvimento de IAs?": {

        "opcoes": 
        ("A - Acelerar o processamento de criptografia quântica nos servidores locais da empresa.",
        "B - Garantir que dados sensíveis de pessoas possam ser protegidos e anonimizados ao treinar modelos computacionais.",
        "C - Impedir totalmente que qualquer empresa utilize computação em nuvem para armazenar seus arquivos."),
        
        "correta": "B",

    },

    "5. Por que as regulamentações de IA exigem a 'IA Explicável' (Explainable AI - XAI)?": {

        "opcoes": 
        ("A - Para que os especialistas possam auditar, entender e responsabilizar a IA pelas decisões críticas que ela toma.",
        "B - Para obrigar os desenvolvedores a publicarem o código-fonte completo de seus softwares gratuitamente na internet.",
        "C - Para impedir que os computadores funcionem sem a supervisão direta de um gerador de energia a diesel.",),
        
        "correta": "A",

    },
}

pr3 = {
    "1. O que caracteriza um ataque do tipo 'Trojan Weights' (pesos de trojan) na cadeia de suprimentos de IA?": {

        "opcoes": 
        ("A - Quando um modelo de IA de código aberto baixado da internet possui um backdoor oculto em seus parâmetros que só ativa sob um gatilho específico.",
        "B - Quando o sistema operacional apaga todos os drivers de vídeo para impedir que a placa gráfica execute jogos durante o expediente.",
        "C - Quando o hacker rouba fisicamente os cabos de rede do servidor central usando disfarces corporativos." ),

        "correta": "A",

    },

    "2. Como o 'Aprendizado Federado' (Federated Learning) ajuda a proteger a privacidade das empresas?": { 

        "opcoes": 
        ("A - Ele criptografa a internet inteira com senhas de 1000 caracteres geradas por inteligência artificial quântica.",
        "B - Ele permite treinar modelos de IA de forma descentralizada, enviando apenas os aprendizados matemáticos sem expor os dados brutos originais.",
        "C - Ele obriga todas as empresas a compartilharem seus senhas e dados confidenciais publicamente com o governo."),
        
        "correta": "B",

    },

    "3. O que é a 'Biometria Comportamental' aplicada por sistemas de segurança modernos?": {

        "opcoes": 
        ("A - A análise contínua de padrões únicos de digitação, cliques e movimentação de mouse para autenticar a identidade do usuário de forma invisível.",
        "B - O escaneamento da íris dos funcionários utilizando câmeras web de alta resolução antes de abrir qualquer e-mail.",
        "C - O teste de polígrafo digital realizado por robôs de chat toda vez que o funcionário entra na rede corporativa."),

        "correta": "A",

    },

    "4. Qual é o papel das plataformas SOAR (Security Orchestration, Automation, and Response) integradas com IA?": {

        "opcoes": 
        ("A - Desligar permanentemente a internet da empresa toda vez que um funcionário acessa redes sociais.",
        "B - Orquestrar, automatizar e responder a incidentes de segurança cibernética em frações de segundo com o auxílio de agentes autônomos.",
        "C - Criar cópias piratas de softwares corporativos para economizar o orçamento do departamento de TI."),
        
        "correta": "B",

    },

    "5. O que são ataques de 'Side-Channel' (Canal Lateral) direcionados a modelos de IA em execução?": {

        "opcoes": 
            ("A - Enviar e-mails maliciosos de phishing para os engenheiros que criaram o algoritmo de segurança.",
            "B - Analisar o consumo de energia elétrica, tempo de resposta ou emissões eletromagnéticas do hardware para extrair segredos de dentro da IA.",
            "C - Mudar a rota física dos satélites de comunicação para interceptar pacotes de dados no espaço."),
        
        "correta": "B",

    },

    "6. Como os sistemas de 'Zero Trust' baseados em IA calculam a confiabilidade de um acesso?": {

        "opcoes": 
            ("A - Atribuindo uma pontuação de risco dinâmica baseada no contexto, comportamento, localização e integridade do dispositivo em tempo real.",
            "B - Confiando cegamente em qualquer usuário que digite a palavra 'admin' corretamente no campo de login.",
            "C - Permitindo acesso total à rede corporativa apenas para quem possui crachás de metal pesado."),

        "correta": "A",

    },

    "7. O que é um 'AI Fuzzer' utilizado por equipes de segurança ofensiva e defensiva?": {

        "opcoes": 
        ("A - Um robô que gera milhares de entradas de dados inválidas, aleatórias ou maliciosas de forma automatizada para encontrar falhas ocultas em softwares.",
        "B - Um programa de edição de vídeo usado exclusivamente para criar deepfakes de comédia para os funcionários.",
        "C - Um antivírus tradicional que limpa arquivos temporários da lixeira do Windows todos os dias."),
        
        "correta": "A",

    },

    "8. Por que a detecção de Deepfakes em tempo real (como em chamadas de vídeo corporativas) é um desafio técnico extremo?": {

        "opcoes": 
        ("A - Porque exige processar latências mínimas de rede e identificar micro-artefatos visuais ou de áudio gerados por IA antes que a vítima perceba a fraude.",
        "B - Porque o computador precisa imprimir cópias físicas do rosto de todas as pessoas em folhas de papel A4.",
        "C - Porque as câmeras web atuais não possuem lentes de vidro temperado contra ataques cibernéticos."),

        "correta": "A",

    },
}

prd = {

    "1. Como a combinação entre 'Data Poisoning' e 'Inversão de Modelo' pode comprometer um sistema corporativo de IA?": {

        "opcoes": 
        ("A - O envenenamento cega os filtros iniciais da IA permitindo brechas, enquanto a inversão de modelo explora as saídas para extrair segredos e dados confidenciais do treinamento.",
        "B - O envenenamento apaga o disco rígido dos servidores, enquanto a inversão força o computador a desligar por superaquecimento.",
        "C - Ambas as técnicas servem exclusivamente para acelerar a velocidade de download de arquivos em redes Wi-Fi públicas."),
        
        "correta": "A",
    },

    "2. Qual é a principal diferença conceitual entre 'Trojan Weights' na cadeia de suprimentos e os 'Ataques Adversariais' tradicionais?": { 

        "opcoes": 
        ("A - Os Trojan Weights são backdoors inseridos permanentemente nos parâmetros do modelo durante seu treinamento/download, enquanto ataques adversariais modificam dados de entrada (como imagens) em tempo de execução.",
        "B - Os Trojan Weights afetam apenas a placa de vídeo do computador, ao passo que ataques adversariais roubam senhas físicas de cofres.",
        "C - Não há diferença, ambos são vírus de computador tradicionais baseados em arquivos executáveis `.exe`."),
        
        "correta": "A",
    },

    "3. De que maneira o 'Aprendizado Federado' atua em conjunto com a 'Privacidade Diferencial' para proteger dados sensíveis?": {
        "opcoes": 
        ("A - Eles criptografam a senha de rede de todos os funcionários utilizando chaves estáticas de 4 dígitos.",
        "B - O aprendizado federado descentraliza o treino sem expor dados brutos, enquanto a privacidade diferencial injeta ruídos matemáticos controlados para impedir a identificação de indivíduos.",
        "C - Eles impedem completamente que qualquer algoritmo de inteligência artificial seja executado em computadores modernos."),
       
        "correta": "B",
    },

    "4. Como a 'Biometria Comportamental' se integra aos princípios de arquitetura 'Zero Trust' em redes corporativas modernas?": {

        "opcoes": 
        ("A - Validando a identidade do usuário de forma contínua e invisível com base em seus padrões de digitação e movimentação, ajustando o nível de acesso dinamicamente em tempo real.",
        "B - Exigindo que o usuário digite sua senha de banco a cada cinco minutos olhando para uma webcam.",
        "C - Bloqueando o computador permanentemente caso o funcionário mude de cadeira no escritório."),
    
        "correta": "A",
    },

    "5. Qual é o papel crítico das plataformas de resposta automatizada (SOAR) acionadas por agentes de IA em ambientes de alta criticidade?": {
        "opcoes": 
        ("A - Enviar e-mails de cobrança para os hackers que tentaram invadir a rede da empresa.",
        "B - Orquestrar contramedidas em enxames autônomos para isolar e neutralizar brechas de segurança em frações de segundo, superando a latência humana.",
        "C - Fazer cópias de segurança de jogos de videogame nos servidores corporativos durante a madrugada."),
    
        "correta": "B",
    },

    "6. O que torna o 'Prompt Injection' um vetor de ataque particularmente difícil de mitigar em LLMs conectadas a APIs externas?": {

        "opcoes": 
        ("A - Porque a IA tem dificuldade em distinguir instruções legítimas do usuário de comandos maliciosos injetados de forma oculta em dados externos que ela processa.",
        "B - Porque os teclados mecânicos atuais possuem falhas físicas em suas placas de circuito impresso.",
        "C - Porque as senhas dos desenvolvedores costumam ser muito fáceis de adivinhar."),
        

        "correta": "A",
    },

    "7. Por que a ausência de 'IA Explicável' (XAI) representa um risco regulatório e de segurança em redes neurais profundas?": {

        "opcoes": 
        ("A - Porque sem XAI os monitores de vídeo perdem a cor automaticamente após um ano de uso.",
        "B - Porque o problema da 'caixa-preta' impede que os especialistas auditem o raciocínio da IA, dificultando a identificação da causa raiz em falhas ou decisões críticas.",
        "C - Porque impede que o sistema operacional seja atualizado para novas versões."),
        
        "correta": "B",
    },

    "8. Como os ataques de 'Side-Channel' (Canal Lateral) desafiam a segurança de hardwares que executam inteligência artificial?": {

        "opcoes": 
        ("A - Eles enviam spams em massa para o e-mail corporativo dos engenheiros de rede.",
        "B - Eles medem o consumo de energia, o calor ou oscilações eletromagnéticas do chip durante o processamento para deduzir os segredos matemáticos da IA.",
        "C - Eles cortam fisicamente os cabos de fibra óptica submarinos."),
        
        "correta": "B",
    },

    "9. Qual é o principal gargalo técnico na detecção de fraudes por Deepfake em chamadas corporativas em tempo real?": {

        "opcoes": 
        ("A - A exigência de imprimir fotos físicas dos rostos dos participantes em papel fotográfico.",
        "B - A necessidade de processar latências ultra baixas e identificar micro-artefatos sintéticos de áudio e vídeo antes que a manipulação engane o tomador de decisão.",
        "C - A falta de cabos de energia adequados para ligar as câmeras web."),
        
        "correta": "B",
    },

    "10. Diante de sistemas de IA auto-evolutivos e ataques de dia zero automatizados, qual deve ser a postura definitiva do especialista humano?": {

        "opcoes": 
        ("A - Atuar na governança estratégica, supervisão ética, auditoria de falhas sistêmicas e alinhamento de diretrizes de segurança que os algoritmos não podem julgar sozinhos.",
        "B - Desligar totalmente a eletricidade de todos os servidores da empresa permanentemente.",
        "C - Deixar que o computador tome todas as decisões administrativas sem qualquer supervisão."),
        
        "correta": "A",

    },

}

mt1 = 0
mt2 = 0
mt3 = 0
inv = ["Pergaminho 1"]

nom = str(input("Digite seu nome: \n"))

print("\n", div)
print(f"\nSeja bem-vindo {nom}, Ao mundo fantasioso das perguntas e respostas de tema: IA na Cybersegurança, Aqui você irá ter diversas opções e oportunidades, como as Torres(Testes de verificação de aprendizado), Pergaminhos(Fonte de Dados), Moedas individuais de cada torre e o Desafio Final, Sinta-se livre para se aventurar nesse mundo inovador, porem, certifique-se de que possua os dados necessários para passar por cada torre, caso contrário, será dificil você passar da mesma, a não ser que utilize do celular pra passar, é claro😂😁\n")

while True:
    vd = 100
    print("\n", div)

    for i in range(len(opcoes)):
        print(f"{i} - {opcoes[i]}")

    resp = int(input("Selecione uma opção para prosseguir: \n"))

    while resp < 0 or resp > 4:
        print("Opção Inválida")
        resp = int(input("Selecione uma opção para prosseguir: \n"))

    print(div, "\n")

    match resp:
        case 0:
            print("Saindo...")
            break


        case 1:
            print(f"Moedas da Torre 1: {mt1}")
            print(f"Moedas da Torre 2: {mt2}")
            print(f"Moedas da Torre 3: {mt3}\n")
            
            if inv == []:
                print(f"{nom} não possui pergaminhos\n")

            else:

                print("Pergaminhos: ")
                for i in inv:
                    print(i)


        case 2:
            for i in range(len(torres)):
                print(f"{i + 1} - {torres[i]}")

            torse = int(input("Selecione uma opção para prosseguir: \n"))

            while torse < 1 or torse > len(torres):
                print("Torre Destruida ou Inexistente")
                torse = int(input("Selecione uma opção para prosseguir: \n"))

            torse = torse - 1

            match torse:

                case 0:
                    print("Torre 1 Selecionada")

                    
                    for pergunta, dados in pr1.items():
                        if vd <= 0:
                            print("Game Over💀👺💀👺")
                            break

                        print(f"\n{pergunta}")

                        for opcao in dados["opcoes"]:
                            print(opcao)

                        solut1 = str(input("Digite sua resposta: \n")).upper()

                        while solut1 != "A" and solut1 != "B" and solut1 != "C":
                            print("Resposta Inválida, -10 pontos de vida")
                            vd -= 10
                            

                            if vd <= 0:
                                print("Game Over💀💀👺")
                                break

                            solut1 = str(input("Digite sua resposta novamente: \n")).upper()

                        if vd <= 0:
                            break

                        if solut1 == dados["correta"]:
                            print("Resposta Correta, Parábens🎉✨")
                            print("+15 Moedas da Torre 1")
                            mt1 += 15
                            continue

                        else:
                            print(f"Resposta Incorreta, A alternativa correta era {dados["correta"]}, -20 pontos de vida")
                            vd -= 20
                            print(f"Vida atual: {vd}")

                case 1:

                    if mt1 < 75:
                        print(f"{nom} não possui moedas suficientes da Torre 1 (75 moedas necessárias)")

                    else:
                        print("Torre 2 Selecionada")
                        
                        for pergunta, dados in pr2.items():
                            if vd <= 0:
                                print("Game Over💀👺💀👺")
                                break

                            print(f"\n{pergunta}")

                            for opcao in dados["opcoes"]:
                                print(opcao)

                            solut2 = str(input("Digite sua resposta: \n")).upper()

                            while solut2 != "A" and solut2 != "B" and solut2 != "C":
                                print("Resposta Inválida, -10 pontos de vida")
                                vd -= 10
                                

                                if vd <= 0:
                                    print("Game Over💀💀👺")
                                    break

                                solut2 = str(input("Digite sua resposta novamente: \n")).upper()

                            if vd <= 0:
                                break

                            if solut2 == dados["correta"]:
                                print("Resposta Correta, Parábens🎉✨")
                                print("+15 Moedas da Torre 2")
                                mt2 += 15
                                continue

                            else:
                                print(f"Resposta Incorreta, A alternativa correta era {dados["correta"]}, -25 pontos de vida")
                                vd -= 25
                                print(f"Vida atual: {vd}")

                case 2:

                    if mt2 < 75 and mt1 < 75:
                        print(f"{nom} não possui moedas suficientes da Torre 2 e da Torre 1 (75 moedas necessárias)")

                    else:
                        
                        print("Torre 3 Selecionada")
                        
                        for pergunta, dados in pr3.items():
                            if vd <= 0:
                                print("Game Over💀👺💀👺")
                                break

                            print(f"\n{pergunta}")

                            for opcao in dados["opcoes"]:
                                print(opcao)

                            solut3 = str(input("Digite sua resposta: \n")).upper()

                            while solut3 != "A" and solut3 != "B" and solut3 != "C":
                                print("Resposta Inválida, -10 pontos de vida")
                                vd -= 10
                                

                                if vd <= 0:
                                    print("Game Over💀💀👺")
                                    break

                                solut3 = str(input("Digite sua resposta novamente: \n")).upper()

                            if vd <= 0:
                                break

                            if solut3 == dados["correta"]:
                                print("Resposta Correta, Parábens🎉✨")
                                print("+15 Moedas da Torre 3")
                                mt3 += 15
                                continue

                            else:
                                print(f"Resposta Incorreta, A alternativa correta era {dados["correta"]}, -30 pontos de vida")
                                vd -= 30
                                print(f"Vida atual: {vd}")

        case 3:
            print("1 - Comprar")
            print("2 - Utilizar\n")

            seleper = int(input("Selecione uma opção para prosseguir\n"))

            while seleper < 1 or seleper > 2:
                print("Opção Inválida")
                seleper = int(input("Selecione uma opção para prosseguir\n"))


            match seleper:
                case 1:
                    print("\n1 - Pergaminho Torre 2 - 60 Moedas da Torre 1")
                    print("2 - Pergaminho Torre 3 - 60 Moedas da Torre 2")
                    print("3 - Pergaminho Desafio Absoluto - 80 Moedas da Torre 3\n")

                    selepercom = int(input("Selecione uma opção para prosseguir\n"))

                    while selepercom < 1 or selepercom > 3:
                        print("Opção Inválida")
                        selepercom = int(input("Selecione uma opção para prosseguir\n"))

                    if selepercom == 1 and mt1 >= 60:
                        if "Pergaminho 2" in inv:
                            print("Você já possui esse pergaminho\n")

                        else:
                            print("Pergaminho 2 Adquirido\n")
                            inv.append("Pergaminho 2")
                            mt1 -= 60

                    elif selepercom == 2 and mt2 >= 60:
                        if "Pergaminho 3" in inv:
                            print("Você já possui esse pergaminho\n")

                        else:
                            print("Pergaminho 3 Adquirido\n")
                            inv.append("Pergaminho 3")
                            mt2 -= 60

                    elif selepercom == 3 and mt3 >= 80:
                        if "Pergaminho Desafio" in inv:
                            print("Você já possui esse pergaminho\n")

                        else:
                            print("Pergaminho Desafio Adquirido\n")
                            inv.append("Pergaminho Desafio")
                            mt3 -= 80

                    else:
                        print("Saldo Insuficiente\n")

                case 2:
                    for i in range(len(inv)):
                        print(f"{i + 1} - {inv[i]}")

                    selepersel = int(input("\nSelecione uma opção para prosseguir: \n"))
                    opv = selepersel - 1

                    while opv < 0 or opv >= len(inv):
                        print("Opção Não Existente no Inventário")
                        selepersel = int(input("Selecione uma opção para prosseguir: \n"))
                        opv = selepersel - 1

                    item = inv[opv]

                    if selepersel == 1 and item == "Pergaminho 1":
                        print("O Novo Campo de Batalha Digital: A Inteligência Artificial na Cibersegurança")
                        print("A transformação digital trouxe para o centro do debate a constante evolução da segurança cibernética, onde a Inteligência Artificial passou a desempenhar um papel duplo e decisivo. Por um lado, os sistemas de proteção modernos apoiam-se na capacidade preditiva e no processamento massivo de dados para antecipar movimentos suspeitos, permitindo respostas quase instantâneas que evitam o colapso de redes inteiras. Por outro lado, essa mesma tecnologia tornou-se um instrumento poderoso para agentes maliciosos. A automação avançada possibilita a criação de táticas de invasão cada vez mais sofisticadas, que vão desde a construção de mensagens persuasivas para enganar os usuários até a manipulação direta dos próprios dados que alimentam os algoritmos de defesa, buscando criar pontos cegos na infraestrutura das organizações. Somado a isso, o avanço da sintetização de voz e imagem introduziu uma nova camada de complexidade às fraudes digitais, onde a fronteira entre o real e o simulado se torna cada vez mais tênue nas interações humanas. Diante desse cenário dinâmico, fica evidente que, por mais avançados que sejam os modelos computacionais, a eficiência da segurança da informação continua dependendo do fator humano — o único capaz de interpretar o contexto estratégico, avaliar nuances éticas e tomar decisões críticas no combate às ameaças virtuais.")

                    elif selepersel == 2 and item == "Pergaminho 2":
                        print("O Horizonte Oculto: Vulnerabilidades Avançadas em Sistemas de Inteligência Artificial")
                        print("À medida que os sistemas de IA tornam-se mais complexos, novos vetores de ataque específicos para essa tecnologia surgem. Um dos maiores desafios atuais é o 'Prompt Injection', onde invasores manipulam entradas de texto para burlar as travas de segurança de uma IA e forçá-la a executar comandos proibidos. Outro risco fascinante e perigoso são os 'Ataques Adversariais', nos quais pequenas alterações invisíveis a olho nu em imagens — como um ruído milimétrico — fazem com que algoritmos de reconhecimento visual confundam completamente objetos, interpretando uma placa de trânsito perigosa como uma placa comum. Além disso, existe a ameaça de 'Inversão de Modelo', técnica em que hackers utilizam as respostas da IA para reconstruir dados confidenciais que foram usados no seu treinamento, violando a privacidade. Para combater isso, cientistas usam a 'Privacidade Diferencial', que adiciona ruídos matemáticos controlados para anonimizar dados. Por fim, a regulamentação moderna exige a 'XAI' (IA Explicável), garantindo que as decisões de modelos complexos possam ser auditadas por humanos, evitando caixas-pretas irresponsáveis.")

                    elif selepersel == 3 and item == "Pergaminho 3":
                        print("A Fronteira Final: Cadeia de Suprimentos, Automação Autônoma e Biometria Comportamental")
                        print("No topo da segurança cibernética moderna, os desafios transcendem o código tradicional. Um dos perigos mais silenciosos é o envenenamento na Cadeia de Suprimentos de Modelos, onde desenvolvedores baixam pesos de redes neurais pré-treinadas de repositórios públicos que contêm backdoors ocultos conhecidos como 'Trojan Weights'. Para mitigar riscos sem expor dados corporativos sensíveis, as empresas adotam o Aprendizado Federado (Federated Learning), permitindo treinar IAs colaborativamente de forma descentralizada e criptografada. Na ponta da defesa, plataformas de resposta automatizada (SOAR) integradas a agentes de IA autônomos conseguem conter brechas em frações de segundo. Além disso, a autenticação estática por senhas deu lugar à Biometria Comportamental baseada em redes neurais, que analisa continuamente a forma como o usuário digita, move o mouse ou interage com o sistema para detectar intrusos em tempo real. Por fim, arquiteturas Zero Trust utilizam pontuações de risco dinâmicas calculadas por IA para revogar acessos instantaneamente diante de qualquer anomalia comportamental.")

                    elif selepersel == 4 and item == "Pergaminho Desafio":
                        print("O Códex Singular: Arquiteturas de Convergência em Defesa e Ofensiva de IA")
                        print("No ápice da segurança cibernética moderna, o ecossistema digital é regido por uma convergência implacável entre algoritmos autônomos e contramedidas avançadas. O vetor de ameaças abrange desde a adulteração inicial de dados de treinamento (Data Poisoning) para cegar modelos defensivos, até ataques sofisticados de injeção de prompt ('Prompt Injection') que sequestram LLMs corporativas. Na cadeia de suprimentos de inteligência artificial, o perigo reside nos 'Trojan Weights' — pesos de redes neurais pré-treinadas comprometidos por backdoors ocultos em repositórios abertos. Enquanto isso, adversários exploram vulnerabilidades físicas e lógicas através de ataques adversariais (ruídos imperceptíveis que corrompem a visão computacional) e inversões de modelo (reconstrução de dados confidenciais a partir das saídas da IA). Para neutralizar esse panorama, a arquitetura defensiva contemporânea exige uma simbiose complexa: o uso de Aprendizado Federado associado à Privacidade Diferencial para treinar modelos descentralizados de forma criptografada; a aplicação de biometria comportamental baseada em redes neurais para autenticação contínua em estruturas Zero Trust; e a integração de plataformas SOAR autônomas capazes de orquestrar enxames de defesa em microssegundos. Por fim, a auditabilidade através de IA Explicável (XAI) e o alinhamento rigoroso por feedback humano tornam-se as últimas barreiras contra a obsolescência humana diante de IAs auto-evolutivas.")

        case 4:

            if mt1 < 100 and mt2 < 100 and mt3 < 100:
                print(f"{nom} não possui moedas suficientes das Torres 1, 2 e 3 (120 Moedas necessárias)")

            else:
                print(f"Olá {nom}, seja bem vindo ao Desafio Final desse teste, Esse exercício abordará todos os temas citados anteriormente nas outras torres, mas tem Cybersegurança como seu tema principal, Aqui a dificuldade será aumentada, e você, sim, você, {nom} da Silva, precisa estar absurdamente preparado para esse desafio final dos anjos e dos demonios porque é dificil, portanto é necessário, ou melhor, recomendado que ja seja lido todos os pergaminhos enfim, chega de enrolação, boa sorte😄😃😃\n")

                print("Prepare-se...")

                for i in range(1, 6):
                    print(i)
                    time.sleep(1)

                print("\nVALENDO!!!! 📢 📢 ⏱")
                tq = 10
                tc = 0

            
                print("Desafio Absoluto Selecionado")
                                    
                for pergunta, dados in prd.items():
                    if vd <= 0:
                        print("Game Over💀👺💀👺")
                        break

                    print(f"\n{pergunta}")

                    for opcao in dados["opcoes"]:
                        print(opcao)

                    solutd = str(input("Digite sua resposta: \n")).upper()

                    while solutd != "A" and solutd != "B" and solutd != "C":
                        print("Resposta Inválida, -20 pontos de vida")
                        vd -= 20
                        

                        if vd <= 0:
                            print("Game Over💀💀👺")
                            break

                        solutd = str(input("Digite sua resposta novamente: \n")).upper()

                    if vd <= 0:
                        break

                    if solutd == dados["correta"]:
                        print("Resposta Correta, Parábens🎉✨")
                        tq -= 1
                        tc += 1
                        continue

                    else:
                        print(f"Resposta Incorreta, A alternativa correta era {dados["correta"]}, -45 pontos de vida")
                        vd -= 45
                        tq -= 1
                        print(f"Vida atual: {vd}")

                if tq <= 0:
                    if tc <= 4:
                        print(f"{nom} apenas acertou {tc} questoes....")

                    elif tc <= 6 and tc > 4:
                        print(f"{nom} acertou {tc} questoes, razoável")

                    elif tc <= 8 and tc > 6:
                        print(f"{nom} acertou {tc} questões, meus parábens")

                    else:
                        print(f"{nom} Meus Parabéns, Você acertou {tc} Questões, por conta disso, você conseguiu zerar o jogo, palmas🥳🥳")

                if tc == 9 or tc == 10:
                    time.sleep(1.3)
                    print("Créditos")
                    time.sleep(1.3)
                    print("Feito por:")
                    time.sleep(1.3)
                    print("Gustavo Nogueira de Sousa")
                    time.sleep(1.3)
                    print("Pedro Henrique Ferreira")
                    time.sleep(1.3)
                    print("Fernando Gabriel")
                    time.sleep(1.3)
                    print("Criado no VScode")
                    time.sleep(1.3)
                    print("Feito em 3 Dias")
                    time.sleep(1.3)
                    print("+680 Linhas de código")
                    time.sleep(1.3)
                    print("Tema: IA na Cyberseurança")
                    time.sleep(1.3)
                    print("E por ultimo, Muito obrigado Pryscilla, por proporcionar um trabalho tão interessante e relevante como esse")
                    time.sleep(1.3)
                    print("Esse vai pro GitHub")
                    time.sleep(1.3)
                    print("FIM")
                    time.sleep(1.3)
                    break
