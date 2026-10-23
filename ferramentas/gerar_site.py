#!/usr/bin/env python3
"""Gera as páginas estáticas do site Compramos Carros na pasta site/.

Cabeçalho, rodapé e textos de todas as páginas estão aqui: altere este ficheiro e
corra  python3 ferramentas/gerar_site.py  para atualizar os .html.
"""
from pathlib import Path
import hashlib
import re

OUT = Path(__file__).resolve().parent.parent / "site"
DOMINIO = "https://compramoscarros.pt"
# Email de contacto mostrado em Contactos e na Política de privacidade.
EMAIL = "comercial@compramoscarros.pt"


def origem_crm():
    """Origem do endereço formEndpoint de config.js (para a política de segurança)."""
    import re
    m = re.search(r'formEndpoint:\s*"(https://[^/"]+)', (OUT / "assets/js/config.js").read_text(encoding="utf-8"))
    return m.group(1) if m else ""


# Política de segurança (CSP) e de referrer: vão em <meta> nas páginas e também como
# cabeçalhos HTTP em site/_headers (lido pelo Cloudflare).
def politica_seguranca():
    return "; ".join([
        "default-src 'none'",
        "script-src 'self' https://connect.facebook.net",
        "style-src 'self' https://fonts.googleapis.com",
        "font-src https://fonts.gstatic.com",
        "img-src 'self' data: blob: https://www.facebook.com",
        "connect-src " + " ".join(filter(None, [origem_crm(), "https://www.facebook.com", "https://connect.facebook.net"])),
        "frame-src https://www.google.com https://maps.google.com",
        "form-action 'self'",
        "base-uri 'none'",
        "upgrade-insecure-requests",
    ])


def sem_html(html):
    """Links internos sem ".html": o Cloudflare serve /pagina a partir de pagina.html
    e reencaminharia /pagina.html para /pagina, o que custa um pedido extra."""
    html = re.sub(r'(href|data-obrigado)="index\.html(#[^"]*)?"', lambda m: f'{m.group(1)}="/{m.group(2) or ""}"', html)
    return re.sub(r'(href|data-obrigado)="([a-z0-9-]+)\.html(#[^"]*)?"', lambda m: f'{m.group(1)}="{m.group(2)}{m.group(3) or ""}"', html)


def versao(caminho):
    """Impressão digital do ficheiro, para o navegador não usar uma versão antiga em cache."""
    return hashlib.sha1((OUT / caminho).read_bytes()).hexdigest()[:8]
MAPA_Q = "MGB Automóveis, Estrada Nacional 249-4, 2785-574 São Domingos de Rana"
from urllib.parse import quote
MAPA_EMBED = "https://www.google.com/maps?q=" + quote(MAPA_Q) + "&output=embed"
MAPA_LINK = "https://www.google.com/maps/search/?api=1&query=" + quote(MAPA_Q)

def ic(path, extra=""):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"' + extra + '>' + path + '</svg>')

I = {
 "user": ic('<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/>'),
 "phone": ic('<rect x="6" y="2" width="12" height="20" rx="2"/><line x1="11" y1="18" x2="13" y2="18"/>'),
 "mail": ic('<rect x="2" y="4" width="20" height="16" rx="1"/><polyline points="2 5 12 13 22 5"/><line x1="2" y1="20" x2="9" y2="12"/><line x1="22" y1="20" x2="15" y2="12"/>'),
 "pin": ic('<path d="M12 22s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/>'),
 "gauge": ic('<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/>'),
 "car": ic('<path d="M3 15v-3l2-5a2 2 0 0 1 1.9-1.4h10.2A2 2 0 0 1 19 7l2 5v3"/><rect x="2" y="12" width="20" height="5" rx="1.5"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>'),
 "whats": '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6.3-.5c.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.2-1.2 2.9s1.2 3.4 1.4 3.6c.2.2 2.4 3.7 5.9 5.2.8.4 1.5.6 2 .7.8.3 1.6.2 2.2.1.7-.1 1.9-.8 2.2-1.6.3-.8.3-1.4.2-1.6-.1-.1-.3-.2-.6-.4z"/></svg>',
 "menu": ic('<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>', ' stroke-width="2"'),
 "seta": ic('<line x1="4" y1="12" x2="20" y2="12"/><polyline points="13 5 20 12 13 19"/>', ' stroke-width="2.2"'),
 "clock": ic('<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 16 14"/>'),
 "shield": ic('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><polyline points="8.5 12 11 14.5 15.5 9.5"/>'),
 "euro": ic('<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5a4 4 0 1 0 0 7"/><line x1="7" y1="11" x2="13" y2="11"/><line x1="7" y1="13.5" x2="13" y2="13.5"/>'),
 "doc": ic('<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><polyline points="14 3 14 8 19 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="13" y2="17"/>'),
 "camera": ic('<path d="M3 8a2 2 0 0 1 2-2h2.5l1.5-2h6l1.5 2H19a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><circle cx="12" cy="13" r="4"/>'),
 "lupa": ic('<circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/>', ' stroke-width="2.2"'),
 "visto": ic('<polyline points="4 12 10 18 20 6"/>', ' stroke-width="3"'),
 "msg": ic('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>'),
}

MENU = [("como-funciona.html", "Como funciona"), ("quem-somos.html", "Quem Somos"),
        ("centro-de-entregas.html", "Centro de Entregas"), ("contactos.html", "Contactos")]

