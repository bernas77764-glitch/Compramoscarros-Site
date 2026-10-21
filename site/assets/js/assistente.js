/*
 * Formulário de avaliação passo a passo (página inicial).
 *
 * Passos: marca → modelo → versão (só nos modelos de versoes.js) → nível de equipamento (só nas
 * marcas de versoes.js) → ano e mês → caixa → segmento → matrícula/km/observações
 * → fotos (só se config.js tiver aceitaFotos) → dados de contacto.
 * As escolhas ficam em campos escondidos com os mesmos nomes do formulário antigo
 * (marca, modelo, versao, ano, mes, transmissao) e mais "segmento" e "observacoes".
 * "versao" junta a motorização e o nível de equipamento ("118d · Pack M / M Sport"), que também
 * seguem em separado em "versao_motor" e "nivel_equipamento".
 * O envio é feito por main.js (CRM ou WhatsApp), como nos outros formulários.
 */
(function () {
  "use strict";

  var form = document.querySelector("form[data-assistente]");
  if (!form) return;

  var MARCAS = window.CC_MARCAS || {};
  var OUTRA_MARCA = "Outra marca", OUTRO_MODELO = "Outro modelo";
  var MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

  function carro(d) {
    return '<svg viewBox="0 0 96 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="' + d + '"/><circle cx="24" cy="31" r="5.5"/><circle cx="72" cy="31" r="5.5"/></svg>';
  }
  function letra(t, y) {
    return '<text x="24" y="' + y + '" font-family="Barlow,sans-serif" font-size="8" font-weight="800" text-anchor="middle" fill="currentColor" stroke="none">' + t + "</text>";
  }
  var CAIXAS = [
    { v: "Manual", nota: "Pedal de embraiagem",
      svg: '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="10" r="3.5"/><circle cx="24" cy="10" r="3.5"/><circle cx="36" cy="10" r="3.5"/><circle cx="12" cy="38" r="3.5"/><circle cx="24" cy="38" r="3.5"/><circle cx="36" cy="38" r="3.5"/><path d="M12 13.5v21M24 13.5v21M36 13.5v21M12 24h24"/></svg>' },
    { v: "Automática", nota: "Sem pedal de embraiagem",
      svg: '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="14" y="4" width="20" height="40" rx="6"/>' + letra("P", 15) + letra("R", 24) + letra("N", 33) + letra("D", 42) + "</svg>" }
  ];
  var SEGMENTOS = [
    { v: "Citadino", svg: carro("M14 31H8v-8l6-3 8-9h22l10 9h4l4 4v7h-6M30 31h36M44 11v9M22 20h36") },
    { v: "Utilitário", svg: carro("M10 31H6v-9l8-3 10-9h26l12 9h12l6 4v8h-6M30 31h36M48 10v9M24 19h38") },
    { v: "Berlina", svg: carro("M10 31H4v-7l8-3 14-9h28l14 9h14l4 4v6h-6M30 31h36M48 12v9M26 21h42") },
    { v: "Carrinha", svg: carro("M10 31H4v-9l6-2 12-10h58l6 10 4 2v9h-12M30 31h36M52 10v10M22 20h64") },
    { v: "SUV / Crossover", svg: carro("M10 31H4v-11l8-2 10-10h38l14 10h10l6 4v9h-8M30 31h36M48 8v10M22 18h52") },
    { v: "Monovolume", svg: carro("M10 31H4v-11l6-3 16-11h46l10 11 6 3v11h-8M30 31h36M54 6v11M26 17h56") },
    { v: "Coupé / Cabrio", svg: carro("M10 31H6v-6l10-3 16-8h20l16 8h16l6 3v6h-8M30 31h36M30 22h40") },
    { v: "Comercial / Pick-up", svg: carro("M10 31H4v-11l6-2 8-10h22v10h48v13h-10M30 31h36M40 8v10") }
  ];

  var $ = function (sel, raiz) { return (raiz || form).querySelector(sel); };
  var $$ = function (sel, raiz) { return Array.prototype.slice.call((raiz || form).querySelectorAll(sel)); };
  var campo = function (nome) { return form.elements[nome]; };
  var ordenar = function (l) { return l.slice().sort(function (a, b) { return String(a).localeCompare(String(b), "pt", { numeric: true, sensitivity: "base" }); }); };
  var normal = function (t) { return String(t).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); };
  var iniciais = function (t) { return t.replace(/[^A-Za-zÀ-ÿ0-9 ]/g, " ").split(/\s+/).filter(Boolean).map(function (p) { return p[0]; }).join("").slice(0, 2).toUpperCase(); };

  // ---------- Construção das listas ----------
  function botaoTile(valor, opc) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = opc.classe || "as-tile";
    b.dataset.v = valor;
    b.setAttribute("role", "option");
    if (opc.svg) b.innerHTML = opc.svg;
    else if (opc.mono) { var m = document.createElement("span"); m.className = "as-mono"; m.textContent = iniciais(valor); b.appendChild(m); }
    b.appendChild(document.createTextNode(opc.texto || valor));
    if (opc.nota) { var s = document.createElement("small"); s.textContent = opc.nota; b.appendChild(s); }
    return b;
  }
  function encher(nome, itens) {
    var caixa = $("[data-as-lista='" + nome + "']");
    caixa.innerHTML = "";
    itens.forEach(function (it) { caixa.appendChild(botaoTile(it.v, it)); });
    marcarEscolhido(nome);
  }
  function marcarEscolhido(nome) {
    var valor = campo(nome).value;
    $$("[data-as-lista='" + nome + "'] > button").forEach(function (b) {
      var sel = b.dataset.v === valor;
      b.classList.toggle("sel", sel);
      b.setAttribute("aria-selected", sel ? "true" : "false");
    });
  }

  var anos = [];
  for (var a = new Date().getFullYear(); a >= 1990; a--) anos.push(String(a));
  encher("marca", ordenar(Object.keys(MARCAS)).concat([OUTRA_MARCA]).map(function (m) { return { v: m, mono: true }; }));
  encher("ano", anos.map(function (x) { return { v: x }; }));
  encher("mes", MESES.map(function (m) { return { v: m, texto: m.slice(0, 3) }; }));
  encher("transmissao", CAIXAS.map(function (c) { return { v: c.v, svg: c.svg, nota: c.nota, classe: "as-grande" }; }));
  encher("segmento", SEGMENTOS.map(function (s) { return { v: s.v, svg: s.svg, classe: "as-grande" }; }));

  // ---------- Passos ----------
  var temFotos = !$("[data-fotos]").hidden;   // main.js mostra o bloco só se o CRM aceitar fotos
  var VERSOES = window.CC_VERSOES || {}, OUTRA_VERSAO = "Outra / não sei";
  var EQUIPAMENTOS = window.CC_EQUIPAMENTOS || {}, OUTRO_EQUIPAMENTO = "Outro / não sei";
  var TODOS = ["marca", "modelo", "versao", "equipamento", "data", "caixa", "segmento", "detalhes", "fotos", "dados"];
  var PASSOS = [], atual = 0;

  // Versões conhecidas do modelo escolhido (versoes.js); sem versões, o passo "Versão" é saltado.
  function versoesDoModelo() {
    var m = VERSOES[campo("marca").value];
    return (m && m[campo("modelo").value]) || null;
  }
  function equipamentosDaMarca() { return EQUIPAMENTOS[campo("marca").value] || null; }
  function atualizarPassos() {
    var comVersao = !!versoesDoModelo(), comEquipamento = !!equipamentosDaMarca();
    if (!comVersao) campo("versao_motor").value = "";
    if (!comEquipamento) campo("nivel_equipamento").value = "";
    comporVersao();
    PASSOS = ["marca", "modelo"].concat(comVersao ? ["versao"] : []).concat(comEquipamento ? ["equipamento"] : [])
      .concat(["data", "caixa", "segmento", "detalhes"]).concat(temFotos ? ["fotos"] : []).concat(["dados"]);
  }
  // "versao" (o campo que o CRM mostra) junta a motorização e o nível de equipamento
  function comporVersao() {
    var partes = [];
    if (campo("versao_motor").value && campo("versao_motor").value !== OUTRA_VERSAO) partes.push(campo("versao_motor").value);
    if (campo("nivel_equipamento").value && campo("nivel_equipamento").value !== OUTRO_EQUIPAMENTO) partes.push(campo("nivel_equipamento").value);
    campo("versao").value = partes.join(" · ");
  }
  atualizarPassos();

  function seccao(id) { return $("[data-passo='" + id + "']"); }
  function outroTexto(id) { var o = $("[data-as-outro]", seccao(id)); return o ? o.querySelector("input") : null; }

  function mostrarOutro(id, visivel) {
    var o = $("[data-as-outro]", seccao(id));
    if (!o) return;
    o.hidden = !visivel;
    o.querySelector("input").disabled = !visivel;
    if (!visivel) o.querySelector("input").value = "";
  }

  function passoCompleto(id) {
    switch (id) {
      case "marca": return campo("marca").value && (campo("marca").value !== OUTRA_MARCA || outroTexto("marca").value.trim());
      case "modelo": return campo("modelo").value && (campo("modelo").value !== OUTRO_MODELO || outroTexto("modelo").value.trim());
      case "versao": return campo("versao_motor").value;
      case "equipamento": return campo("nivel_equipamento").value;
      case "data": return campo("ano").value && campo("mes").value;
      case "caixa": return campo("transmissao").value;
      case "segmento": return campo("segmento").value;
      case "detalhes": return campo("matricula").value.trim() && campo("km").value.trim();
      case "fotos": return true;
      case "dados": return ["nome", "telefone", "email", "distrito"].every(function (n) { return campo(n).value.trim(); }) && campo("consentimento").checked;
    }
    return false;
  }

  function fichas() {
    var e = [];
    var marca = campo("marca").value === OUTRA_MARCA ? outroTexto("marca").value.trim() : campo("marca").value;
    var modelo = campo("modelo").value === OUTRO_MODELO ? outroTexto("modelo").value.trim() : campo("modelo").value;
    if (marca) e.push(marca);
    if (modelo) e.push(modelo);
    if (campo("versao").value) e.push(campo("versao").value);
    if (campo("ano").value) e.push((campo("mes").value ? campo("mes").value.slice(0, 3) + " " : "") + campo("ano").value);
    if (campo("transmissao").value) e.push(campo("transmissao").value);
    if (campo("segmento").value) e.push(campo("segmento").value);
    var caixa = $("[data-as-fichas]");
    caixa.innerHTML = "";
    e.forEach(function (t) { var s = document.createElement("span"); s.textContent = t; caixa.appendChild(s); });
  }

  function atualizarBotoes() {
    var id = PASSOS[atual], ultimo = atual === PASSOS.length - 1;
    $("[data-as-voltar]").style.visibility = atual ? "visible" : "hidden";
    var seg = $("[data-as-seguinte]");
    seg.hidden = ultimo;
    seg.disabled = !passoCompleto(id);
    seg.firstChild.nodeValue = id === "fotos" && !$$(".fotos-lista figure").length ? "Saltar " : "Seguinte ";
    $("[data-as-enviar]").hidden = !ultimo;
  }

  function desenhar(foco) {
    PASSOS.forEach(function (id, n) { seccao(id).hidden = n !== atual; });
    TODOS.forEach(function (id) { if (PASSOS.indexOf(id) < 0) seccao(id).hidden = true; });
    var id = PASSOS[atual];
    $("[data-as-n]").textContent = "Passo " + (atual + 1) + " de " + PASSOS.length;
    $("[data-as-barra]").innerHTML = PASSOS.map(function (_, n) { return '<i class="' + (n < atual ? "feito" : n === atual ? "atual" : "") + '"></i>'; }).join("");
    $("[data-as-setas]").hidden = !$(".as-carrossel", seccao(id));
    fichas();
    atualizarBotoes();
    seccao(id).classList.remove("entrar");
    void seccao(id).offsetWidth;
    seccao(id).classList.add("entrar");
    if (foco) {
      if (window.ccPixel) window.ccPixel.evento("trackCustom", "AvaliacaoPasso", { passo: id, numero: atual + 1 });
      var alvo = $("h2", seccao(id));
      alvo.setAttribute("tabindex", "-1");
      alvo.focus({ preventScroll: true });
      var topo = form.getBoundingClientRect().top;
      if (topo < 0) window.scrollBy({ top: topo - 100, behavior: "smooth" });
    }
  }

  function avancar() {
    if (!passoCompleto(PASSOS[atual]) || atual >= PASSOS.length - 1) return;
    atual++;
    desenhar(true);
  }
  function avancarDepois() { setTimeout(avancar, 230); }

  // ---------- Escolhas ----------
  function escolher(nome, valor) { campo(nome).value = valor; marcarEscolhido(nome); comporVersao(); fichas(); atualizarBotoes(); }

  $("[data-as-lista='marca']").addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    if (campo("marca").value !== b.dataset.v) {
      campo("modelo").value = ""; campo("versao_motor").value = ""; campo("nivel_equipamento").value = "";
      mostrarOutro("modelo", false);
    }
    escolher("marca", b.dataset.v);
    var outra = b.dataset.v === OUTRA_MARCA;
    mostrarOutro("marca", outra);
    var modelos = MARCAS[b.dataset.v] ? ordenar(MARCAS[b.dataset.v]) : [];
    encher("modelo", modelos.concat([OUTRO_MODELO]).map(function (m) { return { v: m }; }));
    $("[data-as-ajuda-modelo]").textContent = outra ? "Indique o modelo do seu carro." : "Modelos " + b.dataset.v + ". Deslize para o lado ou pesquise.";
    atualizarPassos();
    var niveis = equipamentosDaMarca();
    if (niveis) encher("nivel_equipamento", niveis.concat([OUTRO_EQUIPAMENTO]).map(function (v) { return { v: v }; }));
    if (outra) { escolher("modelo", OUTRO_MODELO); mostrarOutro("modelo", true); outroTexto("marca").focus(); }
    else avancarDepois();
  });
  $("[data-as-lista='modelo']").addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    if (campo("modelo").value !== b.dataset.v) campo("versao_motor").value = "";
    escolher("modelo", b.dataset.v);
    atualizarPassos();
    var versoes = versoesDoModelo();
    if (versoes) {
      encher("versao_motor", versoes.concat([OUTRA_VERSAO]).map(function (v) { return { v: v }; }));
      $("[data-as-ajuda-versao]").textContent = "Versões " + campo("marca").value + " " + b.dataset.v + '. Se não souber, escolha "' + OUTRA_VERSAO + '".';
    }
    var outro = b.dataset.v === OUTRO_MODELO;
    mostrarOutro("modelo", outro);
    if (outro) outroTexto("modelo").focus(); else avancarDepois();
  });
  $("[data-as-lista='versao_motor']").addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    escolher("versao_motor", b.dataset.v);
    avancarDepois();
  });
  $("[data-as-lista='nivel_equipamento']").addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    escolher("nivel_equipamento", b.dataset.v);
    avancarDepois();
  });
  $("[data-as-lista='ano']").addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    escolher("ano", b.dataset.v);
    if (campo("mes").value) avancarDepois();
  });
  $("[data-as-lista='mes']").addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    escolher("mes", b.dataset.v);
    if (campo("ano").value) avancarDepois();
  });
  ["transmissao", "segmento"].forEach(function (nome) {
    $("[data-as-lista='" + nome + "']").addEventListener("click", function (ev) {
      var b = ev.target.closest("button"); if (!b) return;
      escolher(nome, b.dataset.v);
      avancarDepois();
    });
  });

  // Pesquisa nas listas de marcas e modelos
  $$("[data-as-pesquisa]").forEach(function (input) {
    input.addEventListener("input", function () {
      var q = normal(input.value);
      $$(".as-carrossel > button", input.closest(".as-passo")).forEach(function (b) {
        b.hidden = normal(b.dataset.v).indexOf(q) < 0 && b.dataset.v !== OUTRA_MARCA && b.dataset.v !== OUTRO_MODELO;
      });
    });
  });

  // Setas para deslizar o carrossel do passo atual
  $("[data-as-setas]").addEventListener("click", function (ev) {
    var d = ev.target.dataset.dir, car = $(".as-carrossel", seccao(PASSOS[atual]));
    if (d && car) car.scrollBy({ left: d * car.clientWidth * 0.8, behavior: "smooth" });
  });

  // Campos de texto: atualizam o botão "Seguinte"; Enter avança
  form.addEventListener("input", function (ev) {
    if (ev.target.name === "matricula") ev.target.value = ev.target.value.toUpperCase();
    if (ev.target.name === "observacoes") {
      var max = ev.target.maxLength, n = ev.target.value.length;
      var contador = $("[data-as-contador]");
      contador.textContent = n + "/" + max;
      contador.classList.toggle("limite", n >= max);
    }
    fichas();
    atualizarBotoes();
  });
  form.addEventListener("change", atualizarBotoes);
  form.addEventListener("keydown", function (ev) {
    if (ev.key === "Enter" && ev.target.tagName === "INPUT" && ev.target.type !== "search") {
      ev.preventDefault();
      if (atual < PASSOS.length - 1) avancar(); else $("[data-as-enviar]").click();
    }
  });
  new MutationObserver(atualizarBotoes).observe($(".fotos-lista"), { childList: true });

  $("[data-as-seguinte]").addEventListener("click", function () {
    if (!passoCompleto(PASSOS[atual])) {
      var invalido = $$("input:not([type='hidden']):not([disabled]), select, textarea", seccao(PASSOS[atual])).filter(function (el) { return !el.checkValidity(); })[0];
      if (invalido) invalido.reportValidity();
      return;
    }
    avancar();
  });
  $("[data-as-voltar]").addEventListener("click", function () { if (atual) { atual--; desenhar(true); } });

  // Último passo: valida antes de deixar main.js enviar
  var primeiroNome = "";
  $("[data-as-enviar]").addEventListener("click", function (ev) {
    var invalido = $$("input:not([type='hidden']):not([disabled]), select", seccao("dados")).filter(function (el) { return !el.checkValidity(); })[0];
    if (invalido) { ev.preventDefault(); invalido.reportValidity(); return; }
    primeiroNome = campo("nome").value.trim().split(" ")[0];
  });

  // Quando main.js confirma o envio, mostra o ecrã final
  var mensagem = $(".mensagem-form");
  new MutationObserver(function () {
    if (!mensagem.classList.contains("sucesso")) return;
    PASSOS.forEach(function (id) { seccao(id).hidden = true; });
    $("[data-as-rodape]").hidden = true;
    $("[data-as-setas]").hidden = true;
    $("[data-as-n]").textContent = "Pedido enviado";
    $("[data-as-barra]").innerHTML = PASSOS.map(function () { return '<i class="feito"></i>'; }).join("");
    $("[data-as-obrigado]").textContent = primeiroNome ? "Obrigado, " + primeiroNome + "!" : "Obrigado!";
    $("[data-as-fim]").hidden = false;
    // O título já agradece; evita repetir "Obrigado!" no início da mensagem
    var t = mensagem.firstChild;
    if (t && t.nodeType === 3) t.nodeValue = t.nodeValue.replace(/^Obrigado!\s*/, "");
  }).observe(mensagem, { attributes: true, attributeFilter: ["class"] });

  desenhar(false);
})();
