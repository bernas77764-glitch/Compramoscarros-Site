/* Dados e utilitários comuns aos protótipos do formulário passo a passo (demonstração). */
(function () {
  "use strict";

  var MARCAS = window.CC_MARCAS || {};
  var ordenar = function (l) {
    return l.slice().sort(function (a, b) { return String(a).localeCompare(String(b), "pt", { numeric: true, sensitivity: "base" }); });
  };
  var anoAtual = new Date().getFullYear();
  var anos = [];
  for (var a = anoAtual; a >= 1990; a--) anos.push(String(a));

  function carro(d) {
    return '<svg viewBox="0 0 96 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="' + d + '"/><circle cx="24" cy="31" r="5.5"/><circle cx="72" cy="31" r="5.5"/></svg>';
  }

  window.CC = {
    MARCAS_POPULARES: ["Renault", "Peugeot", "Mercedes-Benz", "BMW", "Volkswagen", "Citroën", "Seat", "Toyota", "Fiat", "Opel", "Audi", "Nissan"],
    marcas: function () { return ordenar(Object.keys(MARCAS)).concat(["Outra marca"]); },
    modelos: function (m) { return (MARCAS[m] ? ordenar(MARCAS[m]) : []).concat(["Outro modelo"]); },
    anos: anos,
    meses: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    caixas: [
      { id: "Manual", nota: "Pedal de embraiagem",
        svg: '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="10" r="3.5"/><circle cx="24" cy="10" r="3.5"/><circle cx="36" cy="10" r="3.5"/><circle cx="12" cy="38" r="3.5"/><circle cx="24" cy="38" r="3.5"/><circle cx="36" cy="38" r="3.5"/><path d="M12 13.5v21M24 13.5v21M36 13.5v21M12 24h24"/></svg>' },
      { id: "Automática", nota: "Sem pedal de embraiagem",
        svg: '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="14" y="4" width="20" height="40" rx="6"/><text x="24" y="15" font-family="Barlow,sans-serif" font-size="8" font-weight="800" text-anchor="middle" fill="currentColor" stroke="none">P</text><text x="24" y="24" font-family="Barlow,sans-serif" font-size="8" font-weight="800" text-anchor="middle" fill="currentColor" stroke="none">R</text><text x="24" y="33" font-family="Barlow,sans-serif" font-size="8" font-weight="800" text-anchor="middle" fill="currentColor" stroke="none">N</text><text x="24" y="42" font-family="Barlow,sans-serif" font-size="8" font-weight="800" text-anchor="middle" fill="currentColor" stroke="none">D</text></svg>' }
    ],
    segmentos: [
      { id: "Citadino", svg: carro("M14 31H8v-8l6-3 8-9h22l10 9h4l4 4v7h-6M30 31h36M44 11v9M22 20h36") },
      { id: "Utilitário", svg: carro("M10 31H6v-9l8-3 10-9h26l12 9h12l6 4v8h-6M30 31h36M48 10v9M24 19h38") },
      { id: "Berlina", svg: carro("M10 31H4v-7l8-3 14-9h28l14 9h14l4 4v6h-6M30 31h36M48 12v9M26 21h42") },
      { id: "Carrinha", svg: carro("M10 31H4v-9l6-2 12-10h58l6 10 4 2v9h-12M30 31h36M52 10v10M22 20h64") },
      { id: "SUV / Crossover", svg: carro("M10 31H4v-11l8-2 10-10h38l14 10h10l6 4v9h-8M30 31h36M48 8v10M22 18h52") },
      { id: "Monovolume", svg: carro("M10 31H4v-11l6-3 16-11h46l10 11 6 3v11h-8M30 31h36M54 6v11M26 17h56") },
      { id: "Coupé / Cabrio", svg: carro("M10 31H6v-6l10-3 16-8h20l16 8h16l6 3v6h-8M30 31h36M30 22h40") },
      { id: "Comercial / Pick-up", svg: carro("M10 31H4v-11l6-2 8-10h22v10h48v13h-10M30 31h36M40 8v10") }
    ],
    DISTRITOS: ["Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal", "Viana do Castelo", "Vila Real", "Viseu", "Região Autónoma dos Açores", "Região Autónoma da Madeira"],

    estado: { fotos: [] },

    resumo: function () {
      var e = this.estado, p = [];
      if (e.marca) p.push(e.marca);
      if (e.modelo) p.push(e.modelo);
      if (e.ano) p.push((e.mes ? e.mes.slice(0, 3) + " " : "") + e.ano);
      if (e.caixa) p.push(e.caixa);
      if (e.segmento) p.push(e.segmento);
      return p;
    },

    // Escolha de fotos com miniaturas (até 10). Chama aoMudar() sempre que a lista muda.
    fotos: function (input, lista, aoMudar) {
      var self = this;
      function desenhar() {
        lista.innerHTML = "";
        self.estado.fotos.forEach(function (f, i) {
          var fig = document.createElement("figure");
          fig.innerHTML = '<img alt="Foto ' + (i + 1) + '"><button type="button" aria-label="Remover foto">×</button>';
          fig.querySelector("img").src = URL.createObjectURL(f);
          fig.querySelector("button").onclick = function () { self.estado.fotos.splice(i, 1); desenhar(); };
          lista.appendChild(fig);
        });
        if (aoMudar) aoMudar(self.estado.fotos.length);
      }
      input.addEventListener("change", function () {
        var novas = Array.prototype.filter.call(input.files, function (f) { return /^image\//.test(f.type); });
        self.estado.fotos = self.estado.fotos.concat(novas).slice(0, 10);
        input.value = "";
        desenhar();
      });
      desenhar();
    },

    // Filtro de pesquisa simples (sem acentos, sem maiúsculas)
    normal: function (t) { return String(t).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  };
})();