def pagina(ficheiro, titulo, descricao, corpo, atual=None, indexar=True):
    menu = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == atual else ""}>{nome}</a></li>'
        for href, nome in MENU)
    canonical = DOMINIO + "/" + ("" if ficheiro == "index.html" else ficheiro[:-5])
    html = f"""<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{politica_seguranca()}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{titulo}</title>
<meta name="description" content="{descricao}">{"" if indexar else chr(10) + '<meta name="robots" content="noindex, nofollow">'}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMINIO}/assets/img/quem-somos.jpg">
<meta property="og:locale" content="pt_PT">
<meta name="theme-color" content="#2e294e">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={versao("assets/css/style.css")}">
</head>
<body>
<header class="cabecalho">
  <div class="contentor">
    <a class="logo" href="index.html" aria-label="Compramos Carros — página inicial"><img src="assets/img/logo.svg" alt="Compramos Carros" width="180" height="43"></a>
    <button class="menu-botao" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="navegacao">{I["menu"]}</button>
    <nav class="navegacao" id="navegacao" aria-label="Menu principal">
      <ul class="menu">{menu}<li><a class="botao" href="index.html#avaliacao">Avaliação grátis</a></li></ul>
    </nav>
  </div>
</header>

<main>
{corpo.strip()}
</main>

<footer class="rodape">
  <div class="contentor">
    <div class="grelha">
      <div class="marca"><img src="assets/img/logo.svg" alt="Compramos Carros" width="200" height="48" loading="lazy"><p>Uma marca desenvolvida pela MGB Automóveis.</p></div>
      <div><h4>Navegação</h4><ul>{"".join(f'<li><a href="{h}">{n}</a></li>' for h, n in MENU)}</ul></div>
      <div><h4>Contactos</h4><ul><li>Stand Automóveis MGB</li><li>Estrada Nacional 249-4 Vivenda Garcia</li><li>2785-574 S. Domingos de Rana</li><li><a href="tel:+351912263717">912 263 717</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
      <div><h4>Informação</h4><ul><li><a href="politica-de-privacidade.html">Política de privacidade</a></li><li><a href="politica-de-cookies.html">Política de cookies</a></li><li><a href="#" data-preferencias-cookies>Preferências de cookies</a></li><li><a href="https://www.livroreclamacoes.pt/Inicio/" target="_blank" rel="noopener">Livro de reclamações</a></li><li>Seg a Sex das 9h às 19h<br>Sábado das 10h às 18h</li></ul></div>
    </div>
    <p class="base">© <span data-ano>2026</span> Compramos Carros. Todos os direitos reservados.</p>
  </div>
</footer>

<a class="whatsapp" href="https://wa.me/351912263717" target="_blank" rel="noopener" aria-label="Entre em contacto por WhatsApp">{I["whats"]}<span>Entre em contacto</span></a>

<div class="cookies" role="dialog" aria-live="polite" aria-label="Aviso de cookies">
  <p>Utilizamos cookies para melhorar a sua experiência e, se aceitar, cookies da Meta (Facebook e Instagram) para medir e melhorar os nossos anúncios. Saiba mais na nossa <a href="politica-de-cookies.html">Política de cookies</a>.</p>
  <div class="cookies-botoes"><button class="botao" type="button" data-cookies="aceite">Aceitar</button><button class="botao secundario" type="button" data-cookies="recusado">Recusar</button></div>
</div>

<script src="assets/js/config.js?v={versao("assets/js/config.js")}"></script>
<script src="assets/js/pixel.js?v={versao("assets/js/pixel.js")}"></script>
{f'<script src="assets/js/marcas.js?v={versao("assets/js/marcas.js")}"></script>' if 'data-as-lista="marca"' in corpo else ""}
{f'<script src="assets/js/versoes.js?v={versao("assets/js/versoes.js")}"></script>' if 'data-as-lista="motor_escolha"' in corpo else ""}
{f'<script src="assets/js/motorizacoes.js?v={versao("assets/js/motorizacoes.js")}"></script>' if 'data-as-lista="motor_escolha"' in corpo else ""}
<script src="assets/js/main.js?v={versao("assets/js/main.js")}"></script>
{f'<script src="assets/js/assistente.js?v={versao("assets/js/assistente.js")}"></script>' if 'data-assistente' in corpo else ""}
</body>
</html>
"""
    (OUT / ficheiro).write_text(sem_html(html), encoding="utf-8")

AVISO_DADOS = """<div class="consentimento">
  <label class="interruptor"><input type="checkbox" name="consentimento" required aria-label="Aceito o tratamento dos meus dados e ser contactado por telefone, e-mail ou WhatsApp"><span></span></label>
  <p class="aviso-dados">Os dados recolhidos serão incluídos na nossa agenda de contactos, de acordo com a legislação de proteção de dados em vigor, apenas para lhe responder, enviar a proposta e facilitar futuros contactos da Compramos Carros, por telefone, e-mail ou WhatsApp.<br>
  <a href="politica-de-privacidade.html">Para saber mais sobre a nossa Política de Privacidade clique aqui.</a></p>
</div>"""
# No formulário de avaliação: informa também que a viatura pode ser avaliada por parceiros.
AVISO_DADOS_AVALIACAO = """<div class="consentimento">
  <label class="interruptor"><input type="checkbox" name="consentimento" required aria-label="Aceito o tratamento dos meus dados e ser contactado por telefone, e-mail ou WhatsApp"><span></span></label>
  <p class="aviso-dados">Os dados recolhidos serão incluídos na nossa agenda de contactos, de acordo com a legislação de proteção de dados em vigor, apenas para lhe responder, enviar a proposta e facilitar futuros contactos da Compramos Carros, por telefone, e-mail ou WhatsApp. Para lhe fazermos a melhor proposta, os dados e as fotografias da viatura (sem o seu nome nem os seus contactos) podem ser avaliados por comerciantes nossos parceiros.<br>
  <a href="politica-de-privacidade.html">Para saber mais sobre a nossa Política de Privacidade clique aqui.</a></p>
</div>"""

def campo(icone, html):
    return f'<div class="campo">{I[icone]}{html}</div>'

def entrada(nome, rotulo, tipo="text", extra=""):
    return f'<input type="{tipo}" name="{nome}" placeholder="{rotulo}" aria-label="{rotulo}" required{extra}>'

def escolha(nome, rotulo, lista=None, opcoes="", obrigatorio=True):
    dl = f' data-lista="{lista}"' if lista else ""
    req = " required" if obrigatorio else ""
    return f'<select name="{nome}" aria-label="{rotulo}"{dl}{req}><option value="" disabled selected>{rotulo}</option>{opcoes}</select>'

def heroi(rotulo, titulo, sub=""):
    """Topo diagonal das páginas interiores."""
    sub_html = f'<p class="sub">{sub}</p>' if sub else ""
    return f"""<section class="heroi pagina">
  <div class="contentor">
    <span class="rotulo">{rotulo}</span>
    <h1>{titulo}</h1>
    {sub_html}
  </div>
</section>"""

FINAL = f"""<section class="final">
  <div class="contentor">
    <h2>Peça a sua <span>avaliação grátis</span></h2>
    <a class="botao grande" href="index.html#avaliacao">Peça a sua avaliação grátis {I["seta"]}</a>
  </div>
</section>"""

VANTAGENS = [("clock", "Proposta em 24 horas", "Em 24 horas irá receber uma proposta (por email ou contacto telefónico) que será válida por 7 dias úteis."),
             ("euro", "Pagamento por transferência bancária imediata", "Para maior conforto, realizamos o pagamento por transferência bancária imediata."),
             ("doc", "Transferência de propriedade em 48H", "Todo o processo será verificado e devidamente documentado (com cópias de todos os documentos)."),
             ("shield", "Segurança em todo o processo", "Todo o procedimento é acompanhado de documentos que comprovam e validam a transação.")]
vantagens_html = "".join(f'<div>{I[i]}<h3>{t}</h3><p>{d}</p></div>' for i, t, d in VANTAGENS)

# ------------------------------------------------------------------ Início
PASSOS = [("avaliamos", "Avaliamos o seu carro", "Avalie o seu carro conosco e descubra o verdadeiro valor do seu veículo."),
          ("oferta", "Fazemos a oferta", "Fazemos a oferta mais competitiva para o seu veículo. Confie em nós para obter o melhor negócio possível."),
          ("finalizamos", "Finalizamos a compra", "Finalizamos a compra do seu carro de forma rápida e sem complicações.")]
