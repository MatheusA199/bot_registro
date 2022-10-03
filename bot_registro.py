import pyautogui
import pyperclip
import time

def bot_registro():	

	resposta = entrada_resposta_tres()

	sim = verificacao_sim(resposta)
	nao = verificacao_nao(resposta)
	regras = verificacao_regras(resposta)

	if (sim):
		chamar_bot()

	elif (nao):
		escrever_linha_vazia()
		escrever_bot_encerrado()

	elif (regras):
		abrir_escrever_regras()
		escrever_linha_vazia()

		resposta_segunda = entrada_segunda_resposta()
		sim = verificacao_sim(resposta_segunda)
		nao = verificacao_nao(resposta_segunda)

		if (sim):
			chamar_bot()		

		elif(nao):
			escrever_linha_vazia()
			escrever_bot_encerrado()

	else:
		print('Entrada envalida!')
		escrever_bot_encerrado()


def escrever_mensagem_inicial():
	print('***********************************************')
	print('*Bem-Vindo ao Bot de fechar e abrir registros!*')
	print('***********************************************')

def entrada_resposta_tres():
	resposta = str(input('Está tudo correto para executar o script? Digite S(sim), N(não) ou R(exibir requisitos)\n'))
	return resposta

def verificacao_sim(resposta):
	sim = (resposta.lower().strip() == 's')
	return sim

def verificacao_nao(resposta):
	nao = (resposta.lower().strip() == 'n')
	return nao

def verificacao_regras(resposta):
	regras = (resposta.lower().strip() == 'r')
	return regras

def escrever_bot_encerrado():
	print('Bot encerrado.')

def abrir_escrever_regras():
	arquivo = open('regras.txt', 'r', encoding='utf-8')
	regras_escritas = [linha for linha in arquivo]
	arquivo.close()
	print(*regras_escritas)


def escrever_linha_vazia():
	print('')

def entrada_segunda_resposta():
	resposta_segunda = str(input('Agora, deseja rodar o script? S(sim) ou N(não)\n'))
	return resposta_segunda

def contar_10segundos():
	print('O bot começará em 10 segundos!')

	time.sleep(10)
	print('Começou!')
	

def chamar_bot():
	ocorrencia = []	
	contador = 0
	#abrir_arquivo_casos(ocorrencia)
	contar_10segundos()
	abrir_chrome()
	pyautogui.PAUSE = 2
	casos_abrir_direto()
	for i in ocorrencia:
		caso = i
		processos_bot_odair(caso)
	
	escrever_bot_encerrado()

def abrir_arquivo_casos(ocorrencia):
	arquivo = open('casos.txt', 'r', encoding='utf-8')

	for linha in arquivo:
		linha = linha.strip()
		caso = linha.split(' - ')

		linha = linha.strip()
		ocorrencia.append(linha.split(' - '))

	return ocorrencia

def casos_abrir_direto():
	arquivo = open('casos.txt', 'r', encoding='utf-8')
	for linha in arquivo:
		linha = linha.strip().linha.split(' - ')
		caso = linha
		processos_bot_odair(caso)

	escrever_bot_encerrado()

def processos_bot_odair(caso):
	escrever_linha_vazia()
	abrir_chamado(caso)
	trocar_aba_frente()
	clicar_chamado_certo()
	trocar_aba_frente()
	colocar_nome_colaborador(caso)
	clicar_primeiro_fechamento()
	apagar_texto_descricao()
	colocar_descricao(caso)
	fechar_chamado()
	clicar_segundo_chamado()
	apagar_texto_descricao()
	colocar_descricao(caso)
	fechar_chamado()
	fechar_aba_registro_fechado()
	voltar_aba_abrir_registro()
	
def abrir_chrome():
	pyautogui.PAUSE = 2
	pyautogui.click(x=70, y=1005)


def abrir_chamado(caso):
	pyautogui.click(x=482, y=575)
	pyautogui.click(x=122, y=531)

	pyautogui.click(x=744, y=764)

	pyautogui.click(x=199, y=553)
	pyperclip.copy(caso[1])
	pyautogui.hotkey('ctrl','v')
	pyautogui.press('enter')

	pyautogui.press('tab')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.press('tab')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.press('tab')
	pyperclip.copy(caso[2])
	pyautogui.hotkey('ctrl','v')
	pyautogui.write('.')
	pyautogui.click(x=1060, y=271)

def trocar_aba_frente():
	pyautogui.hotkey('ctrl', 'tab')

def clicar_chamado_certo():
	pyautogui.PAUSE = 5
	pyautogui.press('f5')

	pyautogui.PAUSE = 2
	pyautogui.moveTo(x=431, y=280)
	pyautogui.click(button='middle')


def colocar_nome_colaborador(caso):
	pyautogui.click(x=901, y=288)
	pyperclip.copy(caso[0])
	pyautogui.hotkey('ctrl','v')
	pyautogui.press('down')
	pyautogui.press('enter')
	pyautogui.click(x=1175, y=95)

def clicar_primeiro_fechamento():
	pyautogui.click(x=35, y=265)
	pyautogui.press('end')
	pyautogui.click(x=176, y=838)


def apagar_texto_descricao():
	pyautogui.click(x=598, y=400)
	pyautogui.PAUSE = 0.15
	mensagem_apagar = 'Avaliação ou escopo da tarefa'
	for i in range(len(mensagem_apagar)):
		pyautogui.press('backspace')
	pyautogui.press('backspace')
	pyautogui.press('backspace')
	pyautogui.press('backspace')
	pyautogui.press('delete')

def colocar_descricao(caso):
	pyautogui.PAUSE = 2
	pyperclip.copy(caso[2])
	pyautogui.hotkey('ctrl','v')
	pyautogui.write('.')
	pyautogui.press('tab')

	pyperclip.copy(caso[2])
	pyautogui.hotkey('ctrl','v')
	pyautogui.write('.')

def fechar_chamado():
	pyautogui.click(x=1082, y=95)

def clicar_segundo_chamado():
	pyautogui.click(x=58, y=137)
	pyautogui.press('end')
	pyautogui.click(x=176, y=795)

def fechar_aba_registro_fechado():
	pyautogui.hotkey('ctrl', 'w')

def voltar_aba_abrir_registro():
	pyautogui.hotkey('ctrl', 'shift', 'tab')
	pyautogui.click(x=117, y=170)

if(__name__ == '__main__'):
	bot_registro()