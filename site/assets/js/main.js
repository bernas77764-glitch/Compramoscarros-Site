(function () {
  "use strict";

  var CFG = window.CC_CONFIG || {};

  // ---------- Menu móvel ----------
  var botaoMenu = document.querySelector(".menu-botao");
  var navegacao = document.querySelector(".navegacao");
  if (botaoMenu && navegacao) {
    botaoMenu.addEventListener("click", function () {
      var aberta = navegacao.classList.toggle("aberta");
      botaoMenu.setAttribute("aria-expanded", aberta ? "true" : "false");
    });
  }

  // ---------- Ano no rodapé ----------
  Array.prototype.forEach.call(document.querySelectorAll("[data-ano]"), function (el) {
    el.textContent = new Date().getFullYear();
  });

  // ---------- Aviso de cookies ----------
  var cookies = document.querySelector(".cookies");
  if (cookies) {
    var aceite = false;
    try { aceite = localStorage.getItem("cc_cookies") === "1"; } catch (e) {}
    if (!aceite) cookies.classList.add("visivel");
    cookies.querySelector("button").addEventListener("click", function () {
      try { localStorage.setItem("cc_cookies", "1"); } catch (e) {}
      cookies.classList.remove("visivel");
    });
  }

  // ---------- Listas do formulário de avaliação ----------
  var DISTRITOS = ["Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro",
    "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal", "Viana do Castelo",
    "Vila Real", "Viseu", "Região Autónoma dos Açores", "Região Autónoma da Madeira"];

  var MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"];

  // Lista em assets/js/marcas.js
  var MARCAS = window.CC_MARCAS || {};
  var OUTRA_MARCA = "Outra marca", OUTRO_MODELO = "Outro modelo";

  function ordenar(lista) {
    return lista.slice().sort(function (a, b) {
      return String(a).localeCompare(String(b), "pt", { numeric: true, sensitivity: "base" });
    });
  }

  // Mostra (e torna obrigatório) o campo de texto livre quando a opção é "Outra..."
  function alternar(campoTexto, visivel) {
    if (!campoTexto) return;
    var input = campoTexto.querySelector("input");
    campoTexto.hidden = !visivel;
    input.disabled = !visivel;
    if (!visivel) input.value = "";
  }

  function preencher(select, valores) {
    var primeira = select.querySelector("option[value='']");
    select.innerHTML = "";
    if (primeira) select.appendChild(primeira);
    valores.forEach(function (v) {
      var o = document.createElement("option");
      o.value = String(v);
      o.textContent = String(v);
      select.appendChild(o);
    });
  }

  var sel = function (nome) { return document.querySelector("[data-lista='" + nome + "']"); };

  if (sel("distrito")) preencher(sel("distrito"), DISTRITOS);
  if (sel("mes")) preencher(sel("mes"), MESES);
  if (sel("ano")) {
    var anos = [];
    for (var a = new Date().getFullYear(); a >= 1990; a--) anos.push(a);
    preencher(sel("ano"), anos);
  }
  if (sel("marca") && sel("modelo")) {
    var marca = sel("marca"), modelo = sel("modelo");
    var marcaOutra = document.querySelector("[data-outro='marca']");
    var modeloOutro = document.querySelector("[data-outro='modelo']");
    preencher(marca, ordenar(Object.keys(MARCAS)).concat([OUTRA_MARCA]));
    marca.addEventListener("change", function () {
      var modelos = MARCAS[marca.value] ? ordenar(MARCAS[marca.value]) : [];
      preencher(modelo, modelos.concat([OUTRO_MODELO]));
      modelo.value = marca.value === OUTRA_MARCA ? OUTRO_MODELO : "";
      alternar(marcaOutra, marca.value === OUTRA_MARCA);
      alternar(modeloOutro, modelo.value === OUTRO_MODELO);
    });
    modelo.addEventListener("change", function () {
      alternar(modeloOutro, modelo.value === OUTRO_MODELO);
    });
  }

  // A matrícula é guardada em maiúsculas (AA-00-AA)
  var matricula = document.querySelector("input[name='matricula']");
  if (matricula) {
    matricula.addEventListener("input", function () { matricula.value = matricula.value.toUpperCase(); });
  }

  // ---------- Envio dos formulários ----------
  function resumo(form) {
    var linhas = [form.getAttribute("data-assunto") || "Pedido através do site"];
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.name === "_gotcha" || el.type === "submit" || el.type === "checkbox" || !el.value) return;
      var rotulo = el.getAttribute("aria-label") || el.name;
      linhas.push(rotulo + ": " + el.value);
    });
    return linhas.join("\n");
  }

  function mostrar(form, tipo, texto) {
    var caixa = form.querySelector(".mensagem-form");
    caixa.className = "mensagem-form " + tipo;
    caixa.textContent = texto;
  }

  Array.prototype.forEach.call(document.querySelectorAll("form[data-formulario]"), function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (form.elements._gotcha && form.elements._gotcha.value) return;

      var botao = form.querySelector("button[type='submit']");

      if (!CFG.formEndpoint) {
        var url = "https://wa.me/" + CFG.whatsapp + "?text=" + encodeURIComponent(resumo(form));
        window.open(url, "_blank", "noopener");
        mostrar(form, "sucesso", "Abrimos o WhatsApp com o seu pedido. Basta carregar em enviar para concluir.");
        return;
      }

      botao.disabled = true;
      var dados = new FormData(form);
      dados.append("_subject", form.getAttribute("data-assunto") || "Pedido através do site");
      fetch(CFG.formEndpoint, { method: "POST", body: dados, headers: { Accept: "application/json" } })
        .then(function (r) {
          if (!r.ok) throw new Error(r.status);
          form.reset();
          mostrar(form, "sucesso", "Obrigado! Recebemos o seu pedido e entraremos em contacto o mais brevemente possível.");
        })
        .catch(function () {
          mostrar(form, "erro", "Não foi possível enviar o pedido. Por favor ligue-nos para o " + CFG.telefone + " ou contacte-nos por WhatsApp.");
        })
        .then(function () { botao.disabled = false; });
    });
  });
})();