passos_html = "".join(
    f'<div class="etapa"><div class="n">0{n}</div><img src="assets/img/icones/{f}.png" alt="" width="60" height="60" loading="lazy"><h3>{t}</h3><p>{d}</p></div>'
    for n, (f, t, d) in enumerate(PASSOS, 1))

inicio = f"""
<section class="heroi inicio" id="avaliacao">
  <div class="contentor grelha">
    <div class="texto">
      <h1>A forma <span class="contorno">fácil</span> de <span class="lima">vender</span> o seu carro</h1>
      <p class="sub">Em apenas <b>3 etapas</b> compramos o seu carro de <b>forma simplificada e justa!</b></p>
      <div class="numeros"><div><b>24h</b><span>Proposta</span></div><div><b>7</b><span>Dias úteis de validade</span></div><div><b>Imediato</b><span>Pagamento</span></div></div>
    </div>

    <form class="cartao assistente" data-formulario data-assistente data-obrigado="obrigado.html" data-assunto="Pedido de avaliação grátis" novalidate>
      <input class="armadilha" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <input type="hidden" name="marca" aria-label="Marca do carro">
      <input type="hidden" name="modelo" aria-label="Modelo do carro">
      <input type="hidden" name="versao" aria-label="Versão do carro">
      <input type="hidden" name="combustivel" aria-label="Combustível">
      <input type="hidden" name="versao_motor" aria-label="Motorização">
      <input type="hidden" name="motor_escolha">
      <input type="hidden" name="nivel_equipamento" aria-label="Nível de equipamento">
      <input type="hidden" name="ano" aria-label="Ano do Carro">
      <input type="hidden" name="mes" aria-label="Mês do Carro">
      <input type="hidden" name="transmissao" aria-label="Transmissão">
      <input type="hidden" name="segmento" aria-label="Segmento">

      <div class="as-cab"><span class="as-n" data-as-n>Passo 1</span><div class="as-setas" data-as-setas><button type="button" data-dir="-1" aria-label="Ver anteriores">↑</button><button type="button" data-dir="1" aria-label="Ver seguintes">↓</button></div></div>
      <div class="as-barra" data-as-barra aria-hidden="true"></div>
      <div class="as-fichas" data-as-fichas aria-live="polite"></div>

      <section class="as-passo" data-passo="marca">
        <h2>Qual é a <em>marca</em>?</h2>
        <p class="as-ajuda">Marque agora a avaliação do seu veículo! Deslize para baixo ou pesquise.</p>
        <label class="as-pesquisa">{I["lupa"]}<input type="search" data-as-pesquisa placeholder="Pesquisar marca…" aria-label="Pesquisar marca" autocomplete="off"></label>
        <div class="as-carrossel" data-as-lista="marca" role="listbox" aria-label="Marcas"></div>
        <div class="campo largo as-outro" data-as-outro hidden>{I["car"]}<input type="text" name="marca_outra" placeholder="Indique a marca" aria-label="Marca (outra)" required disabled></div>
      </section>

      <section class="as-passo" data-passo="modelo" hidden>
        <h2>E o <em>modelo</em>?</h2>
        <p class="as-ajuda" data-as-ajuda-modelo></p>
        <label class="as-pesquisa">{I["lupa"]}<input type="search" data-as-pesquisa placeholder="Pesquisar modelo…" aria-label="Pesquisar modelo" autocomplete="off"></label>
        <div class="as-carrossel" data-as-lista="modelo" role="listbox" aria-label="Modelos"></div>
        <div class="campo largo as-outro" data-as-outro hidden>{I["car"]}<input type="text" name="modelo_outro" placeholder="Indique o modelo" aria-label="Modelo (outro)" required disabled></div>
      </section>

      <section class="as-passo" data-passo="combustivel" hidden>
        <h2>Qual o <em>combustível</em>?</h2>
        <div class="as-grandes tres" data-as-lista="combustivel" role="listbox" aria-label="Combustível"></div>
      </section>

      <section class="as-passo" data-passo="versao" hidden>
        <h2>Qual é a <em>motorização</em>?</h2>
        <p class="as-ajuda" data-as-ajuda-versao>Se não souber, escolha "Outra / não sei".</p>
        <div class="as-versoes" data-as-lista="motor_escolha" role="listbox" aria-label="Motorizações"></div>
        <div class="campo largo as-outro" data-as-motor-texto hidden>{I["car"]}<input type="text" name="motor_texto" maxlength="60" placeholder="Motorização / potência (opcional)" aria-label="Motorização indicada pelo cliente"></div>
      </section>

      <section class="as-passo" data-passo="equipamento" hidden>
        <h2>Nível de <em>equipamento</em></h2>
        <p class="as-ajuda" data-as-ajuda-equipamento>Por exemplo Pack M, AMG Line, S line ou Sportline. Se não souber, escolha "Outro / não sei".</p>
        <div class="as-versoes" data-as-lista="nivel_equipamento" role="listbox" aria-label="Níveis de equipamento"></div>
      </section>

      <section class="as-passo" data-passo="data" hidden>
        <h2>Quando foi <em>matriculado</em>?</h2>
        <p class="as-ajuda">Escolha o ano e o mês da primeira matrícula.</p>
        <p class="as-sub">Ano</p>
        <div class="as-carrossel uma-linha as-anos" data-as-lista="ano" role="listbox" aria-label="Ano"></div>
        <p class="as-sub">Mês</p>
        <div class="as-meses" data-as-lista="mes" role="listbox" aria-label="Mês"></div>
      </section>

      <section class="as-passo" data-passo="caixa" hidden>
        <h2>Tipo de <em>caixa</em></h2>
        <div class="as-grandes" data-as-lista="transmissao" role="listbox" aria-label="Tipo de caixa"></div>
      </section>

      <section class="as-passo" data-passo="segmento" hidden>
        <h2>Qual o <em>segmento</em>?</h2>
        <p class="as-ajuda">Escolha o formato que mais se parece com o seu carro.</p>
        <div class="as-grandes quatro" data-as-lista="segmento" role="listbox" aria-label="Segmento"></div>
      </section>

      <section class="as-passo" data-passo="detalhes" hidden>
        <h2>Mais alguns <em>detalhes</em></h2>
        <div class="campos">
          {campo("car", entrada("matricula", "Matrícula (ex.: AA-00-AA)", extra=' maxlength="8" autocapitalize="characters" autocomplete="off" spellcheck="false" pattern="[A-Z]{2}-[0-9]{2}-[0-9]{2}|[0-9]{2}-[0-9]{2}-[A-Z]{2}|[0-9]{2}-[A-Z]{2}-[0-9]{2}|[A-Z]{2}-[0-9]{2}-[A-Z]{2}"'))}
          {campo("gauge", entrada("km", "KM do carro", "number", ' min="0" step="1" inputmode="numeric"'))}
          <p class="campo-erro largo" data-matricula-erro hidden>Matrícula inválida. Só aceitamos matrículas portuguesas: <b>AA-00-00</b>, <b>00-00-AA</b>, <b>00-AA-00</b> ou <b>AA-00-AA</b>.</p>
          <div class="campo largo area">{I["msg"]}<textarea name="observacoes" maxlength="100" placeholder="Observações (opcional): extras, estado geral, revisões, eventuais danos…" aria-label="Observações (máximo 100 caracteres)"></textarea><span class="contador" data-as-contador aria-live="polite">0/100</span></div>
        </div>
      </section>

      <section class="as-passo" data-passo="fotos" hidden>
        <h2>Mostre-nos o seu <em>carro</em></h2>
        <p class="as-ajuda">Opcional, mas ajuda-nos a fazer uma proposta mais certa.</p>
        <div class="fotos largo" data-fotos hidden>
          <label class="fotos-zona">{I["camera"]}<span><b>Fotos do carro (opcional)</b>Até 10 fotos: exterior, interior, conta-quilómetros e eventuais danos.</span><input type="file" accept="image/*" multiple aria-label="Fotos do carro"></label>
          <div class="fotos-lista" aria-live="polite"></div>
        </div>
      </section>

      <section class="as-passo" data-passo="dados" hidden>
        <h2>Os seus <em>dados</em></h2>
        <p class="as-ajuda">Para lhe enviarmos a proposta em 24 horas.</p>
        <div class="campos">
          {campo("user", entrada("nome", "Nome", extra=' autocomplete="name"'))}
          {campo("phone", entrada("telefone", "Telefone", "tel", ' autocomplete="tel" inputmode="tel"'))}
          {campo("mail", entrada("email", "E-mail", "email", ' autocomplete="email"'))}
          {campo("pin", escolha("distrito", "Distrito", "distrito"))}
        </div>
        {AVISO_DADOS_AVALIACAO}
      </section>

      <div class="as-fim" data-as-fim hidden>
        <span class="as-visto">{I["visto"]}</span>
        <h2 data-as-obrigado>Obrigado!</h2>
      </div>

      <div class="mensagem-form" role="status"></div>
      <div class="as-rodape" data-as-rodape>
        <button class="as-voltar" type="button" data-as-voltar>← Voltar</button>
        <button class="botao" type="button" data-as-seguinte>Seguinte {I["seta"]}</button>
        <button class="botao" type="submit" data-as-enviar hidden>Pedir avaliação grátis {I["seta"]}</button>
      </div>
    </form>
  </div>
</section>

<section class="seccao colada">
  <div class="contentor">
    <h2 class="titulo">Processo <span>simplificado</span></h2>
    <div class="etapas">{passos_html}</div>
  </div>
</section>

<section class="faixa">
  <div class="contentor"><div class="vantagens">{vantagens_html}</div></div>
</section>

{FINAL}
"""
pagina("index.html", "Compramos Carros",
       "A forma fácil de vender o seu carro. Em apenas 3 etapas compramos o seu carro de forma simplificada e justa! Peça a sua avaliação grátis.",
       inicio)

