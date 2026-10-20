#!/usr/bin/env python3
"""Gera 3 propostas de layout da página inicial em site/propostas/."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site" / "propostas"
A = "../assets/img/"

def ic(d):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I = {
 "user": ic('<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/>'),
 "phone": ic('<rect x="6" y="2" width="12" height="20" rx="2"/><line x1="11" y1="18" x2="13" y2="18"/>'),
 "mail": ic('<rect x="2" y="4" width="20" height="16" rx="1"/><polyline points="2 5 12 13 22 5"/>'),
 "pin": ic('<path d="M12 22s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/>'),
 "gauge": ic('<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/>'),
 "car": ic('<path d="M3 15v-3l2-5a2 2 0 0 1 1.9-1.4h10.2A2 2 0 0 1 19 7l2 5v3"/><rect x="2" y="12" width="20" height="5" rx="1.5"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>'),
 "check": ic('<polyline points="4 12 10 18 20 6"/>'),
 "clock": ic('<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 16 14"/>'),
 "shield": ic('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><polyline points="8.5 12 11 14.5 15.5 9.5"/>'),
 "euro": ic('<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5a4 4 0 1 0 0 7"/><line x1="7" y1="11" x2="13" y2="11"/><line x1="7" y1="13.5" x2="13" y2="13.5"/>'),
 "doc": ic('<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><polyline points="14 3 14 8 19 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="13" y2="17"/>'),
 "seta": ic('<line x1="4" y1="12" x2="20" y2="12"/><polyline points="13 5 20 12 13 19"/>'),
 "whats": '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6.3-.5c.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.2-1.2 2.9s1.2 3.4 1.4 3.6c.2.2 2.4 3.7 5.9 5.2.8.4 1.5.6 2 .7.8.3 1.6.2 2.2.1.7-.1 1.9-.8 2.2-1.6.3-.8.3-1.4.2-1.6-.1-.1-.3-.2-.6-.4z"/></svg>',
}

def campo(icone, controlo, largo=False):
    return f'<label class="f-campo{" largo" if largo else ""}">{I[icone]}{controlo}</label>'
def inp(rot, tipo="text"):
    return f'<input type="{tipo}" placeholder="{rot}" aria-label="{rot}">'
def sel(rot):
    return f'<select aria-label="{rot}"><option>{rot}</option></select>'

CONTACTO = [campo("user", inp("Nome")), campo("phone", inp("Telefone", "tel")),
            campo("mail", inp("E-mail", "email")), campo("pin", sel("Distrito"))]
VIATURA = [campo("gauge", inp("KM do carro")), campo("car", inp("Matrícula do carro")),
           campo("car", sel("Ano do Carro")), campo("car", sel("Mês do Carro")),
           campo("car", sel("Marca do carro")), campo("car", sel("Modelo do carro")),
           campo("car", inp("Versão do carro")), campo("car", sel("Transmissão"))]
CONSENT = '<label class="f-consent"><input type="checkbox"><span>Os dados recolhidos serão incluídos na nossa agenda de contactos, de acordo com a legislação de proteção de dados em vigor, apenas para facilitar futuros contactos da Compramos Carros. <a href="../politica-de-privacidade.html">Para saber mais sobre a nossa Política de Privacidade clique aqui.</a></span></label>'

PASSOS = [("avaliamos", "Avaliamos o seu carro", "Avalie o seu carro conosco e descubra o verdadeiro valor do seu veículo."),
          ("oferta", "Fazemos a oferta", "Fazemos a oferta mais competitiva para o seu veículo. Confie em nós para obter o melhor negócio possível."),
          ("finalizamos", "Finalizamos a compra", "Finalizamos a compra do seu carro de forma rápida e sem complicações.")]
VANTAGENS = [("clock", "Proposta em 24 horas", "Em 24 horas irá receber uma proposta (por email ou contacto telefónico) que será válida por 7 dias úteis."),
             ("euro", "Pagamento por transferência bancária imediata", "Para maior conforto, realizamos o pagamento por transferência bancária imediata."),
             ("doc", "Transferência de propriedade em 48H", "Todo o processo será verificado e devidamente documentado (com cópias de todos os documentos)."),
             ("shield", "Segurança em todo o processo", "Todo o procedimento é acompanhado de documentos que comprovam e validam a transação.")]
EQUIPA = [("francisco-matos", "Francisco Matos"), ("manuel-gama-barros", "Manuel Gama Barros"), ("bernardo-soares", "Bernardo Soares")]

def pagina(nome, titulo_prop, css, corpo):
    html = f"""<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Compramos Carros — {titulo_prop}</title>
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="base.css">
<style>{css}</style>
</head>
<body>
<header class="topo"><div class="contentor">
  <a href="#"><img src="{A}logo.svg" alt="Compramos Carros" width="176" height="42"></a>
  <nav><a href="#">Como funciona</a><a href="#">Quem Somos</a><a href="#">Centro de Entregas</a><a href="#">Contactos</a><a class="botao" href="#avaliacao">Avaliação grátis</a></nav>
