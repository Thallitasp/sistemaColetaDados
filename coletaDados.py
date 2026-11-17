# coletaDados.py


class SistemaColetaDados:
    """
    Sistema básico de coleta e análise de dados de clientes para a empresa
    fictícia TechNova Soluções Digitais (Atividade Avaliativa Fase 1).
    """

    def __init__(self, nome_empresa: str = "TechNova Soluções Digitais") -> None:
        """
        Inicializa o sistema com o nome da empresa e a lista vazia de registros.

        Args:
            nome_empresa (str): Nome da empresa fictícia proprietária do sistema.
        """
        self.nome_empresa = nome_empresa
        self.registros: list[dict] = []

    def classificar_perfil_cliente(self, idade: int, renda: float, nota: int) -> str:
        """
        Aplica estruturas condicionais e operadores lógicos/relacionais para
        classificar o perfil de atendimento do cliente.

        Args:
            idade (int): Idade do cliente em anos.
            renda (float): Renda mensal informada em reais.
            nota (int): Nota de satisfação de 1 a 5.

        Returns:
            str: Classificação estratégica do cliente.
        """
        if renda >= 5000.0 and nota >= 4:
            return "Cliente VIP Promotor"
        elif idade < 25 and nota >= 4:
            return "Jovem Engajado"
        elif nota <= 2 or renda < 1500.0:
            return "Atenção / Retenção Prioritária"
        else:
            return "Cliente Padrão"

    def coletar_novo_cliente(self) -> None:
        """
        Executa o fluxo sequencial e repetitivo de coleta e validação de dados
        de um novo cliente.
        """
        print("\n" + "=" * 52)
        print(f"   COLETA DE DADOS — {self.nome_empresa.upper()}")
        print("=" * 52)

        # 1. Coleta de texto (str) com validação de campo não vazio
        while True:
            nome = input("Nome completo do cliente: ").strip()
            if len(nome) >= 3:
                break
            print("[Erro] O nome deve conter pelo menos 3 caracteres.")

        cidade = input("Cidade/UF de residência: ").strip()
        if not cidade:
            cidade = "Não informada"

        # 2. Coleta de inteiro (int) com operadores relacionais e lógicos
        while True:
            try:
                idade = int(input("Idade do cliente (18 a 110): ").strip())
                if 18 <= idade <= 110:
                    break
                print("[Erro] Idade fora da faixa permitida (18 a 110 anos).")
            except ValueError:
                print("[Erro] Digite um número inteiro válido para a idade.")

        # 3. Coleta de ponto flutuante (float) para renda mensal
        while True:
            try:
                entrada_renda = input("Renda mensal aproximada (R$): ").strip().replace(",", ".")
                renda = float(entrada_renda)
                if renda >= 0.0:
                    break
                print("[Erro] A renda mensal não pode ser negativa.")
            except ValueError:
                print("[Erro] Digite um valor numérico válido (ex: 3200.50).")

        # 4. Coleta de nota de satisfação (1 a 5)
        while True:
            try:
                nota = int(input("Nota de satisfação com nossos serviços (1 a 5): ").strip())
                if 1 <= nota <= 5:
                    break
                print("[Erro] A nota deve ser um número inteiro entre 1 e 5.")
            except ValueError:
                print("[Erro] Digite um número inteiro de 1 a 5.")

        # 5. Coleta booleana (bool) sobre interesse em novidades
        resposta_newsletter = input("Deseja receber novidades por e-mail? (S/N): ").strip().upper()
        aceita_contato: bool = resposta_newsletter == "S"

        # Processamento condicional do perfil
        perfil = self.classificar_perfil_cliente(idade, renda, nota)

        # Armazenamento estruturado do registro
        cliente = {
            "id": len(self.registros) + 1,
            "nome": nome,
            "cidade": cidade,
            "idade": idade,
            "renda": renda,
            "nota": nota,
            "aceita_contato": aceita_contato,
            "perfil": perfil,
        }
        self.registros.append(cliente)

        print("\n" + "-" * 52)
        print(f"[Sucesso] Cadastro #{cliente['id']} registrado para {nome}!")
        print(f"Classificação automática: {perfil}")
        print("-" * 52)

    def listar_clientes_cadastrados(self) -> None:
        """
        Percorre a lista de clientes coletados com um loop 'for' e exibe
        os dados formatados.
        """
        print("\n" + "=" * 52)
        print("           CLIENTES COLETADOS NO SISTEMA")
        print("=" * 52)

        if not self.registros:
            print("Nenhum registro coletado até o momento.")
            return

        for cliente in self.registros:
            contato_str = "Sim" if cliente["aceita_contato"] else "Não"
            print(
                f"ID: {cliente['id']:02d} | {cliente['nome']} ({cliente['idade']} anos - {cliente['cidade']})\n"
                f"         Renda: R$ {cliente['renda']:.2f} | Nota: {cliente['nota']}/5 | "
                f"Newsletter: {contato_str} | Perfil: {cliente['perfil']}"
            )
            print("-" * 52)

    def exibir_relatorio_geral(self) -> None:
        """
        Processa estatísticas consolidadas sobre todos os dados coletados
        utilizando estrutura de repetição 'for' e acumuladores.
        """
        print("\n" + "=" * 52)
        print(f"   RELATÓRIO ANALÍTICO — {self.nome_empresa.upper()}")
        print("=" * 52)

        total = len(self.registros)
        if total == 0:
            print("Não há dados suficientes para gerar o relatório.")
            return

        soma_idades = 0
        soma_rendas = 0.0
        soma_notas = 0
        promotores = 0
        opt_in_newsletter = 0

        for registro in self.registros:
            soma_idades += registro["idade"]
            soma_rendas += registro["renda"]
            soma_notas += registro["nota"]

            if registro["nota"] >= 4:
                promotores += 1

            if registro["aceita_contato"]:
                opt_in_newsletter += 1

        media_idade = soma_idades / total
        media_renda = soma_rendas / total
        media_nota = soma_notas / total
        taxa_satisfacao = (promotores / total) * 100

        print(f"Total de clientes entrevistados: {total}")
        print(f"Média de idade do público: {media_idade:.1f} anos")
        print(f"Renda mensal média: R$ {media_renda:.2f}")
        print(f"Nota média de satisfação: {media_nota:.2f} / 5.00")
        print(f"Clientes satisfeitos (notas 4 e 5): {promotores} ({taxa_satisfacao:.1f}%)")
        print(f"Aceitaram receber novidades: {opt_in_newsletter} de {total}")
        print("=" * 52)

    def executar_menu(self) -> None:
        """
        Mantém o menu interativo principal em execução utilizando loop 'while'.
        """
        while True:
            print("\n" + "#" * 52)
            print(f"  {self.nome_empresa.upper()} - COLETA DE DADOS")
            print("#" * 52)
            print("1 - Coletar dados de novo cliente")
            print("2 - Listar clientes cadastrados")
            print("3 - Exibir relatório estatístico consolidado")
            print("0 - Encerrar sistema")
            print("#" * 52)

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.coletar_novo_cliente()
            elif opcao == "2":
                self.listar_clientes_cadastrados()
            elif opcao == "3":
                self.exibir_relatorio_geral()
            elif opcao == "0":
                print("\nEncerrando o sistema de coleta de dados. Até logo!")
                break
            else:
                print("\n[Erro] Opção inválida! Digite 0, 1, 2 ou 3.")


if __name__ == "__main__":
    sistema = SistemaColetaDados()
    sistema.executar_menu()