# ------------------------------------------------------------------ Como funciona
CRITERIOS = [("impostos", "Ter os impostos em dia"), ("ipo", "Ter IPO válida"),
             ("matricula", "Ter matrícula portuguesa"), ("chaves", "Ter duplicado de chaves"),
             ("penhora", "Não estar penhorado"), ("proprietario", "Ser proprietário do carro*"),
             ("manuais", "Ter Manuais e Livro de Revisões atualizado"),
             ("perda-total", "Nunca ter sido considerado Perda Total, num sinistro"),
             ("taxi", "Nunca ter sido utilizado como Táxi, Rent-a-car, Escola de Condução ou Competição"),
             ("quilometragem", "Quilometragem não viciada")]
crit_html = "".join(
    f'<div class="criterio"><img src="assets/img/icones/{f}.png" alt="" width="60" height="60" loading="lazy"><h3>{t}</h3></div>'
    for f, t in CRITERIOS)
PECA = f'<p><a class="botao" href="index.html#avaliacao">Peça a sua avaliação grátis {I["seta"]}</a></p>'

como = f"""
{heroi("Como funciona", 'Como <span class="lima">funciona</span>', "Em apenas <b>3 etapas</b> compramos o seu carro de <b>forma simplificada e justa!</b>")}

<section class="seccao colada">
  <div class="contentor bloco">
    <div>
      <p class="n-seccao">01</p>
      <h2>Facilidade e <span>simplicidade</span></h2>
      <p>Insira todos os detalhes relativos ao veículo que deseja vender e submeta para avaliação no Compramos Carros. É de vital importância que seja sincero e honesto nas condições do seu automóvel, pois é com base nessa informação que será efectuada a proposta (sempre sujeita a uma inspeção presencial).</p>
      <p><b>Em 24 horas irá receber uma proposta (por email ou contacto telefónico) que será válida por 7 dias úteis.</b></p>
      <p>Quando receber o email com a nossa proposta, agende directamente no nosso calendário a inspeção final e entrega do seu veículo.</p>
      {PECA}
    </div>
    <div class="imagem"><img src="assets/img/como-funciona-facilidade.jpg" alt="Cliente satisfeito junto ao seu carro" width="651" height="428"></div>
  </div>
</section>

<section class="seccao cinza">
  <div class="contentor">
    <p class="n-seccao">02</p>
    <h2 class="titulo">Critérios de <span>avaliação</span></h2>
    <p class="intro">Além dos dados que nos fornece ao inserir as informações do seu veículo, nossa avaliação leva em conta os seguintes critérios:</p>
    <div class="criterios">{crit_html}</div>
    <p class="nota">Caso haja incertezas ou se suspeitar que o seu veículo possa não cumprir com estes critérios, por favor mencione isso ao inserir os dados do seu carro para avaliação.</p>
    <p class="nota">*Se o seu carro estiver sob financiamento, também estamos aptos a adquiri-lo. Nesse caso, solicitaremos o valor de quitação à instituição financeira e cuidaremos de todo o processo, mediante a sua autorização. O pagamento será realizado por meio de ajuste de contas.</p>
    <p class="centro mt-30"><a class="botao" href="index.html#avaliacao">Peça a sua avaliação grátis {I["seta"]}</a></p>
  </div>
</section>

<section class="seccao">
  <div class="contentor bloco inverso">
    <div>
      <p class="n-seccao">03</p>
      <h2>Inspeção antes de <span>entrega</span></h2>
      <p>Nem todos somos especialistas na avaliação dos danos e estado geral do automóvel, essa é a nossa função e com a nossa vasta experiência sabemos fazê-lo muito bem. Pedimos apenas que seja sincero e objectivo na informação fornecida.</p>
      <p><b>De forma a ser um processo completamente justo para ambas as partes, reservamo-nos o direito de realizar uma inspeção no carro para determinar se desejamos ou não adquiri-lo e qual será o valor definitivo da compra.</b></p>
    </div>
    <div class="imagem azul"><img src="assets/img/como-funciona-inspecao.jpg" alt="Carros num stand" width="651" height="428" loading="lazy"></div>
  </div>
</section>

<section class="faixa">
  <div class="contentor bloco">
    <div>
      <p class="n-seccao">04</p>
      <h2>Conclusão da <span>venda</span></h2>
      <p>Após a verificação do veículo e a conclusão do acordo referente ao valor de transação, será pedida uma Certidão do veículo para verificar se o mesmo está apto para o processo de transferência de propriedade. Todo o processo será verificado e devidamente documentado (com cópias de todos os documentos)</p>
      <p><b class="branco">O pagamento será efectuado por transferência bancária imediata</b>, sendo necessário o NIB (Número de Identificação Bancária) ou SPIN (Identificador para derivação de Conta). <b class="branco">O processo de transferência de registo de propriedade, será efectuado no máximo em 48H.</b></p>
      <p>Com este processo concluído evitamos todos os problemas que por vezes sucedem na venda a particulares (multas, portagens sem pagamento, IUC’s sem pagamento, etc)</p>
    </div>
    <div class="imagem"><img src="assets/img/como-funciona-conclusao.jpg" alt="Verificação de um carro antes da compra" width="651" height="428" loading="lazy"></div>
  </div>
</section>

{FINAL}
"""
pagina("como-funciona.html", "Como Funciona - Compramos Carros",
       "Saiba como funciona a venda do seu carro ao Compramos Carros: proposta em 24 horas, critérios de avaliação, inspeção e conclusão da venda.",
       como, "como-funciona.html")