</div></header>
<main>
{corpo}
</main>
<footer class="rodape"><div class="contentor">
  <div class="grelha">
    <div class="marca"><img src="{A}logo.svg" alt="Compramos Carros"><p>Uma marca desenvolvida pela MGB Automóveis.</p></div>
    <div><h4>Navegação</h4><ul><li><a href="#">Como funciona</a></li><li><a href="#">Quem Somos</a></li><li><a href="#">Centro de Entregas</a></li><li><a href="#">Contactos</a></li></ul></div>
    <div><h4>Contactos</h4><ul><li>Stand Automóveis MGB</li><li>Estrada Nacional 249-4 Vivenda Garcia</li><li>2785-574 S. Domingos de Rana</li><li><a href="tel:+351912263717">912 263 717</a></li></ul></div>
    <div><h4>Informação</h4><ul><li><a href="#">Política de privacidade</a></li><li><a href="#">Política de cookies</a></li><li><a href="#">Livro de reclamações</a></li><li>Seg a Sex das 9h às 19h<br>Sábado das 10h às 18h</li></ul></div>
  </div>
  <p class="base">© 2026 Compramos Carros. Todos os direitos reservados.</p>
</div></footer>
<a class="whatsapp" href="https://wa.me/351912263717" aria-label="WhatsApp">{I["whats"]}</a>
<a class="etiqueta-proposta" href="index.html">{titulo_prop} · ver outras propostas</a>
</body>
</html>"""
    (OUT / nome).write_text(html, encoding="utf-8")

# =====================================================================
# Proposta A — "Clara": fundo claro, título azul-escuro, faixa de confiança
# =====================================================================
css_a = """
.heroi { position: relative; padding: 64px 0 80px; background: linear-gradient(180deg, #eef8f6 0%, #fff 70%); }
.heroi::before { content: ""; position: absolute; right: -180px; top: -180px; width: 560px; height: 560px; border-radius: 50%; background: radial-gradient(circle, rgba(27,153,139,.18), transparent 65%); }
.heroi .grelha { display: grid; grid-template-columns: 1.05fr 1fr; gap: 56px; align-items: center; position: relative; }
.selo { display: inline-flex; gap: 8px; align-items: center; background: #fff; border: 1px solid var(--linha); border-radius: 999px; padding: 7px 14px 7px 8px; font-weight: 700; color: var(--verde); font-size: 14px; box-shadow: 0 4px 14px rgba(0,0,0,.05); margin-bottom: 22px; }
.selo span { background: var(--lima); color: var(--azul); border-radius: 999px; padding: 3px 10px; font-weight: 800; }
.heroi h1 { font-size: clamp(40px, 5.4vw, 70px); font-weight: 800; text-transform: uppercase; letter-spacing: -.01em; }
.heroi h1 em { font-style: normal; color: var(--verde); position: relative; white-space: nowrap; }
.heroi h1 em::after { content: ""; position: absolute; left: 0; right: 0; bottom: .06em; height: .22em; background: var(--lima); z-index: -1; border-radius: 4px; }
.heroi .sub { font-size: 21px; color: var(--suave); max-width: 520px; }
.heroi .sub b { color: var(--azul); }
.foto-heroi { position: relative; margin-top: 30px; }
.foto-heroi img { border-radius: 22px; width: 100%; max-width: 520px; aspect-ratio: 16/10; object-fit: cover; box-shadow: 0 20px 50px rgba(46,41,78,.18); }
.foto-heroi .bolha { position: absolute; left: -18px; bottom: -22px; background: var(--azul); color: #fff; border-radius: 16px; padding: 14px 18px; display: flex; gap: 12px; align-items: center; box-shadow: 0 14px 30px rgba(46,41,78,.3); }
.foto-heroi .bolha svg { width: 34px; height: 34px; color: var(--lima); }
.foto-heroi .bolha b { display: block; font-size: 18px; }
.cartao { background: #fff; border-radius: 22px; box-shadow: 0 24px 60px rgba(46,41,78,.14); padding: 30px; border-top: 6px solid var(--lima); }
.cartao h2 { font-size: 24px; text-transform: uppercase; margin-bottom: 4px; }
.cartao .ajuda { color: var(--suave); margin-bottom: 20px; }
.cartao .botao { width: 100%; justify-content: center; margin-top: 20px; }
.confianca { background: var(--azul); color: #fff; }
.confianca .contentor { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; }
.confianca div { display: flex; gap: 14px; align-items: center; padding: 26px 22px; border-right: 1px solid rgba(255,255,255,.1); font-weight: 700; }
.confianca div:last-child { border: 0; }
.confianca svg { width: 34px; height: 34px; flex: 0 0 34px; color: var(--lima); }
.passos { padding: 90px 0; text-align: center; }
.passos .rotulo { color: var(--verde); font-weight: 800; letter-spacing: .12em; text-transform: uppercase; font-size: 14px; }
.passos h2 { font-size: clamp(32px, 4vw, 46px); text-transform: uppercase; margin-bottom: 48px; }
.passos .grelha { display: grid; grid-template-columns: repeat(3, 1fr); gap: 26px; }
.passo { background: var(--fundo); border-radius: 22px; padding: 40px 28px 34px; position: relative; text-align: center; transition: transform .2s, box-shadow .2s; }
.passo:hover { transform: translateY(-6px); box-shadow: 0 20px 40px rgba(46,41,78,.1); background: #fff; }
.passo .num { position: absolute; top: -18px; left: 50%; transform: translateX(-50%); width: 40px; height: 40px; border-radius: 50%; background: var(--lima); color: var(--azul); font-weight: 900; display: grid; place-items: center; font-size: 18px; }
.passo img { width: 74px; margin: 0 auto 16px; }
.passo h3 { text-transform: uppercase; font-size: 20px; }
.passo p { color: var(--suave); margin: 0; }
.cta { background: linear-gradient(120deg, var(--verde), #24667a 55%, var(--azul)); color: #fff; border-radius: 26px; padding: 50px; display: flex; justify-content: space-between; align-items: center; gap: 30px; margin-bottom: 90px; position: relative; overflow: hidden; }
.cta::after { content: ""; position: absolute; right: -60px; bottom: -80px; width: 220px; height: 220px; border: 28px solid var(--lima); border-radius: 50%; opacity: .9; }
.cta h2 { color: #fff; font-size: clamp(26px, 3vw, 38px); text-transform: uppercase; margin: 0; position: relative; z-index: 1; }
.cta h2 span { color: var(--lima); }
.cta .botao { position: relative; z-index: 1; flex: 0 0 auto; }
@media (max-width: 960px) {
  .heroi .grelha { grid-template-columns: 1fr; }
  .confianca .contentor { grid-template-columns: 1fr 1fr; }
  .confianca div:nth-child(2) { border-right: 0; }
  .passos .grelha { grid-template-columns: 1fr; gap: 40px; }
  .cta { flex-direction: column; text-align: center; padding: 40px 24px; }
}
@media (max-width: 560px) { .confianca .contentor { grid-template-columns: 1fr; } .confianca div { border-right: 0; border-bottom: 1px solid rgba(255,255,255,.1); padding: 18px 4px; } .foto-heroi { display: none; } }
"""
corpo_a = f"""
<section class="heroi" id="avaliacao"><div class="contentor grelha">
  <div>
    <div class="selo"><span>3 etapas</span> Peça a sua avaliação grátis</div>
    <h1>A forma fácil de <em>vender</em> o seu carro</h1>
    <p class="sub">Em apenas <b>3 etapas</b> compramos o seu carro de <b>forma simplificada e justa!</b></p>
    <div class="foto-heroi"><img src="{A}quem-somos.jpg" alt=""><div class="bolha">{I["clock"]}<div><b>Proposta em 24 horas</b>válida por 7 dias úteis</div></div></div>
  </div>
  <form class="cartao" onsubmit="return false">
    <h2>Marque agora a avaliação do seu veículo!</h2>
    <p class="ajuda">Preencha o formulário e aproveite uma avaliação gratuita!</p>
    <div class="f-grelha">{''.join(CONTACTO + VIATURA)}</div>
    {CONSENT}
    <button class="botao">Pedir avaliação grátis {I["seta"].replace('<svg', '<svg width="20" height="20"')}</button>
  </form>
</div></section>
<section class="confianca"><div class="contentor">{''.join(f'<div>{I[i]}<span>{t}</span></div>' for i, t, _ in VANTAGENS)}</div></section>
<section class="passos"><div class="contentor">
  <p class="rotulo">Como funciona</p>
  <h2>Processo simplificado</h2>
  <div class="grelha">{''.join(f'<div class="passo"><span class="num">{n}</span><img src="{A}icones/{f}.png" alt=""><h3>{t}</h3><p>{d}</p></div>' for n, (f, t, d) in enumerate(PASSOS, 1))}</div>
</div></section>
<div class="contentor"><div class="cta"><h2>Peça a sua <span>avaliação grátis</span></h2><a class="botao" href="#avaliacao">Pedir avaliação grátis</a></div></div>
"""
pagina("proposta-a.html", "Proposta A · Clara", css_a, corpo_a)

# =====================================================================
# Proposta B — "Imersiva": fotografia em fundo, cronologia e equipa
# =====================================================================
css_b = """
.heroi { position: relative; color: #fff; padding: 80px 0 120px; background: url('../assets/img/inicio-processo.webp') right center / cover no-repeat; }
.heroi::before { content: ""; position: absolute; inset: 0; background: linear-gradient(100deg, rgba(46,41,78,.97) 0%, rgba(46,41,78,.9) 38%, rgba(27,153,139,.75) 100%); }
.heroi .grelha { position: relative; display: grid; grid-template-columns: 1fr 470px; gap: 60px; align-items: center; }
.heroi h1 { color: #fff; font-size: clamp(42px, 5.6vw, 76px); font-weight: 900; text-transform: uppercase; line-height: 1.02; }
.heroi h1 span { color: var(--lima); display: block; }
.heroi .sub { font-size: 22px; color: rgba(255,255,255,.9); max-width: 540px; }
.heroi .sub b { color: var(--lima); }
.heroi .lista { list-style: none; padding: 0; margin: 28px 0 34px; display: grid; gap: 12px; }
.heroi .lista li { display: flex; gap: 12px; align-items: center; font-weight: 600; font-size: 17px; }
.heroi .lista svg { width: 24px; height: 24px; background: var(--lima); color: var(--azul); border-radius: 50%; padding: 4px; flex: 0 0 24px; }
.cartao { background: rgba(255,255,255,.97); border-radius: 20px; padding: 28px; color: var(--texto); box-shadow: 0 30px 70px rgba(0,0,0,.35); backdrop-filter: blur(6px); }
.cartao h2 { font-size: 22px; text-transform: uppercase; text-align: center; margin-bottom: 18px; }
.cartao h2 span { display: block; color: var(--verde); font-size: 15px; letter-spacing: .1em; }
.cartao .botao { width: 100%; justify-content: center; margin-top: 18px; }
.onda { display: block; width: 100%; height: 70px; margin-top: -69px; position: relative; }
.cronologia { padding: 70px 0 90px; }
.cronologia h2, .equipa h2 { text-align: center; font-size: clamp(32px, 4vw, 46px); text-transform: uppercase; margin-bottom: 56px; }
.cronologia .linha { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; position: relative; }
.cronologia .linha::before { content: ""; position: absolute; left: 16%; right: 16%; top: 44px; height: 4px; background: repeating-linear-gradient(90deg, var(--lima) 0 14px, transparent 14px 24px); }
.etapa { text-align: center; position: relative; }
.etapa .circulo { width: 92px; height: 92px; border-radius: 50%; background: #fff; border: 4px solid var(--verde); display: grid; place-items: center; margin: 0 auto 22px; position: relative; box-shadow: 0 10px 24px rgba(27,153,139,.2); }
.etapa .circulo img { width: 54px; }
.etapa .circulo b { position: absolute; top: -8px; right: -8px; width: 32px; height: 32px; border-radius: 50%; background: var(--laranja); color: #fff; display: grid; place-items: center; font-size: 15px; }
.etapa h3 { text-transform: uppercase; font-size: 20px; }
.etapa p { color: var(--suave); max-width: 320px; margin: 0 auto; }
.distingue { background: var(--fundo); padding: 90px 0; }
.distingue .grelha { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
.distingue img { border-radius: 24px; box-shadow: 0 24px 50px rgba(46,41,78,.18); }
.distingue h2 { font-size: clamp(30px, 3.6vw, 42px); text-transform: uppercase; }
.distingue .item { display: flex; gap: 16px; margin-top: 22px; }
.distingue .item svg { width: 46px; height: 46px; flex: 0 0 46px; padding: 10px; border-radius: 12px; background: var(--azul); color: var(--lima); }
.distingue .item h3 { font-size: 18px; margin: 0 0 4px; }
.distingue .item p { margin: 0; color: var(--suave); }
.equipa { padding: 90px 0; }
.equipa .grelha { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
.membro { position: relative; border-radius: 22px; overflow: hidden; }
.membro img { width: 100%; aspect-ratio: 4/5; object-fit: cover; transition: transform .4s; }
.membro:hover img { transform: scale(1.04); }
.membro h3 { position: absolute; left: 14px; right: 14px; bottom: 14px; margin: 0; background: rgba(46,41,78,.9); color: #fff; padding: 12px 16px; border-radius: 12px; font-size: 16px; text-transform: uppercase; border-left: 5px solid var(--lima); }
@media (max-width: 960px) {
  .heroi .grelha, .distingue .grelha { grid-template-columns: 1fr; }
  .cronologia .linha { grid-template-columns: 1fr; gap: 44px; }
  .cronologia .linha::before { display: none; }
  .equipa .grelha { grid-template-columns: 1fr; max-width: 380px; margin: 0 auto; }
}
"""
corpo_b = f"""
<section class="heroi" id="avaliacao"><div class="contentor grelha">
  <div>
    <h1>A forma fácil de <span>vender o seu carro</span></h1>
    <p class="sub">Em apenas <b>3 etapas</b> compramos o seu carro de <b>forma simplificada e justa!</b></p>
    <ul class="lista">{''.join(f'<li>{I["check"]}{t}</li>' for _, t, _ in VANTAGENS[:3])}</ul>
    <a class="botao contorno" href="#processo">Como funciona</a>
  </div>
  <form class="cartao" onsubmit="return false">
    <h2><span>Marque agora</span>A avaliação do seu veículo!</h2>
    <div class="f-grelha">{''.join(CONTACTO + VIATURA)}</div>
    {CONSENT}
    <button class="botao">Pedir avaliação grátis</button>
  </form>
</div></section>
<svg class="onda" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70V30C240 0 480 0 720 25s480 45 720 15v30z" fill="#fff"/></svg>
<section class="cronologia" id="processo"><div class="contentor">
  <h2>Processo simplificado</h2>
  <div class="linha">{''.join(f'<div class="etapa"><div class="circulo"><img src="{A}icones/{f}.png" alt=""><b>{n}</b></div><h3>{t}</h3><p>{d}</p></div>' for n, (f, t, d) in enumerate(PASSOS, 1))}</div>
</div></section>
<section class="distingue"><div class="contentor grelha">
  <img src="{A}quem-somos-distingue.jpg" alt="">
  <div>
    <h2>O que nos distingue</h2>
    {''.join(f'<div class="item">{I[i]}<div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in [VANTAGENS[0], VANTAGENS[3], VANTAGENS[1]])}
  </div>
</div></section>
<section class="equipa"><div class="contentor">
  <h2>A equipa</h2>
  <div class="grelha">{''.join(f'<div class="membro"><img src="{A}equipa-{f}.jpg" alt="{n}"><h3>{n}</h3></div>' for f, n in EQUIPA)}</div>
</div></section>
"""
pagina("proposta-b.html", "Proposta B · Imersiva", css_b, corpo_b)

# =====================================================================
# Proposta C — "Arrojada": diagonais, números grandes e formulário em 2 passos
# =====================================================================
css_c = """
.heroi { position: relative; background: var(--verde); color: #fff; padding: 70px 0 150px; clip-path: polygon(0 0, 100% 0, 100% 86%, 0 100%); overflow: hidden; }
.heroi::before { content: ""; position: absolute; inset: 0; background: linear-gradient(135deg, transparent 45%, var(--azul) 45%); opacity: .95; }
.heroi::after { content: "COMPRAMOS"; position: absolute; left: -10px; bottom: 40px; font: 900 190px/1 "Barlow", sans-serif; color: rgba(255,255,255,.06); letter-spacing: -.02em; white-space: nowrap; }
.heroi .grelha { position: relative; z-index: 1; display: grid; grid-template-columns: 1.1fr 1fr; gap: 50px; align-items: center; }
.heroi h1 { color: #fff; font-size: clamp(46px, 6.4vw, 92px); font-weight: 900; text-transform: uppercase; line-height: .95; letter-spacing: -.02em; }
.heroi h1 .lima { color: var(--lima); }
.heroi h1 .contorno { -webkit-text-stroke: 2px #fff; color: transparent; }
.heroi .sub { font-size: 22px; max-width: 520px; }
.heroi .sub b { color: var(--lima); }
.heroi .numeros { display: flex; gap: 34px; margin-top: 30px; }
.heroi .numeros div { border-left: 4px solid var(--lima); padding-left: 14px; }
.heroi .numeros b { display: block; font-size: 40px; font-weight: 900; line-height: 1; color: var(--lima); }
.heroi .numeros span { font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: .04em; }
.cartao { background: #fff; color: var(--texto); border-radius: 6px 40px 6px 40px; padding: 30px; box-shadow: 18px 18px 0 var(--lima), 0 30px 60px rgba(0,0,0,.3); }
.cartao .cab { display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; }
.cartao h2 { font-size: 22px; text-transform: uppercase; margin: 0; }
.progresso { display: flex; gap: 6px; }
.progresso i { width: 34px; height: 6px; border-radius: 4px; background: var(--linha); }
.progresso i.ativo { background: var(--verde); }
.passo-form { display: none; }
.passo-form.ativo { display: block; }
.passo-form .titulo { font-weight: 800; color: var(--verde); text-transform: uppercase; font-size: 14px; letter-spacing: .08em; margin-bottom: 12px; }
.acoes { display: flex; justify-content: space-between; align-items: center; margin-top: 20px; gap: 12px; }
.acoes .voltar { background: none; border: 0; font: 700 15px "Barlow", sans-serif; color: var(--suave); cursor: pointer; }
.etapas { padding: 30px 0 90px; }
.etapas h2 { font-size: clamp(36px, 5vw, 64px); font-weight: 900; text-transform: uppercase; line-height: 1; margin-bottom: 50px; }
.etapas h2 span { color: var(--verde); }
.etapas .grelha { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; border-top: 3px solid var(--azul); }
.etapa { padding: 34px 30px 10px 0; position: relative; }
.etapa + .etapa { padding-left: 30px; border-left: 1px solid var(--linha); }
.etapa .n { font: 900 84px/1 "Barlow", sans-serif; color: var(--lima); -webkit-text-stroke: 2px var(--azul); }
.etapa img { width: 58px; position: absolute; right: 18px; top: 40px; opacity: .9; }
.etapa h3 { text-transform: uppercase; font-size: 22px; margin-top: 10px; }
.etapa p { color: var(--suave); }
.faixa { background: var(--azul); color: #fff; padding: 70px 0; position: relative; overflow: hidden; }
.faixa .grelha { display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; position: relative; }
.faixa svg { width: 40px; height: 40px; color: var(--lima); margin-bottom: 12px; }
.faixa h3 { color: #fff; font-size: 19px; text-transform: uppercase; }
.faixa p { color: #c9c7d6; font-size: 15px; margin: 0; }
.final { padding: 90px 0; text-align: center; }
.final h2 { font-size: clamp(34px, 5vw, 60px); font-weight: 900; text-transform: uppercase; line-height: 1; }
.final h2 span { background: var(--lima); padding: 0 12px; }
.final .botao { margin-top: 26px; font-size: 18px; padding: 20px 36px; }
@media (max-width: 960px) {
  .heroi { clip-path: polygon(0 0, 100% 0, 100% 95%, 0 100%); padding-bottom: 90px; }
  .heroi .grelha, .etapas .grelha { grid-template-columns: 1fr; }
  .etapa + .etapa { padding-left: 0; border-left: 0; border-top: 1px solid var(--linha); }
  .faixa .grelha { grid-template-columns: 1fr 1fr; }
  .heroi::after { font-size: 90px; }
  .cartao { box-shadow: 10px 10px 0 var(--lima), 0 20px 40px rgba(0,0,0,.3); }
}
@media (max-width: 560px) { .faixa .grelha { grid-template-columns: 1fr; } .heroi .numeros { gap: 18px; } .heroi .numeros b { font-size: 30px; } }
"""
corpo_c = f"""
<section class="heroi" id="avaliacao"><div class="contentor grelha">
  <div>
    <h1>A forma <span class="contorno">fácil</span> de <span class="lima">vender</span> o seu carro</h1>
    <p class="sub">Em apenas <b>3 etapas</b> compramos o seu carro de <b>forma simplificada e justa!</b></p>
    <div class="numeros"><div><b>24h</b><span>Proposta</span></div><div><b>7</b><span>Dias úteis de validade</span></div><div><b>48H</b><span>Transferência</span></div></div>
  </div>
  <form class="cartao" onsubmit="return false">
    <div class="cab"><h2>Marque agora</h2><div class="progresso"><i class="ativo"></i><i></i></div></div>
    <div class="passo-form ativo" data-passo="1">
      <p class="titulo">1. Os seus dados</p>
      <div class="f-grelha">{''.join(c.replace('f-campo"', 'f-campo largo"') for c in CONTACTO)}</div>
      <div class="acoes"><span></span><button class="botao" type="button" data-avancar>Seguinte {I["seta"].replace('<svg', '<svg width="20" height="20"')}</button></div>
    </div>
    <div class="passo-form" data-passo="2">
      <p class="titulo">2. O seu carro</p>
      <div class="f-grelha">{''.join(VIATURA)}</div>
      {CONSENT}
      <div class="acoes"><button class="voltar" type="button" data-voltar>← Voltar</button><button class="botao">Pedir avaliação grátis</button></div>
    </div>
  </form>
</div></section>
<section class="etapas"><div class="contentor">
  <h2>Processo <span>simplificado</span></h2>
  <div class="grelha">{''.join(f'<div class="etapa"><div class="n">0{n}</div><img src="{A}icones/{f}.png" alt=""><h3>{t}</h3><p>{d}</p></div>' for n, (f, t, d) in enumerate(PASSOS, 1))}</div>
</div></section>
<section class="faixa"><div class="contentor grelha">{''.join(f'<div>{I[i]}<h3>{t}</h3><p>{d}</p></div>' for i, t, d in VANTAGENS)}</div></section>
<section class="final"><div class="contentor">
  <h2>Peça a sua <span>avaliação grátis</span></h2>
  <a class="botao" href="#avaliacao">Pedir avaliação grátis</a>
</div></section>
<script>
(function () {{
  var f = document.querySelector('.cartao'), p = f.querySelectorAll('.passo-form'), b = f.querySelectorAll('.progresso i');
  function ir(n) {{ p.forEach(function (x, i) {{ x.classList.toggle('ativo', i === n); }}); b.forEach(function (x, i) {{ x.classList.toggle('ativo', i <= n); }}); }}
  f.querySelector('[data-avancar]').addEventListener('click', function () {{ ir(1); }});
  f.querySelector('[data-voltar]').addEventListener('click', function () {{ ir(0); }});
}})();
</script>
"""
pagina("proposta-c.html", "Proposta C · Arrojada", css_c, corpo_c)

# Índice das propostas
(OUT / "index.html").write_text(f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Compramos Carros — Propostas de layout</title>
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="base.css">
<style>
body {{ background: linear-gradient(180deg, var(--verde), var(--azul)); min-height: 100vh; color: #fff; }}
.c {{ max-width: 980px; margin: 0 auto; padding: 50px 20px; }}
.c > img {{ width: 200px; background: #fff; padding: 12px 16px; border-radius: 12px; }}
h1 {{ color: #fff; font-size: 40px; text-transform: uppercase; margin: 30px 0 6px; }}
.g {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 30px; }}
.g a {{ background: #fff; color: var(--azul); text-decoration: none; border-radius: 18px; padding: 26px; border-top: 6px solid var(--lima); transition: transform .2s; }}
.g a:hover {{ transform: translateY(-4px); }}
.g b {{ display: block; font-size: 22px; text-transform: uppercase; margin-bottom: 6px; }}
.g span {{ color: var(--suave); }}
@media (max-width: 760px) {{ .g {{ grid-template-columns: 1fr; }} }}
</style></head><body><div class="c">
<img src="{A}logo.svg" alt="Compramos Carros">
<h1>Propostas de layout</h1>
<p>Página inicial em três estilos, com as cores, o logotipo e os textos do site.</p>
<div class="g">
<a href="proposta-a.html"><b>A · Clara</b><span>Fundo claro e arejado, faixa com as vantagens e passos em cartões numerados.</span></a>
<a href="proposta-b.html"><b>B · Imersiva</b><span>Fotografia em fundo, cronologia do processo, "O que nos distingue" e equipa.</span></a>
<a href="proposta-c.html"><b>C · Arrojada</b><span>Diagonais, números grandes (24h · 7 dias · 48H) e formulário em 2 passos.</span></a>
</div></div></body></html>""", encoding="utf-8")
print("ok")
