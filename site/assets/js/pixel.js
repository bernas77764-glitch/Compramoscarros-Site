/*
 * Meta Pixel (Facebook/Instagram), só depois de o visitante aceitar os cookies (RGPD).
 *
 * É o código oficial da Meta, num ficheiro próprio porque a política de segurança do site não
 * permite scripts escritos nas páginas. Eventos enviados:
 *   PageView          em todas as páginas
 *   Lead              na página Obrigado (uma vez por pedido de avaliação)
 *   Contact           quando o formulário de contactos é enviado (main.js)
 *   AvaliacaoPasso    a cada passo do formulário de avaliação (assistente.js), para ver onde
 *                     os visitantes desistem
 */
(function () {
  "use strict";

  var PIXEL_ID = "1312328063221205";
  var CHAVE_CONSENTIMENTO = "cc_cookies_v2";

  function carregar() {
    if (window.fbq) return;
    /* eslint-disable */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0";
      n.queue = []; t = b.createElement(e); t.async = !0;
      t.src = v; s = b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t, s);
    }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    /* eslint-enable */
    window.fbq("init", PIXEL_ID);
    window.fbq("track", "PageView");

    // Conversão: página Obrigado depois de um pedido de avaliação (não repete ao recarregar)
    if (document.querySelector("[data-obrigado-pagina]")) {
      try {
        if (sessionStorage.getItem("cc_obrigado") && !sessionStorage.getItem("cc_lead_contado")) {
          window.fbq("track", "Lead");
          sessionStorage.setItem("cc_lead_contado", "1");
        }
      } catch (e) {}
    }
  }

  function consentimento() {
    try { return localStorage.getItem(CHAVE_CONSENTIMENTO); } catch (e) { return null; }
  }

  window.ccPixel = {
    chave: CHAVE_CONSENTIMENTO,
    carregar: carregar,
    // Envia um evento só se o pixel estiver ativo (visitante aceitou os cookies)
    evento: function (tipo, nome, dados) {
      if (window.fbq) window.fbq(tipo, nome, dados || {});
    }
  };

  if (consentimento() === "aceite") carregar();
})();