# ------------------------------------------------------------------ Quem somos
EQUIPA = [("francisco-matos", "Francisco Matos"), ("manuel-gama-barros", "Manuel Gama Barros"),
          ("bernardo-soares", "Bernardo Soares")]
equipa_html = "".join(
    f'<div class="membro"><img src="assets/img/equipa-{f}.jpg" alt="{n}" width="429" height="550" loading="lazy"><h3>{n}</h3></div>'
    for f, n in EQUIPA)
quem = f"""
{heroi("Quem somos", 'Quem <span class="lima">somos</span>')}

<section class="seccao colada">
  <div class="contentor bloco">
    <div>
      <h2>Bem-vindo ao <span>Compramos Carros</span></h2>
      <p><b>Bem-vindo ao Compramos Carros, uma marca desenvolvida pela MGB Automóveis.</b></p>
      <p>Nossa missão é oferecer um processo simples, rápido e transparente para si que deseja vender o seu carro!</p>
      {PECA}
    </div>
    <div class="imagem"><img src="assets/img/quem-somos.jpg" alt="Aperto de mão junto a um carro vermelho" width="651" height="428"></div>
  </div>
</section>

<section class="seccao cinza">
  <div class="contentor">
    <h2 class="titulo">A <span>equipa</span></h2>
    <p class="intro"><b class="forte">A nossa força reside na equipa dedicada e disponível!</b> Cada um de nós, com nossa experiência única e paixão pelo negócio, esforça-se para lhe proporcionar a experiência mais tranquila e confortável no processo de venda do seu carro.</p>
    <div class="equipa">{equipa_html}</div>
  </div>
</section>

<section class="faixa">
  <div class="contentor bloco inverso">
    <div>
      <h2>O que nos <span>distingue</span></h2>
      <p>O que nos diferencia face à nossa concorrência, é a rapidez na formalização da oferta para o seu carro. Temos critérios de velocidade ambiciosos, e num prazo de 24 horas recebe a nossa oferta (durante o horário laboral, das 10h às 19h).</p>
      <p>Além disso, garantimos segurança em todo o processo. Todo o procedimento é acompanhado de documentos que comprovam e validam a transação. Para maior conforto, realizamos o pagamento por transferência bancária imediata.</p>
    </div>
    <div class="imagem"><img src="assets/img/quem-somos-distingue.jpg" alt="Aperto de mão junto a um carro azul" width="651" height="428" loading="lazy"></div>
  </div>
</section>

{FINAL}
"""
pagina("quem-somos.html", "Quem Somos - Compramos Carros",
       "Bem-vindo ao Compramos Carros, uma marca desenvolvida pela MGB Automóveis. Um processo simples, rápido e transparente para vender o seu carro.",
       quem, "quem-somos.html")

# ------------------------------------------------------------------ Centro de entregas
MAPA = f"""<div class="mapa"><iframe src="{MAPA_EMBED}" title="Mapa — Stand Automóveis MGB, São Domingos de Rana" loading="lazy" allowfullscreen></iframe></div>"""
centro = f"""
{heroi("Centro de entregas", 'Centro de <span class="lima">entregas</span>', "Bem-vindo ao Centro de Entrega, onde oferecemos um atendimento excepcional para garantir sua total satisfação.")}

<section class="seccao colada">
  <div class="contentor">
    <div class="infos">
      <div class="info"><img src="assets/img/icones/morada.png" alt="" width="62" height="62"><h3>Stand Automóveis MGB</h3><p>Estrada Nacional 249-4 Vivenda Garcia.<br>2785-574 S. Domingos de Rana</p></div>
      <div class="info"><img src="assets/img/icones/horario.png" alt="" width="62" height="62"><h3>Seg a Sex das 9h às 19h. Sábado das 10h às 18h</h3><p>Disponibilidade extra mediante marcação</p></div>
      <div class="info"><img src="assets/img/icones/telefone.png" alt="" width="62" height="62"><p><a href="tel:+351912263717">912 263 717</a></p><p>(Chamada para rede móvel nacional)</p></div>
    </div>
    {MAPA}
    <p class="mapa-ligacao">Para ver o mapa no google Maps <a href="{MAPA_LINK}" target="_blank" rel="noopener">clique aqui</a></p>
  </div>
</section>

{FINAL}
"""
pagina("centro-de-entregas.html", "Centro de Entregas - Compramos Carros",
       "Centro de Entregas Compramos Carros: Stand Automóveis MGB, Estrada Nacional 249-4, São Domingos de Rana. Seg a Sex das 9h às 19h, Sábado das 10h às 18h.",
       centro, "centro-de-entregas.html")

# ------------------------------------------------------------------ Contactos
contactos = f"""
{heroi("Contactos", 'Fale <span class="lima">connosco</span>', "A nossa equipa está aqui para o ajudar. Entre em contacto connosco e iremos atender o seu pedido o mais brevemente possível.")}

<section class="seccao colada">
  <div class="contentor contactos-grelha">
    <form class="cartao" data-formulario data-assunto="Contacto através do site">
      <div class="cab"><h2><small>Contactos</small>Fale connosco</h2></div>
      <input class="armadilha" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="campos">
        {campo("user", entrada("nome", "Nome", extra=' autocomplete="name"'))}
        {campo("phone", entrada("telefone", "Telefone", "tel", ' autocomplete="tel" inputmode="tel"'))}
        <div class="campo largo">{I["mail"]}{entrada("email", "E-mail", "email", ' autocomplete="email"')}</div>
        <div class="campo largo area">{I["msg"]}<textarea name="mensagem" placeholder="Mensagem" aria-label="Mensagem" required></textarea></div>
      </div>
      {AVISO_DADOS}
      <div class="formulario-acao"><button class="botao" type="submit">Enviar {I["seta"]}</button></div>
      <div class="mensagem-form" role="status"></div>
    </form>

    <div>
      {MAPA}
      <ul class="lista-contactos">
        <li><span class="ico">{I["pin"]}</span><span><b>Stand Automóveis MGB</b><br>Estrada Nacional 249-4 Vivenda Garcia<br>2785-574. São Domingos de Rana</span></li>
        <li><span class="ico">{I["whats"]}</span><span><b>WhatsApp</b><br><a href="https://wa.me/351912263717" target="_blank" rel="noopener">912 263 717</a></span></li>
        <li><span class="ico">{I["phone"]}</span><span><b>Telefone</b><br><a href="tel:+351912263717">912 263 717</a></span></li>
        <li><span class="ico">{I["mail"]}</span><span><b>E-mail</b><br><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
      </ul>
    </div>
  </div>
</section>
"""
pagina("contactos.html", "Contactos - Compramos Carros",
       "Fale connosco. A equipa Compramos Carros está aqui para o ajudar: 912 263 717, Stand Automóveis MGB, São Domingos de Rana.",
       contactos, "contactos.html")

# ------------------------------------------------------------------ Política de privacidade
EMPRESA = "Barros Matos e Soares Automóveis Lda."
privacidade = f"""
{heroi("Informação legal", 'Política de <span class="lima">privacidade</span>')}

<section class="seccao colada">
  <div class="contentor estreito legal">
    <p><b class="destaque-escuro">Termos e Condições | Política de Privacidade | Informação sobre Proteção de Dados</b></p>

    <h2>Quem somos?</h2>
    <p>Cumprindo o Regulamento (UE) 2016/679 do Parlamento Europeu e do Conselho, de 27 de abril de 2016 (Regulamento Geral sobre a Proteção de Dados — RGPD), informamos que o site Compramos Carros, marca desenvolvida pela MGB Automóveis, é gerido pela {EMPRESA}, pessoa coletiva n.º 517923122, com sede na Estrada Nacional 249-4, Vivenda Garcia, 2785-574 São Domingos de Rana, Portugal, que atua na área da compra e venda de automóveis.</p>

    <h2>Quem é o responsável pelo tratamento de dados?</h2>
    <p>A entidade responsável pelo tratamento dos dados pessoais é a {EMPRESA}, que decide quais os dados recolhidos, os meios de tratamento e as finalidades para que são utilizados. Pode contactar-nos através de <a href="mailto:{EMAIL}">{EMAIL}</a>, do telefone 912 263 717 ou por carta para a morada acima.</p>

    <h2>Porquê uma política de privacidade?</h2>
    <p>Porque a {EMPRESA} está empenhada em proteger a privacidade dos seus utilizadores e, neste contexto, elaborou a presente Política de Privacidade para demonstrar o seu compromisso com as regras de privacidade e de proteção de dados pessoais. Caso não concorde com esta Política de Privacidade, não deverá preencher os formulários.</p>

    <h2>O que é abrangido por esta política de privacidade?</h2>
    <p>Esta Política de Privacidade aplica-se à recolha e ao tratamento de dados pessoais efetuados pela {EMPRESA} no âmbito da sua atividade, através deste site, dos e-mails e mensagens que lhe enviamos e das páginas para marcar a inspeção e enviar fotografias.</p>

    <h2>Titularidade dos dados</h2>
    <p>Ao registar os seus dados, o utilizador declara ser o titular legal desses dados e ser maior de 18 anos.</p>

    <h2>Que dados pessoais recolhemos e como?</h2>
    <p>Os dados pessoais são sempre fornecidos pelo utilizador quando preenche os nossos formulários ou nos envia fotografias. São os adequados, pertinentes e não excessivos para as finalidades indicadas abaixo:</p>
    <ul>
      <li><b>Dados de contacto:</b> nome e apelido, e-mail, telefone e distrito;</li>
      <li><b>Dados da viatura:</b> matrícula, marca, modelo, versão, nível de equipamento, mês e ano da matrícula, quilómetros e transmissão;</li>
      <li><b>Mensagem ou observações</b> que decida escrever;</li>
      <li><b>Fotografias da viatura</b>, se as enviar (opcional). Pedimos que não fotografe pessoas nem documentos pessoais. Sempre que o seu browser o permite, as fotografias são reduzidas antes do envio e ficam sem os metadados, incluindo a localização GPS;</li>
      <li><b>Marcação da inspeção:</b> o dia e a hora que escolher;</li>
      <li><b>Dados técnicos:</b> para impedir abusos do formulário, guardamos uma versão codificada e irreversível do endereço IP (não guardamos o endereço IP em si) e a data e hora do pedido.</li>
    </ul>

    <h2>Para que são utilizados os dados e com que fundamento?</h2>
    <ul>
      <li><b>Avaliar a viatura e enviar-lhe a proposta de compra</b> por e-mail, telefone ou WhatsApp — diligências pré-contratuais a seu pedido (RGPD, art. 6.º, n.º 1, alínea b);</li>
      <li><b>Marcar, alterar ou cancelar a inspeção da viatura</b> e enviar-lhe a confirmação — diligências pré-contratuais (alínea b);</li>
      <li><b>Concluir a compra da viatura</b> e cumprir obrigações fiscais, contabilísticas e de registo automóvel — execução do contrato e obrigação legal (alíneas b e c);</li>
      <li><b>Obter avaliações da viatura junto de comerciantes parceiros</b>, para preparar a proposta de compra — diligências pré-contratuais e interesse legítimo em obter o melhor valor (alíneas b e f);</li>
      <li><b>Responder às suas mensagens e pedidos de contacto</b> — diligências pré-contratuais ou interesse legítimo em responder (alíneas b e f);</li>
      <li><b>Proteger o site e os formulários</b> contra abusos e envios automáticos — interesse legítimo na segurança (alínea f).</li>
    </ul>
    <p>Não tomamos decisões exclusivamente automatizadas sobre si: as propostas são preparadas pela nossa equipa. Não utilizamos os seus dados para publicidade nem os vendemos ou cedemos a terceiros para fins comerciais.</p>

    <h2>Quem tem acesso aos seus dados?</h2>
    <p>Os seus dados são consultados apenas pela equipa comercial da {EMPRESA}, num sistema de gestão protegido por autenticação. Recorremos ainda aos seguintes prestadores de serviços (subcontratantes), que tratam os dados apenas por nossa conta e segundo as nossas instruções:</p>
    <ul>
      <li><b>Cloudflare, Inc.</b> — alojamento do sistema de gestão, base de dados, armazenamento das fotografias e proteção do site;</li>
      <li><b>Resend (Plus Five Five, Inc.)</b> — envio dos e-mails (servidores na União Europeia);</li>
      <li><b>Google (Google Calendar)</b> — agenda interna das inspeções (nome, contacto e dados da viatura);</li>
      <li><b>Meta Platforms (WhatsApp)</b> — envio da proposta e troca de mensagens por WhatsApp, quando usado;</li>
      <li><b>GitHub, Inc.</b> — alojamento das páginas públicas do site.</li>
    </ul>
    <p><b>Comerciantes parceiros:</b> para avaliar a viatura, podemos partilhar com comerciantes de automóveis nossos parceiros, obrigados a confidencialidade, os dados da viatura (marca, modelo, versão, data da matrícula, quilómetros, parte da matrícula e distrito) e as fotografias que escolhermos. <b>Nunca partilhamos o seu nome, os seus contactos nem as mensagens que nos enviou.</b></p>
    <p>Alguns destes prestadores podem tratar dados fora da União Europeia, nomeadamente nos Estados Unidos. Nesses casos, a transferência está protegida pelo Quadro de Privacidade de Dados UE-EUA (EU-U.S. Data Privacy Framework) ou por cláusulas contratuais-tipo aprovadas pela Comissão Europeia.</p>
    <p>Os dados podem ainda ser comunicados a entidades públicas quando a lei o exija (por exemplo, a Autoridade Tributária ou o registo automóvel, no caso de uma compra).</p>

    <h2>Por quanto tempo conservamos os dados?</h2>
    <ul>
      <li><b>Pedidos que não resultem em compra</b> (incluindo as fotografias): até 2 anos após o último contacto, para podermos dar seguimento ao pedido e responder a novos contactos sobre a mesma viatura. Depois disso, são apagados.</li>
      <li><b>Compras concluídas:</b> os dados e documentos da transação são conservados durante o prazo exigido pela legislação fiscal e contabilística (10 anos).</li>
      <li><b>Dados técnicos de proteção contra abusos:</b> enquanto existir o pedido a que dizem respeito.</li>
    </ul>
    <p>Pode pedir o apagamento antes destes prazos, exceto quando a lei nos obrigue a conservar os dados.</p>

    <h2>Como exercer os seus direitos?</h2>
    <p>O utilizador pode exercer os seus direitos de acesso, retificação, limitação do tratamento, oposição, portabilidade e apagamento dos seus dados pessoais, através de e-mail para <a href="mailto:{EMAIL}">{EMAIL}</a> ou por carta para a morada da sede acima indicada. Respondemos no prazo máximo de um mês.</p>
    <p>Pode ainda apresentar queixa junto da Comissão Nacional de Proteção de Dados em <a href="https://www.cnpd.pt/" target="_blank" rel="noopener">www.cnpd.pt</a>.</p>

    <h2>Como é assegurada a segurança dos seus dados pessoais?</h2>
    <p>A {EMPRESA} adota medidas técnicas e organizativas para proteger os seus dados, nomeadamente:</p>
    <ul>
      <li>todas as comunicações com o site e o sistema de gestão são cifradas (HTTPS);</li>
      <li>o acesso ao sistema de gestão está limitado à equipa comercial e exige autenticação;</li>
      <li>os links pessoais para marcar a inspeção e enviar fotografias são únicos, impossíveis de adivinhar e expiram;</li>
      <li>os formulários estão protegidos contra envios automáticos e abusos;</li>
      <li>só são aceites fotografias verdadeiras, verificadas pelo conteúdo do ficheiro.</li>
    </ul>
    <p>Recomendamos ainda que utilize um browser atualizado e que confirme que está no endereço compramoscarros.pt antes de preencher os formulários.</p>

    <h2>Proteção contra spam</h2>
    <p>O spamming consiste no envio indiferenciado de e-mails a desconhecidos. A {EMPRESA} garante que não utilizará os dados recolhidos para outro fim que não os indicados nesta Política de Privacidade e que não os cederá a terceiros para fins comerciais.</p>

    <h2>Alterações a esta política</h2>
    <p>Podemos atualizar esta Política de Privacidade. A versão em vigor está sempre disponível nesta página. Última atualização: 21 de outubro de 2026.</p>
  </div>
</section>
"""
pagina("politica-de-privacidade.html", "Política de Privacidade - Compramos Carros",
       "Política de Privacidade e informação sobre proteção de dados do site Compramos Carros.",
       privacidade)

# ------------------------------------------------------------------ Política de cookies
COOKIES = [
 ("Cookies próprios", "são aqueles que são enviados para o equipamento terminal do utilizador a partir de um computador ou domínio gerido pelo próprio editor e do qual fornece o serviço solicitado pelo utilizador."),
 ("Cookies de terceiros", "Os que são enviados para o equipamento terminal do utilizador a partir de um computador ou domínio que não é gerido pelo editor, mas por outra entidade que trata os dados obtidos por meio de cookies."),
 ("Cookies de sessão", "São um tipo de cookies projectados para angariar e armazenar dados enquanto o utilizador acede a uma página web."),
 ("Cookies persistentes", "São um tipo de cookies em que os dados permanecem armazenados no terminal e podem ser acedidos e tratados durante um período definido pelo responsável do cookie, e que pode variar de alguns minutos a vários anos."),
 ("Cookies técnicos", "São aqueles que permitem ao utilizador a navegação através de site, plataforma ou aplicação e a utilização das diferentes opções ou serviços que nele existam como por exemplo, controlar o tráfego e a comunicação de dados, identificar a sessão, aceder a áreas restritas, recordar os elementos que integram um pedido, realizar o processo de compra de um pedido, realizar a solicitação de inscrição ou participação num evento, utilizar recursos de segurança enquanto navega, armazenar conteúdos para a difusão de vídeos ou sons ou compartilhar conteúdos através de redes sociais."),
 ("Cookies de personalização", "São aqueles que permitem ao utilizador aceder ao serviço com algumas características de carácter geral predefinidas com base numa série de critérios no terminal do utilizador como por exemplo o idioma, tipo de browser através do qual acede ao serviço, a configuração regional de onde acede o serviço, etc."),
 ("Cookies de análise", "São aqueles que permitem aos seus responsáveis acompanhar e analisar o comportamento dos utilizadores dos sites aos quais estejam vinculados. A informação recolhida através de tais cookies é usada para medir a actividade dos sites, aplicativos ou plataformas e para a criação de perfis de navegação dos utilizadores desses sites, aplicativos e plataformas, a fim de realizar melhorias em base na análise dos dados de uso feito pelos utilizadores do serviço."),
 ("Cookies publicitárias", "São aqueles que permitem a gestão, da forma mais eficaz possível, dos espaços publicitários que, o editor haja incluído num site, aplicativo ou plataforma de onde presta o serviço solicitado com base em critérios como o conteúdo editado ou a frequência em que os anúncios são exibidos."),
 ("Cookies de publicidade comportamental", "São aqueles que armazenam informações sobre o comportamento do utilizador obtido através da observação contínua de seus hábitos de navegação, permitindo desenvolver um perfil específico para exibir anúncios com base no mesmo."),
]
cookies = f"""
{heroi("Informação legal", 'Política de <span class="lima">cookies</span>')}

<section class="seccao colada">
  <div class="contentor estreito legal">
    <h2>Como usamos os cookies?</h2>
    <p>Um cookie é um arquivo que é instalado no computador quando se acede a determinadas páginas na Internet. Os Cookies que utilizamos são os seguintes:</p>
    <ul>{"".join(f"<li><b>{t}:</b> {d}</li>" for t, d in COOKIES)}</ul>
    <h2>Meta Pixel (Facebook e Instagram)</h2>
    <p>Se aceitar os cookies, o site carrega o Meta Pixel, da Meta Platforms Ireland Ltd. Serve para medirmos a eficácia dos nossos anúncios no Facebook e no Instagram (por exemplo, quantas pessoas que viram um anúncio pediram depois uma avaliação) e para mostrar anúncios a quem já visitou o site. São registadas as páginas visitadas, os passos do formulário de avaliação concluídos e o envio de pedidos, nunca o conteúdo dos campos que preenche (nome, telefone, email, matrícula). A Meta pode instalar os cookies <b>_fbp</b> (até 3 meses) e <b>fr</b> (até 3 meses). Mais informação na <a href="https://www.facebook.com/privacy/policy/" target="_blank" rel="noopener">Política de Privacidade da Meta</a>.</p>
    <p>Se recusar, o Meta Pixel não é carregado. Pode mudar a sua escolha a qualquer momento em <a href="#" data-preferencias-cookies>Preferências de cookies</a>, no rodapé de todas as páginas. A sua escolha é guardada apenas no seu navegador.</p>
  </div>
</section>
"""
pagina("politica-de-cookies.html", "Política de Cookies - Compramos Carros",
       "Política de Cookies do site Compramos Carros.", cookies)

# ------------------------------------------------------------------ 404
# ------------------------------------------------------------------ Obrigado (depois do pedido de avaliação)
obrigado = f"""
<section class="heroi pagina" data-obrigado-pagina>
  <div class="contentor">
    <span class="rotulo">Pedido enviado</span>
    <h1><span data-obrigado-nome>Obrigado!</span></h1>
    <p class="sub">Recebemos o pedido de avaliação <span data-obrigado-viatura>do seu carro</span>. <b>Em 24 horas irá receber uma proposta</b> (por email ou contacto telefónico).</p>
  </div>
</section>

<section class="seccao colada">
  <div class="contentor">
    <div class="aviso-fotos" data-obrigado-fotos hidden>
      <span class="ico">{I["camera"]}</span>
      <div><b>Não foi possível enviar as fotos.</b> O seu pedido chegou, mas sem as fotos. Pode enviá-las por WhatsApp para o 912 263 717.</div>
      <a class="botao" href="https://wa.me/351912263717" target="_blank" rel="noopener">Enviar fotos por WhatsApp</a>
    </div>
    <h2 class="titulo">E agora, <span>o que acontece?</span></h2>
    <div class="etapas">
      <div class="etapa"><div class="n">01</div><img src="assets/img/icones/oferta.png" alt="" width="60" height="60"><h3>Recebe a proposta</h3><p>Em 24 horas irá receber uma proposta (por email ou contacto telefónico) que será válida por 7 dias úteis.</p></div>
      <div class="etapa"><div class="n">02</div><img src="assets/img/icones/avaliamos.png" alt="" width="60" height="60"><h3>Inspeção e entrega</h3><p>Quando receber o email com a nossa proposta, agende directamente no nosso calendário a inspeção final e entrega do seu veículo.</p></div>
      <div class="etapa"><div class="n">03</div><img src="assets/img/icones/finalizamos.png" alt="" width="60" height="60"><h3>Pagamento imediato</h3><p>Para maior conforto, realizamos o pagamento por transferência bancária imediata.</p></div>
    </div>
    <p class="mt-44"><a class="botao" href="como-funciona.html">Saiba como funciona {I["seta"]}</a></p>
  </div>
</section>
"""
pagina("obrigado.html", "Obrigado - Compramos Carros",
       "Recebemos o seu pedido de avaliação. Em 24 horas irá receber uma proposta.", obrigado, indexar=False)

erro = f"""
{heroi("Erro 404", 'Página não <span class="lima">encontrada</span>', "A página que procura não existe ou foi movida.")}
<section class="seccao colada"><div class="contentor">
  <p><a class="botao" href="index.html">Voltar à página inicial {I["seta"]}</a></p>
</div></section>
"""
pagina("404.html", "Página não encontrada - Compramos Carros", "Página não encontrada.", erro)
# Num 404 servido noutro caminho, os endereços relativos falham: usar absolutos.
p = OUT / "404.html"
s = p.read_text(encoding="utf-8")
for a in ['href="', 'src="']:
    for alvo in ["assets/", "como-funciona", "quem-somos", "centro-de", "contactos", "politica-de", "favicon"]:
        s = s.replace(a + alvo, a + "/" + alvo)
p.write_text(s, encoding="utf-8")

# ------------------------------------------------------------------ SEO / alojamento
paginas = ["", "como-funciona", "quem-somos", "centro-de-entregas", "contactos",
           "politica-de-privacidade", "politica-de-cookies"]
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{DOMINIO}/{p}</loc></url>\n" for p in paginas) + "</urlset>\n", encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n", encoding="utf-8")

# Cabeçalhos de segurança, lidos pelo Cloudflare (ficheiros estáticos do Worker).
# A CSP é a mesma das páginas, mais frame-ancestors, que só funciona como cabeçalho.
(OUT / "_headers").write_text(f"""/*
  Content-Security-Policy: {politica_seguranca()}; frame-ancestors 'none'
  Strict-Transport-Security: max-age=31536000
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=()
  Cross-Origin-Opener-Policy: same-origin

/assets/*
  Cache-Control: public, max-age=86400
""", encoding="utf-8")
print("ok")
